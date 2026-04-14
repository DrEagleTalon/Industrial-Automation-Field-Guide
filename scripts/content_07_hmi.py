"""Content for 07_HMI_SCADA_Systems."""

FOLDER = "07_HMI_SCADA_Systems"

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

"HMI Basics.html":{
    "title":"HMI Basics",
    "meta":{"category":"HMI / SCADA","tags":["#HMI","#screen","#operator","#panelview"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"ISA-101, IEC 62682","equipment":"PanelView, Siemens Comfort/TP, Magelis, Proface"},
    "sections":[
        {"title":"Description","body": p(
            "An HMI (Human-Machine Interface) is the touchscreen or PC-based interface an operator uses to see and control the machine. Unlike a SCADA system, an HMI is typically machine-local and shows one machine or cell.")},
        {"title":"Core Elements","body": ul([
                "<strong>Screens</strong> — pages of graphics, each covering a machine area or function.",
                "<strong>Tags</strong> — the data connection to the PLC (see <a href=\"../06_PLC_Programming_&_Logic/HMI IO Tags &amp; Linking.html\">HMI I/O Tags</a>).",
                "<strong>Animations</strong> — visibility, color, fill, rotation driven by tag values.",
                "<strong>Controls</strong> — buttons, numeric entry, dropdowns, recipe managers.",
                "<strong>Alarms</strong> — banner, history, and summary views.",
                "<strong>Trends</strong> — time-series graphs of analog values.",
                "<strong>Security</strong> — user accounts, roles, and audit trails.",
            ])},
        {"title":"Hardware Form Factors","body": table(
            ["Form Factor","Typical Use","Notes"],
            [
                ["Panel-mount touchscreen","Machine-local operator interface","4\" to 22\" common"],
                ["PC-based thin client","Central operator stations","ThinManager / VersaVirtual"],
                ["Web-based HMI","Any browser","Ignition Perspective, FactoryTalk Optix"],
                ["Pendants","Robots, CNC, gantries","Handheld"],
                ["Mobile dashboards","Supervisor / maintenance","Read-only typically"],
            ])},
        {"title":"Design Principles (ISA-101)","body": ul([
                "Design for the 3am operator — simple, clear, unambiguous.",
                "Consistent layout across screens: title bar, nav, alarm banner, footer in the same place.",
                "Limit colors: reserve red for alarm, yellow for warning, green for running, gray for idle. Avoid rainbow dashboards.",
                "Show process values as numbers <em>and</em> visual indicators (bar, gauge, color).",
                "Group related items so the eye doesn't hunt.",
                "Keep navigation shallow — target ≤ 3 clicks to any destination.",
            ])},
        {"title":"Common Screens","body": ul([
                "Overview — whole-machine status at a glance.",
                "Area / cell — detail of one machine section.",
                "Manual / maintenance — force inputs, jog motors, run individual actions (with keyed access).",
                "Alarms — active, history, shelved.",
                "Trends — analog histories and key performance indicators.",
                "Recipes — tunable batch or product parameters.",
                "Diagnostics — PLC connection, I/O status, firmware info.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "HMI IP / node address documented and matches PLC communication setup.",
            "Navigation tested from every screen back to the Home screen.",
            "All tags have quality-of-data indication when stale or bad.",
            "Manual-mode screens require login and are audited.",
            "Backup of the HMI project saved off-device.",
        ])},
    ],
    "related":[
        ("Screen Navigation & User Inputs","Screen Navigation &amp; User Inputs.html"),
        ("Tag Management & Alarms","Tag Management &amp; Alarms.html"),
        ("Connecting HMI to PLC (EthernetIP, Modbus)","Connecting HMI to PLC (EthernetIP, Modbus).html"),
        ("Basic SCADA Architecture","Basic SCADA Architecture.html"),
        ("HMI IO Tags & Linking","../06_PLC_Programming_&_Logic/HMI IO Tags &amp; Linking.html"),
    ],
},

"Screen Navigation & User Inputs.html":{
    "title":"Screen Navigation & User Inputs",
    "meta":{"category":"HMI / SCADA","tags":["#UI","#navigation","#buttons","#security"],
            "difficulty":"Beginner","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Operators spend more time navigating your HMI than programming it. A clean, predictable navigation pattern reduces errors and speeds up fault handling.")},
        {"title":"Patterns That Work","body": ul([
                "Fixed top header with Home / Overview / Alarms / Login.",
                "Fixed bottom banner with the top active alarm, current user, and date/time.",
                "Main-area content specific to the selected screen.",
                "Breadcrumb or page title showing 'where am I'.",
                "Back / Home buttons on every screen.",
            ])},
        {"title":"User Inputs","body": ul([
                "<strong>Momentary buttons</strong> — press and release generates a one-shot to the PLC.",
                "<strong>Maintained buttons</strong> — toggle. Rare — usually better handled as a state in the PLC.",
                "<strong>Numeric entry</strong> — keypad pop-up with min/max limits and engineering unit display.",
                "<strong>Dropdowns</strong> — for mode selection, recipe selection.",
                "<strong>Confirm dialogs</strong> — required for destructive actions (jog in manual, clear totalizers).",
                "<strong>Swipe / gesture</strong> — only on newer HMIs; keep as augmentation, not the primary control.",
            ])},
        {"title":"Security & Audit","body": ul([
                "Roles: Viewer (read-only), Operator (run/stop), Maintenance (manual, setpoints), Engineer (everything).",
                "Auto-logout after inactivity.",
                "Audit log every write operation with user, tag, old value, new value, timestamp.",
                "No shared 'admin' login — per-person accounts.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Every screen has Home and Back navigation in the same location.",
            "Confirm dialogs on all destructive or manual-mode writes.",
            "Audit log verified to capture changes.",
            "Screen load time < 1 s from any transition.",
        ])},
    ],
    "related":[
        ("HMI Basics","HMI Basics.html"),
        ("Tag Management & Alarms","Tag Management &amp; Alarms.html"),
    ],
},

