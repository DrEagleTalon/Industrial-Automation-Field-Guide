"""Content for 09_Troubleshooting_&_Diagnostics."""

FOLDER = "09_Troubleshooting_&_Diagnostics"

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

"General Troubleshooting Methodology.html":{
    "title":"General Troubleshooting Methodology",
    "meta":{"category":"Troubleshooting & Diagnostics","tags":["#troubleshooting","#method","#divideandconquer","#rootcause"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Good troubleshooting is a disciplined process, not a talent. A junior tech with a clean method will out-diagnose a senior tech working on intuition every time.")},
        {"title":"The Method","body": ol([
                "<strong>Verify the problem</strong> — witness it or reproduce it; don't work from second-hand reports alone.",
                "<strong>Check what changed</strong> — 90% of new problems come from a recent change (software, parts, parameters, maintenance).",
                "<strong>Gather evidence</strong> — fault codes, alarms, recent history, operator description.",
                "<strong>Form a hypothesis</strong> — what's the simplest explanation that fits the evidence?",
                "<strong>Test safely</strong> — one thing at a time, reversible steps first.",
                "<strong>Confirm root cause</strong> — not just the symptom. If you can't explain <em>why</em>, you'll see it again.",
                "<strong>Document</strong> — for yourself (next time) and for the team.",
            ])},
        {"title":"Divide & Conquer","body": ul([
                "Break the system into halves and test at the boundary.",
                "For signal problems, measure upstream and downstream of suspect component.",
                "For logic problems, test one permissive at a time.",
                "For network problems, test physical layer before protocol.",
            ])},
        {"title":"Safety First","body": ul([
                "LOTO before any work inside a panel. See <a href=\"../01_Electrical_Fundamentals/Lockout Tagout (LOTO) Procedures.html\">LOTO</a>.",
                "PPE rated for the available fault current and arc flash.",
                "Never bypass a safety device to 'check something quickly'.",
                "Two hands on the meter — one behind your back when probing live.",
            ])},
        {"title":"Documentation Habits","body": ul([
                "Log the symptom, cause, and fix for every non-trivial event.",
                "Record meter readings, fault codes, timestamps.",
                "Update the schematic if the field wiring doesn't match.",
                "Photograph the condition before you touch anything you can't easily restore.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Problem reproduced and described precisely.",
            "Recent changes identified and ruled in or out.",
            "Evidence collected before parts are swapped.",
            "Root cause documented — not just 'replaced contactor'.",
        ])},
    ],
    "related":[
        ("Power Circuit Faults","Power Circuit Faults.html"),
        ("Control Circuit Faults","Control Circuit Faults.html"),
        ("Reading Schematics & Wiring Diagrams","../14_Soft_Skills_Workflow/Reading Schematics &amp; Wiring Diagrams.html"),
        ("Writing Work Orders & Reports","../14_Soft_Skills_Workflow/Writing Work Orders &amp; Reports.html"),
    ],
},

"Power Circuit Faults.html":{
    "title":"Power Circuit Faults",
    "meta":{"category":"Troubleshooting & Diagnostics","tags":["#power","#breaker","#fuse","#shortcircuit","#groundfault"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Power-side faults are the ones that pop breakers, blow fuses, and can hurt people. They demand slower, safer diagnostics than control-side problems.")},
        {"title":"Common Fault Types","body": table(
            ["Fault","Signature","Typical Cause"],
            [
                ["Short circuit","Breaker trips instantly or fuse blows violently","Pinched cable, loose lug touching case, motor winding-to-winding"],
                ["Ground fault","GFCI/GFI trips; phase current mismatch","Damaged insulation, moisture, worn motor winding"],
                ["Overload","Breaker trips slowly (thermal curve)","Mechanical bind, undersized conductor"],
                ["Single-phasing","Motor hums, one phase at zero current","Blown one fuse, open wire"],
                ["Voltage unbalance > 1%","High motor temperature, reduced torque","Uneven loading, transformer tap, loose connection"],
                ["Over-voltage","All equipment runs hot","Lost neutral, utility issue, wrong tap"],
                ["Arc fault","Loud bang, scorching, carbon tracks","Loose connection, insulation breakdown, stab worn"],
            ])},
        {"title":"Diagnostic Workflow","body": ol([
                "LOTO and verify dead before any internal inspection.",
                "Visual: look for scorching, melted lugs, bowed bus, discolored insulation.",
                "Check torque on every power lug with a calibrated torque wrench.",
                "Megger motor leads separately from the panel — see <a href=\"../04_Motor_Control/Motor Megger Testing.html\">Motor Megger Testing</a>.",
                "With system re-energized and load off, measure line-to-line and line-to-ground voltages at the main.",
                "Re-energize the load slowly — watch for rising current with an amp clamp.",
            ])},
        {"title":"Common Field Causes","body": ul([
                "A loose lug at a contactor that looks fine until you torque it — loose for years, then fails fast.",
                "Rodent damage on flexible cord to a motor that runs intermittently.",
                "A flex conduit that rubs through insulation at a sharp bend.",
                "A neutral on a 120/240 split-phase that opens, swinging voltages wildly.",
                "Water in a junction box after a wash-down.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "LOTO applied and verified.",
            "Megger before closing any breaker on a newly-wired circuit.",
            "All lugs torqued to spec.",
            "IR camera scan after first energization.",
            "Fault investigated to root cause before a repair is signed off.",
        ])},
    ],
    "related":[
        ("Control Circuit Faults","Control Circuit Faults.html"),
        ("Motor Overheating & Tripping","Motor Overheating &amp; Tripping.html"),
        ("Motor Megger Testing","../04_Motor_Control/Motor Megger Testing.html"),
        ("Fuses vs Breakers","../02_Power_Distribution/Fuses vs Breakers.html"),
        ("General Troubleshooting Methodology","General Troubleshooting Methodology.html"),
    ],
},

"Control Circuit Faults.html":{
    "title":"Control Circuit Faults",
    "meta":{"category":"Troubleshooting & Diagnostics","tags":["#control","#24VDC","#relay","#contact"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Control-side problems are the everyday bread and butter of troubleshooting: a motor won't start, a solenoid chatters, a light stays on, an input reads wrong.")},
        {"title":"Voltage Check First","body": ul([
                "Measure supply voltage at the source (control transformer output or 24 VDC supply output).",
                "Then measure at the target device's coil or input.",
                "A drop of more than 10% across a run indicates high-resistance connections or undersized wire.",
            ])},
        {"title":"Common Symptoms","body": table(
            ["Symptom","Likely Cause","First Check"],
            [
                ["Contactor won't pick","Open control path","Voltage at coil; aux contact positions"],
                ["Contactor chatters","Low coil voltage, intermittent contact","Supply voltage under load"],
                ["Sensor reads wrong","Sinking vs sourcing mismatch","<a href=\"../05_PLCs & Automation Hardware/Sinking vs Sourcing Inputs.html\">Polarity check</a>"],
                ["Solenoid won't release","Stuck plunger or wrong coil voltage","Manual test, measure off-state voltage"],
                ["Output works in manual, not auto","Logic interlock missing","<a href=\"../06_PLC_Programming_&_Logic/Interlocking &amp; Permissives.html\">Permissive review</a>"],
                ["Random faults","Loose terminal or bad wire","Re-torque; wiggle test"],
            ])},
        {"title":"Tooling","body": ul([
                "Multimeter (DMM) — voltage, continuity, resistance.",
                "Clamp-on ammeter for DC and AC, down to milliamps.",
                "Low-impedance tester (LoZ / Wiggy) to defeat ghost voltages.",
                "Logic probe or PLC online to watch inputs / outputs in real time.",
                "Schematic on tablet or laminated print — never troubleshoot blind.",
            ])},
        {"title":"Ghost Voltages","body": p(
            "High-impedance meters will read capacitive-coupled 'ghost' voltages on disconnected wires — often 30–60 V on a cable that is actually dead. Use a LoZ tester or a solenoid tester to check for a real circuit.")
        },
        {"title":"Field Checklist","body": tasks([
            "Voltage measured at source and at load.",
            "Schematic matches field wiring — or schematic updated.",
            "Intermittent faults investigated with data log, not single-shot reading.",
            "Loose connections re-torqued and recorded.",
        ])},
    ],
    "related":[
        ("Power Circuit Faults","Power Circuit Faults.html"),
        ("PLC Input Not Responding","PLC Input Not Responding.html"),
        ("PLC Output Not Driving Load","PLC Output Not Driving Load.html"),
        ("Wiring & Testing Control Circuits","../03_Control_Devices/Wiring &amp; Testing Control Circuits.html"),
        ("General Troubleshooting Methodology","General Troubleshooting Methodology.html"),
    ],
},

"Motor Overheating & Tripping.html":{
    "title":"Motor Overheating & Tripping",
    "meta":{"category":"Troubleshooting & Diagnostics","tags":["#motor","#overload","#overheat","#unbalance"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "A motor that trips or runs hot is complaining about something. Before replacing the overload or winding, diagnose what is causing the heat.")},
        {"title":"Common Causes","body": table(
            ["Cause","Evidence","Fix"],
            [
                ["Mechanical overload","High running current, close to FLA or above","Reduce load, check bearings, realign, clean"],
                ["Voltage unbalance","Phase voltages differ > 1%","Measure, find the source — often a loose lug upstream"],
                ["Single-phasing","One phase current zero","Find the open phase — fuse, cable, breaker"],
                ["Blocked cooling","Dust / debris on fan or frame","Clean frame and fan; verify airflow"],
                ["VFD running low-speed too long","Temp climbs on TEFC motor","Add blower or use inverter-duty motor"],
                ["Ambient too high","> 40 °C room temp","Cool the room or derate the motor"],
                ["Bearing failure","Noise, current rising slowly","Replace bearings; check coupling alignment"],
                ["Aged insulation","Low IR on megger","Rewind or replace"],
                ["Wrong overload setting","Trips on normal start","Reset to nameplate FLA; check trip class"],
                ["Frequent starts","Exceeded starts/hour","VFD or soft-start; schedule starts"],
            ])},
        {"title":"Measurements Worth Logging","body": ul([
                "All three line-to-line voltages, running and stopped.",
                "All three line currents at steady state.",
                "Percent unbalance (max deviation / average × 100).",
                "Surface temperature on the motor frame with an IR thermometer.",
                "Motor winding temperature if a PTC / RTD is fitted.",
                "Cooling air temperature entering the motor.",
            ])},
        {"title":"Reference Numbers","body": ul([
                "Voltage unbalance < 1% is good; 2% causes 15–20% current unbalance; > 5% is a fault.",
                "TEFC frame temperature ~40–60 °C above ambient is normal at full load.",
                "Class F motor handles 105 °C rise over 40 °C ambient.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Megger tested and recorded — see <a href=\"../04_Motor_Control/Motor Megger Testing.html\">Megger Testing</a>.",
            "Voltage and current unbalance calculated.",
            "Bearings listened to with a stethoscope.",
            "Frame clear of debris and airflow unobstructed.",
            "Overload setting confirmed at FLA.",
        ])},
    ],
    "related":[
        ("Overload Relays","../04_Motor_Control/Overload Relays.html"),
        ("Motor Megger Testing","../04_Motor_Control/Motor Megger Testing.html"),
        ("3-Phase Motor Basics","../04_Motor_Control/3-Phase Motor Basics.html"),
        ("VFD Trips & Fault Codes","VFD Trips &amp; Fault Codes.html"),
    ],
},

"VFD Trips & Fault Codes.html":{
    "title":"VFD Trips & Fault Codes",
    "meta":{"category":"Troubleshooting & Diagnostics","tags":["#VFD","#faultcode","#overcurrent","#overvoltage","#DCbus"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Every VFD has a fault code list that looks intimidating but boils down to a dozen root causes. Know those and you'll solve 90% of drive trips in one pass.")},
        {"title":"Family of Common Faults","body": table(
            ["Fault Category","Examples","Typical Cause"],
            [
                ["Overcurrent (F3 / F4 / F7)","OC at start, OC running","Undersized ramp, shorted motor lead, mechanical bind"],
                ["DC bus overvoltage","F5, bus high","Decel too fast, regen without DB resistor, high line voltage"],
                ["DC bus undervoltage","F6, bus low","Incoming voltage sag, missing phase, failing supply"],
                ["Ground fault","F13","Insulation failure, wet motor, long cable with high capacitance"],
                ["Overload (I²t)","F7, OL trip","Sustained high current, motor thermal model"],
                ["Motor overtemp","F71","PTC/RTD input, winding too hot, blocked cooling"],
                ["Drive overtemp","F8","Heatsink dusty, fan failure, ambient too high"],
                ["Comm loss","F81 / F83","Network cable, IP conflict, switch fault"],
                ["Encoder loss","F93","Encoder wiring, PPR wrong, noise"],
                ["Parameter fault","F100+","Inconsistent parameter set after firmware change"],
                ["Phase loss","F17","Open input or output phase"],
                ["Auto-tune fault","F80","Motor wiring wrong, locked rotor during tune"],
            ])},
        {"title":"Troubleshooting Flow","body": ol([
                "Read the fault code and the timestamp — many drives store the last 10.",
                "Check drive log for current, voltage, and speed at the moment of fault.",
                "Cycle power and check status — does it start clean or refault immediately?",
                "Perform a <a href=\"../04_Motor_Control/Motor Megger Testing.html\">megger test</a> if the fault is ground or short.",
                "Verify nameplate parameters and auto-tune values.",
                "Check input and output waveforms if possible (scope at the output).",
                "Review the load — mechanical bind is a frequent overcurrent culprit.",
            ])},
        {"title":"Vendor Fault Reference","body": ul([
                "Rockwell PowerFlex 525: F3 OC, F4 DC bus OV, F5 DC bus UV, F6 load loss, F7 OL, F13 GF, F63 missing phase.",
                "Siemens SINAMICS G120: F3xxx range for power, F5xxx for current, F7xxx for bus, F9xxx for comm.",
                "ABB ACS580: fault codes 2xxx for current, 3xxx for voltage, 4xxx for temperature.",
                "Always keep the drive manual's fault list bookmarked on your tablet.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Fault code recorded with timestamp.",
            "Drive log exported before clearing.",
            "Motor megger tested if fault is ground or short.",
            "Root cause documented before clearing the fault.",
            "Parameter changes noted if any were made.",
        ])},
    ],
    "related":[
        ("Variable Frequency Drives (VFDs) Basics","../04_Motor_Control/Variable Frequency Drives (VFDs) Basics.html"),
        ("VFD Parameters & Setup","../04_Motor_Control/VFD Parameters &amp; Setup.html"),
        ("Motor Overheating & Tripping","Motor Overheating &amp; Tripping.html"),
        ("Motor Megger Testing","../04_Motor_Control/Motor Megger Testing.html"),
    ],
},

"PLC Input Not Responding.html":{
    "title":"PLC Input Not Responding",
    "meta":{"category":"Troubleshooting & Diagnostics","tags":["#PLC","#input","#sensor","#24VDC"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "The PLC isn't seeing an input that the field device is supposedly sending. A fast, reliable diagnostic path covers 95% of cases.")},
        {"title":"Diagnostic Ladder","body": ol([
                "At the PLC: is the module status LED healthy (green)?",
                "At the module: does the point LED light when the device is activated?",
                "If point LED lights: the module sees it. The problem is in software — is the tag mapped correctly?",
                "If point LED does <em>not</em> light: the signal isn't getting there. Measure voltage on the terminal with the sensor active and inactive.",
                "If voltage is wrong: check field wiring, sinking/sourcing polarity, and sensor power.",
                "If voltage is correct but LED doesn't light: module defect — swap and re-check.",
            ])},
        {"title":"Common Causes","body": table(
            ["Cause","How to Spot"],
            [
                ["Wrong sensor polarity","PNP sensor on sourcing input (or vice versa)"],
                ["No sensor power","Sensor V+ open, blown fuse on 24 V bus"],
                ["Broken wire","Continuity test from terminal to sensor"],
                ["Terminal not tight","Voltage appears when wiggled"],
                ["Wrong tag mapping in PLC","Online monitor shows different input reacting"],
                ["Module damaged","Other points on the module also stuck or flaky"],
                ["Sensor fault","Sensor has 24 V but never switches — replace"],
                ["Misaligned sensor","Target is too far / wrong angle"],
            ])},
        {"title":"Useful Checks","body": ul([
                "Put the PLC online and watch the input in the tag window while manually activating the sensor.",
                "Force-on test: with safety interlocks respected, manually close the input to confirm the module works.",
                "Check if the input is part of an interlock that might be preventing a downstream action.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Module status LED and point LED observed.",
            "Voltage at input terminal verified in both states.",
            "Sensor polarity matches module type.",
            "Tag mapping confirmed in PLC.",
            "Sensor alignment and sensing distance checked.",
        ])},
    ],
    "related":[
        ("PLC Output Not Driving Load","PLC Output Not Driving Load.html"),
        ("Sinking vs Sourcing Inputs","../05_PLCs & Automation Hardware/Sinking vs Sourcing Inputs.html"),
        ("Discrete IO Modules","../05_PLCs & Automation Hardware/Discrete IO Modules.html"),
        ("Sensor Not Detecting","Sensor Not Detecting.html"),
    ],
},

"PLC Output Not Driving Load.html":{
    "title":"PLC Output Not Driving Load",
    "meta":{"category":"Troubleshooting & Diagnostics","tags":["#PLC","#output","#solenoid","#coil"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "PLC output is commanded on in software but the field device doesn't operate. Three places can go wrong: software, module, or field wiring.")},
        {"title":"Step-by-Step","body": ol([
                "Online monitor: is the tag actually TRUE? (Watch for conflicting rungs writing the same output.)",
                "Module LED for that point: lit?",
                "If LED lit but load doesn't operate: measure voltage at the output terminal and at the load.",
                "If LED not lit: software isn't actually commanding the point — or module is damaged.",
                "Disconnect load; measure open-circuit voltage at the terminal when the point is commanded.",
            ])},
        {"title":"Common Causes","body": table(
            ["Cause","How to Spot"],
            [
                ["Software conflict","Two rungs write the same coil; last wins, first appears dead"],
                ["Module fuse blown","Many modules have replaceable fuses per channel"],
                ["Over-current on sourcing output","Short on load side trips internal protection"],
                ["Wrong output type","Sinking output with load wired for sourcing"],
                ["No load-side common","Load has no path back to 0 V / neutral"],
                ["Interposing relay coil open","Replace relay; add suppression"],
                ["Solenoid coil open","Measure coil resistance"],
                ["Module damaged","Persistent off with no voltage at terminal"],
            ])},
        {"title":"Inductive Load Safety","body": p(
            "Driving solenoids, contactor coils, or relay coils directly from a PLC output without suppression will eventually destroy the module. Use an <a href=\"../03_Control_Devices/Relays &amp; Interposing Relays.html\">interposing relay</a>, and put a flyback diode on DC coils or an RC snubber on AC coils."
        )},
        {"title":"Field Checklist","body": tasks([
            "PLC online-monitor confirms the coil is commanded.",
            "Module LED state observed.",
            "Voltage at terminal measured with and without load.",
            "Suppression in place on inductive loads.",
            "No conflicting writes to the output tag.",
        ])},
    ],
    "related":[
        ("PLC Input Not Responding","PLC Input Not Responding.html"),
        ("Discrete IO Modules","../05_PLCs & Automation Hardware/Discrete IO Modules.html"),
        ("Wiring Inputs & Outputs to PLCs","../05_PLCs & Automation Hardware/Wiring Inputs &amp; Outputs to PLCs.html"),
        ("Relays & Interposing Relays","../03_Control_Devices/Relays &amp; Interposing Relays.html"),
    ],
},

"Sensor Not Detecting.html":{
    "title":"Sensor Not Detecting",
    "meta":{"category":"Troubleshooting & Diagnostics","tags":["#sensor","#prox","#photoelectric","#alignment"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "The sensor is powered but not seeing the target. This is 30% of field calls. Walk through the basics before swapping the sensor.")},
        {"title":"Common Causes","body": table(
            ["Cause","How to Spot","Fix"],
            [
                ["Misalignment","Target passes outside sensing range or angle","Realign, add deflector"],
                ["Sensing distance exceeded","Inductive too far from target","Spec check; closer mount"],
                ["Dirty lens (photoelectric)","Film of dust, oil, mist","Clean; add air purge"],
                ["Reflector dirty (retro)","Same","Clean"],
                ["Wrong target material","Non-ferrous object on standard inductive","Use all-metal or capacitive"],
                ["Wrong sensor type","Clear bottle on standard PE","Clear-object or ultrasonic sensor"],
                ["Background reflection","PE picks up far-side machine frame","Background suppression or polar filter"],
                ["Power not present","Sensor LED off","Check 24 V at terminal"],
                ["Polarity","Sensor output wired to wrong terminal","Swap"],
                ["Sensor drift","Temperature or vibration affecting teach","Re-teach; replace if chronic"],
                ["Sensor damage","Cracked housing, melted lens","Replace, add guard"],
            ])},
        {"title":"Quick Tests","body": ol([
                "Look at the sensor's own LEDs (power, output, margin).",
                "Wave a known target across the face at the expected distance.",
                "Measure output terminal voltage when triggered and idle.",
                "For PE: try a known reflector card or white cardboard at proper distance.",
                "For inductive: use a steel machinist tool close to the face as a known target.",
            ])},
        {"title":"Alignment Tips","body": ul([
                "Photoelectric alignment: use the sensor's signal-strength indicator (most have one).",
                "Mount on a rigid bracket — a vibrating bracket is the most common cause of intermittent detect.",
                "Add teach-in or adjust margin to handle the dirtiest expected condition, not just the cleanest.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Sensor power and LEDs observed.",
            "Output tested with a known target.",
            "Alignment verified with signal strength indicator.",
            "Mounting bracket confirmed rigid.",
            "Lens / reflector cleaned.",
        ])},
    ],
    "related":[
        ("Proximity Sensors Inductive Capacitive","../03_Control_Devices/Proximity Sensors Inductive Capacitive.html"),
        ("Photoelectric Sensors","../03_Control_Devices/Photoelectric Sensors.html"),
        ("Limit Switches & Mechanical Sensors","../03_Control_Devices/Limit Switches &amp; Mechanical Sensors.html"),
        ("PLC Input Not Responding","PLC Input Not Responding.html"),
    ],
},

