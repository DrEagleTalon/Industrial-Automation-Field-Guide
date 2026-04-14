"""Content for 05_PLCs & Automation Hardware."""

FOLDER = "05_PLCs & Automation Hardware"

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

"What is a PLC.html": {
    "title": "What is a PLC",
    "meta": {"category":"PLCs & Automation Hardware","tags":["#PLC","#controller","#scan","#automation"],
             "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13",
             "standards":"IEC 61131-1, IEC 61131-2","equipment":"ControlLogix, CompactLogix, S7-1500, Modicon, Omron"},
    "sections":[
        {"title":"Description","body": p(
            "A Programmable Logic Controller (PLC) is a purpose-built industrial computer that executes control programs deterministically in a repeating scan. It reads inputs, runs user logic, and writes outputs — over and over — with predictable timing that ordinary PCs can't match. PLCs replaced rooms full of hard-wired relays in the 1970s and remain the core of discrete and process control today.")},
        {"title":"Core Concepts","body":
            "<h3>What a PLC is</h3>" + ul([
                "A ruggedized controller with CPU, memory, communications, and a chassis or rack of I/O modules.",
                "Designed for noisy, hot, vibrating, dirty electrical environments.",
                "Programmed in <a href=\"../06_PLC_Programming_&_Logic/Ladder Logic Basics.html\">Ladder Logic</a>, Structured Text, Function Block, Instruction List, or SFC (see <a href=\"../11_Standards_and_Codes/IEC 61131-3 – PLC Programming.html\">IEC 61131-3</a>).",
                "Executes a scan cycle (input → logic → output) typically every 1 to 50 milliseconds.",
            ]) +
            "<h3>The scan cycle</h3>" + ol([
                "<strong>Input scan</strong> — all physical inputs are latched into an input image table.",
                "<strong>Program execution</strong> — user logic runs against the input image and updates the output image.",
                "<strong>Output scan</strong> — output image is written to physical output modules.",
                "<strong>Housekeeping</strong> — comms, diagnostics, watchdog, user-task scheduling.",
            ]) +
            "<h3>Why deterministic scan matters</h3>" + p(
                "Interlock, emergency stop, and machine timing logic must execute within a known time budget every cycle. A PC running Windows can't guarantee that. A PLC can."
            )
        },
        {"title":"Architecture","body": table(
            ["Element","Purpose"],
            [
                ["CPU / processor","Executes the program, manages tasks, holds the I/O image"],
                ["Power supply","Converts control-panel 24 VDC or 120 VAC to logic voltages"],
                ["Backplane / rack","Carries power and communication between modules"],
                ["Discrete I/O","On/off inputs and outputs — see <a href=\"Discrete IO Modules.html\">Discrete I/O</a>"],
                ["Analog I/O","Continuous signals — see <a href=\"Analog IO Basics.html\">Analog I/O</a>"],
                ["Specialty I/O","High-speed counter, motion, weigh, thermocouple"],
                ["Communications","Ethernet/IP, PROFINET, Modbus, DeviceNet, serial"],
            ])},
        {"title":"PLC Sizes","body": table(
            ["Class","Examples","Typical Use"],
            [
                ["Micro / Nano","Micro800, LOGO!, CLICK","Small machines, replaces 10–40 relays"],
                ["Small","MicroLogix, S7-1200, CompactLogix 5370","OEM machines, small process skids"],
                ["Medium","ControlLogix 5570/5580, S7-1500, CompactLogix 5380","Lines, cells, typical plant controls"],
                ["Large","ControlLogix 5580 L8x, S7-1500 F, Modicon M580","High I/O count, redundant, process"],
                ["Safety / hybrid","GuardLogix, S7-1500 F, Modicon Safety","Functional-safety integrated controllers"],
            ])},
        {"title":"Field Checklist","body": tasks([
            "Controller memory sized for program + future growth (target ≤60% used).",
            "Firmware revision documented and matched across development and field.",
            "Communication module IP / node addresses recorded on the drawing.",
            "Battery / NVRAM status noted for legacy platforms.",
            "Backup of running program kept in the panel binder and in version control.",
        ])},
    ],
    "related":[
        ("PLC vs Relay Logic","PLC vs Relay Logic.html"),
        ("Discrete IO Modules","Discrete IO Modules.html"),
        ("Analog IO Basics","Analog IO Basics.html"),
        ("Ladder Logic Basics","../06_PLC_Programming_&_Logic/Ladder Logic Basics.html"),
        ("IEC 61131-3","../11_Standards_and_Codes/IEC 61131-3 – PLC Programming.html"),
    ],
},

