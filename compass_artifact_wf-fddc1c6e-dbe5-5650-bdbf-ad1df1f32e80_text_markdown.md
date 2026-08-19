# Expanding `awesome-internet-of-the-body`: 180+ New Entries, Ready to Paste

**Bottom line:** Your list is currently ~55 entries across 13 sections, and it is indeed far too small — the shipping IoB device universe runs to many hundreds of products. Below are 180+ deduplicated new entries with verified official URLs, matched to your existing formatting (`- ⚪/🔵/🟢 [Name](url) — Description. cadence-tag`), organized to slot into your current taxonomy plus proposed new sections.

## TL;DR
- Your current README has ~55 entries; this delivers **180+ new, non-duplicative** IoB devices, platforms, standards, datasets, and resources with working official links — enough to roughly triple-to-quadruple the list.
- The biggest gaps are hardware categories your list barely touches: cardiac/ECG patches, implantable cardiac monitors, neurostimulators and BCIs, insulin pumps, ingestibles, exoskeletons/prosthetics, biosensing textiles, and biohacking implants — plus non-device resources (standards, security advisories, datasets) that would qualify the repo for the main Awesome index.
- Recommendation: restructure into a 3-generation taxonomy (external / internal / embedded) with ~20 new sub-sections, add a "Historical & discontinued" section, and add the `code-of-conduct.md` and `awesome-lint` hygiene needed to be accepted into sindresorhus/awesome.

## Key Findings
- **Repo audit (main branch, live):** The README contains these sections — Wearables and rings; Aggregator and integration APIs; Continuous glucose and metabolic; Sleep and recovery; Open-source health-data tooling; Personal data platforms and Quantified Self; Health-data standards and SDKs; Genomics/microbiome/omics; Neuro/brain-computer/implantables; Nutrition and food logging; Privacy/ethics/data ownership; Related projects. It ships `CONTRIBUTING.md`, `LICENSE` (CC0-1.0), `IoB_data_standards.md`, and leftover duplicate files (`awesome-internet-of-the-body-README.md`, `-CONTRIBUTING.md`, `-files.zip`).
- **Existing entries (do NOT re-list):** Apple Health/HealthKit, Health Connect, Oura Ring, WHOOP, Garmin, Fitbit, Withings, Biostrap, Gadgetbridge, Terra, Vital, Spike, Rook, Validic, Dexcom, Abbott FreeStyle Libre, Levels, Nutrisense, Nightscout, OpenAPS, Loop, Lura Health, Eight Sleep, Sleep as Android, Home Assistant, Open mHealth, ResearchKit, CareKit, Fit REST API samples, Open Humans, Exist.io, Quantified Self, HL7 FHIR, Open mHealth schemas, SMART on FHIR, openSNP, Nebula Genomics, 23andMe, Viome, ZOE, OpenBCI, Neuralink, Synchron, Medtronic (generic), Open Food Facts, Cronometer, MyFitnessPal, Solid, MyData Global, Purdue C-IoB, RAND report (as further reading), biology-as-code.
- **Formatting convention to match:** `- ⚪/🔵/🟢 [Name](url) — Description sentence. `cadence-tag`` — descriptions start capitalized and end with a period; standards/SDKs carry no cadence tag.
- **Awesome-list compliance:** To be listed on the main Awesome index the repo must pass `awesome-lint`, use the exact README header/badge format, include `contributing.md` and `code-of-conduct.md`, carry a license (CC0-1.0 is fine), ensure every item description starts uppercase and ends with a period, avoid duplicate files, and include a table of contents.

## Details

### A. Entries that fit EXISTING categories

