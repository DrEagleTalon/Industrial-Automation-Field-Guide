"""Content for 06_PLC_Programming_&_Logic."""

FOLDER = "06_PLC_Programming_&_Logic"

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

"Ladder Logic Basics.html":{
    "title":"Ladder Logic Basics",
    "meta":{"category":"PLC Programming & Logic","tags":["#ladder","#LD","#IEC61131","#rung"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"IEC 61131-3"},
    "sections":[
        {"title":"Description","body": p(
            "Ladder logic (LD) is a graphical PLC programming language that mimics relay schematics. It's the most common and the easiest for electricians to read because every rung looks like a control wire.")},
        {"title":"Core Concepts","body":
            "<h3>The ladder</h3>" + p(
                "Two vertical rails represent power. Horizontal rungs between them contain contacts (inputs) and coils (outputs). A rung 'executes' when there is a continuous path of true contacts from left rail to right rail."
            ) +
            "<h3>Core contacts and coils</h3>" + table(
                ["Symbol","Name","Meaning"],
                [
                    ["-| |-","NO contact (XIC)","Passes power when the tag is TRUE"],
                    ["-|/|-","NC contact (XIO)","Passes power when the tag is FALSE"],
                    ["-( )-","Output coil (OTE)","Tag equals the rung state"],
                    ["-(L)-","Latch (OTL)","Sets the tag TRUE when rung is true; stays set"],
                    ["-(U)-","Unlatch (OTU)","Resets a latched tag"],
                    ["-[ONS]-","One-shot","TRUE for one scan on rising edge"],
                ]) +
            "<h3>Sample rung</h3>" + code(
"|--| StartPB |--+--| Running |--+--( Running )--|\n"
"               |                |\n"
"               +--| SealIn |----+\n"
"\n"
"Rung reads: 'Start PB OR (SealIn AND Running) -> Running'\n"
"A textbook <a href=\"Start-Stop Logic.html\">start-stop</a> rung.\n")
        },
        {"title":"Program Organization","body": ul([
                "Use routines or program blocks for each machine function (Filler, Capper, Conveyor).",
                "Keep one function per routine; name tags descriptively (Conveyor1_Motor_Running, not M103).",
                "Use Add-On Instructions (AOIs) / Function Blocks for repeated logic.",
                "Tasks: periodic task for control logic, continuous for slower things, event-triggered for interrupts.",
            ])},
        {"title":"Common Mistakes","body": ul([
                "Dual-coil: the same output written on two different rungs — last rung wins; the first appears dead.",
                "Latches without an obvious reset — leaves outputs stuck after a fault.",
                "No first-scan initialization for retentive tags — unknown state after a power cycle.",
                "Relying on scan order between unrelated routines — tasks may be re-ordered.",
                "Hard-coded timer presets instead of configuration tags.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Every coil has exactly one rung that writes it.",
            "First-scan logic initializes retained outputs to a safe state.",
            "Function block / AOI version documented and locked.",
            "Rung comments explain intent, not just the symbol names.",
            "Safety logic is <em>not</em> in ladder on a standard PLC — use a safety PLC.",
        ])},
    ],
    "related":[
        ("Boolean Logic Review","Boolean Logic Review.html"),
        ("Start-Stop Logic","Start-Stop Logic.html"),
        ("Set - Reset Latch","Set - Reset Latch.html"),
        ("Timers (TON - TOF - TP)","Timers (TON - TOF - TP).html"),
        ("What is a PLC","../05_PLCs & Automation Hardware/What is a PLC.html"),
    ],
},

"Boolean Logic Review.html":{
    "title":"Boolean Logic Review",
    "meta":{"category":"PLC Programming & Logic","tags":["#boolean","#AND","#OR","#NOT","#XOR"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Every rung in ladder logic is a Boolean expression. Clean logic is testable, readable, and fails in predictable ways. Messy logic is the #1 reason machines misbehave.")},
        {"title":"Basic Operators","body": table(
            ["Operator","Ladder","Structured Text","Description"],
            [
                ["AND","series contacts","A AND B","TRUE when both are TRUE"],
                ["OR","parallel contacts","A OR B","TRUE when at least one is TRUE"],
                ["NOT","NC contact","NOT A","TRUE when A is FALSE"],
                ["XOR","-- (derived)","A XOR B","TRUE when exactly one is TRUE"],
                ["NAND","-- (derived)","NOT (A AND B)",""],
                ["NOR","-- (derived)","NOT (A OR B)",""],
            ])},
        {"title":"De Morgan's Laws","body": code(
"NOT (A AND B) = (NOT A) OR (NOT B)\n"
"NOT (A OR B)  = (NOT A) AND (NOT B)\n"
"\n"
"Practical example — instead of:\n"
"   NOT (Running OR Faulted)\n"
"write:\n"
"   NOT Running AND NOT Faulted\n"
"Easier to read on a ladder rung.\n")},
        {"title":"Truth Tables","body": table(
            ["A","B","A AND B","A OR B","A XOR B"],
            [["0","0","0","0","0"],["0","1","0","1","1"],["1","0","0","1","1"],["1","1","1","1","0"]]
        )},
        {"title":"Practical Habits","body": ul([
                "Write the intent in plain English above each rung — then translate.",
                "Prefer positive logic (Running = TRUE) over negative (NotRunning).",
                "Collapse double-negatives. NOT NOT A = A.",
                "Avoid > 4 conditions in a single rung; factor into named intermediate tags.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "No triple-negated logic anywhere.",
            "Tag names match the Boolean meaning (Running, Faulted, Homed).",
            "Intermediate logic tags documented.",
        ])},
    ],
    "related":[
        ("Ladder Logic Basics","Ladder Logic Basics.html"),
        ("Interlocking & Permissives","Interlocking &amp; Permissives.html"),
    ],
},

"Start-Stop Logic.html":{
    "title":"Start-Stop Logic",
    "meta":{"category":"PLC Programming & Logic","tags":["#startstop","#sealin","#motor","#latch"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "The canonical start-stop circuit. Momentary Start PB energizes an output that seals itself in, and a momentary Stop PB (wired normally closed) drops it out. It's the Hello World of PLC logic and the pattern repeats everywhere from motor starters to sequence steps.")},
        {"title":"The Rung","body": code(
"|--| Stop_NC |--+--| Start_PB |--+--( Motor_Run )--|\n"
"                |                |\n"
"                +--| Motor_Run |-+\n"
"\n"
"Stop_NC  — 1756 DI wired to a NC pushbutton. Broken wire = stop.\n"
"Start_PB — 1756 DI wired to a NO pushbutton.\n"
"Motor_Run — output coil (seal-in via its own tag).\n")},
        {"title":"Why Stop is Normally Closed","body": p(
            "If the Stop PB wire breaks, the input goes FALSE and the motor stops automatically. Fail-safe. Never wire Stop as NO — a broken wire would make stopping impossible.")
        },
        {"title":"Variations","body": ul([
                "<strong>With fault interlock</strong>: <code>Stop_NC AND NOT Faulted AND (Start_PB OR Motor_Run) → Motor_Run</code>.",
                "<strong>With permissive</strong>: insert interlock conditions in series (door closed, upstream ready).",
                "<strong>With jog</strong>: parallel momentary path: <code>OR (Jog_PB AND NOT Motor_Run)</code>.",
                "<strong>SetReset</strong>: equivalent to Set + Reset coils — see <a href=\"Set - Reset Latch.html\">Set-Reset Latch</a>.",
            ])},
        {"title":"Common Mistakes","body": ul([
                "Seal-in wired back to Start_PB input instead of Motor_Run — the motor latches on forever when you press Start once.",
                "Stop PB wired NO — violates fail-safe principle.",
                "Stop in the output coil's rung as a separate rung — defeats the logic.",
                "Hardware E-stop replaced by a software stop in ladder — never acceptable without a safety PLC.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Start PB wired NO, Stop PB wired NC, confirmed at the terminal block.",
            "Seal-in uses the output tag, not the Start input.",
            "Fault conditions interrupt the seal-in path.",
            "E-stop is <em>hard-wired</em> independent of this logic.",
            "Online monitor confirms the rung pickup and drop behavior.",
        ])},
    ],
    "related":[
        ("Ladder Logic Basics","Ladder Logic Basics.html"),
        ("Set - Reset Latch","Set - Reset Latch.html"),
        ("Interlocking & Permissives","Interlocking &amp; Permissives.html"),
        ("Direct-On-Line Starters","../04_Motor_Control/Direct-On-Line Starters.html"),
        ("Latching Circuits & Seal-in Logic","../03_Control_Devices/Latching Circuits &amp; Seal-in Logic.html"),
    ],
},

"Timers (TON - TOF - TP).html":{
    "title":"Timers (TON, TOF, TP)",
    "meta":{"category":"PLC Programming & Logic","tags":["#timer","#TON","#TOF","#TP","#IEC61131"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"IEC 61131-3"},
    "sections":[
        {"title":"Description","body": p(
            "Timers are one of the four function-block types defined by IEC 61131-3 (along with counters, bistables, and edge detectors). Every PLC supports them; the behavior is standard across brands.")},
        {"title":"The Three Standard Timers","body": table(
            ["Timer","Input","Behavior","Output"],
            [
                ["TON (On-delay)","IN = TRUE for PT seconds","Starts counting when IN goes TRUE. Resets when IN goes FALSE.","Q = TRUE after PT; FALSE when IN is FALSE"],
                ["TOF (Off-delay)","IN = TRUE","Q goes TRUE immediately when IN goes TRUE. When IN goes FALSE, timer counts PT, then Q → FALSE.","Q = TRUE for PT after IN falling edge"],
                ["TP (Pulse)","IN rising edge","Q goes TRUE for exactly PT, regardless of further IN changes.","One-shot fixed-width pulse"],
            ])},
        {"title":"Rockwell Equivalents","body": ul([
                "<strong>TON</strong> — direct equivalent. .TT = running, .DN = done, .EN = enabled, .ACC = accumulated.",
                "<strong>TOF</strong> — same concept. .DN is TRUE while the input is TRUE + during the delay.",
                "<strong>RTO</strong> — retentive timer; accumulates even when the input goes FALSE. Must be explicitly reset.",
                "Use .PRE for preset, .ACC for accumulated, in ms.",
            ])},
        {"title":"Common Uses","body": ul([
                "<strong>Debounce</strong> a noisy sensor (TON of 20–50 ms).",
                "<strong>Delay fault reaction</strong> until a condition has been present for N seconds (prevents transient trips).",
                "<strong>One-shot horn</strong> on alarm (TP for 2 s).",
                "<strong>Post-purge</strong> fan after burner off (TOF for 60 s).",
                "<strong>Wait for acknowledge</strong> before continuing a sequence.",
            ])},
        {"title":"Sample Logic","body": code(
"IF Sensor THEN\n"
"   Debounce_TON(IN := TRUE, PT := T#50ms);\n"
"ELSE\n"
"   Debounce_TON(IN := FALSE, PT := T#50ms);\n"
"END_IF;\n"
"Sensor_Filtered := Debounce_TON.Q;\n")},
        {"title":"Field Checklist","body": tasks([
            "Preset values are tag-driven, not hard-coded, so they can be tuned from the HMI.",
            "Retentive timers have a clear reset condition on first-scan and fault reset.",
            "Unit (ms vs. s) explicit in the tag name (Delay_ms).",
            "Timers not used as a substitute for physical interlocks.",
        ])},
    ],
    "related":[
        ("Ladder Logic Basics","Ladder Logic Basics.html"),
        ("Counters","Counters.html"),
        ("Basic State Machine Programming","Basic State Machine Programming.html"),
    ],
},

"Counters.html":{
    "title":"Counters",
    "meta":{"category":"PLC Programming & Logic","tags":["#counter","#CTU","#CTD","#CTUD","#IEC61131"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"IEC 61131-3"},
    "sections":[
        {"title":"Description","body": p(
            "Counters increment or decrement on edges. Use them to tally events — parts made, bottles capped, faults per shift, revolutions. They have been a PLC primitive since the first machines in the 1970s.")},
        {"title":"Standard Counter Types","body": table(
            ["Counter","Behavior","Reset"],
            [
                ["CTU (up)","Increments CV on CU rising edge; Q = TRUE when CV >= PV","Reset input clears CV"],
                ["CTD (down)","Decrements CV on CD rising edge; Q = TRUE when CV <= 0","Load input sets CV = PV"],
                ["CTUD (up/down)","Both inputs; QU / QD flags","Reset + Load inputs"],
            ])},
        {"title":"Rockwell Equivalents","body": ul([
                "<strong>CTU</strong> — Count Up. .ACC counts, .PRE is target, .DN when ACC ≥ PRE.",
                "<strong>CTD</strong> — Count Down.",
                "<strong>RES</strong> — used to reset the counter's ACC.",
                "Note: the ACC is retentive. A power cycle keeps the count unless explicitly reset.",
            ])},
        {"title":"Common Uses","body": ul([
                "Parts-per-shift totalizer (reset on shift change).",
                "Batch count with trigger when preset reached.",
                "Revolution count from an <a href=\"../13_Specialty_Topics/Encoders &amp; Resolvers.html\">encoder</a>.",
                "Fault counter to detect intermittent problems.",
                "Index step counter on a state machine.",
            ])},
        {"title":"High-Speed Counting","body": p(
            "Regular counters only see edges that happen on the scan. For pulse rates above a few hundred Hz, use a high-speed counter (HSC) module or built-in HSC input. Typical HSC range: 100 kHz to 5 MHz."
        )},
        {"title":"Field Checklist","body": tasks([
            "Counter reset strategy explicit (shift, day, part type).",
            "Retentive vs. non-retentive behavior documented.",
            "HSC used for anything > 100 Hz.",
            "Preset value tag-driven for HMI adjustment.",
        ])},
    ],
    "related":[
        ("Timers (TON - TOF - TP)","Timers (TON - TOF - TP).html"),
        ("Ladder Logic Basics","Ladder Logic Basics.html"),
        ("Encoders & Resolvers","../13_Specialty_Topics/Encoders &amp; Resolvers.html"),
    ],
},

"Set - Reset Latch.html":{
    "title":"Set / Reset Latch",
    "meta":{"category":"PLC Programming & Logic","tags":["#SR","#RS","#latch","#bistable"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"IEC 61131-3"},
    "sections":[
        {"title":"Description","body": p(
            "Set/Reset bistable elements hold state between scans without a seal-in rung. IEC 61131-3 defines two variants — SR (set-dominant) and RS (reset-dominant) — with predictable behavior when both inputs are true at the same time.")},
        {"title":"SR vs RS","body": table(
            ["Function","Both Inputs TRUE","Priority"],
            [
                ["SR (set-dominant)","Q remains TRUE","Set wins"],
                ["RS (reset-dominant)","Q becomes FALSE","Reset wins"],
            ])},
        {"title":"When to Use","body": ul([
                "Fault/alarm latches — a fault must stay latched until acknowledged. Use RS so Reset dominates.",
                "Mode selectors — running, paused, stopped. Use SR or explicit state logic.",
                "Sequence step bits — use a dedicated step integer instead (see <a href=\"Basic State Machine Programming.html\">State Machines</a>).",
                "E-stop state — never implement in software alone.",
            ])},
        {"title":"Rockwell Ladder","body": code(
"In Studio 5000, use OTL (latch) + OTU (unlatch) on the same tag.\n"
"Set-dominant by scan order — OTL last = set wins; OTU last = reset wins.\n"
"\n"
"|--| FaultCondition |--(L FaultLatch)--|\n"
"|--| AckButton      |--(U FaultLatch)--|\n")
        },
        {"title":"Common Mistakes","body": ul([
                "Using a latch when a simple non-retentive coil would do.",
                "Forgetting to explicitly reset on first scan after a power cycle.",
                "Duplicate OTL/OTU pairs scattered across routines — makes debugging impossible.",
                "Relying on scan-order dominance silently — name the bistable pattern explicitly.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Every latched bit has one and only one Set and one Reset source.",
            "Reset path tested with a fault injection.",
            "First-scan initialization explicit.",
        ])},
    ],
    "related":[
        ("Ladder Logic Basics","Ladder Logic Basics.html"),
        ("Start-Stop Logic","Start-Stop Logic.html"),
        ("Alarms & Fault Detection","Alarms &amp; Fault Detection.html"),
    ],
},

"Interlocking & Permissives.html":{
    "title":"Interlocking & Permissives",
    "meta":{"category":"PLC Programming & Logic","tags":["#interlock","#permissive","#safety","#logic"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "An interlock prevents an action while a condition is unsafe or incorrect. A permissive is the opposite: a set of preconditions that must be TRUE before an action is allowed to start. Both appear in nearly every PLC program.")},
        {"title":"Examples","body": table(
            ["Scenario","Interlock / Permissive"],
            [
                ["Reversing starter","Interlock: can't energize Reverse while Forward is energized"],
                ["Conveyor line","Permissive: downstream must be running before upstream can start"],
                ["Guarded cell","Interlock: robot cannot move when guard door is open"],
                ["Hydraulic press","Permissive: two-hand controls, guard closed, cycle request"],
                ["Heated tank","Interlock: heater disabled without liquid-level sensor covered"],
                ["Mixer","Permissive: lid closed, motor thermal OK, VFD ready"],
            ])},
        {"title":"Programming Patterns","body":
            "<h3>Permissive block</h3>" + code(
"Conveyor_Ready := Motor_OK\n"
"                  AND Guard_Closed\n"
"                  AND Downstream_Ready\n"
"                  AND NOT Faulted\n"
"                  AND Auto_Mode;\n"
"\n"
"Conveyor_Run_Rung:\n"
"|--| Conveyor_Ready |--| Start_PB |--+--( Conveyor_Run )--|\n"
"                                     |\n"
"                                     +--| Conveyor_Run |--+\n") +
            "<h3>Always roll permissives up into named tags</h3>" +
            p("A rung with 12 contacts in series is unreadable at 2 am. Define Conveyor_Ready and the rung becomes one contact.")
        },
        {"title":"Safety vs. Logic Interlocks","body": p(
            "An interlock implemented in ladder protects <em>process</em>, not people. Safety interlocks (E-stop, guard switches, light curtains) must be implemented in hardware or a <a href=\"../05_PLCs & Automation Hardware/Safety Relays &amp; Safety PLCs.html\">safety PLC</a> — see <a href=\"../12_Safety_Systems_Advanced/Safety Fencing &amp; Interlocks.html\">Safety Fencing</a>.")
        },
        {"title":"Field Checklist","body": tasks([
            "Each permissive has a named tag describing it.",
            "Interlocks tested with deliberate fault injection during commissioning.",
            "Safety interlocks are independent of process interlocks.",
            "Diagnostic display on HMI shows which permissive is missing.",
        ])},
    ],
    "related":[
        ("Ladder Logic Basics","Ladder Logic Basics.html"),
        ("Start-Stop Logic","Start-Stop Logic.html"),
        ("Safety Fencing & Interlocks","../12_Safety_Systems_Advanced/Safety Fencing &amp; Interlocks.html"),
        ("Alarms & Fault Detection","Alarms &amp; Fault Detection.html"),
    ],
},

"Alarms & Fault Detection.html":{
    "title":"Alarms & Fault Detection",
    "meta":{"category":"PLC Programming & Logic","tags":["#alarm","#fault","#diagnostics","#HMI"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Good alarm logic tells an operator what is wrong, not that something is wrong. Bad alarm logic generates alarm storms, trains operators to ignore them, and hides the real problem when it matters.")},
        {"title":"Alarm Design Principles","body": ul([
                "Every alarm has a unique ID, a clear message, and a documented response.",
                "Alarms are latched in logic so a transient fault still appears on the HMI.",
                "Alarms are cleared by an explicit Acknowledge + Reset sequence — not auto-cleared.",
                "Severity classes: Info / Warning / Alarm / Critical Shutdown.",
                "Avoid double-alarming — if A causes B, suppress B while A is active.",
                "Time-stamp every alarm at the PLC (scan-synchronous), not at the HMI.",
            ])},
        {"title":"Typical PLC Structure","body": code(
"Alarm 'Conveyor Jam':\n"
"  Condition:   Motor_Running AND NOT Zero_Speed_Sensor AND Delay.DN\n"
"  Latch:       RS with ack as reset\n"
"  Action:      Stop motor, set machine to Faulted state\n"
"  HMI ID:      AL_Conv1_Jam\n"
"  Message:     'Conveyor 1 jam detected, clear debris and reset'\n")},
        {"title":"Data Structure","body": p(
            "Use a UDT / struct with the fields below so every alarm has the same shape.",
            "Fields: ID (int), Active (bool), Latched (bool), Ack (bool), Severity (int), Message (string), TimeStamp (DT), Value (real), SetPoint (real).")
        },
        {"title":"Fault vs. Alarm","body": table(
            ["","Alarm","Fault"],
            [
                ["Effect on machine","Usually keeps running, notifies operator","Shuts down or pauses the sequence"],
                ["Reset","Acknowledge","Acknowledge + explicit reset + conditions cleared"],
                ["Typical examples","High temperature, low pressure warning","E-stop active, motor overload tripped, drive fault"],
            ])},
        {"title":"ISA-18.2 Alarm Management","body": p(
            "The ISA-18.2 standard sets rationalization rules: every alarm should be operable, unique, timely, necessary. Worth reading if you're drowning in alarms."
        )},
        {"title":"Field Checklist","body": tasks([
            "Alarm list maintained as a separate document with messages and responses.",
            "Each alarm has an HMI message and a diagnostic help entry.",
            "Alarm history logged with timestamps.",
            "Acknowledge and reset behavior tested.",
            "Suppression logic prevents alarm storms during normal shutdowns.",
        ])},
    ],
    "related":[
        ("Set - Reset Latch","Set - Reset Latch.html"),
        ("Interlocking & Permissives","Interlocking &amp; Permissives.html"),
        ("Tag Management & Alarms","../07_HMI_SCADA_Systems/Tag Management &amp; Alarms.html"),
        ("General Troubleshooting Methodology","../09_Troubleshooting_&_Diagnostics/General Troubleshooting Methodology.html"),
    ],
},

"HMI IO Tags & Linking.html":{
    "title":"HMI I/O Tags & Linking",
    "meta":{"category":"PLC Programming & Logic","tags":["#HMI","#tags","#linking","#OPC","#namespace"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "An HMI is only useful when its graphics read and write PLC data reliably. The tag layer between the two is where reliability lives or dies.")},
        {"title":"Tagging Approaches","body": ul([
                "<strong>Direct import from PLC</strong> — modern tools (FactoryTalk View, TIA Portal, Ignition, Wonderware) can browse and import tags. Good for consistency.",
                "<strong>Mapped HMI tags</strong> — HMI-side tags mapped to PLC addresses. Older style; prone to drift when the PLC changes.",
                "<strong>UDT / Struct tags</strong> — group related values (Setpoint, PV, Output) into one structure and bind a faceplate to it. Best practice on modern platforms.",
            ])},
        {"title":"Naming Conventions","body": ul([
                "Use a consistent pattern: Area_Equipment_Attribute (Filler_Motor_Running).",
                "Camel-case or snake-case — pick one and stick to it.",
                "Booleans start with a verb or state (Is, Has, Running, Faulted).",
                "Setpoints end with _SP; process values with _PV; outputs with _OUT.",
                "No cryptic numeric tags like B3:17/4 — use tag-based PLCs or alias them.",
            ])},
        {"title":"Performance","body": ul([
                "Minimize the number of distinct tags per screen (target < 200).",
                "Use change-driven updates instead of poll-all-at-fixed-rate where possible.",
                "Group tags into HMI tag groups that match update-rate needs.",
                "Diagnostic screens should be on their own group to avoid hogging bandwidth.",
            ])},
        {"title":"Security","body": ul([
                "Write access limited to operator-level and above.",
                "Tunable parameters (recipes, setpoints) require a login.",
                "Never tie an HMI Write Button directly to a commanded motor output — always go through the PLC state machine.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Tag database versioned and backed up.",
            "HMI tags match PLC names where possible.",
            "Quality-of-data indication on every screen (comm OK / stale / bad).",
            "Update groups tuned to avoid CPU / network saturation.",
        ])},
    ],
    "related":[
        ("Tag Management & Alarms","../07_HMI_SCADA_Systems/Tag Management &amp; Alarms.html"),
        ("HMI Basics","../07_HMI_SCADA_Systems/HMI Basics.html"),
        ("Connecting HMI to PLC (EthernetIP, Modbus)","../07_HMI_SCADA_Systems/Connecting HMI to PLC (EthernetIP, Modbus).html"),
        ("Data Blocks & Structured Text","Data Blocks &amp; Structured Text.html"),
    ],
},

"Basic State Machine Programming.html":{
    "title":"Basic State Machine Programming",
    "meta":{"category":"PLC Programming & Logic","tags":["#statemachine","#SFC","#sequence","#step"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "State machines describe the behavior of a machine as a finite set of states and the transitions between them. They make sequence logic readable, testable, and maintainable — the opposite of rungs full of ad-hoc conditions.")},
        {"title":"The Pattern","body": code(
"Step := 0  // Idle\n"
"\n"
"CASE Step OF\n"
"  0:  // Idle\n"
"     IF StartCommand THEN Step := 10; END_IF;\n"
"  10: // Clamp\n"
"     Clamp_Out := TRUE;\n"
"     IF Clamp_Closed_LS THEN Step := 20; END_IF;\n"
"  20: // Cycle\n"
"     Cycle_Out := TRUE;\n"
"     IF Cycle_Complete THEN Step := 30; END_IF;\n"
"  30: // Unclamp\n"
"     Clamp_Out := FALSE;\n"
"     IF Clamp_Open_LS THEN Step := 0; END_IF;\n"
"  999: // Fault\n"
"     Latch fault, wait for reset\n"
"END_CASE;\n")},
        {"title":"Design Rules","body": ul([
                "One variable (Step) owns the state — outputs are driven by the step, not the other way around.",
                "Use step gaps (10, 20, 30) so you can insert new steps later without renumbering.",
                "Fault state (999) collects all error exits; reset returns to 0.",
                "Timers or counters are owned by the state that uses them — reset on entry.",
                "HMI displays the current step description for diagnostics.",
            ])},
        {"title":"SFC (Sequential Function Chart)","body": p(
            "SFC is IEC 61131-3's graphical state machine language — steps, transitions, actions, alternative and parallel branches. If your platform supports SFC well, it's worth using for sequential machines. Studio 5000 supports it; TIA Portal S7-1500 supports it."
        )},
        {"title":"Common Mistakes","body": ul([
                "Setting the step from multiple places without a guard — race conditions.",
                "Leaving timers running across states.",
                "No fault state — when something goes wrong, the machine hangs silently.",
                "Packing too much into one state — states should be a single discrete action.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Step variable exposed to HMI.",
            "Each state has an entry action, a hold action, and an exit condition.",
            "Fault state is the only exit from an error condition.",
            "Step timeouts set on every state to catch missing inputs.",
        ])},
    ],
    "related":[
        ("Ladder Logic Basics","Ladder Logic Basics.html"),
        ("Data Blocks & Structured Text","Data Blocks &amp; Structured Text.html"),
        ("Alarms & Fault Detection","Alarms &amp; Fault Detection.html"),
        ("Startup Sequences","../10_System_Integration_&_Commissioning/Startup Sequences.html"),
    ],
},

"Data Blocks & Structured Text.html":{
    "title":"Data Blocks & Structured Text",
    "meta":{"category":"PLC Programming & Logic","tags":["#ST","#SCL","#datablock","#UDT","#IEC61131"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"IEC 61131-3"},
    "sections":[
        {"title":"Description","body": p(
            "Structured Text (ST) is the text-based IEC 61131-3 language. It looks like Pascal or a simplified C. Use it for math, loops, string handling, and any logic that would be unreadable in ladder.")},
        {"title":"Syntax Essentials","body": code(
"// Assignment\n"
"Count := Count + 1;\n"
"\n"
"// If-then-else\n"
"IF Temperature > 80.0 THEN\n"
"    Fan := TRUE;\n"
"ELSIF Temperature < 70.0 THEN\n"
"    Fan := FALSE;\n"
"END_IF;\n"
"\n"
"// Case\n"
"CASE Step OF\n"
"  1: StartUp();\n"
"  2: Run();\n"
"  ELSE Stop();\n"
"END_CASE;\n"
"\n"
"// For loop\n"
"FOR i := 0 TO 9 DO\n"
"    Buffer[i] := 0;\n"
"END_FOR;\n"
"\n"
"// Function call\n"
"Result := Scale(Raw := Analog_In, RawMin := 6242, RawMax := 31208,\n"
"                EU_Min := 0.0, EU_Max := 100.0);\n")},
        {"title":"Data Structures","body":
            "<h3>UDT / Struct</h3>" + p(
                "Group related fields into a single user-defined type. Every AB ControlLogix programmer ends up living inside UDTs — they're the difference between a tidy project and chaos."
            ) + code(
"TYPE Motor_Data :\n"
"  STRUCT\n"
"    Run_Cmd  : BOOL;\n"
"    Running  : BOOL;\n"
"    Fault    : BOOL;\n"
"    Speed_SP : REAL;\n"
"    Speed_PV : REAL;\n"
"    Hours    : DINT;\n"
"  END_STRUCT;\n"
"END_TYPE;\n"
"\n"
"Motor1 : Motor_Data;\n"
"Motor1.Run_Cmd := TRUE;\n") +
            "<h3>Arrays</h3>" + p(
                "Fixed-size, indexed from 0 (Codesys, Siemens, most platforms) or from 1 (some) or configurable (Rockwell). Use for buffers, recipes, lookup tables."
            ) +
            "<h3>Data blocks (Siemens)</h3>" + p(
                "In Siemens S7, a DB is a block of named memory. Use global DBs for shared state and instance DBs that are bound to an FB's local data. Tag-based platforms like Rockwell don't have DBs per se — everything is in the tag database."
            )
        },
        {"title":"When ST Shines","body": ul([
                "Scaling, filtering, PID, and math-heavy logic.",
                "String parsing or message construction.",
                "Looping over arrays of tags.",
                "Complex state machines with many branches.",
                "Algorithms that need to be version-controlled and diffed like source code.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Comments explain intent, not syntax.",
            "UDTs used for every repeated data shape.",
            "Arrays have bound checks or guaranteed safe indices.",
            "No hard-coded magic numbers — named constants or parameters.",
            "Functions / function-blocks have documented inputs and outputs.",
        ])},
    ],
    "related":[
        ("Ladder Logic Basics","Ladder Logic Basics.html"),
        ("Basic State Machine Programming","Basic State Machine Programming.html"),
        ("IEC 61131-3 – PLC Programming","../11_Standards_and_Codes/IEC 61131-3 – PLC Programming.html"),
    ],
},

}
CONTENT = {FOLDER: PAGES}