"PLC vs Relay Logic.html": {
    "title": "PLC vs Relay Logic",
    "meta": {"category":"PLCs & Automation Hardware","tags":["#relaylogic","#PLC","#migration","#hardwired"],
             "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Hard-wired relay logic was the original industrial control method. Every state transition was a physical contact; every interlock was a wire. PLCs replaced that with software but kept the visual language (ladder logic) so existing electricians could read it. Understanding the differences is critical when you troubleshoot older machines or retrofit hard-wired panels to a PLC.")},
        {"title":"Side-by-Side","body": table(
            ["Aspect","Relay Logic","PLC"],
            [
                ["Changes","Rewiring","Software edit"],
                ["Size","Large panel, many relays","Compact CPU + I/O"],
                ["Speed","~25–50 ms per operation","1–50 ms full scan"],
                ["Diagnostics","Meter tracing contact by contact","Online monitor of every rung and tag"],
                ["Documentation","Hand-drawn ladder schematics","Exported program + auto-generated diagnostics"],
                ["Cost (small systems)","Lower for < 10 relays","Breaks even around 10–20 relays"],
                ["Cost (large systems)","Very expensive — panels, labor, maintenance","Lower"],
                ["Complex functions","Impractical (PID, math, comms)","Built-in"],
                ["Mean time to repair","High — trace, replace, rewire","Low — reload backup, swap module"],
            ])},
        {"title":"When hard-wired still wins","body": ul([
                "Safety-rated stop circuits that must be fail-safe and independent of software — see <a href=\"../12_Safety_Systems_Advanced/Emergency Stops (E-Stops).html\">E-Stops</a>.",
                "Very small and cheap machines where adding a PLC isn't justified.",
                "As a monitored backup to a PLC-based interlock.",
            ])},
        {"title":"Retrofit Strategy","body": ol([
                "Trace the existing schematic and build a clean electronic copy.",
                "Identify safety functions — keep those hard-wired or implement them in a <a href=\"Safety Relays &amp; Safety PLCs.html\">safety PLC</a>.",
                "Map every input and output to a PLC tag.",
                "Translate each rung to ladder logic.",
                "Add improvements that were impossible before — fault logs, alarm messages, HMI.",
                "Commission with the old panel still available as a comparison reference if possible.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Safety circuits remain independent of the PLC unless a safety PLC is used.",
            "Every external relay retained is documented in the PLC program description.",
            "Power-up state of the PLC doesn't create an unexpected output pulse.",
            "Old hand-drawn drawings are updated to reflect the PLC retrofit.",
        ])},
    ],
    "related":[
        ("What is a PLC","What is a PLC.html"),
        ("Ladder Logic Basics","../06_PLC_Programming_&_Logic/Ladder Logic Basics.html"),
        ("Safety Relays & Safety PLCs","Safety Relays &amp; Safety PLCs.html"),
    ],
},

