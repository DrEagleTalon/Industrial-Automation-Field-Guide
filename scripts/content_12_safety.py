"""Content for 12_Safety_Systems_Advanced."""

FOLDER = "12_Safety_Systems_Advanced"

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

"Emergency Stops (E-Stops).html":{
    "title":"Emergency Stops (E-Stops)",
    "meta":{"category":"Safety Systems (Advanced)","tags":["#estop","#ISO13850","#stopcategory","#safety"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"ISO 13850, NFPA 79, IEC 60204-1"},
    "sections":[
        {"title":"Description","body": p(
            "An emergency stop is the last line of defense: when something goes wrong, anyone near the machine can bring it to a safe state with a single action. The rules for E-stops are highly prescribed and non-negotiable.")},
        {"title":"Mandatory Requirements","body": ul([
                "Red palm (mushroom) button on a yellow background.",
                "Self-latching — stays engaged after the hit; requires deliberate reset (twist or pull).",
                "Directly operated opening contacts (positive-opening per IEC 60947-5-5).",
                "Wired to bring the machine to its defined stop category.",
                "Reset is a separate deliberate action, never automatic.",
                "Every location where hazards are reachable must have an E-stop accessible.",
            ])},
        {"title":"Stop Categories","body": table(
            ["Category","Behavior","When to use"],
            [
                ["0","Immediate removal of actuator power","Most common; fail-safe coast"],
                ["1","Controlled stop; power removed once stopped","Required for axes that are more dangerous coasting (long spin-down)"],
                ["2","Controlled stop; power maintained","Functional stops only, not E-stops"],
            ])},
        {"title":"Typical Wiring","body": code(
"E-stop PB (dual channel) -> Safety relay / safety PLC\n"
"    -> Contactor drop (cat 0) or\n"
"    -> Drive Safe Stop 1 input + contactor drop after timer (cat 1)\n"
"\n"
"Dual channel detects shorts and opens even with one bad contact.\n"
"Reset: separate pushbutton, monitored by safety relay.\n")},
        {"title":"Do / Don't","body": ul([
                "Do wire E-stop directly to a safety relay or safety PLC, never to a standard PLC input as the sole action path.",
                "Do use dual-channel wiring with cross-monitoring.",
                "Do test E-stop function weekly or monthly per the procedure.",
                "Don't rely on software only for stopping.",
                "Don't use an E-stop as a routine production stop — it wears the contacts and trains operators badly.",
                "Don't defeat or bypass E-stop for convenience.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Every E-stop is red palm on yellow background.",
            "Dual channel with cross-monitoring to a safety relay or safety PLC.",
            "Reset is a separate, deliberate action.",
            "Proof-test done and signed off.",
            "Stop category documented for each E-stop function.",
        ])},
    ],
    "related":[
        ("Safety Relays & Safety PLCs","../05_PLCs & Automation Hardware/Safety Relays &amp; Safety PLCs.html"),
        ("Risk Assessments & Functional Safety","Risk Assessments &amp; Functional Safety.html"),
        ("Safety Fencing & Interlocks","Safety Fencing &amp; Interlocks.html"),
        ("Motor Braking Techniques","../04_Motor_Control/Motor Braking Techniques.html"),
        ("NFPA 79 – Machinery Electrical","../11_Standards_and_Codes/NFPA 79 – Machinery Electrical.html"),
    ],
},

"Two-Hand Controls.html":{
    "title":"Two-Hand Controls",
    "meta":{"category":"Safety Systems (Advanced)","tags":["#twohand","#ISO13851","#synchronous","#press"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"ISO 13851, ANSI B11.2"},
    "sections":[
        {"title":"Description","body": p(
            "Two-hand controls force the operator to use both hands to run the machine during a hazardous motion — keeping them out of the pinch point. Classic on presses, punches, and stamps.")},
        {"title":"Classification (ISO 13851)","body": table(
            ["Type","Both-hand requirement","Synchronous","Release stops"],
            [
                ["I","Yes","No","No"],
                ["II","Yes","No","Yes"],
                ["III A","Yes","≤ 500 ms","Yes"],
                ["III B","Yes","≤ 500 ms","Yes"],
                ["III C","Yes","≤ 500 ms","Yes, with category 4 architecture"],
            ])},
        {"title":"Design Requirements","body": ul([
                "Both pushbuttons must be pressed within 500 ms (Type III).",
                "Release of either button must stop the dangerous motion immediately.",
                "Both pushbuttons must be released and re-pressed to start a new cycle.",
                "Pushbuttons placed at least 260 mm apart; anti-tie-down protection required.",
                "Monitoring is typically a dedicated safety relay or a safety PLC function block.",
            ])},
        {"title":"When Two-Hand Alone Isn't Enough","body": ul([
                "Multi-operator stations — use a separate two-hand per operator.",
                "When someone else can enter the hazard zone — add light curtains / fencing.",
                "When dangerous motion must continue without hands (setup mode) — don't use two-hand.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Type and synchronous timing verified.",
            "Button distance ≥ 260 mm.",
            "Synchronization test at 400 ms and 550 ms (should fail above 500 ms).",
            "Release test on each button.",
            "Safety relay or safety PLC function block logged.",
        ])},
    ],
    "related":[
        ("Emergency Stops (E-Stops)","Emergency Stops (E-Stops).html"),
        ("Safety Fencing & Interlocks","Safety Fencing &amp; Interlocks.html"),
        ("Safety Relays & Safety PLCs","../05_PLCs & Automation Hardware/Safety Relays &amp; Safety PLCs.html"),
        ("Risk Assessments & Functional Safety","Risk Assessments &amp; Functional Safety.html"),
    ],
},

"Safety Fencing & Interlocks.html":{
    "title":"Safety Fencing & Interlocks",
    "meta":{"category":"Safety Systems (Advanced)","tags":["#guarding","#interlock","#lightcurtain","#lock"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"ISO 14119, ISO 13857, ISO 13855"},
    "sections":[
        {"title":"Description","body": p(
            "Fencing and interlocks separate people from hazards. Done right, they let you maintain and troubleshoot safely; done wrong, they get tied down, defeated, or bypassed.")},
        {"title":"Types of Guarding","body": table(
            ["Type","When to use"],
            [
                ["Fixed guard","Hazards that don't need routine access"],
                ["Interlocked guard","Access needed but dangerous motion must stop"],
                ["Interlocked guard with locking","Stop time > access time, or high-speed hazard"],
                ["Light curtain","Frequent access to the zone (loading, material handling)"],
                ["Safety mat / edge","Floor-area protection"],
                ["Scanner (laser, radar)","Configurable zones, AGVs, mobile equipment"],
            ])},
        {"title":"Guard Placement (ISO 13855)","body": p(
            "Distance from the hazard depends on the reaction time of the safety system and the access method. Formula: S = K × T + C. K is the reach speed (2 m/s for walking toward a light curtain). T is the system reaction time. C accounts for reach-through (varies by resolution of the protective device)."
        )},
        {"title":"Interlock Switches","body": ul([
                "<strong>Mechanical</strong> — tongue-actuated, positive-opening contacts. Reliable, cheap.",
                "<strong>Magnetic / coded</strong> — no exposed mechanism, defeat-resistant.",
                "<strong>RFID-coded</strong> — each switch coded to a specific actuator; highest defeat resistance.",
                "<strong>Locking</strong> — solenoid holds the door locked until it's safe to open.",
                "Always dual-channel, monitored by a safety relay or safety PLC.",
            ])},
        {"title":"Typical Wiring","body": code(
"Two-channel interlock switch (S1, S2)\n"
"S1 -> Safety relay A1 channel 1\n"
"S2 -> Safety relay A2 channel 2\n"
"Safety relay outputs -> contactor drop + alarm\n"
"Reset: separate monitored pushbutton.\n")},
        {"title":"Defeat Resistance","body": ul([
                "Use coded / RFID switches where possible.",
                "Do not leave the actuator accessible separate from the door.",
                "Tamper-evident hardware.",
                "Training + enforcement — culture beats hardware.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Guard placement verified with safety-distance calculation.",
            "Dual-channel switches and monitoring used.",
            "Coded / RFID switches on accessible guards.",
            "Locking guards when stop time > reach time.",
            "Periodic test documented.",
        ])},
    ],
    "related":[
        ("Emergency Stops (E-Stops)","Emergency Stops (E-Stops).html"),
        ("Safety Relays & Safety PLCs","../05_PLCs & Automation Hardware/Safety Relays &amp; Safety PLCs.html"),
        ("Risk Assessments & Functional Safety","Risk Assessments &amp; Functional Safety.html"),
        ("SIL - PL Functional Safety Intro","../11_Standards_and_Codes/SIL - PL Functional Safety Intro.html"),
    ],
},

"Safety PLCs & Redundancy.html":{
    "title":"Safety PLCs & Redundancy",
    "meta":{"category":"Safety Systems (Advanced)","tags":["#safetyPLC","#GuardLogix","#FPLC","#redundancy"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"IEC 61508, IEC 62061, ISO 13849-1"},
    "sections":[
        {"title":"Description","body": p(
            "A safety PLC (or F-PLC) runs a safety program certified up to SIL 3 / PL e. Unlike a standard PLC, it uses redundant / diverse CPUs, self-tests, and certified safety function blocks.")},
        {"title":"How They Achieve Safety","body": ul([
                "Dual processor running the same program twice and comparing results each scan.",
                "Diverse code paths / timing to catch systematic faults.",
                "Continuous memory tests, watchdog, plausibility checks.",
                "Safety-rated I/O with dual-channel sensing and readback.",
                "Certified (TÜV) function blocks: E-stop, guard lock, STO, SS1.",
            ])},
        {"title":"Integrated vs Standalone","body": table(
            ["Approach","Example","Pros","Cons"],
            [
                ["Integrated safety + standard","GuardLogix, S7-1500 F","Single platform, shared I/O","Vendor-locked; more complex"],
                ["Standalone safety","Pilz PSS, Sick Flexi","Independent of standard PLC","Extra hardware, extra programming"],
            ])},
        {"title":"Redundancy in Process","body": ul([
                "Redundant-pair controllers for SIS (safety instrumented systems) in process industry.",
                "Hot-standby switchover on controller fault.",
                "Triple-modular redundancy (2-out-of-3) for highest availability.",
                "Common in petrochemical, power, and pharma critical systems.",
            ])},
        {"title":"Programming Conventions","body": ul([
                "Safety tags / variables separated from standard.",
                "Only certified function blocks used in safety code.",
                "Safety program signed and locked after validation.",
                "Audit trail of every change.",
                "Annual / periodic proof-test against the hazard.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Safety program signed, sealed, and archived.",
            "Proof-test procedure written and executed.",
            "Version mismatch between safety and standard programs prevented by tooling.",
            "SIL / PL calculation filed with the machine record.",
            "Training on safety-specific software tooling documented.",
        ])},
    ],
    "related":[
        ("Safety Relays & Safety PLCs","../05_PLCs & Automation Hardware/Safety Relays &amp; Safety PLCs.html"),
        ("Risk Assessments & Functional Safety","Risk Assessments &amp; Functional Safety.html"),
        ("Emergency Stops (E-Stops)","Emergency Stops (E-Stops).html"),
        ("SIL - PL Functional Safety Intro","../11_Standards_and_Codes/SIL - PL Functional Safety Intro.html"),
    ],
},

"Risk Assessments & Functional Safety.html":{
    "title":"Risk Assessments & Functional Safety",
    "meta":{"category":"Safety Systems (Advanced)","tags":["#riskassessment","#ISO12100","#ISO13849","#IEC62061"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"ISO 12100, ISO 13849-1, IEC 62061"},
    "sections":[
        {"title":"Description","body": p(
            "Risk assessment is the mandatory first step for every new machine or major modification. It translates hazards into a required performance level for each safety function — the foundation for everything that follows.")},
        {"title":"Method (ISO 12100)","body": ol([
                "Define the machine, its limits, and intended use.",
                "Identify hazards at every state (run, setup, maintenance, clean).",
                "Estimate risk: severity, frequency/exposure, possibility of avoidance.",
                "Evaluate whether risk reduction is needed.",
                "Apply the three-step method of risk reduction: inherently safe design → safeguards → information/warnings.",
                "Document results.",
            ])},
        {"title":"Required Performance Level","body": p(
            "Use the ISO 13849-1 risk graph to turn severity / exposure / avoidance into a Required PL (PLr). Or use the IEC 62061 method for SIL. The safety system must achieve at least the required level."
        )},
        {"title":"Three-Step Reduction","body": ol([
                "<strong>Inherently safe design</strong> — eliminate the hazard, reduce energy, guard by geometry, fail-safe defaults.",
                "<strong>Safeguarding</strong> — guards, interlocks, light curtains, E-stops, two-hand controls.",
                "<strong>Information / warnings</strong> — signs, labels, training. Last resort.",
            ])},
        {"title":"Validation","body": ul([
                "Every safety function is tested for correct action — including failure modes.",
                "Safety distances measured against calculated minimums.",
                "PFHd / MTTFd calculations verified.",
                "Documentation complete: assessment, design, validation, user instructions.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Risk assessment filed in the machine record.",
            "Each hazard mapped to a safety function with a defined SIL / PL.",
            "Validation test signed off.",
            "Residual risks communicated to operators via training and signage.",
        ])},
    ],
    "related":[
        ("SIL - PL Functional Safety Intro","../11_Standards_and_Codes/SIL - PL Functional Safety Intro.html"),
        ("Emergency Stops (E-Stops)","Emergency Stops (E-Stops).html"),
        ("Safety Fencing & Interlocks","Safety Fencing &amp; Interlocks.html"),
        ("Safety PLCs & Redundancy","Safety PLCs &amp; Redundancy.html"),
    ],
},

}
CONTENT = {FOLDER: PAGES}