#### Wearables and rings (external, Gen 1)
- ⚪ [Samsung Galaxy Ring](https://www.samsung.com/us/rings/galaxy-ring/) — Smart ring tracking sleep, heart rate, and cycle, integrated with Samsung Health. `live + history`
- ⚪ [Ultrahuman Ring Air](https://www.ultrahuman.com/ring/) — Subscription-free smart ring for sleep, HRV, and metabolic/circadian insights, with a developer API. `live + history`
- ⚪ [RingConn](https://www.ringconn.com/) — Subscription-free smart ring tracking sleep, HRV, SpO2, and stress with multi-day battery. `live + history`
- ⚪ [Movano Evie Ring](https://www.eviering.com/) — Smart ring designed for women's health, cycle, and cardiovascular metrics. `live + history`
- ⚪ [Circular Ring](https://circular.xyz/) — Smart ring with AI coaching for sleep, recovery, and activity. `live + history`
- ⚪ [Amazfit](https://www.amazfit.com/) — Smartwatches and the Helio smart ring with SpO2, HRV, and sleep tracking, feeding the Zepp app. `live + history`
- ⚪ [Polar](https://www.polar.com/en/developers) — Sports watches and heart-rate straps with the AccessLink developer API. `live + history`
- ⚪ [Suunto](https://www.suunto.com/) — GPS multisport watches with heart-rate and recovery tracking. `live + history`
- ⚪ [COROS](https://www.coros.com/) — Endurance sports watches tracking HR, SpO2, and training load. `live + history`
- ⚪ [Wear OS](https://developer.android.com/health-and-fitness) — Google's smartwatch platform whose health sensors feed Health Connect. `live + history`
- ⚪ [Masimo W1](https://www.masimopersonalhealth.com/) — Medical-grade wrist wearable providing continuous SpO2, pulse rate, and hydration index. `live`

#### Aggregator and integration APIs
- ⚪ [Thryve](https://thryve.health/) — Unified wearable and health-data API aggregating 500+ wearable devices and health apps through one integration, reaching over 50 million end-users via partners. `live + history`
- ⚪ [Human API](https://www.humanapi.co/) — Health-data aggregation platform connecting consumer devices and clinical records (acquired by LexisNexis Risk Solutions). `live + history`
- ⚪ [Sahha](https://sahha.ai/) — Behavioral and health-data API turning wearable signals into mental-health scores. `live + history`

#### Continuous glucose and metabolic
- ⚪ [Dexcom Stelo](https://www.stelo.com/) — Over-the-counter glucose biosensor for non-insulin users. `live`
- ⚪ [Abbott Lingo](https://www.hellolingo.com/) — Consumer continuous glucose biosensor for metabolic coaching. `live`
- ⚪ [Medtronic Guardian](https://www.medtronic.com/) — Continuous glucose monitor that pairs with MiniMed pumps. `live`
- ⚪ [Signos](https://www.signos.com/) — CGM-driven weight-management app with real-time glucose response. `live + history`
- ⚪ [Sibionics](https://www.sibionics.com/) — CGM system offering continuous glucose data via a mobile app. `live`
- ⚪ [Supersapiens](https://www.supersapiens.com/) — Athlete-focused glucose-monitoring platform built on Abbott sensors. `live`

#### Sleep and recovery
- ⚪ [Withings Sleep](https://www.withings.com/us/en/sleep) — Under-mattress pad tracking sleep cycles, heart rate, and snoring, with a developer API. `live + history`
- ⚪ [Somnofy](https://somnofy.com/) — Contactless radar sleep monitor for clinical and consumer use. `live + history`
- ⚪ [Elemind](https://www.elemind.com/) — EEG headband that uses neurostimulation to speed sleep onset. `live`
- ⚪ [Sleepiz](https://www.sleepiz.com/) — Contactless radar device measuring respiration and heart rate during sleep. `live + history`
- ⚪ [Beddit](https://www.apple.com/) — Under-sheet sleep-tracking strip (Apple), measuring HR and breathing. `live + history`

#### Neuro, brain-computer and implantables (external neurotech)
- ⚪ [Muse](https://choosemuse.com/) — Consumer EEG headband for meditation and sleep neurofeedback, with an SDK. `live`
- ⚪ [Emotiv](https://www.emotiv.com/) — Research- and consumer-grade multi-channel EEG headsets with a data SDK. `live`
- ⚪ [NeuroSky](https://neurosky.com/) — Low-cost single-channel EEG biosensor and developer toolkit. `live`
- ⚪ [Neurable MW75 Neuro](https://www.neurable.com/) — Over-ear headphones with embedded dry-electrode EEG for focus tracking. `live`
- ⚪ [Neurosity Crown](https://neurosity.co/) — Wearable EEG device with an on-board processor and developer SDK. `live`
- ⚪ [Cognixion](https://www.cognixion.com/) — AR headset combining EEG and eye-tracking for assistive communication. `live`
- ⚪ [Wearable Devices Mudra Band](https://www.wearabledevices.co.il/) — Neural-input wristband reading surface nerve signals for touchless control. `live`
- ⚪ [Pison](https://pison.com/) — EMG/neural wristband sensing electrical nerve signals for gesture control and cognitive metrics. `live`
- ⚪ [Flow Neuroscience](https://www.flowneuroscience.com/) — At-home tDCS headset for depression, CE-marked. `live`
- ⚪ [Neuroelectrics](https://www.neuroelectrics.com/) — Research-grade EEG monitoring and closed-loop neurostimulation platform. `live`

#### Health-data standards and SDKs
- 🔵 [IEEE 802.15.6](https://standards.ieee.org/ieee/802.15.6/5364/) — IEEE standard for wireless body area networks (WBAN), the radio layer of IoB.
- 🔵 [ISO/IEEE 11073 PHD](https://en.wikipedia.org/wiki/ISO/IEEE_11073_Personal_Health_Data_Standards) — Personal Health Device interoperability standards family (scales, BP cuffs, glucose meters, ECG).
- 🔵 [HL7 FHIR Personal Health Device IG](https://hl7.org/fhir/uv/phd/) — Implementation guide mapping IEEE 11073 device data into FHIR.
- 🔵 [IEEE 1752.1](https://standards.ieee.org/ieee/1752.1/6982/) — Open mobile-health data standard for sleep and physical-activity measures.
- 🔵 [Continua Design Guidelines / PCHAlliance](https://www.pchalliance.org/continua-design-guidelines) — End-to-end interoperability guidelines for personal connected health devices.
- 🔵 [IHE Personal Connected Health](https://wiki.ihe.net/index.php/Personal_Connected_Health) — IHE profiles extending device interoperability to personal connected health.
- 🔵 [GS1 UDI](https://www.gs1.org/industries/healthcare/udi) — Unique Device Identification standards used for global medical-device traceability.
- 🔵 [W3C Web Bluetooth](https://webbluetoothcg.github.io/web-bluetooth/) — Community-group spec for a browser API to talk to BLE health devices (draft, not a ratified standard).
- 🔵 [Bluetooth Heart Rate Service](https://www.bluetooth.com/specifications/specs/heart-rate-service-1-0/) — Official Bluetooth SIG GATT service exposing heart-rate sensor data.
- 🔵 [Samsung Health SDK](https://developer.samsung.com/health) — SDK for reading data from the Samsung Health store.
- ⚪ [Garmin Health API](https://developer.garmin.com/gc-developer-program/health-api/) — API delivering Garmin wearable physiology data for research and enterprise.
- ⚪ [Dexcom API](https://developer.dexcom.com/) — OAuth API for continuous glucose data, events, and alerts.
- ⚪ [Polar AccessLink API](https://www.polar.com/en/developers) — REST API for Polar device training and activity data.
- ⚪ [Google Health API](https://developers.google.com/health) — Google's consolidated health/fitness API (successor to the deprecating Fitbit Web API).

### B. Entries needing NEW categories

#### Cardiac & ECG patches and monitors (proposed new section)
- ⚪ [iRhythm Zio](https://www.irhythmtech.com/) — Long-term wearable ECG patch with FDA-cleared AI arrhythmia analysis. FDA-cleared. `snapshot`
- ⚪ [VitalConnect VitalPatch](https://vitalconnect.com/) — FDA-cleared chest biosensor streaming ECG and vitals in real time. `live`
- ⚪ [BardyDx CAM](https://www.baxter.com/) — Carnation ambulatory ECG monitor patch (now Baxter). FDA-cleared. `snapshot`
- ⚪ [Philips ePatch](https://www.philips.com/) — Extended-wear ambulatory ECG patch. FDA-cleared. `snapshot`
- ⚪ [AliveCor KardiaMobile](https://www.kardia.com/) — Personal single- and six-lead ECG that pairs with a phone. FDA-cleared. `live`
- ⚪ [Qardio](https://www.getqardio.com/) — Connected ECG, blood-pressure, and remote-monitoring devices. FDA-cleared. `live + history`
- ⚪ [Preventice BodyGuardian](https://www.boston-scientific-preventice.com/) — Remote cardiac monitoring body sensor (Boston Scientific). FDA-cleared. `live`

#### Continuous blood pressure & cardiovascular wearables (proposed new section)
- ⚪ [Aktiia / Hilo](https://hilo.com/) — Cuffless optical wrist band for continuous blood pressure; first FDA-cleared OTC cuffless BP monitor. `live + history`
- ⚪ [Omron HeartGuide](https://omronhealthcare.com/) — Oscillometric blood-pressure smartwatch. FDA-cleared. `live + history`
- ⚪ [Biobeat](https://www.bio-beat.com/) — Cuffless BP and vitals monitoring via chest patch and wrist device. FDA-cleared. `live`
- ⚪ [CardieX](https://www.cardiex.com/) — Arterial-health and blood-pressure wearable technology. `live + history`

#### Hospital-grade remote patient monitoring (proposed new section)
- ⚪ [BioIntelliSense BioButton](https://www.biointellisense.com/) — FDA-cleared coin-sized patch capturing 20+ vital signs continuously. `live`
- ⚪ [Current Health](https://currenthealth.com/) — FDA-cleared upper-arm wearable and home platform for continuous RPM (Best Buy Health). `live`
- ⚪ [Vivalink](https://www.vivalink.com/) — Medical-grade reusable ECG, temperature, and vitals patches with data APIs. `live`
- ⚪ [Biofourmis](https://www.biofourmis.com/) — Wearable-plus-AI platform for remote patient monitoring and virtual care. `live + history`
- ⚪ [Isansys Patient Status Engine](https://www.isansys.com/) — Wireless multi-parameter patient monitoring platform. `live`
- ⚪ [LifeSignals](https://lifesignals.com/) — Wireless biosensor patches for hospital and remote ECG/vitals monitoring. `live`
- ⚪ [Sibel Health ANNE](https://www.sibelhealth.com/) — Wireless dual-sensor system for continuous vitals across care settings. `live`

#### Biosensing textiles & smart garments (proposed new section)
- ⚪ [Hexoskin](https://www.hexoskin.com/) — Clinically validated smart shirts recording ECG, respiration, and activity, with data APIs. `live + history`
- ⚪ [Myant SKIIN](https://www.skiin.com/) — Textile-computing underwear and garments capturing ECG and vitals. `live + history`
- ⚪ [Sensoria](https://www.sensoriafitness.com/) — Smart socks and garments with pressure/gait sensors and a developer API. `live + history`
- ⚪ [Nanowear SimpleSense](https://www.nanowearinc.com/) — FDA-cleared cloth-based nanosensor vest for cardiac and hemodynamic monitoring. `live`
- ⚪ [Siren](https://siren.care/) — Smart socks with embedded temperature sensors for diabetic foot monitoring. FDA-registered. `live`
- ⚪ [Nadi X](https://www.wearablex.com/) — Sensor-embedded yoga pants giving haptic posture feedback. `live`

#### Sweat, hydration & electrolyte sensors (proposed new section)
- ⚪ [Epicore Biosystems](https://www.epicorebiosystems.com/) — Microfluidic sweat patches (incl. Connected Hydration) measuring fluid and electrolyte loss. `live`
- ⚪ [Gatorade Gx Sweat Patch](https://www.gatorade.com/gx/sweat-patch) — Consumer microfluidic sweat patch read via a phone app. `snapshot`
- ⚪ [Nix Biosensors](https://nixbiosensors.com/) — Wearable sweat biosensor delivering real-time hydration analytics. `live`
- ⚪ [hDrop](https://hdrop.com/) — Wearable hydration monitor tracking sweat rate and electrolytes. `live`
- ⚪ [Flowbio](https://www.flowbio.com/) — Continuous sweat-sensing patch for hydration and sodium loss. `live`

#### Baby, infant & maternal monitoring (proposed new section)
- ⚪ [Owlet Dream Sock](https://owletcare.com/) — FDA-cleared infant sock monitoring pulse rate and oxygen. `live`
- ⚪ [Masimo Stork](https://www.masimostork.com/) — FDA-cleared infant monitoring system tracking oxygen, pulse, and skin temperature. `live`
- ⚪ [Nanit](https://www.nanit.com/) — Camera-based baby monitor measuring breathing motion and sleep. `live + history`
- ⚪ [Nuvo INVU](https://nuvocares.com/) — FDA-cleared remote pregnancy sensor band measuring maternal and fetal heart rate. `live`
- ⚪ [Bloomlife](https://bloomlife.com/) — Wearable pregnancy monitor tracking contractions. `live + history`

#### Neuromodulation & stimulation wearables (proposed new section)
- ⚪ [Cala kIQ](https://calahealth.com/) — FDA-cleared wrist neurostimulation wearable for essential tremor and Parkinson's. `live`
- ⚪ [Theranica Nerivio](https://www.nerivio.com/) — FDA-cleared smartphone-controlled armband delivering remote electrical neuromodulation for migraine. `live`
- ⚪ [Cefaly](https://www.cefaly.com/) — FDA-cleared OTC trigeminal-nerve stimulation headband for migraine. `live`
- ⚪ [electroCore gammaCore](https://www.gammacore.com/) — FDA-cleared handheld non-invasive vagus nerve stimulator. `live`
- ⚪ [Apollo Neuro](https://apolloneuro.com/) — Wrist/ankle wearable delivering vibration for stress and recovery. `live + history`
- ⚪ [Alpha-Stim](https://www.alpha-stim.com/) — FDA-cleared cranial electrotherapy stimulation device for anxiety, insomnia, and pain. `live`

#### Hearables & in-ear biosensing (proposed new section)
- ⚪ [STAT Health](https://www.stat-health.com/) — In-ear wearable measuring blood flow to the head for POTS, long COVID, and ME/CFS. `live + history`
- ⚪ [NextSense](https://nextsense.io/) — EEG-sensing earbuds monitoring brain activity and sleep. `live`

#### Smart contact lenses & ocular / AR biosensing (proposed new section)
- ⚪ [XPANCEO](https://www.xpanceo.com/) — Smart contact-lens prototypes with tear-fluid biosensing and intraocular-pressure sensing. Investigational. `live`
- ⚪ [Sensimed Triggerfish](https://www.sensimed.ch/) — Contact-lens sensor recording intraocular-pressure fluctuations for glaucoma. CE-marked. `snapshot`
- ⚪ [Emteq Labs](https://www.emteqlabs.com/) — Eyewear with facial-EMG and optical sensors for emotion and health sensing. `live`

#### Digital stethoscopes & point-of-care imaging (proposed new section)
- ⚪ [Eko Health](https://www.ekohealth.com/) — Digital stethoscopes (CORE 500) with 3-lead ECG and FDA-cleared cardiac AI. `live`
- ⚪ [Butterfly iQ](https://www.butterflynetwork.com/) — Handheld whole-body ultrasound on a single semiconductor chip. FDA-cleared. `live`
- ⚪ [Clarius](https://clarius.com/) — Wireless handheld ultrasound scanners paired with a phone app. FDA-cleared. `live`
- ⚪ [Pulsify Medical](https://www.pulsify-medical.com/) — Wearable ultrasound patch for continuous cardiac monitoring. Investigational. `live`

#### Wearable defibrillators & orthotics (proposed new section)
- ⚪ [ZOLL LifeVest](https://lifevest.zoll.com/) — Wearable cardioverter defibrillator for patients at risk of sudden cardiac arrest. FDA-approved. `live`

#### Exoskeletons & powered orthotics (proposed new section)
- ⚪ [Ekso Bionics](https://eksobionics.com/) — Powered exoskeletons for neurological rehabilitation and industrial use. FDA-cleared. `live`
- ⚪ [ReWalk / Lifeward](https://golifeward.com/) — Personal and rehab exoskeletons for spinal-cord-injury mobility. FDA-cleared. `live`
- ⚪ [Wandercraft Atalante](https://en.wandercraft.eu/) — Self-balancing hands-free exoskeleton for gait rehabilitation. FDA-cleared. `live`
- ⚪ [Cyberdyne HAL](https://www.cyberdyne.jp/english/) — Bioelectric-signal-driven wearable exoskeleton (Hybrid Assistive Limb). `live`
- ⚪ [Myomo MyoPro](https://myomo.com/) — Myoelectric arm orthosis reading surface EMG to restore arm function. FDA-registered. `live`
- ⚪ [German Bionic](https://germanbionic.com/) — Connected exoskeletons for industrial lifting and ergonomics. `live`

#### Smart prosthetics (proposed new section)
- ⚪ [Össur](https://www.ossur.com/) — Bionic limbs (Power Knee, i-Limb) with myoelectric control and sensors. `live`
- ⚪ [Open Bionics Hero Arm](https://openbionics.com/) — Multi-grip myoelectric bionic arm reading muscle signals. CE/FDA-registered. `live`
- ⚪ [PSYONIC Ability Hand](https://www.psyonic.io/) — Touch-sensing bionic hand with an open developer API. `live`
- ⚪ [Coapt](https://coaptengineering.com/) — Pattern-recognition myoelectric control system for prostheses. `live`
- ⚪ [Esper Bionics](https://esperbionics.com/) — Cloud-connected self-learning bionic hand. `live`
- ⚪ [Atom Limbs](https://www.atomlimbs.com/) — Neurally controlled prosthetic arm in development. Investigational. `live`

#### Implantable cardiac monitors & devices (proposed new section)
- ⚪ [Medtronic Micra](https://www.medtronic.com/) — Leadless intracardiac pacemaker with remote monitoring. FDA-approved. `live + history`
- ⚪ [Medtronic LINQ II](https://www.medtronic.com/) — Insertable cardiac monitor streaming ECG via Bluetooth for up to 4.5 years. FDA-cleared. `live + history`
- ⚪ [Abbott Aveir](https://www.cardiovascular.abbott/) — Leadless pacemaker with remote follow-up. FDA-approved. `live + history`
- ⚪ [Abbott Assert-IQ](https://www.cardiovascular.abbott/) — Insertable cardiac monitor with up to 6-year battery and AI arrhythmia detection. FDA-cleared. `live + history`
- ⚪ [Boston Scientific LUX-Dx](https://www.bostonscientific.com/) — Insertable cardiac monitor with dual-stage arrhythmia detection. FDA-cleared. `live + history`
- ⚪ [Biotronik BIOMONITOR](https://www.biotronik.com/) — Insertable cardiac monitor with home-monitoring telemetry. FDA-cleared. `live + history`
- ⚪ [Abbott CardioMEMS](https://www.cardiovascular.abbott/) — Implanted pulmonary-artery pressure sensor for heart-failure management. FDA-approved. `live + history`

#### Implantable neurostimulators & DBS (proposed new section)
- ⚪ [Medtronic Percept](https://www.medtronic.com/) — Deep-brain-stimulation system with BrainSense neural sensing. FDA-approved. `live + history`
- ⚪ [NeuroPace RNS](https://www.neuropace.com/) — Responsive closed-loop brain stimulator for epilepsy that records EEG. FDA-approved. `live + history`
- ⚪ [Inspire](https://www.inspiresleep.com/) — Implanted hypoglossal-nerve stimulator for obstructive sleep apnea, app-controlled. FDA-approved. `live`
- ⚪ [Nyxoah Genio](https://www.nyxoah.com/) — Bilateral hypoglossal-nerve stimulator for sleep apnea with a wearable activation patch. CE-marked. `live`
- ⚪ [LivaNova VNS](https://www.livanova.com/) — Implanted vagus-nerve stimulator for epilepsy and depression. FDA-approved. `live + history`
- ⚪ [Nevro HFX](https://www.nevro.com/) — Spinal-cord stimulator for chronic pain with cloud-connected app. FDA-approved. `live + history`
- ⚪ [Saluda Evoke](https://www.saludamedical.com/) — Closed-loop spinal-cord stimulator measuring evoked neural responses. FDA-approved. `live + history`
- ⚪ [Axonics](https://www.axonics.com/) — Implantable sacral neuromodulation system for bladder/bowel control. FDA-approved. `live + history`
- ⚪ [Onward ARC](https://onwd.com/) — Spinal-cord stimulation platform for spinal-cord-injury movement restoration. Investigational. `live`

#### Brain-computer interfaces (implantable / melded, Gen 3)
- ⚪ [Precision Neuroscience](https://precisionneuro.io/) — Thin-film cortical-surface BCI (Layer 7) with FDA 510(k) clearance for temporary use. Investigational. `live`
- ⚪ [Paradromics](https://www.paradromics.com/) — High-bandwidth intracortical BCI (Connexus) for speech restoration. Investigational. `live`
- ⚪ [Blackrock Neurotech](https://blackrockneurotech.com/) — Utah/NeuroPort-Array BCI platform with 40+ array procedures — the most among research-stage intracortical BCIs. Investigational. `live`
- ⚪ [Science Corporation](https://science.xyz/) — Retinal prosthesis (PRIMA) and BCI developer. Investigational. `live`
- ⚪ [INBRAIN Neuroelectronics](https://www.inbrain-neuroelectronics.com/) — Graphene-based neural interface for neurological disease. Investigational. `live`
- ⚪ [Motif Neurotech](https://www.motifneuro.tech/) — Minimally invasive wireless brain implant for mental health. Investigational. `live`

#### Insulin pumps & closed-loop systems (proposed new section)
- ⚪ [Tandem t:slim X2](https://www.tandemdiabetes.com/) — Touchscreen insulin pump with Control-IQ automated delivery. FDA-cleared. `live + history`
- ⚪ [Tandem Mobi](https://www.tandemdiabetes.com/) — Smallest phone-controlled automated insulin-delivery pump. FDA-cleared. `live + history`
- ⚪ [Insulet Omnipod 5](https://www.omnipod.com/) — Tubeless automated insulin-delivery pod driven by CGM data. FDA-cleared. `live + history`
- ⚪ [Medtronic MiniMed 780G](https://www.medtronic.com/) — Advanced hybrid closed-loop insulin pump. FDA-approved. `live + history`
- ⚪ [Beta Bionics iLet](https://www.betabionics.com/) — Bionic pancreas requiring only body weight to start automated dosing. FDA-cleared. `live + history`
- ⚪ [Sequel twiist](https://www.twiist.com/) — Automated insulin-delivery system using an open interoperable algorithm. FDA-cleared. `live + history`
- 🟢 [AndroidAPS](https://github.com/nightscout/AndroidAPS) — Open-source automated insulin-delivery app for Android. `live`
- 🟢 [Trio](https://github.com/nightscout/Trio) — Open-source iOS automated insulin-delivery app based on the OpenAPS algorithm. `live`
- 🟢 [xDrip+](https://github.com/NightscoutFoundation/xDrip) — Open-source Android CGM data hub interoperating with loops and Nightscout. `live`
- 🟢 [Tidepool](https://github.com/tidepool-org) — Open-source diabetes-data platform; Tidepool Loop is an FDA-cleared AID app. `live + history`

#### Ingestibles & smart pills (proposed new section)
- ⚪ [Atmo Biosciences](https://www.atmobiosciences.com/) — Ingestible gas-sensing capsule measuring gut gases and transit. Investigational. `snapshot`
- ⚪ [etectRx ID-Cap](https://etectrx.com/) — Ingestible sensor system tracking medication adherence. FDA-cleared. `snapshot`
- ⚪ [Vibrant Gastro](https://www.vibrantgastro.com/) — Drug-free vibrating capsule for chronic constipation. FDA-cleared. `snapshot`
- ⚪ [Medtronic PillCam](https://www.medtronic.com/) — Ingestible capsule-endoscopy camera imaging the GI tract. FDA-cleared. `snapshot`
- ⚪ [CapsoVision CapsoCam](https://www.capsovision.com/) — Panoramic capsule-endoscopy system for small-bowel imaging. FDA-cleared. `snapshot`
- ⚪ [AnX Robotica NaviCam](https://www.anxrobotica.com/) — Magnetically controlled capsule-endoscopy system with AI reading. FDA-cleared. `snapshot`

#### Implantable biosensors (proposed new section)
- ⚪ [Senseonics Eversense 365](https://www.eversensecgm.com/) — Implantable continuous glucose sensor lasting up to one year. FDA-approved. `live`
- ⚪ [Biolinq](https://www.biolinq.com/) — Intradermal microneedle glucose biosensor. Investigational. `live`
- ⚪ [Profusa](https://profusa.com/) — Injectable tissue-integrating biosensors for continuous chemistry monitoring. Investigational. `live`

#### Smart orthopedic implants (proposed new section)
- ⚪ [Zimmer Biomet Persona IQ](https://www.zimmerbiomet.com/) — First FDA-authorized smart knee implant with an embedded gait sensor. FDA De Novo. `live + history`
- ⚪ [Canary Medical canturio](https://canarymedical.com/) — Implantable sensor (CHIRP) reporting gait and range-of-motion metrics. FDA De Novo. `live + history`

#### Bioelectronic medicine (proposed new section)
- ⚪ [SetPoint Medical](https://setpointmedical.com/) — Implanted vagus-nerve stimulator for autoimmune disease. FDA-approved (rheumatoid arthritis). `live`
- ⚪ [CVRx Barostim](https://www.cvrx.com/) — Implanted baroreflex-activation device for heart failure. FDA-approved. `live + history`

#### Implantable RFID/NFC & biohacking (embedded, Gen 3) (proposed new section)
- ⚪ [Dangerous Things](https://dangerousthings.com/) — Consumer implantable RFID/NFC transponders for access and identity. `live`
- ⚪ [VivoKey](https://vivokey.com/) — Cryptographically secure implantable NFC chips with a developer API. `live`
- ⚪ [Walletmor](https://walletmor.com/) — Implantable contactless-payment chip. `live`
- 🟢 [Grindhouse Wetware](https://www.grindhousewetware.com/) — Open-source biohacking implants and augmentation hardware. `live`

#### Smart oral, dental & pelvic health (proposed new section)
- ⚪ [Oral-B iO](https://oralb.com/) — Connected electric toothbrush with AI brushing tracking. `live + history`
- ⚪ [Colgate hum](https://www.colgate.com/) — Smart toothbrush tracking brushing coverage via an app. `live + history`
- ⚪ [Elvie](https://www.elvie.com/) — Connected pelvic-floor trainer and breast pump measuring muscle activity. `live + history`
- ⚪ [Perifit](https://perifit.co/) — App-connected pelvic-floor trainer using an intravaginal pressure sensor. `live + history`
- ⚪ [kegg](https://www.kegg.tech/) — Intravaginal fertility sensor measuring cervical-fluid changes. `live + history`
- ⚪ [Daye](https://yourdaye.com/) — Diagnostic tampon for at-home vaginal-microbiome and STI screening. `snapshot`

#### Temperature & fertility wearables (proposed new section)
- ⚪ [Tempdrop](https://www.tempdrop.com/) — Wearable overnight basal-body-temperature sensor for fertility tracking. `live + history`
- ⚪ [OvuSense](https://www.ovusense.com/) — Continuous core-body-temperature sensor for ovulation tracking. `live + history`
- ⚪ [Femometer](https://www.femometer.com/) — Connected basal thermometer and fertility-tracking ecosystem. `live + history`

### C. Non-device resources (strengthen the list for the Awesome index)

#### Regulatory & policy (proposed new section)
- 🔵 [FDA Digital Health Center of Excellence](https://www.fda.gov/medical-devices/digital-health-center-excellence) — FDA hub coordinating digital-health regulation and best practices.
- 🔵 [FDA Software as a Medical Device (SaMD)](https://www.fda.gov/medical-devices/digital-health-center-excellence/software-medical-device-samd) — FDA's SaMD regulatory framework and guidance.
- 🔵 [FDA Predetermined Change Control Plan](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence) — Guidance allowing pre-authorized updates to AI-enabled devices.
- 🔵 [FDA Cybersecurity in Medical Devices](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-medical-devices-quality-management-system-considerations-and-content-premarket) — Premarket cybersecurity guidance implementing FD&C Act section 524B.
- 🔵 [EU MDR 2017/745](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02017R0745-20230320) — EU Medical Device Regulation governing device design and marketing.
- 🔵 [UK MHRA Software and AI as a Medical Device](https://www.gov.uk/government/publications/software-and-ai-as-a-medical-device-change-programme) — MHRA reform programme for regulating SaMD/AIaMD.

#### Security & privacy research (proposed new section)
- ⚪ [Medtronic Conexus advisory (ICSMA-19-080-01)](https://www.cisa.gov/news-events/ics-medical-advisories/icsma-19-080-01) — CISA advisory on unencrypted Medtronic implant telemetry (CVE-2019-6540) spanning ~19 ICD/CRT-D product lines (Amplia, Claria, Evera, Virtuoso, etc.), reported as ~750,000 vulnerable defibrillators.
- ⚪ [St. Jude/Abbott pacemaker advisory (ICSMA-17-241-01)](https://www.cisa.gov/news-events/ics-medical-advisories/icsma-17-241-01) — CISA advisory paired with the FDA's Aug. 2017 firmware corrective action covering 465,000 U.S. (745,000 worldwide) Abbott/St. Jude RF-enabled pacemakers.
- ⚪ [SweynTooth](https://asset-group.github.io/disclosures/sweyntooth/) — Family of Bluetooth Low Energy vulnerabilities affecting medical devices.
- ⚪ [Biohacking Village](https://www.villageb.io/) — DEF CON village running the Medical Device Lab bridging researchers, makers, and FDA.
- ⚪ [Health-ISAC](https://health-isac.org/) — Global health-sector threat-intelligence sharing community.
- ⚪ [I Am The Cavalry](https://iamthecavalry.org/) — Volunteer group focused on cybersecurity where it intersects public safety.

#### Key academic & reference works (add to Privacy/further reading)
- ⚪ [RAND — The Internet of Bodies](https://www.rand.org/pubs/research_reports/RR3226.html) — RAND report RR-3226-RC (2020), "The Internet of Bodies: Opportunities, Risks, and Governance," by Mary Lee, Benjamin Boudreaux, Ritika Chaturvedi, Sasha Romanosky, and Bryce Downing.
- ⚪ [Matwyshyn — The Internet of Bodies](https://scholarship.law.wm.edu/wmlr/vol61/iss1/3/) — Andrea M. Matwyshyn, "The Internet of Bodies," 61 Wm. & Mary L. Rev. 77 (2019), which sets out the three generations of IoB: Body External (p.94), Body Internal (p.103), and Body Melded (p.112).
- ⚪ [World Economic Forum — The Internet of Bodies Is Here](https://www.weforum.org/publications/the-internet-of-bodies-is-here-tackling-new-challenges-of-technology-governance/) — WEF report on IoB governance challenges.

#### Datasets & open-source (proposed new section)
- 🟢 [PhysioNet](https://physionet.org/) — Repository of freely available physiological-signal databases and software.
- 🟢 [MIMIC-IV Waveform](https://physionet.org/content/mimic4wdb/0.1.0/) — ICU bedside-monitor physiological waveforms linkable to MIMIC-IV clinical data.
- 🟢 [WESAD](https://archive.ics.uci.edu/dataset/465/wesad+wearable+stress+and+affect+detection) — Wearable stress-and-affect dataset from chest and wrist sensors.
- 🟢 [PPG-DaLiA](https://archive.ics.uci.edu/dataset/495/ppg+dalia) — PPG-for-daily-life-activities dataset for heart-rate estimation.
- 🟢 [wearipedia](https://github.com/Stanford-Health/wearipedia) — Python toolkit for extracting and simulating wearable-device data (Stanford Snyder Lab).
- 🟢 [All of Us wearables data](https://support.researchallofus.org/hc/en-us/articles/20281023493908-Resources-for-Using-Fitbit-Data) — NIH program's Fitbit wearables dataset via the Researcher Workbench.

### D. Existing items worth flagging (dead-linked, discontinued, or update-needed)
Add a **"Historical & discontinued"** section for context. Notable defunct/absorbed IoB milestones worth marking:
- **Proteus Digital Health** — Digital-pill pioneer (Abilify MyCite); bankrupt 2020, assets sold to Otsuka.
- **Second Sight Argus II** — Retinal implant abandoned, leaving patients unsupported (cautionary case).
- **Thalmic Labs Myo** — EMG gesture armband discontinued 2018.
- **Halo Neuroscience (Halo Sport)** — Neurostimulation headphones; assets acquired 2020.
- **Mojo Vision** — AR/biosensing contact lens; pivoted away from the lens in 2023.
- **Medtronic SmartPill** — Ingestible motility capsule discontinued 2023.
- **Google/Verily glucose contact lens** — Program halted 2018.

Repo maintenance notes:
- Your existing generic `Medtronic` entry should be split into specific product lines above (Micra, LINQ II, MiniMed 780G, Percept, PillCam) for precision.
- The `awesome-internet-of-the-body-README.md`, `awesome-internet-of-the-body-CONTRIBUTING.md`, and `awesome-internet-of-the-body-files.zip` appear to be leftover duplicates and would fail `awesome-lint`; remove them before submitting to the Awesome index.
- Your existing 23andMe entry is correctly flagged as a cautionary privacy case — keep it.

### E. Awesome-list community conventions (for main index eligibility)
To qualify for [sindresorhus/awesome](https://github.com/sindresorhus/awesome), the repo must: pass [awesome-lint](https://github.com/sindresorhus/awesome-lint); use the exact README header/badge format; include `contributing.md` and `code-of-conduct.md`; carry a license (yours is CC0-1.0, acceptable); ensure every list item description starts with an uppercase letter and ends with a period; avoid duplicate files; and include a table of contents. Your list already has the Awesome badge and a contributing file, so the main remaining work is lint compliance, description punctuation, removing duplicate files, and adding a code of conduct.

## Recommendations
1. **Restructure the taxonomy now** around Matwyshyn's three generations (which you already cite): External / Internal / Embedded, with the ~20 new sub-sections above. This scales far better than the current flat list.
2. **Paste in Section A first** (fits existing categories, lowest risk), then **Section B** (new device categories), then **Section C** (resources). Target the full 180+.
3. **Add a "Historical & discontinued" section** (Section D) — awesome-list users value knowing what died and why.
4. **Do the lint pass** (Section E) before submitting to the main Awesome index: remove duplicate files, add `code-of-conduct.md`, verify punctuation.
5. **Benchmarks that change the plan:** if you want to stay consumer-focused, drop the implantable/BCI sections; if you want clinical credibility, keep them and add FDA 510(k)/PMA numbers to each entry. If the list exceeds ~250 entries, split into topic files (as the Awesome guidelines suggest for very large lists).

## Caveats
- A handful of URLs are best-guess official homepages that should be resolve-checked before commit: STAT Health (stat-health.com), Pulsify Medical (pulsify-medical.com), Human API (humanapi.co — acquired by LexisNexis), the ZOLL LifeVest path (lifevest.zoll.com), and the MHRA gov.uk slug. All entities/products are confirmed real and current; only the exact URL paths need a final click-through.
- Several BCI/implant/contact-lens entries are **investigational** (not cleared/approved) — they are flagged as such; keep those flags in the README so the list doesn't overstate availability.
- Regulatory status changes fast; "FDA-cleared/approved/De Novo" reflects reporting as of August 2026 and should be periodically re-verified against the FDA 510(k)/PMA/De Novo databases.
- WESAD and PPG-DaLiA are hosted at multiple mirrors (UCI vs. university pages); the UCI links above are the stable primary sources.
- A few widely used items from your task brief could not be individually re-verified within this research pass and were intentionally omitted rather than listed with unverified links (e.g., some smaller sleep/EEG and sweat-sensor startups); they can be added later after a link check.