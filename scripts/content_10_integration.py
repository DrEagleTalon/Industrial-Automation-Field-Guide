"""Content for 10_System_Integration_&_Commissioning."""

FOLDER = "10_System_Integration_&_Commissioning"

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

"Control Panel Layout & BOM.html":{
    "title":"Control Panel Layout & BOM",
    "meta":{"category":"System Integration & Commissioning","tags":["#panel","#layout","#BOM","#UL508A","#heat"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"UL 508A, NFPA 79, IEC 60204-1"},
    "sections":[
        {"title":"Description","body": p(
            "Control panel layout and the bill of materials (BOM) are where a good machine design is either set up or hamstrung. The goal: a panel that's serviceable, meets code, fits the heat load, and can be built repeatably.")},
        {"title":"Layout Principles","body": ul([
                "Top: incoming power, disconnect, main breaker, transformers.",
                "Middle: contactors, drives, overloads, safety relays.",
                "Bottom: PLC, terminal blocks, I/O, comms.",
                "Heat rises — put heat generators (drives, transformers, DC supplies) near the top or where cooling is.",
                "Wire ducts horizontal and vertical in a grid; leave 25% spare capacity.",
                "Space drives for airflow per datasheet.",
                "Keep 24 VDC and 480 VAC in separate ducts.",
                "Mount DIN rails at comfortable service height (30–60 in).",
                "Leave room for future I/O — add blank DIN rail and terminal strip.",
                "Label every component with a unique tag matching the BOM and schematic.",
            ])},
        {"title":"Thermal Design","body": p(
            "Sum the steady-state heat dissipation of every component (use datasheet W). Add margin for worst-case ambient. Compare against enclosure free convection, fan venting, or closed-loop air conditioner rating. See <a href=\"../13_Specialty_Topics/Panel Cooling &amp; Power Conditioning.html\">Panel Cooling</a>."
        )},
        {"title":"BOM Best Practices","body": ul([
                "Manufacturer part numbers, revisions, and suppliers.",
                "Qty per panel, alternates, and approved-equivalents column.",
                "Footprint or size for layout and spares planning.",
                "Safety-critical parts flagged — these require exact replacement.",
                "Include hardware (terminal blocks, end clamps, labels, wire markers).",
                "Export BOM to procurement / ERP and keep aligned with drawings.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Heat load calculation complete and filed.",
            "Spare DIN rail and duct capacity available.",
            "All components labeled and match schematic.",
            "UL 508A listing requirements met if needed — see <a href=\"../11_Standards_and_Codes/UL 508A – Control Panels.html\">UL 508A</a>.",
            "Panel photo documented for as-built record.",
        ])},
    ],
    "related":[
        ("Documentation Best Practices","Documentation Best Practices.html"),
        ("UL 508A – Control Panels","../11_Standards_and_Codes/UL 508A – Control Panels.html"),
        ("NFPA 79 – Machinery Electrical","../11_Standards_and_Codes/NFPA 79 – Machinery Electrical.html"),
        ("Panel Cooling & Power Conditioning","../13_Specialty_Topics/Panel Cooling &amp; Power Conditioning.html"),
        ("Panel Wiring Best Practices","../02_Power_Distribution/Panel Wiring Best Practices.html"),
    ],
},

"IO Checkout & Loop Testing.html":{
    "title":"IO Checkout & Loop Testing",
    "meta":{"category":"System Integration & Commissioning","tags":["#IO","#checkout","#loop","#pointcheck","#commissioning"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "I/O checkout (point-by-point) and loop testing (analog end-to-end) verify that every physical connection behaves the way the drawings and program say it should. Done well, they uncover 80% of field wiring problems before power-on.")},
        {"title":"Discrete I/O Checkout","body": ol([
                "Print the I/O list — tag, address, function, terminal, device, location.",
                "For each input: physically actuate the field device; confirm the PLC input reads correctly; sign off.",
                "For each output: force the PLC output (with proper safety) or drive from manual-mode logic; confirm the field device operates; sign off.",
                "Correct any labeling, tag, or wiring mismatch immediately and update the drawing.",
            ])},
        {"title":"Analog Loop Test","body": ol([
                "Isolate the instrument; inject a known source at the transmitter terminals (4 / 8 / 12 / 16 / 20 mA, or equivalent in mV for thermocouple).",
                "Observe the raw count in the PLC and scaled value in the HMI at each point.",
                "Record deviation from expected at each step.",
                "Confirm engineering units and range match the drawing.",
                "Restore field wiring and re-test from the transmitter.",
            ])},
        {"title":"Sign-off Form","body": code(
"I/O CHECKOUT SHEET\n"
"\n"
"Tag:            _______________________________\n"
"Address:        _______________________________\n"
"Type:           DI / DO / AI / AO\n"
"Field Device:   _______________________________\n"
"Test:           Actuated device / Forced output / Injected signal\n"
"Result:         PASS / FAIL\n"
"Comments:       _______________________________\n"
"Checked by:     ______________   Date: ___________\n"
"Witnessed by:   ______________   Date: ___________\n")},
        {"title":"Forcing I/O Safely","body": ul([
                "Forcing outputs can move real equipment. Verify LOTO or known safe state before forcing.",
                "Document every forced value. Clear forces before sign-off.",
                "Use PLC run-time force monitor to confirm no forces remain.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Every point on the I/O list signed off.",
            "Analog loops tested at 5 points including 0% and 100%.",
            "All forces cleared before handing over.",
            "Mismatches corrected in drawings and program.",
            "Sign-off binder filed with commissioning docs.",
        ])},
    ],
    "related":[
        ("Commissioning Reports & Sign-off","Commissioning Reports &amp; Sign-off.html"),
        ("Analog IO Basics","../05_PLCs & Automation Hardware/Analog IO Basics.html"),
        ("Discrete IO Modules","../05_PLCs & Automation Hardware/Discrete IO Modules.html"),
        ("PID Tuning Basics","PID Tuning Basics.html"),
    ],
},