"Network Communication Loss.html":{
    "title":"Network Communication Loss",
    "meta":{"category":"Troubleshooting & Diagnostics","tags":["#network","#comms","#EthernetIP","#Profinet","#drop"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "The PLC loses connection to a drive, an HMI, a remote I/O, or a peer controller. Could be cable, switch, config, or load. A structured approach beats guessing.")},
        {"title":"Quick Triage","body": ol([
                "Confirm what disconnected and when — fault log, alarm history.",
                "Did anything change? New device added, firmware push, switch reboot?",
                "Ping the peer from the PLC's engineering workstation.",
                "Check link lights and switch-port counters.",
                "Swap cable to a known-good spare if physical fault suspected.",
            ])},
        {"title":"Common Causes","body": table(
            ["Cause","Evidence"],
            [
                ["Cable fault","Intermittent, physical tug fixes it"],
                ["Connector","RJ45 loose in socket — industrial dust"],
                ["Duplex mismatch","High CRC errors on switch counter"],
                ["Power loss on device","Whole device silent, no link"],
                ["Switch port disabled / bad","Other ports fine"],
                ["IP conflict","Random drops, two devices show same IP"],
                ["VLAN change","Everyone works, new device doesn't"],
                ["Firewall / ACL","Ping works, protocol doesn't"],
                ["Network loop w/o STP","Broadcast storm, lots of devices affected"],
                ["Storm from single device","One noisy device floods network"],
                ["EtherNet/IP multicast flood","Lack of IGMP snooping"],
                ["Firmware bug","Stable, then starts dropping after upgrade"],
            ])},
        {"title":"Tools","body": ul([
                "Ping, arp, tracert — see <a href=\"../08_Industrial_Networks_&_Protocols/Network Troubleshooting (Ping, ARP, etc).html\">Network Troubleshooting</a>.",
                "Managed switch diagnostics — port counters, CPU load.",
                "Wireshark capture at a mirrored port.",
                "Cable tester / time-domain reflectometer.",
                "EtherNet/IP CIP connection status page on the AB module.",
            ])},
        {"title":"Preventive Measures","body": ul([
                "Ring topology with DLR / MRP / RSTP for redundant paths.",
                "Port security so a rogue device on a patch panel can't bring down the network.",
                "Proper strain relief and shielded industrial connectors.",
                "Documented IP plan; no DHCP on OT.",
                "SNMP monitoring of switches into the plant alarm stack.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Ping from host OS to peer succeeds.",
            "Switch port counters reviewed for CRC, giants, runts.",
            "Cable swapped as part of elimination.",
            "IP plan verified — no duplicates.",
            "Firmware versions of both ends recorded.",
        ])},
    ],
    "related":[
        ("Network Troubleshooting (Ping, ARP, etc)","../08_Industrial_Networks_&_Protocols/Network Troubleshooting (Ping, ARP, etc).html"),
        ("Common Protocols","../08_Industrial_Networks_&_Protocols/Common Protocols.html"),
        ("Switches & Managed Networks","../08_Industrial_Networks_&_Protocols/Switches &amp; Managed Networks.html"),
        ("IP Addressing & Subnetting","../08_Industrial_Networks_&_Protocols/IP Addressing &amp; Subnetting.html"),
    ],
},

}
CONTENT = {FOLDER: PAGES}
