# Awesome Internet of the Body [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
  <img src="assets/banner.png" alt="Awesome Internet of the Body — a curated map of the apps and platforms that gather human data" width="840">
</p>

> A curated list of apps, platforms, devices, and open-source projects that gather human data — the "Internet of the Body" (IoB).

The Internet of the Body (or Internet of Bodies, IoB) — a term coined by Andrea M. Matwyshyn in 2016 — describes "a network of human bodies whose integrity and functionality rely at least in part on the internet and related technologies." In plain terms: the growing web of wearables, implants, sensors, and apps that measure a human being and move that data across a network.

This list catalogs the software and hardware that does the measuring, with a bias toward open-source and standards-based projects you can actually inspect. The core idea: each entry is a place you can consume human data via app integrations — an API, SDK, webhook, or open export — rather than re-instrument the body yourself. Wherever an entry exposes one, its integration surface is linked.

> This is a reference index, not medical advice and not an endorsement. Every device here collects sensitive personal data — read the Privacy, ethics and data ownership section before you trust any of them.
>
> Legend — openness: 🟢 open source, 🔵 open standard / SDK, ⚪ commercial / proprietary. Cadence (how you consume it): `live` real-time / streaming / webhook, `snapshot` point-in-time or one-time export, `live + history` a live-ish feed plus a historical archive. Standards, SDKs, and tooling carry either mode, so they are left untagged.

## Contents