"PLC-HMI-VFD Integration.html":{
    "title":"PLC-HMI-VFD Integration",
    "meta":{"category":"System Integration & Commissioning","tags":["#integration","#PLC","#HMI","#VFD","#commissioning"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Pulling the PLC, HMI, and drives together into a single working system is its own skill. Each alone is simple; the integration is where pieces disagree on protocol, timing, addresses, and fault handling.")},
        {"title":"Integration Checklist","body": ol([
                "IP plan published and matched by all devices. See <a href=\"../08_Industrial_Networks_&_Protocols/IP Addressing &amp; Subnetting.html\">IP Addressing</a>.",
                "PLC communication modules configured for the drive and HMI protocols.",
                "Drive added to PLC controller organizer with correct EDS / GSD / ESI file.",
                "Connection parameters (RPI, slot, connection timeout) tuned.",
                "HMI connected, tags imported, faceplates instantiated.",
                "Alarms propagated from drive faults to PLC and onward to HMI.",
                "Commands and status mapped both ways for drive control.",
                "Speed reference path validated (local vs. remote).",
                "Safety interlocks verified — drive Safe-Torque-Off, emergency stop.",
                "Recovery from power cycle and network loss tested.",
            ])},
        {"title":"Common Pitfalls","body": ul([
                "EDS file revision doesn't match drive firmware — configuration errors appear subtle.",
                "Command source parameter left in keypad mode after bench testing.",
                "HMI button writes directly to the drive tag, bypassing PLC sequence logic.",
                "Drive's network-loss reaction set to 'maintain last speed' for a hoist.",
                "Drive parameters not saved to flash after commissioning — first power cycle clears them.",
                "Time sync missing — alarms across PLC / drive / HMI don't line up.",
            ])},
        {"title":"Recommended Architecture","body": code(
"HMI ---(tags)--- PLC ---(implicit I/O)--- Drive\n"
"                 |\n"
"                 +-- state machine / interlocks / sequence\n"
"                 |\n"
"                 +-- alarm aggregation\n"
"\n"
"Operator buttons go to PLC tags, NEVER directly to drive control bits.\n"
"PLC is the single source of truth for drive commands.\n")},
        {"title":"Field Checklist","body": tasks([
            "Parameter file archived for each drive.",
            "PLC program archived; HMI project archived.",
            "Alarm propagation verified by deliberate fault injection.",
            "Manual override (local/remote) tested.",
            "System runs through a complete cycle with no operator intervention.",
            "Commissioning report signed — see <a href=\"Commissioning Reports &amp; Sign-off.html\">Commissioning Reports</a>.",
        ])},
    ],
    "related":[
        ("Startup Sequences","Startup Sequences.html"),
        ("Commissioning Reports & Sign-off","Commissioning Reports &amp; Sign-off.html"),
        ("VFD Parameters & Setup","../04_Motor_Control/VFD Parameters &amp; Setup.html"),
        ("Connecting HMI to PLC (EthernetIP, Modbus)","../07_HMI_SCADA_Systems/Connecting HMI to PLC (EthernetIP, Modbus).html"),
        ("HMI IO Tags & Linking","../06_PLC_Programming_&_Logic/HMI IO Tags &amp; Linking.html"),
    ],
},

"Startup Sequences.html":{
    "title":"Startup Sequences",
    "meta":{"category":"System Integration & Commissioning","tags":["#startup","#powerup","#sequence","#initialization"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Powering up a machine in the right order every time — and knowing how it should behave after a power loss — is the difference between a reliable system and one that surprises operators.")},
        {"title":"Typical Sequence","body": ol([
                "Main disconnect closed.",
                "Control power transformer energized; 24 VDC supplies stable.",
                "PLC boots; first-scan logic runs.",
                "HMI boots; connects to PLC.",
                "Drives power up; load parameters; self-test; wait for enable.",
                "Safety relay / safety PLC boots; safety loop checked.",
                "Field I/O modules online.",
                "PLC enters a 'Ready' state once all preconditions are true.",
                "Operator is prompted to reset faults, acknowledge, and arm the machine.",
                "Start command is accepted and the normal sequence begins.",
            ])},
        {"title":"First-Scan Logic","body": p(
            "On every power-up, the PLC's first-scan bit (S:FS on AB, a dedicated tag on other platforms) can be used to initialize retained tags to safe values. Every motor command should be forced FALSE; sequence step should be 0 (idle); fault latches should be cleared to a known state so the machine starts from zero.")},
        {"title":"Power Loss Recovery","body": ul([
                "Decide per machine: auto-restart, auto-restart with operator ack, or manual only.",
                "Process systems (continuous) often auto-restart to avoid batch loss.",
                "Discrete / motion systems typically require operator ack.",
                "Safety requires operator ack — never auto-start after an E-stop.",
                "Document the chosen behavior and match it in logic and operator procedure.",
            ])},
        {"title":"Cold Start vs Warm Start","body": table(
            ["Cold start","Warm start"],
            [
                ["PLC memory reinitialized from program","PLC resumes from last state"],
                ["Tags reset to defaults","Retentive tags kept"],
                ["Recipes reloaded","Active recipe kept"],
                ["Sequences at step 0","Current step kept — dangerous without ack"],
            ])},
        {"title":"Field Checklist","body": tasks([
            "Power-up order documented and posted at the panel.",
            "First-scan initialization verified.",
            "Power-loss recovery behavior matches procedure and risk assessment.",
            "Safety relays rearmed by operator ack, not automatically.",
            "Sequence verified to start from idle on a cold start.",
        ])},
    ],
    "related":[
        ("PLC-HMI-VFD Integration","PLC-HMI-VFD Integration.html"),
        ("Basic State Machine Programming","../06_PLC_Programming_&_Logic/Basic State Machine Programming.html"),
        ("Risk Assessments & Functional Safety","../12_Safety_Systems_Advanced/Risk Assessments &amp; Functional Safety.html"),
        ("Emergency Stops (E-Stops)","../12_Safety_Systems_Advanced/Emergency Stops (E-Stops).html"),
    ],
},

"PID Tuning Basics.html":{
    "title":"PID Tuning Basics",
    "meta":{"category":"System Integration & Commissioning","tags":["#PID","#process","#tuning","#ZN","#loop"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "PID (Proportional-Integral-Derivative) is the workhorse control algorithm in process automation. Most engineers can name the three terms, far fewer can tune a loop that behaves well at the first try. The good news: you don't need to — you need a method.")},
        {"title":"The Three Terms","body": table(
            ["Term","What it does","Effect"],
            [
                ["P","Proportional to current error","Fast reaction; larger gain = faster and less stable"],
                ["I","Integrates error over time","Removes steady-state offset; too much causes windup and oscillation"],
                ["D","Rate of change of error","Anticipates; noisy signals cause chatter"],
            ])},
        {"title":"Tuning Methods","body":
            "<h3>Ziegler-Nichols (closed-loop)</h3>" + ol([
                "Set I and D to zero. Raise P slowly until the PV just sustains steady oscillation.",
                "Note the ultimate gain Ku and the oscillation period Tu.",
                "Apply: P = 0.6 Ku, I = 2 × P / Tu, D = P × Tu / 8.",
                "Trim from there.",
            ]) +
            "<h3>Cohen-Coon (open-loop / step test)</h3>" + p(
                "Bump the output by a step and record the PV response. Measure dead time L, time constant T, and process gain K. Use Cohen-Coon formulas to compute P, I, D. Better for slow dead-time-dominated processes like temperature loops."
            ) +
            "<h3>IMC / lambda tuning</h3>" + p(
                "Pick a desired closed-loop time constant lambda. Compute P and I from the open-loop model. Simple and robust. Default for many modern process loops."
            ) +
            "<h3>Autotune</h3>" + p(
                "Almost every modern PLC or drive has an autotune button. Works well on well-behaved loops. Review the gains before locking them in."
            )
        },
        {"title":"Common Loop Types","body": table(
            ["Loop","Typical Behavior","Tuning Notes"],
            [
                ["Flow","Fast, noisy","Low P, low I, little or no D"],
                ["Level","Slow, integrating","Low I gain; avoid D"],
                ["Pressure","Fast","Similar to flow"],
                ["Temperature","Slow, dead-time","High I, moderate P, small D"],
                ["Position (servo)","Fast, accurate","Cascade with velocity loop; use feed-forward"],
            ])},
        {"title":"Practical Tips","body": ul([
                "Tune one loop at a time; don't chase inter-loop interactions.",
                "Start conservative (slow) and speed up — the opposite will damage equipment.",
                "Avoid D on noisy signals unless you filter first.",
                "Set output limits and anti-windup.",
                "Trend and archive the tuning tests — you'll tune again.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Output limits set on the PID block.",
            "Anti-windup enabled.",
            "Test tuning logged and saved.",
            "Operator able to switch auto / manual safely.",
            "Trend views available on HMI for setpoint, PV, output.",
        ])},
    ],
    "related":[
        ("Analog IO Basics","../05_PLCs & Automation Hardware/Analog IO Basics.html"),
        ("IO Checkout & Loop Testing","IO Checkout &amp; Loop Testing.html"),
        ("Data Logging & Trends","../07_HMI_SCADA_Systems/Data Logging &amp; Trends.html"),
    ],
},

"Documentation Best Practices.html":{
    "title":"Documentation Best Practices",
    "meta":{"category":"System Integration & Commissioning","tags":["#docs","#drawings","#asbuilt","#version"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Documentation is the cheapest insurance on a machine. Poorly-documented systems take 2–5× longer to service. Aim for a binder (or equivalent online) that lets the next tech fix your work at 2 a.m.")},
        {"title":"What Every Machine Needs","body": ul([
                "Cover sheet: machine name, owner, install date, contact.",
                "Index of documents by part number.",
                "Electrical schematics (as-built).",
                "Single-line diagram.",
                "Pneumatic / hydraulic schematics if applicable.",
                "I/O list: tag, address, function, device, location.",
                "Network topology diagram with IPs.",
                "BOM and spare parts list.",
                "PLC program backup (paper summary + electronic).",
                "HMI project backup.",
                "Drive parameter file per drive.",
                "Commissioning sign-off sheets.",
                "Manufacturer manuals for key components.",
                "Maintenance procedures / PMs.",
                "Change log / revision history.",
            ])},
        {"title":"Storage","body": ul([
                "Paper copy in the panel or on the machine for field use.",
                "Electronic copy in version control (Git, SharePoint, Teams).",
                "Backup copy offsite.",
                "Naming convention: <MachineID>_<DocType>_<Rev>_<YYYYMMDD>.",
            ])},
        {"title":"As-Built vs As-Designed","body": p(
            "Every time the field doesn't match the drawing, the drawing is wrong — and it will stay wrong until someone updates it. Make redlines as you troubleshoot. Fold them into a new revision on any formal change.")},
        {"title":"Version Control","body": ul([
                "Store PLC / HMI / drive files in a code repository (Git) rather than folders of copies.",
                "Tag every commit with a release number.",
                "Document what changed and why — 'fix bug' isn't enough.",
                "Review and approve changes before merging.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Binder is complete and current.",
            "Redlines transferred to drawings quarterly.",
            "PLC / HMI backups verified by restore test annually.",
            "Drive parameter files dated and archived.",
            "Change log actually used, not just the folder structure.",
        ])},
    ],
    "related":[
        ("Change Management","Change Management.html"),
        ("Commissioning Reports & Sign-off","Commissioning Reports &amp; Sign-off.html"),
        ("Project Handoff Docs","../14_Soft_Skills_Workflow/Project Handoff Docs.html"),
        ("Reading Schematics & Wiring Diagrams","../14_Soft_Skills_Workflow/Reading Schematics &amp; Wiring Diagrams.html"),
    ],
},

"Change Management.html":{
    "title":"Change Management",
    "meta":{"category":"System Integration & Commissioning","tags":["#change","#MOC","#rollback","#audit"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Uncontrolled changes are the #1 cause of broken production. A simple Management of Change (MOC) process keeps drifting intent, undocumented tweaks, and finger-pointing in check.")},
        {"title":"What a Change Process Looks Like","body": ol([
                "<strong>Request</strong> — who, what, why. Include business justification and risk.",
                "<strong>Review</strong> — engineering, operations, safety representatives.",
                "<strong>Approval</strong> — documented go / no-go.",
                "<strong>Plan</strong> — steps, timeline, rollback strategy.",
                "<strong>Execute</strong> — change window, pre-tests.",
                "<strong>Verify</strong> — post-change functional test.",
                "<strong>Close out</strong> — update drawings, program history, operator training if needed.",
            ])},
        {"title":"Rollback Strategy","body": ul([
                "Full backup of PLC, HMI, drive parameters before any change.",
                "Documented restore procedure tested before the change window.",
                "Defined criteria for calling a rollback (timeouts, faults, quality).",
                "Who decides the rollback: named person and alternate.",
            ])},
        {"title":"PLC / HMI Change Audit","body": ul([
                "Signed program with revision number.",
                "Change description in commit message or program comment.",
                "Recorded online edits — avoid them when possible; run from a saved project.",
                "Backup taken immediately after the change goes permanent.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "MOC form used for every non-trivial change.",
            "Rollback tested before production change.",
            "Drawings and program updated in the same session.",
            "Operators briefed on new behavior.",
            "Post-change verification signed off.",
        ])},
    ],
    "related":[
        ("Documentation Best Practices","Documentation Best Practices.html"),
        ("Commissioning Reports & Sign-off","Commissioning Reports &amp; Sign-off.html"),
        ("Risk Assessments & Functional Safety","../12_Safety_Systems_Advanced/Risk Assessments &amp; Functional Safety.html"),
    ],
},

"Commissioning Reports & Sign-off.html":{
    "title":"Commissioning Reports & Sign-off",
    "meta":{"category":"System Integration & Commissioning","tags":["#commissioning","#signoff","#acceptance","#FAT","#SAT"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "A commissioning report is the bridge between the integrator's work and the end-user's ownership. Signed and filed, it is both a legal and an operational record of how the machine was handed over.")},
        {"title":"Typical Phases","body": table(
            ["Phase","Where","What's tested"],
            [
                ["FAT (Factory Acceptance Test)","Integrator's shop","Functional, without real process — mostly software and I/O"],
                ["SAT (Site Acceptance Test)","Customer site","Integrated with real utilities and process"],
                ["Performance Test","Site, with production material","Rate, yield, OEE, stability"],
                ["Final Handover","Site","All documents, spares, training delivered"],
            ])},
        {"title":"What Gets Signed","body": ul([
                "I/O checkout sheets.",
                "Loop test sheets.",
                "Safety validation report (stop categories, reaction times).",
                "Functional test matrix (every feature exercised).",
                "Performance test results.",
                "Outstanding punch list with agreed dates.",
                "Drawings marked as-built.",
                "Program / HMI / drive backups archived.",
                "Training sign-off per operator / maintainer.",
                "Spares inventory confirmation.",
            ])},
        {"title":"Punch List Discipline","body": ul([
                "Any unfinished item gets a number, owner, severity, and target date.",
                "Handover does not mean 'punch list empty' — it means agreed.",
                "Track to closure; follow up at 30 / 60 / 90 days.",
                "Close items in writing with sign-off.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Every commissioning phase signed by both parties.",
            "Punch list agreed with owners and dates.",
            "All backups archived on customer media.",
            "Operator and maintenance training completed.",
            "Report filed in the plant binder and electronically.",
        ])},
    ],
    "related":[
        ("IO Checkout & Loop Testing","IO Checkout &amp; Loop Testing.html"),
        ("PLC-HMI-VFD Integration","PLC-HMI-VFD Integration.html"),
        ("Change Management","Change Management.html"),
        ("Documentation Best Practices","Documentation Best Practices.html"),
        ("Project Handoff Docs","../14_Soft_Skills_Workflow/Project Handoff Docs.html"),
    ],
},

}
CONTENT = {FOLDER: PAGES}
