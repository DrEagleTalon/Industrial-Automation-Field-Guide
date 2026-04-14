"""Content for 13_Specialty_Topics."""

FOLDER = "13_Specialty_Topics"

def table(headers, rows):
    out = ["<table>", "<thead><tr>"]
    for h in headers: out.append(f"<th>{h}</th>")
    out.append("</tr></thead><tbody>")
    for r in rows:
        out.append("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)
def ul(items): return "<ul>" + "".join(f"<li>{it}</li>" for it in items) + "</ul>"
def ol(items): return "<ol>" + "".join(f"<li>{it}</li>" for it in items) + "</ol>"
def code(block): return f"<pre><code>{block}</code></pre>"
def tasks(items): return "<ul>" + "".join(f'<li class="task unchecked"><span class="checkbox">&#x2610;</span> {it}</li>' for it in items) + "</ul>"
def p(*paragraphs): return "\n".join(f"<p>{x}</p>" for x in paragraphs)

PAGES = {

"Robotic Integration.html":{
    "title":"Robotic Integration",
    "meta":{"category":"Specialty Topics","tags":["#robot","#FANUC","#ABB","#KUKA","#integration"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"ISO 10218, RIA/ANSI R15.06"},
    "sections":[
        {"title":"Description","body": p(
            "Industrial robots (FANUC, ABB, KUKA, Yaskawa, Kawasaki, UR) handle picking, welding, palletizing, assembly, and machine tending. Integrating them with PLCs, sensors, and HMIs is now a standard controls-engineering task.")},
        {"title":"Integration Points","body": ul([
                "<strong>Safety</strong> — cell guarding, E-stops, safety-rated motion. See <a href=\"../12_Safety_Systems_Advanced/Safety Fencing &amp; Interlocks.html\">Safety Fencing</a>.",
                "<strong>Signaling</strong> — digital I/O or Ethernet to tell the robot what to do and hear what it's done.",
                "<strong>Teach</strong> — pendant-based vs offline programming.",
                "<strong>Vision</strong> — 2D or 3D vision for part location.",
                "<strong>End-of-arm tooling</strong> — grippers, vacuum cups, welding guns.",
                "<strong>Collaborative vs industrial</strong> — cobots need force-limiting or speed-and-separation monitoring.",
            ])},
        {"title":"Communication","body": table(
            ["Protocol","Used for"],
            [
                ["Digital I/O (24 VDC)","Simple start / stop / ready / busy handshake"],
                ["EtherNet/IP (FANUC)","Full I/O + register exchange to Rockwell PLCs"],
                ["PROFINET (KUKA, ABB)","Common in Siemens-heavy plants"],
                ["Modbus TCP","Universal simple exchange"],
                ["Robot-specific (RSI, RMI)","Real-time motion streaming"],
            ])},
        {"title":"Typical Interlock Set","body": ul([
                "Safety OK (guards closed, E-stops clear) — dual-channel safety loop.",
                "Robot home / at safe position.",
                "Fixture clamped / part present.",
                "Cycle start command.",
                "Robot running / completed status.",
                "Fault / need-operator signals.",
            ])},
        {"title":"Cobot Notes","body": p(
            "Collaborative robots (UR, ABB YuMi, FANUC CRX, Doosan) require a risk assessment just like any industrial robot. 'Collaborative' describes the robot, not the application — a cobot handling a sharp knife still needs guarding."
        )},
        {"title":"Field Checklist","body": tasks([
            "Safety-validated guarding around cell.",
            "Robot program backup saved and archived.",
            "PLC-to-robot I/O documented in both controllers.",
            "Home position / cycle start tested from cold boot.",
            "Manual override tested for service.",
        ])},
    ],
    "related":[
        ("Servo Motors & Motion Control","Servo Motors &amp; Motion Control.html"),
        ("Encoders & Resolvers","Encoders &amp; Resolvers.html"),
        ("Safety PLCs & Redundancy","../12_Safety_Systems_Advanced/Safety PLCs &amp; Redundancy.html"),
        ("Common Protocols","../08_Industrial_Networks_&_Protocols/Common Protocols.html"),
    ],
},

"Servo Motors & Motion Control.html":{
    "title":"Servo Motors & Motion Control",
    "meta":{"category":"Specialty Topics","tags":["#servo","#motion","#PLCopen","#encoder","#torque"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"PLCopen Motion Control"},
    "sections":[
        {"title":"Description","body": p(
            "A servo motor is a motor-drive pair with closed-loop position, velocity, or torque control and a feedback device. Servos dominate applications that need accurate positioning, synchronized motion, or gentle acceleration profiles.")},
        {"title":"Architecture","body": ul([
                "Permanent-magnet (or induction) motor with an integral feedback device (encoder or resolver).",
                "Servo drive that closes position, velocity, and torque loops in nested layers.",
                "Network link to a motion controller (PLC or dedicated motion card).",
                "Cables: motor power + feedback (often hybrid cable on modern drives).",
            ])},
        {"title":"Common Networks","body": table(
            ["Network","Strengths"],
            [
                ["EtherCAT","Sub-microsecond sync, widely adopted"],
                ["SERCOS III","Deterministic, motion-specific"],
                ["PROFINET IRT","Siemens ecosystem"],
                ["EtherNet/IP CIP Motion","Rockwell ecosystem (Kinetix)"],
                ["Mechatrolink","Yaskawa"],
            ])},
        {"title":"PLCopen Function Blocks","body": ul([
                "MC_Power — enable the axis.",
                "MC_Home — reference to a known position.",
                "MC_MoveAbsolute — go to a target in absolute coordinates.",
                "MC_MoveRelative — move by a distance.",
                "MC_GearIn / MC_CamIn — electronic gearing and camming.",
                "MC_Stop / MC_Halt — controlled stop.",
                "State machine is standardized — Standstill, Discrete Motion, Homing, Stopping, ErrorStop.",
            ])},
        {"title":"Tuning","body": ul([
                "Start with low gains and verify the mechanical system works.",
                "Tune velocity loop first, then position loop.",
                "Watch for resonance — notch filters help.",
                "Set current and velocity limits to match mechanical design.",
                "Avoid over-tuning — it fights noise and wears the mechanics.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Axis home reference documented.",
            "Position / velocity / torque limits set.",
            "Faults wired to PLC and HMI.",
            "Holding brake commissioned for vertical / gravity axes.",
            "Backup of drive parameters archived.",
        ])},
    ],
    "related":[
        ("Encoders & Resolvers","Encoders &amp; Resolvers.html"),
        ("Variable Frequency Drives (VFDs) Basics","../04_Motor_Control/Variable Frequency Drives (VFDs) Basics.html"),
        ("Robotic Integration","Robotic Integration.html"),
        ("Motor Braking Techniques","../04_Motor_Control/Motor Braking Techniques.html"),
    ],
},

"Encoders & Resolvers.html":{
    "title":"Encoders & Resolvers",
    "meta":{"category":"Specialty Topics","tags":["#encoder","#resolver","#incremental","#absolute","#SSI"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Encoders and resolvers measure rotary (and sometimes linear) position. Essential for servo motors, positioning systems, conveyor tracking, and closed-loop VFD control.")},
        {"title":"Types","body": table(
            ["Type","How it works","Typical Use"],
            [
                ["Incremental encoder","Pulses per revolution; direction from A/B phases","Speed feedback, conveyor tracking"],
                ["Absolute encoder","Unique position word at every angle","Servo feedback, axes that must know position at power-up"],
                ["Multi-turn absolute","Also counts revolutions","Long-travel axes, tool changers"],
                ["Resolver","Sin/cos analog, rotating transformer","Harsh environments, welding, military, high temperature"],
                ["Hall-effect","Three-phase commutation signals","Simple BLDC commutation"],
                ["Magnetic / optical linear","Scale + read head","Machine tools, gantries"],
            ])},
        {"title":"Signal Interfaces","body": ul([
                "TTL (5 V) — short cables, simple.",
                "HTL / push-pull (24 V) — noise-immune, longer cables.",
                "RS-422 / differential — long cables, standard on modern encoders.",
                "SSI (Synchronous Serial Interface) — absolute encoder serial.",
                "BiSS, EnDat, Hiperface — high-speed absolute serial, widely used on servos.",
            ])},
        {"title":"Selection Criteria","body": ul([
                "Resolution — counts / revolution required for the application.",
                "Environment — temperature, moisture, vibration, shock.",
                "Mounting — hollow shaft, solid shaft, flange.",
                "Electrical — voltage, interface, cable length.",
                "Diagnostics — modern encoders provide health, over-temp, and position-error flags.",
            ])},
        {"title":"Common Problems","body": table(
            ["Symptom","Cause"],
            [
                ["Counts in one direction only","A/B swapped or one channel failed"],
                ["Noise / erratic counts","Unshielded cable near VFD cable, ground loop"],
                ["Position drift","Slip in coupling or feedback in wrong gear ratio"],
                ["Faulted at power-up","Absolute encoder battery or memory error"],
            ])},
        {"title":"Field Checklist","body": tasks([
            "Encoder type matches drive / PLC input expectations.",
            "Shielded cable routed separately from power.",
            "Coupling to shaft rigid and non-slipping.",
            "Resolution / PPR matches the application math.",
            "Absolute encoder homed or referenced on install.",
        ])},
    ],
    "related":[
        ("Servo Motors & Motion Control","Servo Motors &amp; Motion Control.html"),
        ("Counters","../06_PLC_Programming_&_Logic/Counters.html"),
        ("Variable Frequency Drives (VFDs) Basics","../04_Motor_Control/Variable Frequency Drives (VFDs) Basics.html"),
    ],
},

"Industrial Wireless.html":{
    "title":"Industrial Wireless",
    "meta":{"category":"Specialty Topics","tags":["#wireless","#WiFi","#Bluetooth","#LoRa","#802154"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Wireless has a place in industrial networking — mobile equipment, portable diagnostics, remote sensors — but the default should still be wired. Radio is a shared medium; copper and fiber are not.")},
        {"title":"Technologies","body": table(
            ["Tech","Range","Use Case"],
            [
                ["Industrial Wi-Fi (802.11ac/ax)","50–200 m indoors","AGVs, mobile terminals, large plants"],
                ["Bluetooth LE","10–30 m","Sensor connectivity, beacons"],
                ["Zigbee (802.15.4)","30 m","Low-power mesh, lighting, HVAC"],
                ["LoRaWAN","km range","Slow, intermittent data; utility metering"],
                ["Cellular 4G/5G","National","Remote sites, failover"],
                ["Private 5G","Plant-wide","Deterministic mobile, replacing Wi-Fi for mission-critical"],
                ["ISA100 / WirelessHART","30–100 m","Process instrumentation"],
            ])},
        {"title":"Where Wireless Is Appropriate","body": ul([
                "Equipment that moves (AGVs, cranes, mobile HMIs).",
                "Temporary installations, pilots, surveys.",
                "Devices where running cable is prohibitively expensive.",
                "Non-safety, non-deterministic signals.",
            ])},
        {"title":"Where To Avoid","body": ul([
                "E-stops and safety — wired, always.",
                "Motion-critical, deterministic control.",
                "High-throughput vision streams.",
                "Environments with a lot of unrelated radio traffic.",
            ])},
        {"title":"Design Considerations","body": ul([
                "Site survey for RF coverage and interference.",
                "Dedicated SSID / APN, separated from corporate Wi-Fi.",
                "Authentication: WPA3 Enterprise, certificate-based.",
                "Fallback to wired for critical functions.",
                "Redundant APs / gateways for coverage and availability.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "RF survey done before install.",
            "Wireless infrastructure on its own VLAN / subnet.",
            "Security: enterprise auth, rotating credentials.",
            "Monitoring of signal strength and retry rates.",
            "Critical functions still reachable via wired fallback.",
        ])},
    ],
    "related":[
        ("Common Protocols","../08_Industrial_Networks_&_Protocols/Common Protocols.html"),
        ("Industrial Ethernet vs IT Ethernet","../08_Industrial_Networks_&_Protocols/Industrial Ethernet vs IT Ethernet.html"),
        ("IIoT Gateways & Edge","IIoT Gateways &amp; Edge.html"),
        ("Remote Access & VPN","Remote Access &amp; VPN.html"),
    ],
},

"Remote Access & VPN.html":{
    "title":"Remote Access & VPN",
    "meta":{"category":"Specialty Topics","tags":["#VPN","#remoteaccess","#cybersecurity","#OT"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"IEC 62443"},
    "sections":[
        {"title":"Description","body": p(
            "Remote access to a plant is a security risk dressed as a convenience. Done right, it lets integrators and OEMs support machines without flying out. Done wrong, it becomes the attacker's front door.")},
        {"title":"Architectures","body": ul([
                "<strong>Cellular modem on the machine</strong> — self-contained. Good for isolated equipment.",
                "<strong>Vendor-hosted VPN</strong> — eWON Flexy, Siemens SCALANCE, MB Connect, IXON. Call-home connection to a vendor cloud; support engineers connect through the cloud.",
                "<strong>Plant VPN</strong> — IT-managed VPN into the OT DMZ; jump host to plant assets.",
                "<strong>Zero-trust broker</strong> — modern architectures like Claroty Secure Remote Access, Dispel, Tosibox.",
            ])},
        {"title":"IEC 62443 Principles","body": ul([
                "Never connect OT directly to the internet.",
                "DMZ between IT and OT with a proxy / jump host.",
                "Least privilege — each user has access only to what they need.",
                "MFA for every external user.",
                "Session recording for audit.",
                "Regular review of accounts and access.",
            ])},
        {"title":"Operational Rules","body": ul([
                "Remote access disabled by default; enabled via a physical key switch or an operator acknowledgment on the machine.",
                "Sessions logged and reviewed.",
                "Vendor access limited to specific equipment and protocols.",
                "Credentials rotated after vendor engagements.",
                "Patch management for the remote-access appliance itself.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Remote access architecture documented.",
            "Key-switch or operator-initiated enable.",
            "MFA required for all external access.",
            "Session recording available and reviewed periodically.",
            "Vendor access scoped to specific assets / protocols.",
        ])},
    ],
    "related":[
        ("Industrial Ethernet vs IT Ethernet","../08_Industrial_Networks_&_Protocols/Industrial Ethernet vs IT Ethernet.html"),
        ("IIoT Gateways & Edge","IIoT Gateways &amp; Edge.html"),
        ("Cloud SCADA & MQTT","Cloud SCADA &amp; MQTT.html"),
        ("Basic SCADA Architecture","../07_HMI_SCADA_Systems/Basic SCADA Architecture.html"),
    ],
},

"Panel Cooling & Power Conditioning.html":{
    "title":"Panel Cooling & Power Conditioning",
    "meta":{"category":"Specialty Topics","tags":["#cooling","#heat","#surge","#UPS","#environmental"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Heat, humidity, and dirty power are the slow-acting killers of panel electronics. A good thermal and power design pays back over the life of every machine.")},
        {"title":"Cooling Options","body": table(
            ["Option","Use When"],
            [
                ["Natural convection","Low heat load, clean dry environment"],
                ["Filtered fan + vent","Moderate heat, clean air"],
                ["Closed-loop air conditioner","Dirty or humid air, heavier heat loads"],
                ["Air-to-air heat exchanger","Hot outside air, clean inside"],
                ["Water-to-air heat exchanger","Chilled water available"],
                ["Vortex cooler","Compressed air available, no other option"],
            ])},
        {"title":"Heat Load Calculation","body": p(
            "Sum the worst-case W from each component's datasheet, add the drive losses (typ. 3–5% of output kW), add contingency. Compare against enclosure dissipation (free convection from painted steel is ~ 5–6 W/m²·K) and the delta-T you can tolerate. Drive and VFD manufacturers publish heat load in kW per amp rating; use it."
        )},
        {"title":"Power Conditioning","body": ul([
                "Surge protection at the service entrance (type 1) and at the panel (type 2).",
                "Transient voltage suppressor (TVSS) across control transformers.",
                "UPS for PLC / HMI / IPC — at least clean shutdown time; ideally ride-through of utility blips.",
                "Line reactor ahead of VFDs on weak / noisy supplies.",
                "Isolation transformers where ground loops are a concern.",
            ])},
        {"title":"Environmental","body": ul([
                "NEMA / IP rating matches the environment (NEMA 4X / IP66 for wash-down).",
                "Condensation: use heater + hygrostat, or dry-air purge.",
                "Dust: positive pressure filtered air or fully sealed.",
                "Vibration: isolation mounts for sensitive gear.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Heat load calc matched to installed cooling.",
            "Filter inspected / replaced on schedule.",
            "Surge protection in place and indicator lights functional.",
            "UPS tested under load.",
            "Heater + hygrostat operational in humid environments.",
        ])},
    ],
    "related":[
        ("Control Panel Layout & BOM","../10_System_Integration_&_Commissioning/Control Panel Layout &amp; BOM.html"),
        ("Energy Monitoring & Smart Breakers","Energy Monitoring &amp; Smart Breakers.html"),
        ("PLC Power Supplies","../05_PLCs & Automation Hardware/PLC Power Supplies.html"),
        ("Industrial Power Systems Overview","../02_Power_Distribution/Industrial Power Systems Overview.html"),
    ],
},

"IO-Link Devices.html":{
    "title":"IO-Link Devices",
    "meta":{"category":"Specialty Topics","tags":["#IOLink","#IODD","#smartsensor","#master"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"IEC 61131-9"},
    "sections":[
        {"title":"Description","body": p(
            "IO-Link is a standardized point-to-point communication between a sensor / actuator and an IO-Link Master. It runs over the same 3-wire cable as a discrete sensor but adds bi-directional digital data, parameters, diagnostics, and identification.")},
        {"title":"Why it's useful","body": ul([
                "Replace a discrete sensor in-place without re-wiring — the signal becomes digital.",
                "Parameters configured from the PLC: teach distance, sensing mode, speed.",
                "Diagnostics: temperature, operating hours, short-circuit detection.",
                "Identification: part number, serial number, firmware.",
                "Reduced wiring — multiple process values over one cable.",
            ])},
        {"title":"Architecture","body": code(
"PLC  --- Ethernet (EtherNet/IP / PROFINET) ---  IO-Link Master (fieldbus module)\n"
"                                                    |\n"
"                                                    +-- port 1 -- sensor 1\n"
"                                                    +-- port 2 -- valve island\n"
"                                                    +-- port 3 -- RFID head\n"
"                                                    +-- port 4 -- level sensor\n"
"\n"
"Each port is either:\n"
"  IO-Link mode (digital, bi-directional 38.4 or 230 kbps)\n"
"  DI mode (acts like a plain discrete input)\n")},
        {"title":"Picking an IO-Link Master","body": ul([
                "Fieldbus: EtherNet/IP, PROFINET, Modbus TCP.",
                "Port count: 4 or 8 typical; wall-mount or in-panel.",
                "Environmental rating: IP67 for in-machine, IP20 for in-panel.",
                "Diagnostic / web page features for commissioning.",
                "Vendor IODD files for every device you plan to connect.",
            ])},
        {"title":"Commissioning","body": ol([
                "Add the IO-Link master in the PLC project via its EDS / GSDML file.",
                "Import the sensor's IODD file into the master's engineering tool.",
                "Bind sensor parameters to PLC tags.",
                "Scale process values in the PLC.",
                "Add diagnostics to HMI (device lost, parameter mismatch).",
            ])},
        {"title":"Field Checklist","body": tasks([
            "IODD library kept current for every installed device.",
            "Device parameters stored in the master for easy replacement.",
            "Diagnostics surfaced to HMI / SCADA.",
            "Port cables rated for IO-Link (unshielded 3-wire adequate).",
        ])},
    ],
    "related":[
        ("Common Protocols","../08_Industrial_Networks_&_Protocols/Common Protocols.html"),
        ("Analog IO Basics","../05_PLCs & Automation Hardware/Analog IO Basics.html"),
        ("Proximity Sensors Inductive Capacitive","../03_Control_Devices/Proximity Sensors Inductive Capacitive.html"),
    ],
},

"Energy Monitoring & Smart Breakers.html":{
    "title":"Energy Monitoring & Smart Breakers",
    "meta":{"category":"Specialty Topics","tags":["#energy","#meter","#smartbreaker","#kWh","#power"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Energy monitoring has moved from a single revenue meter at the service entrance to sub-meters and smart breakers scattered through the plant. The result: line-, cell-, and machine-level visibility that drives real savings.")},
        {"title":"What to Measure","body": ul([
                "Voltage and current per phase.",
                "Real power (kW), apparent power (kVA), reactive power (kVAR).",
                "Power factor and THD.",
                "kWh totals for billing / allocation.",
                "Demand (15-min peak).",
                "Voltage sags / swells and outages.",
            ])},
        {"title":"Hardware Options","body": table(
            ["Device","Typical Use"],
            [
                ["Revenue meter (utility)","Service entrance billing"],
                ["Panel-mount meter","Feeders, MCC buckets"],
                ["CT-based submeter","Machine or circuit level"],
                ["Smart circuit breaker","Built-in metering at every branch"],
                ["Current sensor (Rogowski, split-core)","Retrofit without opening the bus"],
                ["Power logger","Portable, diagnostic or audit"],
            ])},
        {"title":"Integration","body": ul([
                "Most meters speak Modbus TCP or EtherNet/IP.",
                "Pull data into a historian for trending.",
                "Tie to OEE / energy-per-unit calculations.",
                "Feed BMS or enterprise energy management platform.",
            ])},
        {"title":"Use Cases","body": ul([
                "Allocate energy cost to departments / products.",
                "Spot faulty equipment (phase unbalance, elevated current).",
                "Verify energy-savings projects (pre- vs post-retrofit).",
                "Peak-demand shaving via scheduling.",
                "Predictive maintenance — rising current or PF drift.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Meter CT ratio configured to match installed CTs.",
            "Energy data logged at ≥ 1 min intervals.",
            "Utility bill validated against meter totals.",
            "Power quality events logged and reviewed.",
            "Dashboard accessible to operations and management.",
        ])},
    ],
    "related":[
        ("Industrial Power Systems Overview","../02_Power_Distribution/Industrial Power Systems Overview.html"),
        ("Data Logging & Trends","../07_HMI_SCADA_Systems/Data Logging &amp; Trends.html"),
        ("IIoT Gateways & Edge","IIoT Gateways &amp; Edge.html"),
        ("Fuses vs Breakers","../02_Power_Distribution/Fuses vs Breakers.html"),
    ],
},

"IIoT Gateways & Edge.html":{
    "title":"IIoT Gateways & Edge",
    "meta":{"category":"Specialty Topics","tags":["#IIoT","#edge","#gateway","#MQTT","#OPCUA"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "IIoT gateways sit between operational technology and information technology. They collect tags from PLCs, normalize them, buffer offline, and publish to cloud platforms or enterprise systems.")},
        {"title":"What They Do","body": ul([
                "Speak PLC protocols (EtherNet/IP, PROFINET, Modbus) and IT protocols (MQTT, HTTPS, OPC UA, AMQP).",
                "Parse, filter, and scale data before it leaves the plant.",
                "Buffer during network outages; backfill on reconnect.",
                "Run simple edge analytics — first-line fault detection, aggregation.",
                "Provide a secure, monitored boundary to the cloud.",
            ])},
        {"title":"Hardware Options","body": table(
            ["Device","Notes"],
            [
                ["Industrial PC","Full OS, run Ignition Edge, Node-RED, Docker"],
                ["Edge gateway (AB, Siemens, HMS, Kepware)","Purpose-built, hardened"],
                ["Raspberry Pi","For pilots / non-critical; not for production"],
                ["Cell modem with edge capabilities","Remote equipment"],
            ])},
        {"title":"Common Stacks","body": ul([
                "<strong>MQTT + Sparkplug B</strong> — publish / subscribe with a unified namespace; Ignition, HiveMQ, AWS IoT.",
                "<strong>OPC UA</strong> — structured, object-oriented, secure; native in Siemens, Beckhoff.",
                "<strong>HTTPS / REST</strong> — simple posting to cloud endpoints.",
                "<strong>Azure IoT / AWS IoT Core</strong> — cloud-side destinations.",
            ])},
        {"title":"Design Considerations","body": ul([
                "Keep control logic at the PLC; gateways are for data, not control.",
                "Plan the namespace / tag naming before tags multiply.",
                "Secure by default — mTLS, certificate rotation, hardened OS.",
                "Monitor the gateway itself — dead gateways are a silent failure mode.",
                "Backfill strategy defined and tested.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Gateway OS hardened and patched.",
            "Tags named per a documented convention.",
            "Buffer / backfill tested with network outage.",
            "Certificates rotating per policy.",
            "Edge configuration backed up.",
        ])},
    ],
    "related":[
        ("Cloud SCADA & MQTT","Cloud SCADA &amp; MQTT.html"),
        ("Basic SCADA Architecture","../07_HMI_SCADA_Systems/Basic SCADA Architecture.html"),
        ("Remote Access & VPN","Remote Access &amp; VPN.html"),
        ("Common Protocols","../08_Industrial_Networks_&_Protocols/Common Protocols.html"),
    ],
},

"Cloud SCADA & MQTT.html":{
    "title":"Cloud SCADA & MQTT",
    "meta":{"category":"Specialty Topics","tags":["#cloud","#MQTT","#Sparkplug","#IIoT","#unifiednamespace"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Cloud SCADA runs the supervisory layer off-site — operator screens, historian, alarms — while local HMIs and PLCs keep machines running. MQTT with Sparkplug B is the pattern most industrial shops end up on.")},
        {"title":"MQTT Basics","body": ul([
                "Publish / subscribe protocol over TCP (8883 TLS by default).",
                "Topics are hierarchical strings — Plant/Area/Machine/Device/Tag.",
                "Retained messages and last-will give reliable state even after disconnects.",
                "Very lightweight — fits on constrained edge hardware.",
            ])},
        {"title":"Sparkplug B","body": ul([
                "Defines a structured topic namespace and payload for industrial use.",
                "Birth/death messages: edge nodes announce themselves and their metrics.",
                "Report-by-exception — only changes get sent, not every poll.",
                "Quality and timestamp on every value.",
            ])},
        {"title":"Typical Architecture","body": code(
"PLC -- Edge gateway (Ignition Edge, HMS, Kepware, Node-RED)\n"
"        -- MQTT broker (HiveMQ, EMQX, AWS IoT Core, Chariot)\n"
"        -- Consumers:\n"
"            + Cloud SCADA (Ignition Cloud, Canary, Seeq)\n"
"            + Historian\n"
"            + ERP / MES / BI platforms\n")},
        {"title":"Considerations","body": ul([
                "Broker location: on-prem, cloud, or hybrid.",
                "Security: TLS with certificates on every connection.",
                "Scalability: brokers can handle millions of messages per second; plan namespace growth.",
                "Latency: not suitable for real-time control — control stays local.",
                "Cost: cloud ingress / egress adds up; filter at the edge.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Topic namespace planned and documented.",
            "Broker security configured with mTLS.",
            "Edge gateways publish only the tags that matter.",
            "Historian retention and aggregation policies set.",
            "Disaster recovery: broker redundancy and backup."
        ])},
    ],
    "related":[
        ("Basic SCADA Architecture","../07_HMI_SCADA_Systems/Basic SCADA Architecture.html"),
        ("IIoT Gateways & Edge","IIoT Gateways &amp; Edge.html"),
        ("Data Logging & Trends","../07_HMI_SCADA_Systems/Data Logging &amp; Trends.html"),
        ("Remote Access & VPN","Remote Access &amp; VPN.html"),
    ],
},

}
CONTENT = {FOLDER: PAGES}