"Tag Management & Alarms.html":{
    "title":"Tag Management & Alarms",
    "meta":{"category":"HMI / SCADA","tags":["#tags","#alarms","#UDT","#history"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"ISA-18.2"},
    "sections":[
        {"title":"Description","body": p(
            "Tags are the HMI's view into PLC data. Alarms are the most important tag category because they direct operator attention. Both need discipline to stay useful at scale.")},
        {"title":"Tag Organization","body": ul([
                "Group tags by area or machine, then by equipment.",
                "Use UDT-based faceplates so a single motor data structure drives one reusable graphic.",
                "Prefer browsed/imported tags over manually re-created ones — eliminates drift.",
                "Standard prefixes: PV (process value), SP (setpoint), OUT (output), CMD (command), STS (status).",
            ])},
        {"title":"Alarm Priorities","body": table(
            ["Priority","Response Time","Example"],
            [
                ["Critical","Immediate, safe shutdown","E-stop active, reactor pressure high-high"],
                ["High","< 1 minute","Motor overload, pump seal failure"],
                ["Medium","< 10 minutes","Tank level high, sensor drift"],
                ["Low","End of shift","Filter cycle count reached"],
                ["Info","No action","Recipe changed, shift started"],
            ])},
        {"title":"Alarm History & Journaling","body": ul([
                "Store alarm history in a database (SQL typically) for weeks to years.",
                "Each record: ID, time, area, message, severity, acked-by, acked-time.",
                "Expose the history in a searchable view with filters.",
                "Monthly rationalization review — remove or consolidate alarms that fired > 10× with no real response.",
            ])},
        {"title":"Performance","body": ul([
                "HMI polls add up — too many update groups slow the whole system.",
                "Use change-driven or subscription-based update where the PLC supports it (Logix optimized tags, S7 optimized access).",
                "Diagnostic tags on their own group so they don't compete with operator screens.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Tag list versioned and backed up.",
            "Alarm priorities reviewed and documented.",
            "Alarm history verified end-to-end (PLC → HMI → database).",
            "Unused tags purged quarterly.",
            "Comm quality visible on every screen.",
        ])},
    ],
    "related":[
        ("HMI Basics","HMI Basics.html"),
        ("HMI IO Tags & Linking","../06_PLC_Programming_&_Logic/HMI IO Tags &amp; Linking.html"),
        ("Alarms & Fault Detection","../06_PLC_Programming_&_Logic/Alarms &amp; Fault Detection.html"),
        ("Data Logging & Trends","Data Logging &amp; Trends.html"),
    ],
},

"Connecting HMI to PLC (EthernetIP, Modbus).html":{
    "title":"Connecting HMI to PLC",
    "meta":{"category":"HMI / SCADA","tags":["#EthernetIP","#Modbus","#OPCUA","#comms"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Getting the HMI to talk to the PLC reliably is 80% of a field commissioning job. A handful of protocols cover nearly all cases.")},
        {"title":"Common Protocols","body": table(
            ["Protocol","PLC Family","Notes"],
            [
                ["EtherNet/IP (CIP)","Rockwell, Omron, Opto 22","Allen-Bradley native. Implicit messaging for I/O, explicit for tags."],
                ["PROFINET","Siemens","Dominant in Europe. TIA Portal imports/maps tags natively."],
                ["Modbus TCP","Almost everyone","The universal interop protocol; function codes 03, 04, 06, 16."],
                ["Modbus RTU","Legacy, small devices","Serial, RS-485, 9600/19200 baud typical"],
                ["OPC UA","Any","Vendor-neutral, secure. Good for SCADA / IT integration."],
                ["EtherCAT","Beckhoff, Omron, B&R","For very fast I/O and motion"],
                ["BACnet / LON","Building automation","Rare in plant floor, common in HVAC"],
            ])},
        {"title":"Connection Setup (Generic)","body": ol([
                "Confirm IP addressing and subnet — HMI and PLC must be on same subnet or a route must exist (see <a href=\"../08_Industrial_Networks_&_Protocols/IP Addressing &amp; Subnetting.html\">IP Addressing</a>).",
                "Open the PLC's remote-access firewall / permissions if any.",
                "In the HMI project, create a 'device' or 'driver' entry with PLC IP, slot/rack (AB), or connection parameters.",
                "Test the connection using the HMI software's built-in tag browser.",
                "Add tags (preferably by browsing) to the HMI tag database.",
                "Place a quality indicator on the main screen.",
            ])},
        {"title":"Typical Failure Modes","body": table(
            ["Symptom","Likely Cause","Step"],
            [
                ["All tags show ???","Driver not connected — wrong IP or firewall","Ping PLC; check port / firewall"],
                ["Some tags OK, others ??","Tag names don't match PLC","Re-browse and rebind"],
                ["Tags update slowly","Poll rate too fast, too many tags","Split into update groups"],
                ["Intermittent #COMM","Network issue (switch, cable, duplex mismatch)","See <a href=\"../09_Troubleshooting_&_Diagnostics/Network Communication Loss.html\">Network Comm Loss</a>"],
                ["Values correct but writes fail","Write access denied; tag external-access flag wrong","Check tag's external access attribute in PLC"],
            ])},
        {"title":"Security","body": ul([
                "Use per-user logins on the HMI, not shared accounts.",
                "Disable unused protocols on the PLC.",
                "Segregate control network from business network — see <a href=\"../08_Industrial_Networks_&_Protocols/Industrial Ethernet vs IT Ethernet.html\">Industrial vs IT Ethernet</a>.",
                "Harden OPC UA with certificates, not anonymous connections.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "PLC IP, port, and slot documented on the drawing.",
            "HMI comms quality visible on screen.",
            "Tag browsing confirmed (not only manual tag entry).",
            "Writes from HMI tested end-to-end.",
            "Protocol logs or traces captured during commissioning.",
        ])},
    ],
    "related":[
        ("HMI Basics","HMI Basics.html"),
        ("Common Protocols","../08_Industrial_Networks_&_Protocols/Common Protocols.html"),
        ("IP Addressing & Subnetting","../08_Industrial_Networks_&_Protocols/IP Addressing &amp; Subnetting.html"),
        ("Network Communication Loss","../09_Troubleshooting_&_Diagnostics/Network Communication Loss.html"),
    ],
},

"Basic SCADA Architecture.html":{
    "title":"Basic SCADA Architecture",
    "meta":{"category":"HMI / SCADA","tags":["#SCADA","#historian","#server","#client"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "SCADA (Supervisory Control and Data Acquisition) gathers data from many PLCs and machines, centralizes it on servers, and presents it to many clients. Where an HMI is one-to-one with a machine, SCADA is many-to-many.")},
        {"title":"Typical Architecture","body": code(
"                         Business network / IT\n"
"                                 |\n"
"                         +---- Firewall ----+\n"
"                         |                  |\n"
"                  SCADA Server(s)     Historian / DB\n"
"                        /   \\               |\n"
"           Operator clients  Engineering    BI / reporting\n"
"                        |\n"
"                 Control network\n"
"                  /      |       \\\n"
"              PLC 1    PLC 2    PLC N ...\n"
"              |          |        |\n"
"              Field I/O, drives, instruments\n")},
        {"title":"Key Components","body": ul([
                "<strong>SCADA servers</strong> — poll PLCs, run alarm engine, serve screens to clients. Often redundant pair.",
                "<strong>Historian</strong> — stores time-series data (PI, InfluxDB, Canary, Ignition Tag Historian).",
                "<strong>Thin-client infrastructure</strong> — ThinManager, RDS, VDI. Centralized operator stations.",
                "<strong>Relational database</strong> — SQL Server, PostgreSQL for alarm logs, audit, recipes.",
                "<strong>Reporting / BI layer</strong> — dashboards, KPIs, OEE.",
                "<strong>Network layer</strong> — segmented via managed switches and firewalls. See <a href=\"../08_Industrial_Networks_&_Protocols/Switches &amp; Managed Networks.html\">Switches & Managed Networks</a>.",
            ])},
        {"title":"Common Platforms","body": ul([
                "FactoryTalk View SE (Rockwell).",
                "WinCC / WinCC OA (Siemens).",
                "Ignition (Inductive Automation) — tag-based, web-delivered.",
                "Wonderware / AVEVA System Platform.",
                "Vijeo Citect / PlantPAx.",
                "ZenOn, iFix, Cimplicity — older or regional favorites.",
            ])},
        {"title":"Design Considerations","body": ul([
                "Redundancy: hot-standby servers, dual NICs, UPS.",
                "Time synchronization with NTP so alarms and data line up across sources.",
                "Backup / restore procedure tested quarterly.",
                "Licensing — tag-count or concurrent-user-based; buy margin.",
                "Cybersecurity — see <a href=\"../13_Specialty_Topics/Remote Access &amp; VPN.html\">Remote Access & VPN</a> and <a href=\"../08_Industrial_Networks_&_Protocols/Industrial Ethernet vs IT Ethernet.html\">Industrial vs IT Ethernet</a>.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Network diagram up to date and posted in the server room.",
            "Server redundancy tested (fail one; verify switch-over).",
            "Historian retention and rollup policy documented.",
            "All PLCs on SCADA use NTP-synced time.",
            "Disaster recovery: full restore of SCADA in under 8 hours rehearsed.",
        ])},
    ],
    "related":[
        ("HMI Basics","HMI Basics.html"),
        ("Data Logging & Trends","Data Logging &amp; Trends.html"),
        ("Cloud SCADA & MQTT","../13_Specialty_Topics/Cloud SCADA &amp; MQTT.html"),
        ("Industrial Ethernet vs IT Ethernet","../08_Industrial_Networks_&_Protocols/Industrial Ethernet vs IT Ethernet.html"),
    ],
},

"Data Logging & Trends.html":{
    "title":"Data Logging & Trends",
    "meta":{"category":"HMI / SCADA","tags":["#historian","#trends","#dataset","#KPI","#OEE"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Data logging captures the state of key tags over time. Trends plot that data for operators, engineers, and management. Good trends let you see problems that aren't obvious in a real-time value.")},
        {"title":"Logging Strategies","body": table(
            ["Strategy","When to Use"],
            [
                ["Periodic (e.g., 1 s)","Slow-changing process values (temperature, level)"],
                ["On-change / deadband","Values that are mostly flat but sometimes spike"],
                ["Event-driven","Alarms, machine state changes, batch steps"],
                ["Rate grouped","Mix periodic and on-change in one tag group"],
            ])},
        {"title":"Storage","body": ul([
                "Local HMI datalog files (small, rolling).",
                "Plant historian (PI, Canary, Ignition) for long-term.",
                "Time-series database (InfluxDB, TimescaleDB) for self-hosted.",
                "Enterprise data lake for analytics and ML.",
                "Plan retention: raw for weeks, aggregated hourly/daily for years.",
            ])},
        {"title":"Trend Design","body": ul([
                "One plot = one decision. Don't overlay 10 unrelated variables.",
                "Include setpoint alongside process value.",
                "Show alarms as annotations on the time axis.",
                "Time-zoom controls: 1 min, 15 min, 1 hr, 8 hr, shift, day.",
                "Export to CSV for offline analysis.",
            ])},
        {"title":"KPIs & OEE","body": p(
            "Overall Equipment Effectiveness (OEE) = Availability × Performance × Quality. All three factors can be derived from tags you probably already have: uptime (from running state), rate (from counters), and good part count (from QC tags). SCADA / historian is where OEE dashboards live."
        )},
        {"title":"Field Checklist","body": tasks([
            "Logging groups configured with appropriate periods and deadbands.",
            "Disk usage monitored; retention enforced.",
            "NTP running on all data sources.",
            "Time zone / DST handling documented.",
            "Backup + restore of historian tested.",
        ])},
    ],
    "related":[
        ("Basic SCADA Architecture","Basic SCADA Architecture.html"),
        ("Tag Management & Alarms","Tag Management &amp; Alarms.html"),
        ("Cloud SCADA & MQTT","../13_Specialty_Topics/Cloud SCADA &amp; MQTT.html"),
        ("IIoT Gateways & Edge","../13_Specialty_Topics/IIoT Gateways &amp; Edge.html"),
    ],
},

}
CONTENT = {FOLDER: PAGES}