"Discrete IO Modules.html": {
    "title":"Discrete IO Modules",
    "meta":{"category":"PLCs & Automation Hardware","tags":["#discrete","#digital","#IO","#sinking","#sourcing","#isolation"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Discrete (digital) I/O modules handle on/off signals — the single largest category of PLC I/O in a typical machine. Every push-button, limit switch, pilot light, contactor, and solenoid lives on a discrete point.")},
        {"title":"Common Types","body": table(
            ["Type","Common Voltage","Typical Use"],
            [
                ["24 VDC input (sinking / sourcing)","24 VDC","Proximity sensors, limit switches, relay contacts"],
                ["120 VAC input","120 VAC","Legacy panels, push-buttons with transformer-fed control"],
                ["230 VAC input","230 VAC","European machinery, some process controls"],
                ["24 VDC output (transistor)","24 VDC, 0.5–2 A","Solenoids, <a href=\"../03_Control_Devices/Relays &amp; Interposing Relays.html\">interposing relays</a>, LEDs"],
                ["Relay output","Up to 2 A, 240 VAC or 30 VDC","General-purpose dry contact; for mixed voltages"],
                ["120/240 VAC output (triac)","0.5–2 A AC","AC solenoids, small motors via contactor coil"],
            ])},
        {"title":"Key Selection Criteria","body": ul([
                "Input polarity — see <a href=\"Sinking vs Sourcing Inputs.html\">Sinking vs Sourcing</a>.",
                "Points per module — 8, 16, 32 common. More points = cheaper per point but one failure kills more I/O.",
                "Module isolation — group vs. point. Point-isolated is needed when mixing voltages or sources.",
                "Diagnostic features — channel-level fault detect, surge protection, short-circuit protection.",
                "Removable terminal block (RTB) for hot-swap during service.",
            ])},
        {"title":"Wiring Conventions","body": code(
"Sourcing input module, DC sensor with NPN output (sinking sensor):\n"
"  +24V ---+-------- sensor V+\n"
"          |\n"
"  module  |       sensor signal\n"
"  input <-+------- sensor OUT\n"
"   ^ input draws current to common through sensor\n"
"  0V -------------- sensor 0V\n\n"
"Sourcing input module, PNP sensor:\n"
"  +24V -------- sensor V+\n"
"                sensor OUT (switched +24V)\n"
"  input <------ sensor OUT\n"
"  0V  --------- sensor 0V\n\n"
"Mismatch between sinking / sourcing = input never sees a signal.\n")
        },
        {"title":"Field Checklist","body": tasks([
            "Module voltage and polarity match field devices.",
            "Fused or current-limited outputs if driving inductive loads.",
            "Common (return) bus grounded at a single point per NEC 250 rules.",
            "Spare points terminated or labeled to avoid future shorts.",
            "Labels at every terminal block reference the PLC tag and schematic sheet.",
        ])},
    ],
    "related":[
        ("Sinking vs Sourcing Inputs","Sinking vs Sourcing Inputs.html"),
        ("Wiring Inputs & Outputs to PLCs","Wiring Inputs &amp; Outputs to PLCs.html"),
        ("Analog IO Basics","Analog IO Basics.html"),
        ("Relays & Interposing Relays","../03_Control_Devices/Relays &amp; Interposing Relays.html"),
    ],
},

"Analog IO Basics.html":{
    "title":"Analog IO Basics",
    "meta":{"category":"PLCs & Automation Hardware","tags":["#analog","#420mA","#010V","#scaling","#ADC"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Analog I/O handles continuous signals — temperature, pressure, level, flow, speed reference, valve position. Unlike discrete points, analog signals carry a range of values that must be converted to a number the PLC can work with.")},
        {"title":"Signal Standards","body": table(
            ["Signal","Range","Typical Use","Notes"],
            [
                ["4–20 mA current loop","4 = 0%, 20 = 100%","Process instruments, actuators","Self-diagnosing: 0 mA = fault"],
                ["0–20 mA","0 = 0%, 20 = 100%","Older process inputs","No break detection"],
                ["0–10 VDC","0 = 0%, 10 = 100%","VFD speed reference, HMI potentiometers","Ground-loop sensitive over long runs"],
                ["±10 VDC","Bipolar","Bidirectional speed or torque reference",""],
                ["RTD (Pt100, Pt1000)","3 or 4-wire","Temperature","Use 3-wire to cancel lead resistance"],
                ["Thermocouple (J, K, T, E, N)","mV, non-linear","Temperature","Requires cold-junction comp"],
                ["HART","4–20 mA + digital","Smart instruments","Carries diagnostics + secondary variables"],
            ])},
        {"title":"Resolution","body": p(
            "Analog modules use ADCs of 12, 14, 16, or 24 bits. A 16-bit module spanning 4–20 mA gives about 0.244 µA per count — plenty for most applications. The limit is usually the field instrument, not the PLC module."
        )},
        {"title":"Scaling","body": code(
"Raw count to engineering units (4–20 mA input, 16-bit, 0–100 PSI):\n"
"  raw_min = 6242  (4 mA)\n"
"  raw_max = 31208 (20 mA)\n"
"  scaled = (raw - 6242) * (100 - 0) / (31208 - 6242) + 0\n"
"\n"
"Use the CPT / SCP / NORM_X / SCALE instructions of your PLC\n"
"rather than rolling your own math.\n")
        },
        {"title":"Wiring","body": ul([
                "Shielded twisted-pair cable, shield grounded at one end only (usually the PLC).",
                "Separate analog conduit from 480 V and VFD output cables by at least 12 in (30 cm).",
                "4-wire transmitters are powered externally; 2-wire (loop-powered) are powered by the +24 V from the PLC via the loop.",
                "Always use a dedicated analog ground bar — don't bond to motor or power grounds.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Transmitter range in the PLC matches the transmitter's actual range, not its maximum.",
            "Loop integrity verified with a current simulator at 4, 12, 20 mA.",
            "Shield grounded at one end only — no ground loops.",
            "Scaled values verified in the HMI against a calibrated source.",
            "Broken-wire detect (on 4–20 mA, reading ≤ 2 mA) wired to an alarm.",
        ])},
    ],
    "related":[
        ("Discrete IO Modules","Discrete IO Modules.html"),
        ("Wiring Inputs & Outputs to PLCs","Wiring Inputs &amp; Outputs to PLCs.html"),
        ("PID Tuning Basics","../10_System_Integration_&_Commissioning/PID Tuning Basics.html"),
        ("IO Checkout & Loop Testing","../10_System_Integration_&_Commissioning/IO Checkout &amp; Loop Testing.html"),
    ],
},

"Sinking vs Sourcing Inputs.html":{
    "title":"Sinking vs Sourcing Inputs",
    "meta":{"category":"PLCs & Automation Hardware","tags":["#sinking","#sourcing","#PNP","#NPN","#DC","#IO"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Sinking and sourcing describe the direction of current flow on a DC I/O point. Mix them up and the input will never see a signal, or the output will never drive the load. This single concept trips up more beginners than any other.")},
        {"title":"The Rule","body":
            "<h3>Input modules</h3>" + ul([
                "A <strong>sinking input</strong> provides 0 V internally and waits for the field device to supply +V.",
                "A <strong>sourcing input</strong> provides +V internally and waits for the field device to supply 0 V.",
                "You need a matching field device: sinking input + PNP sensor, or sourcing input + NPN sensor. <em>Wrong way round: no signal.</em>",
            ]) +
            "<h3>PNP vs NPN sensor</h3>" + ul([
                "<strong>PNP (sourcing sensor)</strong> — switches +24 V to the output when active. Pairs with sinking input modules. Standard in Europe and most of the world.",
                "<strong>NPN (sinking sensor)</strong> — switches 0 V to the output when active. Pairs with sourcing input modules. Common in Asia and legacy US equipment.",
            ]) +
            "<h3>Output modules</h3>" + p(
                "Same vocabulary, reversed: a sourcing output switches +V to the load; a sinking output switches 0 V. Pick outputs that match your loads and field wiring standard."
            )
        },
        {"title":"Quick Decision Chart","body": table(
            ["Module Type","Field Device Needed","Signal Goes"],
            [
                ["Sinking input","PNP sensor / sourcing field device","+24 V → input point"],
                ["Sourcing input","NPN sensor / sinking field device","input point → 0 V"],
                ["Sourcing output","Load referenced to 0 V","output → load → 0 V"],
                ["Sinking output","Load referenced to +24 V","+24 V → load → output"],
            ])},
        {"title":"Why It Trips People Up","body": ul([
                "Words describe current direction from the module's perspective, not the sensor's.",
                "Some manufacturers label it 'positive logic / negative logic' which confuses more than it clarifies.",
                "Most modern AB and Siemens modules are sinking input / PNP sensor — when in doubt, check the datasheet.",
                "Cheap 'universal' modules let you strap either way at the common terminal; read the manual.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Module polarity confirmed in datasheet before sensor selection.",
            "Sensor polarity labeled on each device and in the wire book.",
            "Don't mix PNP and NPN devices on the same common unless the module allows it.",
            "If you see intermittent inputs, measure voltage with the sensor active and inactive.",
        ])},
    ],
    "related":[
        ("Discrete IO Modules","Discrete IO Modules.html"),
        ("Proximity Sensors Inductive Capacitive","../03_Control_Devices/Proximity Sensors Inductive Capacitive.html"),
        ("Wiring Inputs & Outputs to PLCs","Wiring Inputs &amp; Outputs to PLCs.html"),
    ],
},

"Common PLC Brands & Differences.html":{
    "title":"Common PLC Brands & Differences",
    "meta":{"category":"PLCs & Automation Hardware","tags":["#rockwell","#siemens","#omron","#mitsubishi","#schneider"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Every major PLC vendor follows IEC 61131-3 broadly, but the software, hardware, and philosophy differ. Knowing the strengths and quirks helps you pick tools, hire techs, and work on existing machines without surprises.")},
        {"title":"The Big Five","body": table(
            ["Brand","Platforms","Software","Notable Quirks"],
            [
                ["Rockwell / Allen-Bradley","ControlLogix, CompactLogix, Micro800, MicroLogix","Studio 5000 Logix Designer, Connected Components","Tag-based data, AOIs, Ethernet/IP native. Dominant in North America."],
                ["Siemens","S7-1500, S7-1200, S7-300 (legacy), S7-400 (legacy), LOGO!","TIA Portal","Dominant in Europe. PROFINET native. Powerful SCL (Structured Text) implementation."],
                ["Schneider Electric","Modicon M580/M340, M221","EcoStruxure Machine Expert, Unity Pro, Control Expert","Tight integration with their HMIs (Magelis) and drives (Altivar)."],
                ["Mitsubishi","MELSEC iQ-R, iQ-F, Q, FX","GX Works3","Very common in Asia. Compact form factor. Fast execution."],
                ["Omron","NJ/NX, CJ2, CP1","Sysmac Studio","Motion-control strong. EtherCAT native on NJ/NX."],
            ])},
        {"title":"Honorable Mentions","body": ul([
                "Beckhoff TwinCAT — software-PLC running on industrial PC, EtherCAT native, popular in high-performance motion.",
                "B&R Automation — integrated machine-control platform, now owned by ABB.",
                "Phoenix Contact / WAGO — PC-based and IEC 61131-3 open platforms.",
                "AutomationDirect (Productivity, CLICK, Do-more) — low-cost US brand, straightforward software.",
                "IDEC, Keyence — panel-mount micro PLCs for small OEM machines.",
                "GE (now Emerson) PACSystems — process-heavy.",
            ])},
        {"title":"Picking a Platform","body": ul([
                "Does the plant already standardize on a brand? Match it — spares, training, support matter more than 'which is best'.",
                "Does the OEM require a specific brand? Machine warranty often depends on not swapping the controller.",
                "Is motion required? EtherCAT-based (Beckhoff, Omron NJ, Kollmorgen, B&R) give you the easiest path.",
                "Is safety required? <a href=\"Safety Relays &amp; Safety PLCs.html\">Safety PLCs</a> are brand-specific — plan early.",
                "Are ladder programmers in the labor market? Rockwell dominates for that skillset in North America.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Firmware, software, and license info archived in the panel binder.",
            "Vendor support contract valid for the deployed firmware.",
            "Replacement strategy: identical module in spares or same firmware family.",
            "IDE installation media + license archived off-machine.",
        ])},
    ],
    "related":[
        ("What is a PLC","What is a PLC.html"),
        ("IEC 61131-3 – PLC Programming","../11_Standards_and_Codes/IEC 61131-3 – PLC Programming.html"),
        ("Common Protocols","../08_Industrial_Networks_&_Protocols/Common Protocols.html"),
    ],
},

"Wiring Inputs & Outputs to PLCs.html":{
    "title":"Wiring Inputs & Outputs to PLCs",
    "meta":{"category":"PLCs & Automation Hardware","tags":["#wiring","#IO","#surge","#interposing","#labeling"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "PLC I/O wiring is where a lot of field time goes. Good habits on the first install save hours of troubleshooting later.")},
        {"title":"Best Practices","body": ul([
                "One terminal, one wire. Never double-lug a PLC terminal — use a terminal strip if you need to branch.",
                "Use ferrules on all stranded wires going into spring-cage or screw terminals.",
                "Keep 24 VDC control separate from 120 VAC and 480 VAC in trunking — see <a href=\"../02_Power_Distribution/Panel Wiring Best Practices.html\">Panel Wiring Best Practices</a>.",
                "Fuse each common bus so a shorted field device doesn't take out the module.",
                "Use <a href=\"../03_Control_Devices/Relays &amp; Interposing Relays.html\">interposing relays</a> for any output driving an inductive load (solenoid, contactor coil).",
                "Add flyback diodes or RC snubbers on DC inductive loads.",
                "Label every wire with a unique number that matches the schematic.",
            ])},
        {"title":"Typical DC Input Wiring","body": code(
"Sourcing (PNP sensor to sourcing input):\n"
"  +24VDC -- sensor brown\n"
"  0V     -- sensor blue\n"
"  Output -- sensor black -- PLC input terminal\n"
"  PLC input common terminal -- 0V\n"
)},
        {"title":"Typical DC Output Wiring","body": code(
"Sourcing output, 24 VDC solenoid with interposing relay:\n"
"  PLC output --(+)-- relay coil A1\n"
"  0V -- relay coil A2 (with flyback diode A2 to A1, cathode to A1)\n"
"  Relay contact NO -- switches 120 VAC hot to solenoid\n"
"  120 VAC neutral returns from solenoid\n"
)},
        {"title":"Grounding & Shielding","body": ul([
                "Signal common 0 V bonded to panel ground at one point.",
                "Analog cable shields grounded at the PLC only (not at the sensor).",
                "VFD motor leads shielded and grounded at both ends, drain wire separate.",
                "Machine frame bonded to ground per <a href=\"../11_Standards_and_Codes/NFPA 79 – Machinery Electrical.html\">NFPA 79</a>.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Every wire labeled and matched to schematic.",
            "Each input / output tested end-to-end during <a href=\"../10_System_Integration_&_Commissioning/IO Checkout &amp; Loop Testing.html\">IO checkout</a>.",
            "Ferrules on stranded conductors at every screw terminal.",
            "Interposing relays and flyback diodes in place on inductive loads.",
            "Spare inputs and outputs terminated or labeled to prevent accidental shorts.",
        ])},
    ],
    "related":[
        ("Discrete IO Modules","Discrete IO Modules.html"),
        ("Sinking vs Sourcing Inputs","Sinking vs Sourcing Inputs.html"),
        ("Panel Wiring Best Practices","../02_Power_Distribution/Panel Wiring Best Practices.html"),
        ("IO Checkout & Loop Testing","../10_System_Integration_&_Commissioning/IO Checkout &amp; Loop Testing.html"),
    ],
},

"PLC Power Supplies.html":{
    "title":"PLC Power Supplies",
    "meta":{"category":"PLCs & Automation Hardware","tags":["#PSU","#24VDC","#power","#UPS","#redundancy"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "PLCs and sensors run on clean 24 VDC in nearly every modern panel. The power supply is the one component that will take the whole system down if it fails and is the easiest one to under-specify.")},
        {"title":"Selection","body": table(
            ["Parameter","Guidance"],
            [
                ["Input voltage","Match the control transformer secondary (120 VAC or 230 VAC typical)"],
                ["Output voltage","24 VDC nominal; adjustable ±10%"],
                ["Output current","Sum all 24 VDC loads (PLC, I/O, sensors, HMIs, relays); add 25% margin"],
                ["Ripple / noise","< 50 mVpp is clean enough for industrial control"],
                ["Efficiency","≥ 92% reduces panel heat load"],
                ["MTBF","≥ 500,000 hrs at 40 °C for continuous-duty"],
                ["Features","Short-circuit fold-back, thermal shutdown, status relay, parallel / redundancy diodes"],
                ["Mounting","DIN rail, compact vertical orientation for heat rise"],
            ])},
        {"title":"Redundancy & Buffering","body": ul([
                "Redundant parallel supplies + diode module keeps the bus alive during supply failure.",
                "Buffer modules store energy in capacitors or supercaps to ride through 100–300 ms brownouts — cheap insurance against a contactor surge dropping the 24 VDC bus.",
                "UPS modules add minutes of battery holdup for ordered shutdown.",
            ])},
        {"title":"Typical 24 VDC Bus","body": code(
"Main 24 VDC + --- fuse ---+--- PLC CPU\n"
"                          +--- IO modules common\n"
"                          +--- HMI\n"
"                          +--- field sensors\n"
"Main 24 VDC 0V (common) -- bonded to panel ground at one point\n"
)},
        {"title":"Field Checklist","body": tasks([
            "Supply rated ≥ 125% of measured load.",
            "24 VDC bus fused per-branch, not just at the supply.",
            "Status output wired to PLC for alarm.",
            "Buffer / UPS installed on critical systems.",
            "Output voltage trimmed to 24.2–24.5 V to give sensor margin over long runs.",
            "Ventilation clearance per datasheet.",
        ])},
    ],
    "related":[
        ("Control Transformers","../02_Power_Distribution/Control Transformers.html"),
        ("Panel Cooling & Power Conditioning","../13_Specialty_Topics/Panel Cooling &amp; Power Conditioning.html"),
        ("Wiring Inputs & Outputs to PLCs","Wiring Inputs &amp; Outputs to PLCs.html"),
    ],
},

"Safety Relays & Safety PLCs.html":{
    "title":"Safety Relays & Safety PLCs",
    "meta":{"category":"PLCs & Automation Hardware","tags":["#safety","#SIL","#PL","#GuardLogix","#redundancy"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"ISO 13849-1, IEC 62061, IEC 61508"},
    "sections":[
        {"title":"Description","body": p(
            "Safety relays and safety PLCs are specifically certified to process functional-safety signals — E-stops, light curtains, guard switches, two-hand controls — and bring the machine to a safe state even in the presence of internal faults. An ordinary PLC is <em>not</em> a substitute unless it is certified as a safety PLC.")},
        {"title":"Safety Relay vs Safety PLC","body": table(
            ["Aspect","Safety Relay","Safety PLC"],
            [
                ["Application","1–3 safety functions","Many safety functions, complex logic"],
                ["Configuration","DIP switches, fixed logic","Programmed in certified safety blocks"],
                ["Cost","Low","Higher"],
                ["Flexibility","Low","High"],
                ["Examples","Allen-Bradley MSR, Pilz PNOZ, Sick UE","GuardLogix, S7-1500 F, Pilz PSS4000"],
                ["Typical SIL / PL","SIL 3 / PL e","SIL 3 / PL e"],
            ])},
        {"title":"Safety Categories","body": table(
            ["Spec","Meaning"],
            [
                ["Category B","No specific safety measures — minimal"],
                ["Category 1","Well-tried components, single channel"],
                ["Category 2","Single channel with periodic testing"],
                ["Category 3","Single fault doesn't cause loss of safety function"],
                ["Category 4","Single fault detected, no accumulation of faults"],
                ["SIL 1–4","IEC 61508 / 62061 risk-reduction levels"],
                ["PL a–e","ISO 13849-1 performance levels"],
            ])},
        {"title":"How They Work","body": ul([
                "Dual-channel input sensing with cross-monitoring to detect stuck or shorted wiring.",
                "Force-guided safety contacts on the output relays so a welded contact is detected.",
                "Periodic self-tests of internal circuitry.",
                "Safety PLCs additionally run diverse code paths on redundant CPUs and compare results every scan.",
            ])},
        {"title":"When a Safety PLC Wins","body": ul([
                "More than 3–4 safety functions.",
                "Muting, blanking, speed monitoring, or safe-stop-category-1 (SS1) required.",
                "Shared I/O between safety and standard control (via integrated GuardLogix or F-PLC).",
                "Auditability — version history, change tracking, signed programs.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Safety function risk assessment completed and signed.",
            "Architecture (Cat / PL) matches risk.",
            "Safety I/O verified with forced-fault testing during commissioning.",
            "Safety program and settings locked with a password; signed and archived.",
            "Stop category documented for each E-stop — see <a href=\"../12_Safety_Systems_Advanced/Emergency Stops (E-Stops).html\">E-Stops</a>.",
        ])},
    ],
    "related":[
        ("Emergency Stops (E-Stops)","../12_Safety_Systems_Advanced/Emergency Stops (E-Stops).html"),
        ("Risk Assessments & Functional Safety","../12_Safety_Systems_Advanced/Risk Assessments &amp; Functional Safety.html"),
        ("Safety Fencing & Interlocks","../12_Safety_Systems_Advanced/Safety Fencing &amp; Interlocks.html"),
        ("SIL - PL Functional Safety Intro","../11_Standards_and_Codes/SIL - PL Functional Safety Intro.html"),
    ],
},

}
CONTENT = {FOLDER: PAGES}
