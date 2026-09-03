#!/usr/bin/env python3
"""
IoB Daily Scraper
=================
Finds 1-5 new Internet of the Body (IoB) device/platform stories per day by
querying freely-available RSS/JSON news feeds and keyword-filtered searches.

Usage
-----
    python scraper.py                     # print today's results to stdout
    python scraper.py --output results.md # append results to a markdown file
    python scraper.py --days 3            # look back N days (default: 1)

Dependencies (stdlib only, no pip installs required):
    urllib, json, xml.etree.ElementTree, datetime, argparse, re

The script is intentionally dependency-free so it runs in any Python 3.8+
environment without a virtual environment.
"""

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from typing import NamedTuple

# ---------------------------------------------------------------------------
# Configuration – tweak keywords and sources to your liking
# ---------------------------------------------------------------------------

IOB_KEYWORDS = [
    "wearable",
    "biosensor",
    "implantable",
    "internet of body",
    "internet of bodies",
    "health wearable",
    "smart ring",
    "continuous glucose",
    "CGM",
    "ECG patch",
    "brain computer interface",
    "BCI",
    "neuromodulation",
    "smart prosthetic",
    "digital pill",
    "hormone tracking",
    "biometric",
    "remote patient monitoring",
]

# RSS feeds that cover health-tech / digital-health / wearables
RSS_FEEDS = [
    # TechCrunch health tag
    "https://techcrunch.com/tag/health/feed/",
    # MedCity News
    "https://medcitynews.com/feed/",
    # Digital Health Today
    "https://digitalhealth.today/feed/",
    # Fierce Biotech – devices
    "https://www.fiercebiotech.com/rss/medical-devices",
    # Rock Health blog (Substack mirror if available)
    "https://rockhealth.substack.com/feed",
]

# Hacker News Algolia API – free, no key needed
HN_API = (
    "https://hn.algolia.com/api/v1/search?"
    "query={query}&tags=story&numericFilters=created_at_i>{since}"
)

MAX_RESULTS = 5  # cap returned entries
REQUEST_TIMEOUT = 10  # seconds


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


class Item(NamedTuple):
    title: str
    url: str
    source: str
    published: str  # ISO-8601 date string or empty


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "IoB-Scraper/1.0"})
    with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
        return resp.read()


def _matches_iob(text: str) -> bool:
    """Return True if *text* contains at least one IoB keyword (case-insensitive)."""
    lower = text.lower()
    return any(kw.lower() in lower for kw in IOB_KEYWORDS)


def _parse_rss_date(date_str: str) -> str:
    """Best-effort RFC-2822 → ISO-8601 date conversion."""
    for fmt in (
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
    ):
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            return dt.date().isoformat()
        except ValueError:
            continue
    return date_str.strip()[:10]  # fallback: first 10 chars


# ---------------------------------------------------------------------------
# Source scrapers
# ---------------------------------------------------------------------------


def scrape_rss(feed_url: str, since: datetime) -> list[Item]:
    """Pull items from a single RSS/Atom feed published after *since*."""
    items: list[Item] = []
    try:
        raw = _fetch(feed_url)
    except (urllib.error.URLError, OSError) as exc:
        print(f"[warn] RSS {feed_url}: {exc}", file=sys.stderr)
        return items

    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        print(f"[warn] RSS parse error {feed_url}: {exc}", file=sys.stderr)
        return items

    # Handle both RSS <item> and Atom <entry>
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    entries = root.findall(".//item") or root.findall(".//atom:entry", ns)

    for entry in entries:
        title = (
            (entry.findtext("title") or entry.findtext("atom:title", namespaces=ns) or "")
            .strip()
        )
        link = (
            entry.findtext("link")
            or ""
        ).strip()
        atom_link = entry.find("atom:link", ns)
        if not link and atom_link is not None:
            link = atom_link.get("href", "").strip()
        pub_raw = (
            entry.findtext("pubDate")
            or entry.findtext("atom:published", namespaces=ns)
            or entry.findtext("atom:updated", namespaces=ns)
            or ""
        )
        pub_date = _parse_rss_date(pub_raw) if pub_raw else ""

        # Filter by date
        if pub_date:
            try:
                item_dt = datetime.fromisoformat(pub_date).replace(tzinfo=timezone.utc)
                if item_dt < since:
                    continue
            except ValueError:
                pass  # unparseable date – include anyway

        description = entry.findtext("description") or entry.findtext("summary") or ""
        combined = f"{title} {description}"

        if title and link and _matches_iob(combined):
            items.append(Item(title=title, url=link, source=feed_url, published=pub_date))

    return items


def scrape_hacker_news(query: str, since: datetime) -> list[Item]:
    """Query Hacker News via the Algolia search API."""
    items: list[Item] = []
    since_ts = int(since.timestamp())
    url = HN_API.format(
        query=urllib.parse.quote(query),
        since=since_ts,
    )
    try:
        raw = _fetch(url)
        data = json.loads(raw)
    except (urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
        print(f"[warn] HN API: {exc}", file=sys.stderr)
        return items

    for hit in data.get("hits", []):
        title = hit.get("title", "")
        link = hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID', '')}"
        created = hit.get("created_at", "")[:10]
        if title and _matches_iob(title):
            items.append(Item(title=title, url=link, source="Hacker News", published=created))

    return items


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def collect(days: int = 1) -> list[Item]:
    """Collect IoB news items from the last *days* days, capped at MAX_RESULTS."""
    since = datetime.now(tz=timezone.utc) - timedelta(days=days)
    results: list[Item] = []
    seen_urls: set[str] = set()

    # RSS feeds
    enough = False
    for feed in RSS_FEEDS:
        for item in scrape_rss(feed, since):
            if item.url not in seen_urls:
                seen_urls.add(item.url)
                results.append(item)
            if len(results) >= MAX_RESULTS * 3:  # gather extras before dedup/cap
                enough = True
                break
        if enough:
            break

    # Hacker News (keyword search)
    for kw in ("wearable biosensor", "health wearable", "smart implant"):
        for item in scrape_hacker_news(kw, since):
            if item.url not in seen_urls:
                seen_urls.add(item.url)
                results.append(item)

    return results[:MAX_RESULTS]


def format_markdown(items: list[Item], today: str) -> str:
    lines = [f"\n## IoB Scraper results — {today}\n"]
    if not items:
        lines.append("_No new items found._\n")
    for i, item in enumerate(items, 1):
        pub = f" ({item.published})" if item.published else ""
        lines.append(f"{i}. [{item.title}]({item.url}){pub} — via {item.source}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Find new IoB device news daily.")
    parser.add_argument(
        "--days",
        type=int,
        default=1,
        help="How many days back to search (default: 1)",
    )
    parser.add_argument(
        "--output",
        metavar="FILE",
        help="Append markdown results to FILE instead of printing to stdout",
    )
    args = parser.parse_args()

    print(f"Searching for IoB news from the last {args.days} day(s)…", file=sys.stderr)
    items = collect(days=args.days)
    today = datetime.now(tz=timezone.utc).date().isoformat()
    md = format_markdown(items, today)

    if args.output:
        with open(args.output, "a", encoding="utf-8") as fh:
            fh.write(md)
        print(f"Wrote {len(items)} item(s) to {args.output}", file=sys.stderr)
    else:
        print(md)


if __name__ == "__main__":
    main()
