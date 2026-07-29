# Awesome Internet of the Body [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
  <img src="assets/banner.png" alt="Awesome Internet of the Body — a curated map of the apps and platforms that gather human data" width="840">
</p>

> A curated list of **200+** apps, platforms, devices, and open-source projects that gather human data — the **Internet of the Body** (IoB).

The Internet of the Body (or Internet of Bodies, IoB) — a term coined by [Andrea M. Matwyshyn](https://en.wikipedia.org/wiki/Andrea_M._Matwyshyn) in 2016 — describes *"a network of human bodies whose integrity and functionality rely at least in part on the internet and related technologies."* In plain terms: the growing web of wearables, implants, sensors, and apps that measure a human being and move that data across a network.

This list catalogs the software and hardware that does the measuring, with a bias toward open-source and standards-based projects you can actually inspect. The core idea: each entry is a place you can **consume human data via app integrations** — an API, SDK, webhook, or open export — rather than re-instrument the body yourself. Wherever an entry exposes one, its integration surface is linked.

> **This is a reference index, not medical advice and not an endorsement.** Every device here collects sensitive personal data — read [Privacy, ethics and data ownership](#privacy-ethics-and-data-ownership) before you trust any of them.

### Legend

| Marker | Meaning |
| --- | --- |
| 🟢 | Open source |
| 🔵 | Open standard / public SDK |
| ⚪ | Commercial / proprietary |

| Cadence tag | Meaning |
| --- | --- |
| `` `live` `` | Real-time / streaming / webhook |
| `` `snapshot` `` | Point-in-time or one-time export |
| `` `live + history` `` | Live-ish feed plus a historical archive |

Standards, SDKs, and pure tooling carry either mode, so they are left untagged.

---

## Contents

- [What counts as the Internet of the Body](#what-counts-as-the-internet-of-the-body)
- [Wearables rings and smartwatches](#wearables-rings-and-smartwatches)
- [Fitness platforms and training](#fitness-platforms-and-training)
- [Aggregator and integration APIs](#aggregator-and-integration-apis)
- [Continuous glucose and metabolic](#continuous-glucose-and-metabolic)
- [Sleep and recovery](#sleep-and-recovery)
- [Blood pressure vitals and clinical devices](#blood-pressure-vitals-and-clinical-devices)
- [Remote patient monitoring](#remote-patient-monitoring)
- [Womens health fertility and cycle](#womens-health-fertility-and-cycle)
- [Mental health mood and symptoms](#mental-health-mood-and-symptoms)
- [Open-source health-data tooling](#open-source-health-data-tooling)
- [Personal data platforms and Quantified Self](#personal-data-platforms-and-quantified-self)
- [Health-data standards and SDKs](#health-data-standards-and-sdks)
- [Genomics microbiome and omics](#genomics-microbiome-and-omics)
- [Neuro brain-computer and implantables](#neuro-brain-computer-and-implantables)
- [Nutrition and food logging](#nutrition-and-food-logging)
- [Contactless ambient and smart clothing](#contactless-ambient-and-smart-clothing)
- [Hearing vision and sensory](#hearing-vision-and-sensory)
- [Privacy ethics and data ownership](#privacy-ethics-and-data-ownership)
- [Further reading](#further-reading)
- [Related projects](#related-projects)

---

## What counts as the Internet of the Body

Matwyshyn describes three generations — a useful mental map:

| Generation | Form | Examples |
| --- | --- | --- |
| **1 — External** | Worn on the body | Smartwatches, rings, chest straps, smart glasses |
| **2 — Internal** | Inside the body | Pacemakers, cochlear implants, digital pills, insulin pumps, CGMs |
| **3 — Melded** | Merge with the body while online | Brain-computer interfaces, smart prosthetics wired to nerves |

An entry belongs on this list if it **measures a human** (physiology, biometrics, behavior, or -omics) **and moves that data somewhere** — an app, a cloud, or your own server.

---

## Wearables rings and smartwatches

External, first-generation devices — the largest source of everyday human data.

- ⚪ [Apple Health / HealthKit](https://developer.apple.com/documentation/healthkit) — on-device store aggregating heart rate, activity, ECG, sleep, and dozens of other types; the de-facto hub on iOS. `live + history`
- 🔵 [Health Connect (Android)](https://developer.android.com/health-and-fitness/guides/health-connect) — Google's on-device API that lets fitness and health apps share data with user consent ([samples](https://github.com/android/health-samples)). `live + history`
- ⚪ [Samsung Health](https://developer.samsung.com/health) — Galaxy Watch / Galaxy Ring hub with the [Samsung Health Data SDK](https://developer.samsung.com/health/data). `live + history`
- ⚪ [Oura Ring](https://ouraring.com/) — sleep, HRV, temperature, and readiness, with a [developer API](https://cloud.ouraring.com/docs/). `live + history`
- ⚪ [WHOOP](https://www.whoop.com/) — strain and recovery band with a [public API](https://developer.whoop.com/). `live + history`
- ⚪ [Garmin](https://www.garmin.com/) — GPS and physiology across watches, with a [Health API](https://developer.garmin.com/gc-developer-program/health-api/) for research and [Connect IQ](https://developer.garmin.com/connect-iq/). `live + history`
- ⚪ [Fitbit](https://www.fitbit.com/) — steps, heart rate, and sleep, with a [Web API](https://dev.fitbit.com/build/reference/web-api/). `live + history`
- ⚪ [Withings](https://www.withings.com/) — scales, blood-pressure cuffs, and sleep mats, with a [developer API](https://developer.withings.com/). `live + history`
- ⚪ [Polar](https://www.polar.com/) — training-first watches and HR straps with the [Polar AccessLink API](https://www.polar.com/accesslink-api/). `live + history`
- ⚪ [Suunto](https://www.suunto.com/) — outdoor and sports watches with [Suunto App / Cloud API](https://apizone.suunto.com/). `live + history`
- ⚪ [COROS](https://coros.com/) — endurance sports watches with training and physiology export. `live + history`
- ⚪ [Amazfit / Zepp](https://www.amazfit.com/) — consumer smartwatches and bands via the Zepp app ecosystem. `live + history`
- ⚪ [Huawei Health](https://developer.huawei.com/consumer/en/hms/huawei-healthkit/) — Huawei wearables with [Health Kit](https://developer.huawei.com/consumer/en/doc/HMSCore-Guides/healthkit-introduction-0000001050071670). `live + history`
- ⚪ [Ultrahuman Ring AIR](https://www.ultrahuman.com/) — smart ring for sleep, recovery, and metabolic signals with [partner API docs](https://vision.ultrahuman.com/developer-docs). `live + history`
- ⚪ [Circular Ring](https://www.circular.xyz/) — smart ring focused on sleep and recovery. `live + history`
- ⚪ [RingConn](https://ringconn.com/) — affordable smart ring with sleep and activity metrics. `live + history`
- ⚪ [Biostrap](https://biostrap.com/) — research-grade PPG wearable (wrist and shoe pod) with raw waveform access, [SDK and API](https://biostrap.com/). `live + history`
- ⚪ [Empatica EmbracePlus](https://www.empatica.com/) — medical-grade wristband for seizure and physiological monitoring (E4/Embrace line). `live`
- ⚪ [ActiGraph](https://theactigraph.com/) — research-grade activity monitors widely used in clinical trials. `live + history`
- ⚪ [Google Pixel Watch / Fitbit ecosystem](https://store.google.com/category/watches) — Wear OS health stack feeding Fitbit / Health Connect. `live + history`
- ⚪ [Amazfit Helio Ring](https://www.amazfit.com/) — Zepp ecosystem smart ring for sleep and recovery. `live + history`
- ⚪ [Movano Evie Ring](https://eviering.com/) — women's health-oriented smart ring. `live + history`
- ⚪ [Wyze Watch / Band](https://www.wyze.com/) — budget fitness wearables with app export. `snapshot`
- 🟢 [Gadgetbridge](https://github.com/Freeyourgadget/Gadgetbridge) — Android app that talks to many fitness bands and watches without the vendor cloud, keeping data local. A cornerstone open-source IoB project. `live + history`
- 🟢 [AmazfitBipTools / Zepp tools community](https://codeberg.org/Freeyourgadget/Gadgetbridge) — community reverse-engineering of Amazfit/Zepp protocols (via Gadgetbridge). `live`

---

## Fitness platforms and training

Apps that turn body sensors into training load, routes, and performance history.

- ⚪ [Strava](https://www.strava.com/) — social training platform with a [public API](https://developers.strava.com/) for activities, streams, and segments. `live + history`
- ⚪ [TrainingPeaks](https://www.trainingpeaks.com/) — structured training and TSS with coach-facing analytics and data import/export. `live + history`
- ⚪ [Intervals.icu](https://intervals.icu/) — open-feeling training analytics with a powerful [API](https://intervals.icu/api-docs.html). `live + history`
- ⚪ [Peloton](https://www.onepeloton.com/) — connected fitness classes with heart-rate and workout history. `live + history`
- ⚪ [Zwift](https://www.zwift.com/) — indoor cycling/running virtual world with power and HR streams. `live`
- ⚪ [Wahoo](https://www.wahoofitness.com/) — bike computers and sensors with cloud workout sync. `live + history`
- ⚪ [Concept2](https://www.concept2.com/) — rowing ergometers with [Logbook / API](https://log.concept2.com/). `live + history`
- ⚪ [TrainerRoad](https://www.trainerroad.com/) — structured indoor cycling with power-based metrics. `live + history`
- ⚪ [Runkeeper](https://runkeeper.com/) — GPS running and activity tracking (ASICS). `live + history`
- ⚪ [MapMyRun / MapMyFitness](https://www.mapmyfitness.com/) — Under Armour fitness tracking with route and workout history. `live + history`
- ⚪ [Adidas Running (Runtastic)](https://www.adidas.com/us/running-app) — GPS runs, heart rate, and training plans. `live + history`
- ⚪ [Nike Run Club](https://www.nike.com/nrc-app) — guided runs and activity history. `live + history`
- ⚪ [Hevy](https://www.hevyapp.com/) — strength-training logger with progress charts and export. `live + history`
- ⚪ [Strong](https://www.strong.app/) — weightlifting tracker with workout history. `live + history`
- 🟢 [OpenTracks](https://github.com/OpenTracksApp/OpenTracks) — privacy-friendly open-source sport tracker for Android. `live + history`
- 🟢 [wger](https://github.com/wger-project/wger) — self-hosted workout manager and exercise database. `live + history`
- 🟢 [GoldenCheetah](https://github.com/GoldenCheetah/GoldenCheetah) — open-source cycling and triathlon performance analysis. `snapshot`
- 🟢 [Runalyze](https://runalyze.com/) — detailed running analysis platform with import from many devices. `live + history`

---

## Aggregator and integration APIs

The purest expression of "consume human data via app integrations" — one integration that normalizes many devices into a single schema.

- ⚪ [Terra](https://tryterra.co/) — unified API for 500+ wearables, CGMs, and fitness apps into one schema. `live + history`
- ⚪ [Vital](https://tryvital.io/) — API for wearable and lab data with webhooks and normalized schemas. `live + history`
- ⚪ [Spike](https://spikeapi.com/) — health-data API aggregating wearables and medical devices into one endpoint. `live + history`
- ⚪ [Rook](https://www.tryrook.io/) — health-data API unifying wearables and sensors into a single normalized model. `live + history`
- ⚪ [Validic](https://validic.com/) — enterprise platform connecting clinical programs to consumer health devices and apps. `live + history`
- ⚪ [Human API](https://www.humanapi.co/) — legacy-style health data aggregation for consumer and clinical sources. `live + history`
- ⚪ [Thryve](https://thryve.health/) — European health-data API for wearables and apps (GDPR-oriented). `live + history`
- ⚪ [Point](https://www.ptnt.io/) — wearable data API for developers building health products. `live + history`
- ⚪ [Metriport](https://www.metriport.com/) — open-source-friendly medical record and health-data API (FHIR-oriented). `live + history`
- 🟢 [Open Wearables](https://openwearables.io/) — open-source (MIT) self-hosted platform that unifies wearable data into one API with health intelligence. `live + history`
- ⚪ [Sonar Health](https://www.sonarhealth.co/) — device connectivity layer covering wearables, fitness platforms, and vitals. `live + history`
- ⚪ [HealthSync (appyhapps)](https://play.google.com/store/apps/details?id=nl.appyhapps.healthsync) — Android app that syncs data across Samsung Health, Strava, Garmin, Polar, Oura, and more. `live + history`

---

## Continuous glucose and metabolic

Second-generation sensors that read the body's chemistry in near-real time.

- ⚪ [Dexcom](https://www.dexcom.com/) — CGM with a [developer API](https://developer.dexcom.com/). `live`
- ⚪ [Abbott FreeStyle Libre](https://www.freestyle.abbott/) — widely used flash/continuous glucose monitor (LibreLink / LibreView). `live`
- ⚪ [Medtronic Guardian / MiniMed](https://www.medtronicdiabetes.com/) — CGM and pump systems with CareLink data. `live`
- ⚪ [Senseonics Eversense](https://www.eversense.com/) — long-wear implantable CGM. `live`
- ⚪ [Levels](https://www.levelshealth.com/) — metabolic-health app built on top of CGM hardware. `live + history`
- ⚪ [Nutrisense](https://www.nutrisense.io/) — CGM-based metabolic tracking with dietitian support. `live + history`
- ⚪ [Signos](https://www.signos.com/) — CGM + AI coaching for weight and metabolic health. `live + history`
- ⚪ [Veri](https://www.veri.co/) — metabolic health app pairing CGM with lifestyle insights. `live + history`
- ⚪ [January AI](https://www.january.ai/) — glucose prediction and metabolic coaching. `live + history`
- ⚪ [Supersapiens](https://www.supersapiens.com/) — athlete-oriented glucose monitoring (Abbott Libre Sense). `live`
- ⚪ [Ultrahuman M1](https://www.ultrahuman.com/blood-vision/) — metabolic / blood insights platform alongside the Ring. `live + history`
- ⚪ [Lingo (Abbott)](https://www.hellolingo.com/) — consumer metabolic biosensor brand from Abbott. `live`
- 🟢 [Nightscout](https://github.com/nightscout/cgm-remote-monitor) — the "#WeAreNotWaiting" project: a self-hosted CGM data platform where you own the server and the data. `live`
- 🟢 [OpenAPS](https://github.com/openaps) — open-source "artificial pancreas" reference design that closes the loop between CGM and insulin pump. `live`
- 🟢 [Loop](https://github.com/LoopKit/Loop) — open-source automated insulin-delivery app for iOS. `live`
- 🟢 [AndroidAPS](https://github.com/nightscout/AndroidAPS) — open-source automated insulin delivery for Android. `live`
- 🟢 [Tidepool](https://github.com/tidepool-org) — nonprofit open platform for diabetes data ([tidepool.org](https://www.tidepool.org/)). `live + history`
- 🟢 [xDrip+](https://github.com/NightscoutFoundation/xDrip) — Android app for collecting and sharing CGM data locally. `live`
- 🟢 [Gluroo](https://gluroo.com/) — family-friendly diabetes logging with CGM integrations. `live + history`

---

## Sleep and recovery

- ⚪ [Eight Sleep](https://www.eightsleep.com/) — sensor mattress cover tracking temperature, heart rate, and HRV. `live + history`
- ⚪ [Sleep as Android](https://sleep.urbandroid.org/) — sleep tracking that integrates with many wearables. `live + history`
- ⚪ [Sleep Cycle](https://www.sleepcycle.com/) — phone-based sleep tracking with smart alarm and trends. `live + history`
- ⚪ [Pillow](https://heypillow.com/) — Apple Watch / iOS sleep analysis with stages and export. `live + history`
- ⚪ [Autosleep](https://autosleep.com/) — automatic sleep tracking on Apple Watch. `live + history`
- ⚪ [Sleeptracker-AI](https://sleeptracker.com/) — contactless under-mattress sleep and vital-parameter monitoring with real-time API. `live`
- ⚪ [Withings Sleep](https://www.withings.com/us/en/sleep) — under-mattress sleep mat (part of Withings API). `live + history`
- ⚪ [Dreem / Beacon research line](https://dreem.com/) — EEG sleep headband lineage used in research contexts. `live`
- ⚪ [Somnofy](https://somnofy.com/) — contactless radar-based sleep monitor. `live`
- ⚪ [Emfit QS](https://emfit.com/) — under-mattress ballistocardiography for sleep and HRV. `live + history`

Oura, WHOOP, Ultrahuman, and Garmin (above) all double as primary sleep trackers.

---

## Blood pressure vitals and clinical devices

Connected devices that capture clinical-grade vitals outside the clinic.

- ⚪ [Omron](https://www.omronhealthcare.com/) — connected blood-pressure monitors with app history and partner APIs. `live + history`
- ⚪ [iHealth](https://ihealthlabs.com/) — BP cuffs, pulse oximeters, and scales with cloud API for partners. `live + history`
- ⚪ [QardioArm](https://www.getqardio.com/) — wireless blood-pressure monitor with ECG variants. `live + history`
- ⚪ [Masimo MightySat / W1](https://www.masimo.com/) — medical-grade pulse oximetry and wearable monitoring. `live`
- ⚪ [Nonin](https://www.nonin.com/) — clinical pulse oximeters used in home and hospital settings. `live`
- ⚪ [AliveCor Kardia](https://alivecor.com/) — personal ECG devices with AI rhythm detection. `live + history`
- ⚪ [Eko Health](https://www.ekohealth.com/) — digital stethoscopes with ECG and AI analysis. `live`
- ⚪ [Wellue / Viatom](https://getwellue.com/) — consumer ECG, SpO2, and sleep apnea screening devices. `live + history`
- ⚪ [Tempo / blood-pressure platforms](https://www.hellotempo.com/) — connected hypertension programs (device + coaching). `live + history`
- ⚪ [BodyTrace](https://www.bodytrace.com/) — cellular-connected scales and BP monitors for clinical programs. `live + history`
- ⚪ [Smart Meter](https://www.smartmeterrpm.com/) — cellular RPM devices (glucose, BP, scale, pulse ox). `live + history`

---

## Remote patient monitoring

Platforms that package sensors + clinician workflows for care outside the hospital.

- ⚪ [Biofourmis](https://www.biofourmis.com/) — AI-enabled remote patient management and hospital-at-home. `live`
- ⚪ [HealthSnap](https://healthsnap.io/) — virtual care management with cellular health devices. `live + history`
- ⚪ [Current Health (Best Buy Health)](https://www.currenthealth.com/) — wearable RPM platform for health systems. `live`
- ⚪ [Optimize Health](https://www.optimize.health/) — RPM program software for clinics. `live + history`
- ⚪ [Tenovi](https://www.tenovi.com/) — cellular RPM hub connecting multi-vendor devices. `live`
- ⚪ [Cadence](https://www.cadence.care/) — remote chronic-care platform for cardiometabolic conditions. `live`
- ⚪ [Livongo / Teladoc chronic care](https://www.teladoc.com/) — connected coaching for diabetes, hypertension, and weight. `live + history`
- ⚪ [TytoCare](https://www.tytocare.com/) — home exam kit (throat, heart, lungs, skin, ears) for telehealth. `live`
- ⚪ [BioIntelliSense BioButton](https://biointellisense.com/) — multi-day adhesive patch for continuous vital signs. `live`
- ⚪ [VitalConnect VitalPatch](https://vitalconnect.com/) — clinical wearable biosensor patch. `live`

---

## Womens health fertility and cycle

Hormone, cycle, pregnancy, and fertility tracking — high-sensitivity body data.

- ⚪ [Natural Cycles](https://www.naturalcycles.com/) — FDA-cleared birth-control app using basal body temperature. `live + history`
- ⚪ [Clue](https://helloclue.com/) — cycle and period tracking with science-backed insights. `live + history`
- ⚪ [Flo](https://flo.health/) — period, ovulation, and pregnancy tracking (note past FTC privacy settlement). `live + history`
- ⚪ [Ovia Health](https://www.oviahealth.com/) — fertility, pregnancy, and parenting tracking used by employers/payers. `live + history`
- ⚪ [Tempdrop](https://www.tempdrop.com/) — wearable armband for continuous basal body temperature. `live + history`
- ⚪ [Daysy](https://daysy.me/) — fertility tracker with basal temperature sensor. `live + history`
- ⚪ [Ava Bracelet](https://www.avawomen.com/) — wearable fertility tracker measuring multi-parameter nightly signals. `live + history`
- ⚪ [Mira](https://www.miracare.com/) — at-home hormone monitor with quantitative LH/E3G/PdG. `snapshot`
- ⚪ [Inito](https://www.inito.com/) — fertility hormone monitor with PdG confirmation. `snapshot`
- ⚪ [Glow](https://glowing.com/) — fertility and pregnancy tracking suite. `live + history`
- ⚪ [Kindara](https://www.kindara.com/) — fertility awareness charting. `live + history`
- ⚪ [Premom](https://premom.com/) — ovulation-test reading and fertility tracking. `live + history`

---

## Mental health mood and symptoms

Apps that log subjective state — mood, pain, symptoms — as first-class body data.

- ⚪ [Bearable](https://bearable.app/) — customizable symptom, mood, and factor tracking with correlations. `live + history`
- ⚪ [Daylio](https://daylio.net/) — micro-mood journal with activity tags and trends. `live + history`
- ⚪ [Moodpath / MindDoc](https://minddoc.com/) — structured mood assessments and journaling. `live + history`
- ⚪ [Sanvello](https://www.sanvello.com/) — mood tracking with CBT tools. `live + history`
- ⚪ [Woebot](https://woebothealth.com/) — conversational CBT with check-in data. `live + history`
- ⚪ [Headspace](https://www.headspace.com/) — meditation app with session history and stress tools. `live + history`
- ⚪ [Calm](https://www.calm.com/) — sleep and meditation with engagement history. `live + history`
- ⚪ [How We Feel](https://howwefeel.org/) — emotion-logging app from the Yale Center for Emotional Intelligence. `live + history`
- ⚪ [Migraine Buddy](https://migrainebuddy.com/) — headache and migraine trigger tracking. `live + history`
- ⚪ [Chronic Insights / Flaredown](https://flaredown.com/) — open-feeling chronic-illness symptom tracker. `live + history`
- ⚪ [eMoods](https://emoodtracker.com/) — bipolar and mood charting with export for clinicians. `live + history`
- ⚪ [PTSD Coach](https://www.ptsd.va.gov/appvid/mobile/ptsdcoach_app.asp) — VA symptom-management app with self-assessment tools. `live + history`

---

## Open-source health-data tooling

Projects you can read, run, and self-host. Nightscout, Loop, AndroidAPS, xDrip+, Gadgetbridge, and OpenTracks (above) also belong here.

- 🟢 [Home Assistant](https://github.com/home-assistant/core) — local-first automation platform with many health and wearable integrations; a common place people pool body data at home. `live`
- 🟢 [Open mHealth](https://github.com/openmhealth) — open schemas and libraries that normalize mobile health data across sources.
- 🟢 [ResearchKit](https://github.com/ResearchKit/ResearchKit) — Apple's open framework for building medical-research apps that collect participant data.
- 🟢 [CareKit](https://github.com/carekit-apple/CareKit) — Apple's open framework for care and symptom-tracking apps.
- 🟢 [Open Scale](https://github.com/oliexdev/openScale) — open-source Bluetooth body-scale app supporting many hardware brands. `live + history`
- 🟢 [FitoTrack](https://codeberg.org/jannis/FitoTrack) — privacy-oriented outdoor workout tracker for Android. `live + history`
- 🟢 [Health Connect tools / health-samples](https://github.com/android/health-samples) — official Android samples for reading and writing health data.
- 🟢 [GarminDB](https://github.com/tcgoetz/GarminDB) — download and analyze your Garmin data locally. `snapshot`
- 🟢 [FitbitExport / community exporters](https://github.com/aricooperdavis/fitbit-export) — scripts to pull personal Fitbit archives. `snapshot`
- 🟢 [PhysioZoo](https://github.com/PhysioZoo) — open-source platform for heart-rate variability analysis of physiological signals.
- 🟢 [WFDB (PhysioNet)](https://github.com/MIT-LCP/wfdb-python) — Waveform Database software for PhysioNet physiological signals.
- 🟢 [HeartPy](https://github.com/paulvangentcom/heartrate_analysis_python) — open-source PPG/ECG heart-rate analysis toolkit.
- 🟢 [NeuroKit2](https://github.com/neuropsychology/NeuroKit) — Python toolbox for neurophysiological signal processing.
- 🟢 [MNE-Python](https://github.com/mne-tools/mne-python) — open-source EEG/MEG analysis platform.
- 🟢 [hapi-server / FHIR servers](https://github.com/hapifhir/hapi-fhir) — open-source FHIR server for health-data exchange.

---

## Personal data platforms and Quantified Self

Platforms whose whole purpose is aggregating your body data — for yourself or for research.

- 🟢 [Open Humans](https://github.com/OpenHumans) — nonprofit platform ([openhumans.org](https://www.openhumans.org/)) to aggregate personal data (wearables, genomes, microbiome) and optionally donate it to research. `snapshot`
- ⚪ [Exist.io](https://exist.io/) — correlates data from many trackers to surface personal patterns. `live + history`
- ⚪ [Gyroscope](https://gyrosco.pe/) — polished multi-tracker dashboard for body and life data. `live + history`
- ⚪ [Welltory](https://welltory.com/) — HRV and stress analytics from phone camera or wearables. `live + history`
- ⚪ [Athlytic](https://athlyticapp.com/) — Apple Health–centric training load and recovery dashboard. `live + history`
- ⚪ [Bevel](https://www.bevel.health/) — modern recovery and readiness dashboard over HealthKit. `live + history`
- ⚪ [Gentler Streak](https://gentler.stories.studio/) — recovery-aware activity coaching on Apple Watch. `live + history`
- ⚪ [Echo](https://www.echo.so/) — AI health companion over wearable and lab data. `live + history`
- 🟢 [Quantified Self](https://quantifiedself.com/) — the movement that named "self-knowledge through numbers"; see the community's [tools directory](https://quantifiedself.com/tools/).
- 🟢 [Personal Science / Open Humans projects](https://www.openhumans.org/activity/) — self-research projects built on personal data imports. `snapshot`
- ⚪ [InsideTracker](https://www.insidetracker.com/) — blood-biomarker analysis tied to lifestyle recommendations. `snapshot`
- ⚪ [Function Health](https://www.functionhealth.com/) — broad lab panels with longitudinal biomarker tracking. `snapshot`
- ⚪ [Superpower](https://www.superpower.com/) — membership for labs, wearables, and health data in one place. `live + history`
- ⚪ [Levels (lab + CGM stack)](https://www.levelshealth.com/) — metabolic membership combining CGM and blood work. `live + history`

---

## Health-data standards and SDKs

The plumbing that lets body data move between systems — what makes IoB an internet.

- 🔵 [HL7 FHIR](https://github.com/HL7/fhir) — the dominant open standard for exchanging clinical and health data.
- 🔵 [Open mHealth schemas](https://www.openmhealth.org/documentation/) — normalized JSON schemas for mobile health signals.
- 🔵 [SMART on FHIR](https://github.com/smart-on-fhir) — OAuth-secured apps that plug into electronic health records.
- 🔵 [openEHR](https://www.openehr.org/) — open specifications for future-proof electronic health records.
- 🔵 [IEEE 11073](https://standards.ieee.org/ieee/11073-10407/10633/) — personal health device communication standards (BP, glucose, scales, etc.).
- 🔵 [Bluetooth SIG GATT health profiles](https://www.bluetooth.com/specifications/specs/) — heart-rate, glucose, BP, and related BLE profiles.
- 🔵 [OMH / CommonHealth](https://www.thecommonhealth.org/) — Android personal health record bridging clinical and consumer data.
- 🔵 [Argonaut / US Core FHIR profiles](https://www.hl7.org/fhir/us/core/) — US baseline FHIR profiles for patient access.
- 🔵 [GA4GH](https://www.ga4gh.org/) — genomic data standards and APIs for secure sharing.
- 🔵 [PhysioNet / WFDB formats](https://physionet.org/) — open repositories and formats for physiological signal research.

Apple HealthKit and Google Health Connect (both above) are the two dominant on-device SDKs.

---

## Genomics microbiome and omics

Slower-moving but deeply personal body data.

- 🟢 [openSNP](https://github.com/openSNP/snpr) — open database where people share their genotype and phenotype data. `snapshot`
- 🟢 [Promethease / SNPedia lineage](https://www.snpedia.com/) — community genetics knowledge base used with DTC genotype files. `snapshot`
- 🟢 [Open Humans genetics projects](https://www.openhumans.org/) — pipelines for importing 23andMe, Ancestry, and WGS data. `snapshot`
- ⚪ [Nebula Genomics](https://nebula.org/) — whole-genome sequencing with a privacy-forward pitch. `snapshot`
- ⚪ [23andMe](https://www.23andme.com/) — consumer genetics; note its 2023–2025 data-breach and bankruptcy saga, a cautionary IoB privacy case study. `snapshot`
- ⚪ [AncestryDNA](https://www.ancestry.com/dna/) — consumer genetics with large relative-matching network. `snapshot`
- ⚪ [MyHeritage DNA](https://www.myheritage.com/dna) — consumer genetics and health reports (region-dependent). `snapshot`
- ⚪ [Color Health](https://www.color.com/) — clinical-grade genetic testing for hereditary disease risk. `snapshot`
- ⚪ [Invitae](https://www.invitae.com/) — clinical genetic testing (note corporate restructuring — verify current status). `snapshot`
- ⚪ [Viome](https://www.viome.com/) — microbiome and metabolic testing tied to a nutrition app. `snapshot`
- ⚪ [ZOE](https://zoe.com/) — microbiome and blood-fat testing paired with personalized nutrition. `snapshot`
- ⚪ [Thorne](https://www.thorne.com/) — microbiome and biomarker testing with supplement personalization. `snapshot`
- ⚪ [Ombre (formerly Thryve Inside)](https://www.ombrelab.com/) — gut microbiome testing. `snapshot`
- ⚪ [Sequencing.com](https://sequencing.com/) — personal genome app marketplace and storage. `snapshot`
- ⚪ [Dante Labs](https://www.dantelabs.com/) — consumer whole-genome sequencing. `snapshot`

---

## Neuro brain-computer and implantables

Third-generation, melded devices — the frontier, and the sharpest ethics.

- 🟢 [OpenBCI](https://github.com/OpenBCI) — open-source hardware and software for EEG, EMG, and ECG biosensing. The accessible on-ramp to neural IoB. `live`
- ⚪ [Neuralink](https://neuralink.com/) — implanted brain-computer interface. `live`
- ⚪ [Synchron](https://synchron.com/) — endovascular BCI implanted via blood vessels, no open-skull surgery. `live`
- ⚪ [Blackrock Neurotech](https://blackrockneurotech.com/) — research and clinical invasive BCI systems. `live`
- ⚪ [Precision Neuroscience](https://precisionneuro.io/) — thin-film cortical interface BCI. `live`
- ⚪ [Paradromics](https://www.paradromics.com/) — high-data-rate implantable BCI. `live`
- ⚪ [Medtronic](https://www.medtronic.com/) — connected pacemakers, insulin pumps, and neurostimulators; a huge share of real-world generation-2 IoB. `live + history`
- ⚪ [Boston Scientific](https://www.bostonscientific.com/) — connected CRM and neuromodulation devices. `live + history`
- ⚪ [Abbott Neuromodulation](https://www.neuromodulation.abbott/) — spinal cord and deep-brain stimulation systems. `live + history`
- ⚪ [Cochlear](https://www.cochlear.com/) — cochlear implants with wireless streaming and app control. `live`
- ⚪ [Muse](https://choosemuse.com/) — consumer EEG headband for meditation and research SDKs. `live`
- ⚪ [Emotiv](https://www.emotiv.com/) — multi-channel EEG headsets with BCI software and APIs. `live`
- ⚪ [Neurosity Crown](https://neurosity.co/) — developer-friendly EEG wearable with JS/Python SDK. `live`
- ⚪ [Kernel](https://www.kernel.com/) — non-invasive TD-fNIRS brain imaging (Flow). `live`
- ⚪ [Neurable](https://neurable.com/) — EEG-enabled headphones for attention and cognitive metrics. `live`
- ⚪ [NextMind (Snap)](https://www.nextmind.com/) — non-invasive visual BCI (acquired by Snap). `live`
- ⚪ [CTRL-labs (Meta)](https://about.fb.com/news/2019/09/facebook-to-acquire-ctrl-labs/) — neural wrist interface research at Reality Labs. `live`
- ⚪ [g.tec](https://www.gtec.at/) — research-grade BCI and neurotechnology systems. `live`

---

## Nutrition and food logging

Apps that log what goes into the body — the input side of the human-data picture.

- 🟢 [Open Food Facts](https://github.com/openfoodfacts) — open, crowd-sourced database of foods and their labels ([openfoodfacts.org](https://world.openfoodfacts.org/)).
- ⚪ [Cronometer](https://cronometer.com/) — micronutrient-accurate food and biometric logging with an [API](https://cronometer.com/api/). `live + history`
- ⚪ [MyFitnessPal](https://www.myfitnesspal.com/) — large-scale food and exercise logging. `live + history`
- ⚪ [Lose It!](https://www.loseit.com/) — calorie tracking with barcode scan and trends. `live + history`
- ⚪ [Carb Manager](https://www.carbmanager.com/) — low-carb / keto macro tracking. `live + history`
- ⚪ [MacroFactor](https://macrofactorapp.com/) — adaptive TDEE and macro coaching. `live + history`
- ⚪ [FatSecret](https://www.fatsecret.com/) — food diary with a [platform API](https://platform.fatsecret.com/). `live + history`
- ⚪ [MyNetDiary](https://www.mynetdiary.com/) — food logging with diabetes-friendly features. `live + history`
- ⚪ [Lifesum](https://lifesum.com/) — diet plans and nutrition tracking. `live + history`
- ⚪ [Yazio](https://www.yazio.com/) — calorie counter popular in Europe. `live + history`
- ⚪ [Noom](https://www.noom.com/) — behavior-change weight program with daily logging. `live + history`
- ⚪ [Zero](https://www.zerofasting.com/) — intermittent-fasting tracker. `live + history`
- ⚪ [Ate Food Diary](https://www.ate.food/) — photo-first mindful food journaling. `live + history`
- 🟢 [Open Nutritional Database projects](https://fdc.nal.usda.gov/) — USDA FoodData Central as an open nutrition reference API. `snapshot`

---

## Contactless ambient and smart clothing

Sensors that measure the body without a classic watch or implant.

- ⚪ [Amazon Halo / discontinued lineage](https://www.amazon.com/gp/help/customer/display.html?nodeId=G3N4Z3A3HJAFW4WV) — body composition and tone analysis (mostly sunset; listed as historical IoB case). `snapshot`
- ⚪ [Hexoskin](https://www.hexoskin.com/) — smart shirts with ECG, breathing, and activity sensors for research. `live`
- ⚪ [Whoop Body (apparel partners)](https://www.whoop.com/) — biometric apparel integrations around WHOOP sensors. `live`
- ⚪ [Sensoria](https://www.sensoriafitness.com/) — smart socks and garments for gait and running form. `live`
- ⚪ [Athos](https://www.liveathos.com/) — EMG smart clothing for muscle activation (historical / limited availability). `live`
- ⚪ [Nadi X](https://www.wearablex.com/) — haptic yoga pants with form guidance. `live`
- ⚪ [Spire Health](https://www.spirehealth.com/) — respiratory and activity patches for clinical RPM. `live`
- ⚪ [Xsens / Movella](https://www.movella.com/) — full-body motion-capture wearables. `live`
- ⚪ [Notch Interfaces](https://wearnotch.com/) — wearable motion-capture sensors. `live`
- ⚪ [Google Soli / Nest Hub sensing](https://atap.google.com/soli/) — radar-based sleep and presence sensing on Nest Hub. `live`
- ⚪ [Fullpower MotionX Sleeptracker](https://www.fullpower.com/) — contactless sleep sensing platform powering Sleeptracker-AI products. `live`

---

## Hearing vision and sensory

Sense organs as networked endpoints.

- ⚪ [Starkey](https://www.starkey.com/) — hearing aids with health sensors (activity, fall detection) and app telemetry. `live`
- ⚪ [Phonak / Sonova](https://www.phonak.com/) — connected hearing aids with remote fitting and usage data. `live`
- ⚪ [Oticon](https://www.oticon.com/) — smart hearing aids with app control and logging. `live`
- ⚪ [Apple Hearing Health (AirPods)](https://support.apple.com/en-us/HT210399) — headphone audio levels and hearing tests in HealthKit. `live + history`
- ⚪ [Nuance Audio / EssilorLuxottica](https://www.essilorluxottica.com/) — hearing-aid glasses bridging vision and hearing tech. `live`
- ⚪ [OrCam](https://www.orcam.com/) — vision-assist wearables that narrate the visual world. `live`
- ⚪ [eSight](https://www.esighteyewear.com/) — electronic eyewear for low vision. `live`

---

## Privacy ethics and data ownership

Body data is the most sensitive data there is. Any honest IoB list must point here.

- 🟢 [Solid](https://github.com/solid/solid) — Tim Berners-Lee's protocol for personal data "pods" you control ([inrupt.com](https://www.inrupt.com/)).
- ⚪ [MyData Global](https://www.mydata.org/) — nonprofit advancing human-centric personal-data rights.
- 🟢 [Dataswift / HAT](https://www.dataswift.io/) — personal data account infrastructure (HAT model).
- 🟢 [OpenMined](https://github.com/OpenMined) — open-source tools for privacy-preserving AI on sensitive data.
- 🟢 [Differential Privacy libraries (Google)](https://github.com/google/differential-privacy) — tools for publishing statistics without exposing individuals.
- ⚪ [Patient Privacy Rights](https://patientprivacyrights.org/) — advocacy for medical privacy.
- ⚪ [Electronic Frontier Foundation — health privacy](https://www.eff.org/issues/health-privacy) — civil-liberties guidance on health data.
- ⚪ [HIPAA Journal](https://www.hipaajournal.com/) — breach tracking and compliance news for health data.

**Questions worth asking of any entry above:** where does the data live, can you export or delete it, who can it be sold or subpoenaed to, and what happens to it if the company folds? (The 23andMe collapse is the canonical worked example.)

---

## Further reading

- [Purdue Center for the Internet of Bodies (C-IoB)](https://engineering.purdue.edu/C-IoB)
- [RAND — The Internet of Bodies](https://www.rand.org/pubs/research_reports/RR3226.html)
- [Andrea M. Matwyshyn — The Internet of Bodies](https://www.williamette.edu/law/resources/journals/wlr/pdf/volume-55/55-1matwyshyn.pdf) (law review framing of the term)
- [FDA — Digital Health Center of Excellence](https://www.fda.gov/medical-devices/digital-health-center-excellence)
- [ONC / HealthIT.gov — Patient access APIs](https://www.healthit.gov/)
- [PhysioNet](https://physionet.org/) — open physiological signal databases
- [Awesome Open Source Medical Devices](https://github.com/openelab/awesome-open-source-medical-devices) (related hardware list)

---

## Related projects

- [biology-as-code](https://github.com/murffious/biology_as_code) — Models what a body does with its inputs (digestion, absorption, metabolic pathways) as versioned, provenance-tracked code. This list is its natural sensor-layer companion: the integrations catalogued here are where the real signals would come from.

---

## Contributing

Contributions are welcome — this list is a living map, not a finished atlas. See [contributing guidelines](CONTRIBUTING.md).

In short, an entry must:

1. Gather human data (physiology, biometrics, behavior, or -omics)
2. Be real and verifiable with a working link
3. Prefer open-source or open-standard projects when possible
4. Carry a cadence tag where it is a data feed
5. Use no fabricated links or claims

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, this list is dedicated to the public domain under [CC0 1.0](LICENSE).