- [What counts as the Internet of the Body](#what-counts-as-the-internet-of-the-body)
- [Wearables and rings](#wearables-and-rings)
- [Aggregator and integration APIs](#aggregator-and-integration-apis)
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

## What counts as the Internet of the Body

Matwyshyn describes three generations, a useful mental map. Generation 1 (external) devices are worn on the body — smartwatches, rings, chest straps, smart glasses. Generation 2 (internal) devices sit inside it — pacemakers, cochlear implants, digital pills, insulin pumps. Generation 3 (melded) devices merge with the body while staying online — experimental brain-computer interfaces and smart prosthetics wired to nerves.

An entry belongs on this list if it measures a human (physiology, biometrics, behavior, or -omics) and moves that data somewhere — an app, a cloud, or your own server.

## Wearables and rings

External, first-generation devices — the largest source of everyday human data.

- ⚪ [Apple Health / HealthKit](https://developer.apple.com/documentation/healthkit) — on-device store aggregating heart rate, activity, ECG, and dozens of other types; the de-facto hub on iOS. `live + history`
- 🔵 [Health Connect (Android)](https://developer.android.com/health-and-fitness/guides/health-connect) — Google's on-device API that lets fitness and health apps share data with user consent, with [sample apps](https://github.com/android/health-samples). `live + history`
- ⚪ [Oura Ring](https://ouraring.com/) — sleep, HRV, temperature, and readiness, with a [developer API](https://cloud.ouraring.com/docs/). `live + history`
- ⚪ [WHOOP](https://www.whoop.com/) — strain and recovery band with a [public API](https://developer.whoop.com/). `live + history`
- ⚪ [Garmin](https://www.garmin.com/) — GPS and physiology across watches, with a [Health API](https://developer.garmin.com/gc-developer-program/health-api/) for research. `live + history`
- ⚪ [Fitbit](https://www.fitbit.com/) — steps, heart rate, and sleep, with a [Web API](https://dev.fitbit.com/build/reference/web-api/). `live + history`
- ⚪ [Withings](https://www.withings.com/) — scales, blood-pressure cuffs, and sleep mats, with a [developer API](https://developer.withings.com/). `live + history`
- ⚪ [Biostrap](https://biostrap.com/) — research-grade PPG wearable (wrist and shoe pod) with raw waveform access and a developer API. `live + history`
- 🟢 [Gadgetbridge](https://github.com/Freeyourgadget/Gadgetbridge) — Android app that talks to many fitness bands and watches without the vendor cloud, keeping data local. A cornerstone open-source IoB project. `live + history`

## Aggregator and integration APIs

The purest expression of "consume human data via app integrations" — one integration that normalizes many devices into a single schema.

- ⚪ [Terra](https://tryterra.co/) — unified API for wearables and health data, connecting dozens of devices and apps through one integration. `live + history`
- ⚪ [Vital](https://tryvital.io/) — API for wearable and lab data with webhooks and normalized schemas. `live + history`
- ⚪ [Spike](https://spikeapi.com/) — health-data API aggregating wearables and medical devices into one endpoint. `live + history`
- ⚪ [Rook](https://www.tryrook.io/) — health-data API unifying wearables and sensors into a single normalized model. `live + history`
- ⚪ [Validic](https://validic.com/) — enterprise platform connecting clinical programs to consumer health devices and apps. `live + history`

## Continuous glucose and metabolic

Second-generation sensors that read the body's chemistry in near-real time.

- ⚪ [Dexcom](https://www.dexcom.com/) — CGM with a [developer API](https://developer.dexcom.com/). `live`
- ⚪ [Abbott FreeStyle Libre](https://www.freestyle.abbott/) — widely used CGM. `live`
- ⚪ [Levels](https://www.levelshealth.com/) — metabolic-health app built on top of CGM hardware. `live + history`
- ⚪ [Nutrisense](https://www.nutrisense.io/) — CGM-based metabolic tracking with dietitian support. `live + history`
- 🟢 [Nightscout](https://github.com/nightscout/cgm-remote-monitor) — the "#WeAreNotWaiting" project: a self-hosted CGM data platform where you own the server and the data. `live`
- 🟢 [OpenAPS](https://github.com/openaps) — open-source "artificial pancreas" reference design that closes the loop between CGM and insulin pump. `live`
- 🟢 [Loop](https://github.com/LoopKit/Loop) — open-source automated insulin-delivery app for iOS built on the same idea. `live`

## Sleep and recovery

- ⚪ [Eight Sleep](https://www.eightsleep.com/) — sensor mattress cover tracking temperature, heart rate, and HRV. `live + history`
- ⚪ [Sleep as Android](https://sleep.urbandroid.org/) — sleep tracking that integrates with many wearables. `live + history`

Oura, WHOOP, and Withings (above) all double as sleep trackers.

## Open-source health-data tooling

Projects you can read, run, and self-host. Nightscout and Gadgetbridge (above) also belong here.

- 🟢 [Home Assistant](https://github.com/home-assistant/core) — local-first automation platform with many health and wearable integrations; a common place people pool body data at home. `live`
- 🟢 [Open mHealth](https://github.com/openmhealth) — open schemas and libraries that normalize mobile health data across sources.
- 🟢 [ResearchKit](https://github.com/ResearchKit/ResearchKit) — Apple's open framework for building medical-research apps that collect participant data.
- 🟢 [CareKit](https://github.com/carekit-apple/CareKit) — Apple's open framework for care and symptom-tracking apps.
- 🟢 [Fit REST API samples](https://github.com/googlearchive/fit-samples) — reference code for reading Google fitness data.

## Personal data platforms and Quantified Self

Platforms whose whole purpose is aggregating your body data — for yourself or for research.

- 🟢 [Open Humans](https://github.com/OpenHumans) — nonprofit platform ([openhumans.org](https://www.openhumans.org/)) to aggregate personal data (wearables, genomes, microbiome) and optionally donate it to research. The most IoB-native open project here. `snapshot`
- ⚪ [Exist.io](https://exist.io/) — correlates data from many trackers to surface patterns. `live + history`
- 🟢 [Quantified Self](https://quantifiedself.com/) — the movement that named "self-knowledge through numbers"; see the community's [tools directory](https://quantifiedself.com/tools/).

## Health-data standards and SDKs

The plumbing that lets body data move between systems — what makes IoB an internet.

- 🔵 [HL7 FHIR](https://github.com/HL7/fhir) — the dominant open standard for exchanging clinical and health data.
- 🔵 [Open mHealth schemas](https://www.openmhealth.org/documentation/) — normalized JSON schemas for mobile health signals.
- 🔵 [SMART on FHIR](https://github.com/smart-on-fhir) — apps that plug into electronic health records.

Apple HealthKit and Google Health Connect (both above) are the two dominant on-device SDKs.

## Genomics, microbiome and omics

Slower-moving but deeply personal body data.

- 🟢 [openSNP](https://github.com/openSNP/snpr) — open database where people share their genotype and phenotype data. `snapshot`
- ⚪ [Nebula Genomics](https://nebula.org/) — whole-genome sequencing with a privacy-forward pitch. `snapshot`
- ⚪ [23andMe](https://www.23andme.com/) — consumer genetics; note its 2023–2025 data-breach and bankruptcy saga, a cautionary IoB privacy case study. `snapshot`
- ⚪ [Viome](https://www.viome.com/) — microbiome and metabolic testing tied to a nutrition app. `snapshot`
- ⚪ [ZOE](https://zoe.com/) — microbiome and blood-fat testing paired with personalized nutrition. `snapshot`

## Neuro, brain-computer and implantables

Third-generation, melded devices — the frontier, and the sharpest ethics.

- 🟢 [OpenBCI](https://github.com/OpenBCI) — open-source hardware and software for EEG, EMG, and ECG biosensing. The accessible on-ramp to neural IoB. `live`
- ⚪ [Neuralink](https://neuralink.com/) — implanted brain-computer interface. `live`
- ⚪ [Synchron](https://synchron.com/) — endovascular BCI implanted via blood vessels, with no open-skull surgery. `live`
- ⚪ [Medtronic](https://www.medtronic.com/) — connected pacemakers, insulin pumps, and neurostimulators; a huge share of real-world "generation 2" IoB. `live + history`

## Nutrition and food logging

Apps that log what goes into the body — the input side of the human-data picture.

- 🟢 [Open Food Facts](https://github.com/openfoodfacts) — open, crowd-sourced database of foods and their labels ([openfoodfacts.org](https://world.openfoodfacts.org/)).
- ⚪ [Cronometer](https://cronometer.com/) — micronutrient-accurate food and biometric logging with an [API](https://cronometer.com/api/). `live + history`
- ⚪ [MyFitnessPal](https://www.myfitnesspal.com/) — large-scale food and exercise logging. `live + history`

## Privacy, ethics and data ownership

Body data is the most sensitive data there is. Any honest IoB list must point here.

- 🟢 [Solid](https://github.com/solid/solid) — Tim Berners-Lee's protocol for personal data "pods" you control ([inrupt.com](https://www.inrupt.com/)).
- ⚪ [MyData Global](https://www.mydata.org/) — nonprofit advancing human-centric personal-data rights.

Further reading: the [Purdue Center for the Internet of Bodies](https://engineering.purdue.edu/C-IoB) and the [RAND report on the Internet of Bodies](https://www.rand.org/pubs/research_reports/RR3226.html). And questions worth asking of any entry above: where does the data live, can you export or delete it, who can it be sold or subpoenaed to, and what happens to it if the company folds? (The 23andMe collapse is the canonical worked example.)

## Related projects

- [biology-as-code](https://github.com/murffious/biology_as_code) - Models what a body does with its inputs (digestion, absorption, metabolic pathways) as versioned, provenance-tracked code. This list is its natural sensor-layer companion: the integrations catalogued here are where the real signals would come from.

## Contributing

Contributions are welcome — this list is a starting scaffold, not the finished map. See [contributing guidelines](CONTRIBUTING.md). In short, an entry must gather human data, be real and verifiable with a working link, prefer open-source or open-standard projects, carry a cadence tag where it is a data feed, and use no fabricated links or claims.
