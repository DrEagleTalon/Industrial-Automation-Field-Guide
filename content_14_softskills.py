"""Content for 14_Soft_Skills_Workflow."""

FOLDER = "14_Soft_Skills_Workflow"

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

"Reading Schematics & Wiring Diagrams.html":{
    "title":"Reading Schematics & Wiring Diagrams",
    "meta":{"category":"Soft Skills & Workflow","tags":["#schematics","#wiring","#symbols","#ladder"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Schematics are the map of an electrical system. Reading them quickly and accurately is the single biggest time-saver in troubleshooting.")},
        {"title":"Types of Drawings","body": table(
            ["Drawing","What it shows"],
            [
                ["Single-line / one-line","Simplified power flow for whole plant / feeder"],
                ["Three-line","Actual three-phase power wiring"],
                ["Schematic / ladder","Control logic, rail-to-rail rungs"],
                ["Wiring diagram / interconnect","Device-to-device terminal connections"],
                ["Panel layout","Physical arrangement inside the panel"],
                ["P&ID","Process and instrumentation — process industries"],
                ["Loop sheet","One instrument loop end-to-end"],
                ["Network architecture","Switches, PLCs, HMIs, IPs"],
            ])},
        {"title":"Symbols to Know","body": ul([
                "Contactor / contact (NO, NC, aux NO, aux NC).",
                "Relay coil and contacts.",
                "Pushbutton, selector switch, pilot light.",
                "Limit switch, proximity sensor, photo-sensor.",
                "Fuse, breaker, overload.",
                "Transformer (power, CT, PT).",
                "Ground symbols (equipment, clean, chassis).",
                "Terminal block, wire number, cross-reference.",
                "PLC input, output, analog module symbols.",
            ])},
        {"title":"Navigating a Schematic Set","body": ol([
                "Start with the title block — revision, date, author.",
                "Find the single-line to understand the power layout.",
                "Find the I/O list / PLC diagram for software functions.",
                "Trace a wire: follow wire numbers across sheets via cross-reference codes (e.g., '/5.3' = sheet 5, column 3).",
                "Note relay coils in one place, their contacts listed below showing where they appear.",
            ])},
        {"title":"Red-Lining","body": p(
            "When the field doesn't match the drawing, mark up a copy of the drawing (red-line) to reflect reality, then have an engineer fold the redlines into a new revision. Unrecorded field changes are how drawings rot.")
        },
        {"title":"Field Checklist","body": tasks([
            "Latest revision of schematic available on the floor.",
            "Cross-reference codes understood.",
            "Wire numbers verified on installation.",
            "Red-lines captured during troubleshooting and fed back.",
        ])},
    ],
    "related":[
        ("Using CAD Tools","Using CAD Tools.html"),
        ("Documentation Best Practices","../10_System_Integration_&_Commissioning/Documentation Best Practices.html"),
        ("General Troubleshooting Methodology","../09_Troubleshooting_&_Diagnostics/General Troubleshooting Methodology.html"),
    ],
},

"Using CAD Tools.html":{
    "title":"Using CAD Tools",
    "meta":{"category":"Soft Skills & Workflow","tags":["#CAD","#AutoCAD","#EPLAN","#SolidWorks","#drawings"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Electrical CAD is where schematics are drawn, BOMs generated, and panel layouts built. The tool matters less than the discipline — consistent symbols, standardized templates, and versioned files beat flashy features.")},
        {"title":"Common Tools","body": table(
            ["Tool","Strengths","Typical User"],
            [
                ["AutoCAD Electrical","Familiar, large install base, affordable","Integrators, small shops"],
                ["EPLAN Electric P8","Database-driven, global standard","Large OEMs, Europe"],
                ["SolidWorks Electrical","Tied to mechanical CAD","Shops already on SolidWorks"],
                ["ETAP","Power system analysis","Utilities, large plants"],
                ["Promise / Eplan Pro Panel","3D panel layout","High-volume panel shops"],
                ["KiCad / Altium","Small board-level","PCB and small custom hardware"],
            ])},
        {"title":"Good Habits","body": ul([
                "Standardized title blocks and templates.",
                "Symbol library with IEC or NEMA consistency (don't mix).",
                "Wire numbering scheme documented.",
                "Cross-reference codes generated automatically by the tool.",
                "BOM produced directly from the drawing.",
                "Version control (Git, Vault, SolidWorks PDM).",
            ])},
        {"title":"Productivity Tips","body": ul([
                "Build a library of approved components — don't redraw.",
                "Use page templates for common sheet types.",
                "Automate wire numbering; don't hand-type numbers.",
                "Export to PDF for the field copy; PDF has no surprises.",
                "Annotate with cable tags, tag numbers, and sheet references.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "CAD library locked and versioned.",
            "Templates match company standard.",
            "Cross-references auto-generated.",
            "BOM exported and reconciled with purchasing.",
            "PDF release versioned and archived.",
        ])},
    ],
    "related":[
        ("Reading Schematics & Wiring Diagrams","Reading Schematics &amp; Wiring Diagrams.html"),
        ("Documentation Best Practices","../10_System_Integration_&_Commissioning/Documentation Best Practices.html"),
        ("Control Panel Layout & BOM","../10_System_Integration_&_Commissioning/Control Panel Layout &amp; BOM.html"),
    ],
},

"Writing Work Orders & Reports.html":{
    "title":"Writing Work Orders & Reports",
    "meta":{"category":"Soft Skills & Workflow","tags":["#workorder","#report","#CMMS","#documentation"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "What you write down becomes the memory of the plant. Good work orders and reports make the same problem easier next time; bad ones guarantee you'll repeat every mistake.")},
        {"title":"Good Work Order","body": ul([
                "Equipment ID / location.",
                "Symptom, not the guessed cause. 'Motor trips on startup' > 'Bad overload'.",
                "When it started, how often, under what conditions.",
                "Recent changes (maintenance, parts, operations).",
                "Priority and safety impact.",
                "Contact for clarifications.",
            ])},
        {"title":"Good Completion Report","body": ul([
                "What was found — root cause, not just symptom.",
                "What was done — parts replaced with part numbers, settings changed, values before/after.",
                "What was tested — how you verified the fix.",
                "Time spent and parts used.",
                "Follow-up items (PM adjustments, spares, drawings to update).",
            ])},
        {"title":"Template","body": code(
"WORK COMPLETED REPORT\n"
"\n"
"Equipment:           _______________________________\n"
"Work Order #:        _______________________________\n"
"Date / Shift:        _______________________________\n"
"Technician(s):       _______________________________\n"
"\n"
"Reported Symptom:    _______________________________\n"
"\n"
"Findings / Root Cause:\n"
"  _______________________________\n"
"\n"
"Work Performed:\n"
"  _______________________________\n"
"\n"
"Parts Used (P/N, qty):\n"
"  _______________________________\n"
"\n"
"Verification:\n"
"  _______________________________\n"
"\n"
"Follow-up / PM Recommendations:\n"
"  _______________________________\n"
"\n"
"Time:  Start ________ End ________ Total ________\n")},
        {"title":"Habits That Pay Off","body": ul([
                "Write while it's fresh — not end of shift.",
                "Photos of the condition before and after.",
                "Measurements with units and instrument used.",
                "Honest about what was not tested / unknown.",
                "CMMS updated same day; paper also filed.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Work order logged in CMMS.",
            "Root cause and fix distinguished.",
            "Parts and time recorded.",
            "Follow-up items created.",
            "Drawings / PM updated if needed.",
        ])},
    ],
    "related":[
        ("Client Communication & Support","Client Communication &amp; Support.html"),
        ("Documentation Best Practices","../10_System_Integration_&_Commissioning/Documentation Best Practices.html"),
        ("General Troubleshooting Methodology","../09_Troubleshooting_&_Diagnostics/General Troubleshooting Methodology.html"),
    ],
},

"Client Communication & Support.html":{
    "title":"Client Communication & Support",
    "meta":{"category":"Soft Skills & Workflow","tags":["#communication","#client","#support","#setting-expectations"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Your client is the person asking for help — inside the plant (operations, maintenance) or outside it (customer, vendor). How you communicate with them shapes whether you get invited back. Most technical work is judged on communication, not just on results.")},
        {"title":"Principles","body": ul([
                "<strong>Answer the real question first</strong>, then explain.",
                "<strong>Match the audience</strong> — operator, supervisor, manager, integrator all need different depth.",
                "<strong>Set expectations</strong> before you start: what you'll do, how long, what they'll see, what risks exist.",
                "<strong>Update proactively</strong> — if you're running late or hit a snag, say so early.",
                "<strong>Own outcomes</strong> — don't blame. Explain and propose a fix.",
                "<strong>Confirm understanding</strong> — ask them to repeat the plan or summarize findings.",
            ])},
        {"title":"Troubleshooting Interview","body": ol([
                "What was happening when the problem started?",
                "Is it continuous or intermittent? Since when?",
                "Any changes — parts, operator, raw materials, weather?",
                "Has it been worked on recently?",
                "Any fault codes / alarms / symptoms?",
                "What matters most — production rate, quality, safety, cost?",
            ])},
        {"title":"Delivering Bad News","body": ul([
                "Do it early, not late.",
                "Say what you know and what you don't.",
                "Offer at least one path forward.",
                "Answer 'what does this mean for me?' before they ask.",
                "Write it down — even if you also tell them verbally.",
            ])},
        {"title":"Remote Support","body": ul([
                "Confirm the change window and safety state before connecting.",
                "Narrate what you're doing in the chat / call.",
                "Don't make undocumented changes.",
                "Hand off with a written summary.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Expectations set before work started.",
            "Updates given at natural checkpoints.",
            "Summary emailed after the work.",
            "Client signs off on completion.",
            "Relationship is stronger at the end than at the start.",
        ])},
    ],
    "related":[
        ("Writing Work Orders & Reports","Writing Work Orders &amp; Reports.html"),
        ("Project Handoff Docs","Project Handoff Docs.html"),
        ("Commissioning Reports & Sign-off","../10_System_Integration_&_Commissioning/Commissioning Reports &amp; Sign-off.html"),
    ],
},

"Project Handoff Docs.html":{
    "title":"Project Handoff Docs",
    "meta":{"category":"Soft Skills & Workflow","tags":["#handoff","#docs","#closeout","#training"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Handoff is the moment the project stops being yours and starts being the customer's. The quality of the handoff decides how much support you'll owe after the fact, and how readily they'll call you back for the next job.")},
        {"title":"What Goes in the Package","body": ul([
                "Commissioning reports and sign-off sheets.",
                "As-built drawings (electrical, pneumatic, P&ID, network).",
                "PLC / HMI / drive program and parameter backups.",
                "Operator manuals — how to run, stop, change over.",
                "Maintenance manuals — spares, PMs, troubleshooting flows.",
                "Safety validation records and risk assessment.",
                "Training records — who attended, what was covered.",
                "Outstanding punch list with owners and dates.",
                "Vendor contacts and support agreements.",
                "Warranty terms and response times.",
            ])},
        {"title":"Training","body": ul([
                "At least three rounds: operator run, operator changeover, maintainer troubleshooting.",
                "Record the session.",
                "Hands-on during the training — no PowerPoint monologues alone.",
                "Provide cheat sheets for common tasks.",
            ])},
        {"title":"Follow-Up","body": ul([
                "Check-in at 1 week, 1 month, 3 months.",
                "Capture issues in a log, not ad-hoc emails.",
                "Close warranty items promptly.",
                "Propose continuous-improvement items for the next round.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Complete handoff package delivered electronically and in paper.",
            "Training completed and signed off.",
            "Punch list agreed and dated.",
            "Follow-up schedule on the calendar.",
            "Client testimonial or case study agreed (for next pitch).",
        ])},
    ],
    "related":[
        ("Commissioning Reports & Sign-off","../10_System_Integration_&_Commissioning/Commissioning Reports &amp; Sign-off.html"),
        ("Documentation Best Practices","../10_System_Integration_&_Commissioning/Documentation Best Practices.html"),
        ("Client Communication & Support","Client Communication &amp; Support.html"),
        ("Writing Work Orders & Reports","Writing Work Orders &amp; Reports.html"),
    ],
},

}
CONTENT = {FOLDER: PAGES}
