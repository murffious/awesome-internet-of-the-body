# Awesome Internet of the Body [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
  <img src="assets/banner.png" alt="Awesome Internet of the Body — a curated map of the apps and platforms that gather human data" width="840">
</p>

> A curated list of apps, platforms, devices, and open-source projects that **gather human data** — the "Internet of the Body" (IoB).

The **Internet of the Body** (or *Internet of Bodies*, IoB) — a term coined by
Andrea M. Matwyshyn in 2016 — describes *"a network of human bodies whose
integrity and functionality rely at least in part on the internet and related
technologies."* In plain terms: the growing web of wearables, implants, sensors,
and apps that measure a human being and move that data across a network.

This list catalogs the software and hardware that does the measuring, with a bias
toward **open-source and standards-based** projects you can actually inspect. The
core idea: each entry is a place you can **consume human data via app
integrations** — an API, SDK, webhook, or open export — rather than re-instrument
the body yourself. Wherever an entry exposes one, its integration surface is linked.

> **Scope & ethos.** This is a reference index, **not medical advice** and not an
> endorsement. Every device here collects sensitive personal data — see
> [Privacy, ethics and data ownership](#privacy-ethics-and-data-ownership) before you
> trust any of them.
>
> **Legend.**
> *Openness* — 🟢 open source · 🔵 open standard / SDK · ⚪ commercial / proprietary.
> *Cadence* (how you consume it) — `live` real-time / streaming / webhook · `snapshot` point-in-time or one-time export · `live + history` a live-ish feed plus a historical archive. Standards, SDKs, and tooling carry either mode, so they're left untagged.

---

## Contents

- [What counts as "Internet of the Body"](#what-counts-as-internet-of-the-body)
- [Wearables and rings](#wearables-and-rings)
- [Continuous glucose and metabolic](#continuous-glucose-and-metabolic)
- [Sleep and recovery](#sleep-and-recovery)
- [Open-source health-data tooling](#open-source-health-data-tooling)
- [Personal data platforms and Quantified Self](#personal-data-platforms-and-quantified-self)
- [Health-data standards and SDKs](#health-data-standards-and-sdks)
- [Genomics, microbiome and omics](#genomics-microbiome-and-omics)
- [Neuro, brain-computer and implantables](#neuro-brain-computer-and-implantables)
- [Nutrition and food logging](#nutrition-and-food-logging)
- [Privacy, ethics and data ownership](#privacy-ethics-and-data-ownership)
- [Related projects](#related-projects)
- [Contributing](#contributing)

---

## What counts as "Internet of the Body"

Matwyshyn describes three generations of IoB, useful as a mental map:

| Generation | Relationship to the body | Examples |
|---|---|---|
| **1 — external** | Worn on the body | Smartwatches, rings, chest straps, smart glasses |
| **2 — internal** | Inside the body | Pacemakers, cochlear implants, digital pills, insulin pumps |
| **3 — melded** | Merged with the body, always online | Experimental brain–computer interfaces, smart prosthetics wired to nerves |

An entry belongs on this list if it **measures a human** (physiology, biometrics,
behavior, or -omics) **and moves that data somewhere** — an app, a cloud, or your
own server.

---

## Wearables and rings

External, first-generation devices — the largest source of everyday human data.

- ⚪ **[Apple Health / HealthKit](https://developer.apple.com/documentation/healthkit)** — on-device store aggregating heart rate, activity, ECG, and dozens of other types; the de-facto hub on iOS. `live + history`
- 🔵 **[Health Connect (Android)](https://developer.android.com/health-and-fitness/guides/health-connect)** — Google's on-device API that lets fitness/health apps share data with user consent. Samples: [android/health-samples](https://github.com/android/health-samples). `live + history`
- ⚪ **[Oura Ring](https://ouraring.com/)** — sleep, HRV, temperature, readiness. Has a [developer API](https://cloud.ouraring.com/docs/). `live + history`
- ⚪ **[WHOOP](https://www.whoop.com/)** — strain/recovery band with a [public API](https://developer.whoop.com/). `live + history`
- ⚪ **[Garmin](https://www.garmin.com/)** — GPS + physiology across watches; [Health API](https://developer.garmin.com/gc-developer-program/health-api/) for research. `live + history`
- ⚪ **[Fitbit](https://www.fitbit.com/)** / **[Fitbit Web API](https://dev.fitbit.com/build/reference/web-api/)** — steps, HR, sleep. `live + history`
- ⚪ **[Withings](https://www.withings.com/)** — scales, BP cuffs, sleep mats; [developer API](https://developer.withings.com/). `live + history`
- 🟢 **[Gadgetbridge](https://github.com/Freeyourgadget/Gadgetbridge)** — Android app that talks to many fitness bands/watches **without** the vendor cloud, keeping data local. A cornerstone open-source IoB project. `live + history`

## Continuous glucose and metabolic

Second-generation sensors that read the body's chemistry in near-real time.

- ⚪ **[Dexcom](https://www.dexcom.com/)** — CGM with a [developer API](https://developer.dexcom.com/). `live`
- ⚪ **[Abbott FreeStyle Libre](https://www.freestyle.abbott/)** — widely used CGM. `live`
- ⚪ **[Levels](https://www.levelshealth.com/)** / **[Nutrisense](https://www.nutrisense.io/)** — metabolic-health apps built on top of CGM hardware. `live + history`
- 🟢 **[Nightscout (cgm-remote-monitor)](https://github.com/nightscout/cgm-remote-monitor)** — the "#WeAreNotWaiting" project: self-hosted CGM data platform. You own the server and the data. `live`
- 🟢 **[OpenAPS](https://github.com/openaps)** & 🟢 **[Loop (LoopKit)](https://github.com/LoopKit/Loop)** — open-source "artificial pancreas" systems that close the loop between CGM and insulin pump. `live`

## Sleep and recovery

- ⚪ **[Eight Sleep](https://www.eightsleep.com/)** — sensor mattress cover (temperature, HR, HRV). `live + history`
- ⚪ **[Sleep as Android](https://sleep.urbandroid.org/)** — sleep tracking that integrates with many wearables. `live + history`
- ⚪ Oura / WHOOP / Withings (above) all double as sleep trackers. `live + history`

## Open-source health-data tooling

The heart of an "Internet of the Body" list — projects you can read, run, and self-host.

- 🟢 **[Nightscout](https://github.com/nightscout/cgm-remote-monitor)** — self-hosted CGM data (see above). `live`
- 🟢 **[Gadgetbridge](https://github.com/Freeyourgadget/Gadgetbridge)** — cloud-free wearable sync (see above). `live + history`
- 🟢 **[Home Assistant](https://github.com/home-assistant/core)** — local-first automation platform with many health/wearable integrations; a common place people pool body data at home. `live`
- 🟢 **[Open mHealth](https://github.com/openmhealth)** — open schemas + libraries that normalize mobile health data across sources.
- 🟢 **[ResearchKit](https://github.com/ResearchKit/ResearchKit)** & 🟢 **[CareKit](https://github.com/carekit-apple/CareKit)** — Apple's open frameworks for building medical research and care apps that collect participant data.
- 🟢 **[Google Fit / Fit REST API samples](https://github.com/googlearchive/fit-samples)** — reference code for reading fitness data.

## Personal data platforms and Quantified Self

Platforms whose whole purpose is aggregating *your* body data — for yourself or for research.

- 🟢 **[Open Humans](https://github.com/OpenHumans)** ([openhumans.org](https://www.openhumans.org/)) — nonprofit platform to aggregate personal data (wearables, genomes, microbiome) and optionally donate it to research. The most IoB-native open project here. `snapshot`
- ⚪ **[Exist.io](https://exist.io/)** — correlates data from many trackers to surface patterns. `live + history`
- 🟢 **[Quantified Self (community + resources)](https://quantifiedself.com/)** — the movement that named "self-knowledge through numbers"; see the community's [tools directory](https://quantifiedself.com/tools/).

## Health-data standards and SDKs

The plumbing that lets body data move between systems — what makes IoB an *inter*net.

- 🔵 **[HL7 FHIR](https://github.com/HL7/fhir)** — the dominant open standard for exchanging clinical/health data. [Spec](https://www.hl7.org/fhir/).
- 🔵 **[Open mHealth schemas](https://www.openmhealth.org/documentation/#/schema-docs/schema-library)** — normalized JSON schemas for mobile health signals.
- 🔵 **[SMART on FHIR](https://github.com/smart-on-fhir)** — apps that plug into electronic health records.
- 🔵 **[Apple HealthKit](https://developer.apple.com/documentation/healthkit)** / **[Android Health Connect](https://developer.android.com/health-and-fitness/guides/health-connect)** — the two dominant on-device SDKs.

## Genomics, microbiome and omics

Slower-moving but deeply personal body data.

- 🟢 **[openSNP](https://github.com/openSNP/snpr)** — open database where people share their genotype + phenotype data. `snapshot`
- ⚪ **[Nebula Genomics](https://nebula.org/)** — whole-genome sequencing with a privacy-forward pitch. `snapshot`
- ⚪ **[23andMe](https://www.23andme.com/)** — consumer genetics (note its 2023–2025 data-breach and bankruptcy saga — a cautionary IoB privacy case study). `snapshot`
- ⚪ **[Viome](https://www.viome.com/)** / **[ZOE](https://zoe.com/)** — microbiome + metabolic testing tied to nutrition apps. `snapshot`

## Neuro, brain-computer and implantables

Third-generation, melded devices — the frontier (and the sharpest ethics).

- 🟢 **[OpenBCI](https://github.com/OpenBCI)** — open-source hardware + software for EEG/EMG/ECG biosensing. The accessible on-ramp to neural IoB. `live`
- ⚪ **[Neuralink](https://neuralink.com/)** — implanted brain–computer interface. `live`
- ⚪ **[Synchron](https://synchron.com/)** — endovascular BCI (implanted via blood vessels, no open-skull surgery). `live`
- ⚪ **[Medtronic](https://www.medtronic.com/)** — connected pacemakers, insulin pumps, neurostimulators (a huge share of real-world "generation 2" IoB). `live + history`

## Nutrition and food logging

Apps that log what goes *into* the body — the input side of the human-data picture.

- 🟢 **[Open Food Facts](https://github.com/openfoodfacts)** — open, crowd-sourced database of foods and their labels ([openfoodfacts.org](https://world.openfoodfacts.org/)).
- ⚪ **[Cronometer](https://cronometer.com/)** — micronutrient-accurate food/biometric logging with an [API](https://cronometer.com/api/). `live + history`
- ⚪ **[MyFitnessPal](https://www.myfitnesspal.com/)** — large-scale food and exercise logging. `live + history`

## Privacy, ethics and data ownership

Body data is the most sensitive data there is. Any honest IoB list must point here.

- 🟢 **[Solid](https://github.com/solid/solid)** — Tim Berners-Lee's protocol for personal data "pods" you control ([inrupt.com](https://www.inrupt.com/)).
- ⚪ **[MyData Global](https://www.mydata.org/)** — nonprofit advancing human-centric personal-data rights.
- 🟢 **[Open Humans](https://github.com/OpenHumans)** — consent-first data donation (also listed above).
- **Reference reading:** [Purdue Center for the Internet of Bodies (C-IoB)](https://engineering.purdue.edu/C-IoB) · [RAND — "The Internet of Bodies"](https://www.rand.org/pubs/research_reports/RR3226.html).

Questions worth asking of any entry above: *Where does the data live? Can you
export or delete it? Who can it be sold or subpoenaed to? What happens to it if
the company folds?* (The 23andMe collapse is the canonical worked example.)

---

## Related projects

- **[biology-as-code](https://github.com/murffious/biology_as_code)** — models what a
  body *does* with inputs (digestion, absorption, metabolic pathways) as versioned,
  provenance-tracked code. This list is its natural **sensor-layer** companion: the
  integrations catalogued here are where the real signals would come from. The same
  ethos applies in both — **empty beats fake**, provenance is mandatory, and missing
  data is `UNEVALUABLE`, not a green light.

---

## Contributing

Contributions are welcome — this list is a starting scaffold, not the finished map.
See [CONTRIBUTING.md](CONTRIBUTING.md). In short, to add an entry:

1. It must **gather human data** and be **real / verifiable** (working link).
2. Prefer **open-source or open-standard** projects; label commercial ones ⚪.
3. Add a cadence tag (`live` / `snapshot` / `live + history`) where the entry is a data feed.
4. Put it in the right section, keep the one-line description factual, and use **no fabricated links or claims**.

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors to this curated list have waived
all copyright and related or neighboring rights to it under [CC0 1.0](LICENSE).
