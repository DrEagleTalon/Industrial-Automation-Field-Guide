"""Content for 11_Standards_and_Codes."""

FOLDER = "11_Standards_and_Codes"

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

"NEC 430 – Motors & Controllers.html":{
    "title":"NEC 430 – Motors & Controllers",
    "meta":{"category":"Standards & Codes","tags":["#NEC","#Art430","#motor","#conductor","#overload"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"NFPA 70 / NEC Article 430"},
    "sections":[
        {"title":"Description","body": p(
            "NEC Article 430 governs motor circuits in the US: conductor sizing, overload protection, short-circuit protection, disconnects, and control circuits. Every motor installation is traceable to a handful of 430 rules.")},
        {"title":"Key Sections","body": table(
            ["Section","Topic","Notes"],
            [
                ["430.6","Current used for calculations","Conductors sized from NEC tables (not nameplate); overload from nameplate FLA"],
                ["430.22","Single-motor conductor ampacity","125% of motor FLC (Table 430.250) for continuous-duty"],
                ["430.24","Multiple motors","Sum of 125% largest + 100% others"],
                ["430.32","Overload protection sizing","115% FLA for SF ≤ 1.15; 125% for SF ≥ 1.15"],
                ["430.52","Short-circuit / branch-circuit protection","Up to 250% FLC for ITB breakers (Table 430.52)"],
                ["430.102","Motor disconnect","In sight from controller and motor"],
                ["430.109","Disconnect type","Motor circuit switch, molded-case switch, etc."],
                ["430.122","Power conversion equipment (VFDs)","110% of drive input current, plus adjustment factors"],
            ])},
        {"title":"Sizing Walk-Through","body": p(
            "Example: 10 HP, 3-phase, 460 V motor."
        ) + code(
"Table 430.250 FLC for 10 HP, 460 V:  14 A\n"
"  (note: use Table FLC, not nameplate FLA, for conductor sizing)\n"
"\n"
"Conductor ampacity (430.22): 1.25 x 14 = 17.5 A\n"
"  Minimum #12 AWG THHN copper (20 A @ 60 C) — typically #12 or #10\n"
"\n"
"Branch-circuit protection (430.52, inverse-time breaker, 250%):\n"
"  2.50 x 14 = 35 A  -> 35 A breaker\n"
"  May be rounded up to next standard size per 430.52(C)(1) Exception\n"
"\n"
"Overload (430.32, motor SF = 1.15, set from nameplate FLA = 13 A):\n"
"  1.25 x 13 = 16.25 A maximum trip setting\n")},
        {"title":"Common Mistakes","body": ul([
                "Using nameplate FLA instead of Table FLC to size conductors — 430.6 says no.",
                "Confusing short-circuit breaker size with overload size.",
                "Using motor SF amps (FLA × SF) to set the overload — violates 430.32.",
                "VFD-fed motor sized as if it were across-the-line — drive input can be higher.",
                "Forgetting the disconnect requirement — 430.102 needs one in sight.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Conductor size justified from Table 430.250 + 430.22.",
            "Short-circuit protection sized per 430.52.",
            "Overload set per 430.32 from nameplate FLA.",
            "Disconnect in sight of controller per 430.102.",
            "VFD input sized per 430.122.",
        ])},
    ],
    "related":[
        ("Overload Relays","../04_Motor_Control/Overload Relays.html"),
        ("Motor Nameplate Data","../04_Motor_Control/Motor Nameplate Data.html"),
        ("Fuses vs Breakers","../02_Power_Distribution/Fuses vs Breakers.html"),
        ("NFPA 79 – Machinery Electrical","NFPA 79 – Machinery Electrical.html"),
    ],
},

"UL 508A – Control Panels.html":{
    "title":"UL 508A – Control Panels",
    "meta":{"category":"Standards & Codes","tags":["#UL508A","#panel","#SCCR","#listing"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"UL 508A"},
    "sections":[
        {"title":"Description","body": p(
            "UL 508A is the North American standard for industrial control panels. If your panel needs a UL listing (most AHJs require it), it must be built by a UL 508A shop to UL 508A rules.")},
        {"title":"Core Requirements","body": ul([
                "Components must be individually listed or recognized (UL Listed, UR, CSA).",
                "Short-Circuit Current Rating (SCCR) documented on the panel nameplate.",
                "Wire and component sizing per the standard's tables.",
                "Spacing and insulation per voltage class.",
                "Grounding and bonding of enclosure parts.",
                "Protective devices coordinated with SCCR.",
                "Panel nameplate with listing mark, voltage, current, SCCR, and builder ID.",
            ])},
        {"title":"SCCR","body": p(
            "Short-Circuit Current Rating is the maximum fault current the panel can handle at its supply terminals without damage. It is limited by the lowest-rated component in the fault current path. Common values: 5 kA (default), 10 kA, 22 kA, 65 kA, 100 kA. To raise SCCR, use higher-rated components or an approved current-limiting device (Type 2 coordination)."
        )},
        {"title":"Common Mistakes","body": ul([
                "Mixing non-listed components with listed ones — voids the UL listing.",
                "Claiming default 5 kA SCCR on a panel with a 22 kA service — AHJ rejects it.",
                "Not using the proper Supplementary Information (SSI) or UL's SI guidance for current limiters.",
                "Incorrect conductor sizing between the main and branch circuits.",
                "Shop not UL 508A certified — builder doesn't have authority to apply the label.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "UL 508A shop builds or field-labels the panel.",
            "All components appear on the UL-approved BOM.",
            "SCCR documented with worst-case calculation.",
            "Nameplate applied and panel is complete before energizing.",
            "Panel drawing includes SCCR and component listings.",
        ])},
    ],
    "related":[
        ("Control Panel Layout & BOM","../10_System_Integration_&_Commissioning/Control Panel Layout &amp; BOM.html"),
        ("Fuses vs Breakers","../02_Power_Distribution/Fuses vs Breakers.html"),
        ("NEC 430 – Motors & Controllers","NEC 430 – Motors &amp; Controllers.html"),
        ("NFPA 79 – Machinery Electrical","NFPA 79 – Machinery Electrical.html"),
    ],
},

"IEC 61131-3 – PLC Programming.html":{
    "title":"IEC 61131-3 – PLC Programming",
    "meta":{"category":"Standards & Codes","tags":["#IEC61131","#LD","#ST","#FBD","#SFC","#IL"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"IEC 61131-3"},
    "sections":[
        {"title":"Description","body": p(
            "IEC 61131-3 is the international standard that defines PLC programming languages, data types, and program organization. Every major vendor implements it to one degree or another. Knowing the standard helps you move between platforms.")},
        {"title":"Five Standard Languages","body": table(
            ["Language","Abbreviation","Use Case"],
            [
                ["Ladder Diagram","LD","Relay-style discrete logic, most readable for electricians"],
                ["Function Block Diagram","FBD","Process, PID, continuous logic"],
                ["Structured Text","ST","Math, loops, complex algorithms"],
                ["Sequential Function Chart","SFC","State machines and sequencing"],
                ["Instruction List","IL","Assembly-like; largely deprecated in Ed. 3"],
            ])},
        {"title":"Key Concepts","body": ul([
                "<strong>POUs</strong> — Program Organization Units: Programs, Function Blocks, Functions.",
                "<strong>Data types</strong> — BOOL, INT, DINT, REAL, TIME, STRING, DATE, TIME_OF_DAY, structured types.",
                "<strong>Tasks</strong> — periodic, event, continuous; each task runs POUs with priority.",
                "<strong>Variables</strong> — VAR, VAR_INPUT, VAR_OUTPUT, VAR_IN_OUT, VAR_GLOBAL, VAR_EXTERNAL.",
                "<strong>Standard function blocks</strong> — TON, TOF, TP, CTU, CTD, CTUD, SR, RS, R_TRIG, F_TRIG.",
            ])},
        {"title":"Vendor Variants","body": table(
            ["Vendor","Notes"],
            [
                ["Rockwell Studio 5000","LD, ST, FBD, SFC. Tag-based. Own AOI (Add-On Instruction) concept."],
                ["Siemens TIA Portal","LAD, FBD, STL (IL), SCL (ST), GRAPH (SFC)."],
                ["Codesys","Cleanest IEC 61131-3 reference implementation; used by many brands."],
                ["Beckhoff TwinCAT","IEC 61131-3 + C++ and C# for non-real-time code."],
                ["Schneider EcoStruxure","LD, ST, FBD, SFC. EFB (Elementary Function Blocks)."],
                ["Mitsubishi GX Works3","LD, ST, FBD, SFC with vendor extensions."],
            ])},
        {"title":"Portability","body": p(
            "IEC 61131-3 gives you 80% portability of concepts — syntax still differs by vendor. PLCopen is working to close that gap with XML-based interchange. For now, document algorithms rather than assume you can drop a program from one vendor into another.")},
        {"title":"Field Checklist","body": tasks([
            "Language chosen per logic type (LD for discrete, ST for math, SFC for sequence).",
            "Function blocks reused rather than copy-paste.",
            "Data types declared explicitly.",
            "Tasks and priorities match timing requirements.",
            "Program version and revision recorded.",
        ])},
    ],
    "related":[
        ("Ladder Logic Basics","../06_PLC_Programming_&_Logic/Ladder Logic Basics.html"),
        ("Data Blocks & Structured Text","../06_PLC_Programming_&_Logic/Data Blocks &amp; Structured Text.html"),
        ("Basic State Machine Programming","../06_PLC_Programming_&_Logic/Basic State Machine Programming.html"),
        ("What is a PLC","../05_PLCs & Automation Hardware/What is a PLC.html"),
    ],
},

"NFPA 79 – Machinery Electrical.html":{
    "title":"NFPA 79 – Machinery Electrical",
    "meta":{"category":"Standards & Codes","tags":["#NFPA79","#machinery","#industrial","#OEM"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"NFPA 79, IEC 60204-1"},
    "sections":[
        {"title":"Description","body": p(
            "NFPA 79 covers the electrical / electronic equipment of industrial machinery in North America — think OEM machine builders delivering equipment to a plant. It's the US counterpart to IEC 60204-1 and is referenced by OSHA and most AHJs.")},
        {"title":"Scope","body": ul([
                "Machines 600 V and below.",
                "Supply circuit, disconnects, protection.",
                "Control circuits — voltages, insulation, colors, protection.",
                "Operator control stations.",
                "Grounding, bonding, equipotential.",
                "Wire colors, identification, and routing.",
                "Documentation (drawings, instructions).",
            ])},
        {"title":"Key Rules","body": table(
            ["Topic","Rule (summary)"],
            [
                ["Disconnect","Single-means disconnect per machine, lockable"],
                ["Emergency stop","Required on machines with hazards; palm-type red, yellow background"],
                ["Control voltage","≤ 120 VAC typical, 24 VDC preferred for new designs"],
                ["Control protection","Overcurrent, isolation from power"],
                ["Wire colors","Black = AC > 50 V hot; red = AC control; blue = DC control; white = grounded neutral; green = equipment ground"],
                ["Enclosure","Type rated for environment; UL 508A typical"],
                ["Equipment grounding","Bonded to building earth; continuous path"],
                ["Documentation","Schematics, connection diagrams, parts list delivered with the machine"],
            ])},
        {"title":"Wire Color Quick Reference","body": code(
"Black   - AC power, > 50 V\n"
"Red     - AC control circuits\n"
"Blue    - DC control circuits\n"
"Yellow  - Foreign voltage (fed from external source)\n"
"White   - Grounded (neutral) conductor\n"
"Green / green-yellow - Equipment grounding conductor\n"
"\n"
"See also: <a href=\"../02_Power_Distribution/Wire Color Codes (US &amp; IEC).html\">Wire Color Codes</a>\n")},
        {"title":"Field Checklist","body": tasks([
            "Machine disconnect installed, lockable, labeled.",
            "E-stop conforms to color and shape requirements.",
            "Wire colors match the standard.",
            "Documentation delivered with the machine.",
            "Equipment grounding verified with a low-resistance test.",
        ])},
    ],
    "related":[
        ("Wire Color Codes (US & IEC)","../02_Power_Distribution/Wire Color Codes (US &amp; IEC).html"),
        ("Emergency Stops (E-Stops)","../12_Safety_Systems_Advanced/Emergency Stops (E-Stops).html"),
        ("UL 508A – Control Panels","UL 508A – Control Panels.html"),
        ("Risk Assessments & Functional Safety","../12_Safety_Systems_Advanced/Risk Assessments &amp; Functional Safety.html"),
    ],
},

"SIL - PL Functional Safety Intro.html":{
    "title":"SIL & PL Functional Safety Intro",
    "meta":{"category":"Standards & Codes","tags":["#SIL","#PL","#safety","#ISO13849","#IEC61508"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"IEC 61508, IEC 62061, ISO 13849-1"},
    "sections":[
        {"title":"Description","body": p(
            "Functional safety is the discipline of designing safety-related control functions so they reduce risk to a specified level, even with component failures. SIL and PL are the two common metrics — closely related, used in different domains.")},
        {"title":"The Two Frameworks","body": table(
            ["Framework","Level","Typical Application"],
            [
                ["IEC 61508 / 62061 (SIL)","SIL 1–4","Process industry, complex electronic systems"],
                ["ISO 13849-1 (PL)","PL a–e","Machinery (most factory applications)"],
            ])},
        {"title":"SIL vs PL Cross-Reference","body": table(
            ["SIL","PL","PFHd (1/hr)","Reduction factor"],
            [
                ["---","a","10⁻⁵ to < 10⁻⁴","Low risk reduction"],
                ["1","b","3×10⁻⁶ to < 10⁻⁵",""],
                ["1","c","10⁻⁶ to < 3×10⁻⁶",""],
                ["2","d","10⁻⁷ to < 10⁻⁶",""],
                ["3","e","10⁻⁸ to < 10⁻⁷","Very low risk of failure"],
            ])},
        {"title":"Risk Assessment to Level","body": ol([
                "Identify hazards using a structured method (HAZOP, FMEA, ISO 12100).",
                "Estimate severity, frequency / exposure, and probability of avoidance.",
                "Look up required PL or SIL from a risk graph (ISO 13849 or IEC 62061).",
                "Design safety function to meet that level — component selection, architecture, diagnostics.",
                "Validate by calculation (PFHd) and testing.",
            ])},
        {"title":"Common Safety Functions","body": ul([
                "Emergency stop (ISO 13850).",
                "Safety-related guard interlock (ISO 14119).",
                "Two-hand control (ISO 13851).",
                "Safe Torque Off (STO) and Safe Stop 1/2 on drives (IEC 61800-5-2).",
                "Safe speed, safe position monitoring.",
                "Safety-rated light curtain muting.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Risk assessment documented.",
            "Required SIL / PL specified for each safety function.",
            "Architecture (Cat B / 1 / 2 / 3 / 4) justified.",
            "Component MTTFd, DC, CCF data filed.",
            "Validation tests done and signed off.",
        ])},
    ],
    "related":[
        ("Risk Assessments & Functional Safety","../12_Safety_Systems_Advanced/Risk Assessments &amp; Functional Safety.html"),
        ("Safety Relays & Safety PLCs","../05_PLCs & Automation Hardware/Safety Relays &amp; Safety PLCs.html"),
        ("Emergency Stops (E-Stops)","../12_Safety_Systems_Advanced/Emergency Stops (E-Stops).html"),
        ("Safety Fencing & Interlocks","../12_Safety_Systems_Advanced/Safety Fencing &amp; Interlocks.html"),
    ],
},

}
CONTENT = {FOLDER: PAGES}
