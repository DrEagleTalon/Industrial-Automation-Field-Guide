"""
Content module for 04_Motor_Control.
All page bodies written for field accuracy from working knowledge of
3-phase motor practice, NEC Article 430, IEC 60204-1, and common OEM
documentation (Allen-Bradley, Siemens, Schneider).
"""

FOLDER = "04_Motor_Control"

def table(headers, rows):
    out = ["<table>", "<thead><tr>"]
    for h in headers:
        out.append(f"<th>{h}</th>")
    out.append("</tr></thead><tbody>")
    for r in rows:
        out.append("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)

def ul(items):
    return "<ul>" + "".join(f"<li>{it}</li>" for it in items) + "</ul>"

def ol(items):
    return "<ol>" + "".join(f"<li>{it}</li>" for it in items) + "</ol>"

def code(block):
    return f"<pre><code>{block}</code></pre>"

def tasks(items):
    return "<ul>" + "".join(
        f'<li class="task unchecked"><span class="checkbox">&#x2610;</span> {it}</li>'
        for it in items
    ) + "</ul>"

def p(*paragraphs):
    return "\n".join(f"<p>{x}</p>" for x in paragraphs)


PAGES = {

# ─────────────────────────────────────────────────────────────────────────────
"3-Phase Motor Basics.html": {
    "title": "3-Phase Motor Basics",
    "meta": {
        "category": "Motor Control Systems",
        "tags": ["#motors","#3phase","#induction","#rpm","#slip"],
        "difficulty": "Beginner",
        "status": "final",
        "version": "1.0.0",
        "updated": "2026-04-13",
        "standards": "NEC Art. 430, IEC 60034",
        "equipment": "Squirrel-cage induction motors, wound-rotor motors",
    },
    "sections": [
        {"title":"Description","body": p(
            "Three-phase AC induction motors are the workhorse of industrial automation. They convert three-phase electrical power into rotating mechanical power through electromagnetic induction, with no brushes, commutators, or physical contact between rotor and stator.",
            "This page covers the fundamentals every automation tech needs to know: how the rotating field is made, how slip produces torque, how to read the basics of nameplate data, and why the motor behaves the way it does under start, run, and load.")},
        {"title":"Core Concepts","body":
            "<h3>What is a 3-phase motor?</h3>" + p(
                "A 3-phase induction motor has a stationary stator wound with three sets of coils spaced 120° apart, and a rotor - usually a squirrel-cage of shorted aluminum or copper bars. Three-phase power energizes the stator and creates a rotating magnetic field that drags the rotor along with it."
            ) +
            "<h3>How it works</h3>" + ol([
                "Three-phase AC in the stator produces a smoothly rotating magnetic field at synchronous speed.",
                "The field cuts the rotor bars, inducing a voltage and current in the rotor.",
                "Rotor current in the field produces torque (F = BIL), and the rotor begins to turn.",
                "The rotor always lags the field slightly — this difference is slip, and it is what creates usable torque.",
                "At no load, slip is small (1–2%). At full load, slip is higher (3–5%).",
            ]) +
            "<h3>Synchronous vs actual speed</h3>" + p(
                "Synchronous speed: <code>Ns = (120 × f) / P</code> where f is line frequency and P is the number of poles.",
                "A 4-pole motor on 60 Hz has Ns = 1800 RPM. A typical full-load nameplate speed of 1750 RPM represents about 2.8% slip."
            ) +
            "<h3>When to use 3-phase</h3>" + ul([
                "Any motor above roughly 1 HP in an industrial environment — higher efficiency, smaller size, simpler construction than single-phase.",
                "Constant-speed loads: fans, pumps, conveyors, compressors.",
                "Variable-speed loads when paired with a <a href=\"Variable Frequency Drives (VFDs) Basics.html\">VFD</a>.",
            ])
        },
        {"title":"Specifications & Parameters","body": table(
            ["Parameter","Typical Value / Range","Notes"],
            [
                ["Line voltage","208, 230, 460, 575, 2300, 4160 V","460 V is most common in North American industrial plants"],
                ["Frequency","50 or 60 Hz","Some motors are dual-rated 50/60 Hz"],
                ["Poles","2, 4, 6, 8","Determines base speed at a given frequency"],
                ["Synchronous speed","3600, 1800, 1200, 900 RPM @ 60 Hz","For 2, 4, 6, 8 poles"],
                ["Full-load slip","1–5%","Higher slip motors are used for high starting torque"],
                ["Starting current","500–800% of FLA (DOL start)","Why soft-starters and VFDs exist"],
                ["Starting torque","100–250% of full-load torque","Design B NEMA is the most common"],
                ["Power factor","0.75–0.90 full load","Drops significantly at light load"],
                ["Efficiency","85–96%","NEMA Premium and IE3/IE4 are minimums in many markets"],
                ["Insulation class","B, F, H","Class F (155 °C rise) is the modern standard"],
                ["Service factor","1.0, 1.15, 1.25","Multiplier on continuous HP rating"],
            ])},
        {"title":"Wiring & Diagrams","body": p(
            "Most industrial 3-phase motors have either 3, 6, 9, or 12 leads in the peckerhead. 3-lead motors are internally connected and can only be wired one way. 6- and 9-lead motors can be configured Wye/Delta or for dual-voltage operation.") +
            code("Typical dual-voltage 9-lead wye connection:\n"
                 "Low voltage (parallel wye):  T1-T7, T2-T8, T3-T9, T4-T5-T6 tied\n"
                 "High voltage (series wye):   T4-T7, T5-T8, T6-T9, T1-T2-T3 to line\n"
                 "\n"
                 "Always use the motor manufacturer connection diagram on\n"
                 "the nameplate or inside the peckerhead cover.")
        },
        {"title":"Troubleshooting & Diagnostics","body": table(
            ["Symptom","Likely Cause","Diagnostic Step","Tools Needed"],
            [
                ["Motor hums but won't start","Single-phasing, blown fuse, stuck rotor","Measure all three line voltages at motor terminals","Multimeter, clamp meter"],
                ["Runs slow / high current","Overload, wrong connection, voltage unbalance","Compare FLA to nameplate; check voltage balance < 1%","Clamp meter, DMM"],
                ["Trips overload shortly after start","Mechanical binding, starting across the line on damaged winding","Uncouple from load and restart","Clamp meter"],
                ["Overheating","Blocked ventilation, overload, high ambient, VFD without blower","Check airflow, load current vs. FLA, surface temp","IR camera, clamp meter"],
                ["Bearing noise","Worn bearing, misalignment, VFD shaft currents","Listen with stethoscope; check shaft end-float","Stethoscope, vibration meter"],
                ["Insulation breakdown","Moisture, age, contamination, transient over-voltage","Perform a <a href=\"Motor Megger Testing.html\">megger test</a>","Megohmmeter"],
            ])},
        {"title":"Field Checklist","body": tasks([
            "Confirm supply voltage and frequency match the nameplate.",
            "Verify motor leads are connected for the correct voltage per the nameplate diagram.",
            "Check rotation before coupling to the load — see <a href=\"Motor Wiring & Rotation Checking.html\">Motor Wiring &amp; Rotation Checking</a>.",
            "Measure all three line-to-line voltages; unbalance should be < 1%.",
            "Confirm overload relay is set to nameplate FLA (not SF amps).",
            "Verify grounding and bonding of the motor frame.",
            "Record no-load and full-load amps for a commissioning baseline.",
        ])},
        {"title":"Reference Notes","body": p(
            "NEMA MG 1 is the governing standard for motor construction in North America; IEC 60034 is the international equivalent.",
            "Design letter (A, B, C, D) on the nameplate defines the torque and slip characteristic. Design B is the default for general-purpose applications. Design C is high-starting-torque for loaded starts. Design D is high-slip for punch-press and hoist duty.",
            "When a 60 Hz motor is fed from a VFD at less than about 30 Hz, the shaft fan loses effectiveness — force ventilation or derate the motor.")},
    ],
    "related": [
        ("Motor Nameplate Data", "Motor Nameplate Data.html"),
        ("Motor Contactors & Starters", "Motor Contactors &amp; Starters.html"),
        ("Variable Frequency Drives (VFDs) Basics", "Variable Frequency Drives (VFDs) Basics.html"),
        ("Motor Wiring & Rotation Checking", "Motor Wiring &amp; Rotation Checking.html"),
        ("Overload Relays", "Overload Relays.html"),
        ("3-Phase vs Single-Phase", "../01_Electrical_Fundamentals/Basic Electrical Theory-Single-phase vs Three-phase.html"),
    ],
},

# ─────────────────────────────────────────────────────────────────────────────
"Motor Nameplate Data.html": {
    "title": "Motor Nameplate Data",
    "meta": {
        "category": "Motor Control Systems",
        "tags": ["#nameplate","#FLA","#SF","#NEMA","#motors"],
        "difficulty": "Beginner",
        "status": "final",
        "version": "1.0.0",
        "updated": "2026-04-13",
        "standards": "NEMA MG 1, IEC 60034, NEC 430.7",
        "equipment": "All industrial motors",
    },
    "sections": [
        {"title":"Description","body": p(
            "The motor nameplate is the single most important document on any motor. Before you size protection, set a <a href=\"Overload Relays.html\">overload</a>, program a <a href=\"Variable Frequency Drives (VFDs) Basics.html\">VFD</a>, pick a <a href=\"Motor Contactors &amp; Starters.html\">contactor</a>, or replace a burnt-out unit, the nameplate tells you what the motor actually is — not what someone wrote on the print twenty years ago.")},
        {"title":"Core Concepts","body":
            "<h3>What a nameplate gives you</h3>" + ul([
                "Electrical ratings: HP (or kW), voltage, FLA, frequency, phases, service factor.",
                "Mechanical ratings: speed, frame, enclosure, service conditions.",
                "Design and performance class: NEMA Design letter, efficiency, code letter.",
                "Insulation class and temperature rise.",
                "Bearings, lubrication, and winding connection diagrams.",
            ]) +
            "<h3>Why it matters</h3>" + p(
                "NEC 430.6(A)(1) says you size conductors and short-circuit protection from NEC tables, but you size overload protection from the actual nameplate FLA. Getting these two confused is one of the most common mistakes."
            )
        },
        {"title":"Key Fields Decoded","body": table(
            ["Field","What it means","How to use it"],
            [
                ["HP","Horsepower output at shaft, full load","Don't confuse with input kW"],
                ["kW","Mechanical output power (metric)","HP = kW × 1.341"],
                ["Volts","Rated line-to-line voltage","Multiple values mean the motor is dual-voltage"],
                ["Hz","Rated frequency (50 or 60)","Operating off-frequency requires re-rating"],
                ["FLA (Amps)","Full-load amps at rated voltage and HP","Set <a href=\"Overload Relays.html\">overloads</a> to this value"],
                ["SF","Service factor (1.0, 1.15, 1.25)","Continuous overload capability. SF amps = FLA × SF. Do NOT use SF amps to set overloads — use FLA."],
                ["RPM","Full-load speed","Subtract from synchronous to get slip"],
                ["Frame","NEMA frame (143T, 256T, etc.)","Determines shaft size, bolt pattern, coupling"],
                ["Enclosure","ODP, TEFC, TENV, XP","Dictates environment where the motor can live"],
                ["NEMA Design","A, B, C, D","Torque/slip characteristic"],
                ["Code Letter","A–V","Locked-rotor kVA/HP, used for short-circuit protection sizing"],
                ["Insulation Class","B, F, H","Maximum winding temperature rise"],
                ["Ambient","40 °C standard","Higher ambient requires derating"],
                ["Duty","Continuous (S1), short-time (S2), intermittent (S3)","Match to load profile"],
                ["PF","Power factor at full load","Affects kVA sizing of upstream equipment"],
                ["Efficiency","Full-load efficiency","Higher is better — NEMA Premium / IE3"],
                ["Bearing","DE / ODE bearing numbers","For ordering replacements"],
            ])},
        {"title":"Dual-Voltage / Dual-Winding Nameplates","body": p(
            "Many motors list two voltages and two FLAs. A common 9-lead motor is shown as 230/460 V and, say, 26/13 A. The same motor is being sold as a low-voltage (parallel) or high-voltage (series) machine — the FLA halves when voltage doubles because HP is constant.",
            "The nameplate or peckerhead cover shows the connection diagram. See <a href=\"Motor Wiring &amp; Rotation Checking.html\">Motor Wiring &amp; Rotation Checking</a> for the physical wiring.")
        },
        {"title":"Field Checklist","body": tasks([
            "Take a clear photo of the full nameplate before install.",
            "Record FLA, voltage, connection, and frame on the commissioning sheet.",
            "Cross-check FLA against the overload setting and the feeder conductor ampacity.",
            "Verify enclosure type is appropriate for the room (wash-down, hazardous area, etc.).",
            "Note bearings for spare parts stock.",
            "If motor is on a VFD, confirm VFD parameters match nameplate — see <a href=\"VFD Parameters &amp; Setup.html\">VFD Parameters &amp; Setup</a>.",
        ])},
        {"title":"Reference Notes","body": p(
            "NEC 430.7 lists the marking requirements for every motor sold in the US.",
            "IEC motors typically mark kW, full-load current at multiple voltages, efficiency class (IE1–IE4), duty cycle (S1–S10), and IP rating for the enclosure.",
            "A TEFC motor has Totally Enclosed Fan-Cooled frame; it does not breathe plant air. This is the default industrial enclosure.")},
    ],
    "related": [
        ("3-Phase Motor Basics", "3-Phase Motor Basics.html"),
        ("Overload Relays", "Overload Relays.html"),
        ("Motor Contactors & Starters", "Motor Contactors &amp; Starters.html"),
        ("Variable Frequency Drives (VFDs) Basics", "Variable Frequency Drives (VFDs) Basics.html"),
        ("NEC 430 – Motors & Controllers", "../11_Standards_and_Codes/NEC 430 – Motors &amp; Controllers.html"),
    ],
},

# ─────────────────────────────────────────────────────────────────────────────
"Direct-On-Line Starters.html": {
    "title": "Direct-On-Line Starters",
    "meta": {
        "category": "Motor Control Systems",
        "tags": ["#DOL","#starter","#contactor","#fullvoltagestart","#motors"],
        "difficulty": "Beginner",
        "status": "final",
        "version": "1.0.0",
        "updated": "2026-04-13",
        "standards": "NEC 430, IEC 60947-4-1",
        "equipment": "Magnetic contactor, overload relay, pushbutton control",
    },
    "sections": [
        {"title":"Description","body": p(
            "Direct-on-line (DOL) or 'across-the-line' starting is the simplest method of energizing a 3-phase motor: close a contactor and apply full line voltage to all three windings at once. It delivers maximum torque but also draws 500–800% of full-load amps as inrush.",
            "DOL is the starting method assumed in most ladder schematics and the default method for motors up to about 15 HP on stiff supplies. Above that, the inrush begins to sag the bus, trip upstream breakers, or mechanically shock driven equipment.")},
        {"title":"Core Concepts","body":
            "<h3>What makes a DOL starter</h3>" + ul([
                "Short-circuit protection — fuses or a motor-rated circuit breaker (MCP/MCCB).",
                "A 3-pole magnetic <a href=\"Motor Contactors &amp; Starters.html\">contactor</a> — the switching device.",
                "A thermal or electronic <a href=\"Overload Relays.html\">overload relay</a> — protects the winding.",
                "A control circuit — Start/Stop pushbuttons, aux contact for seal-in, optional reset.",
            ]) +
            "<h3>How the control circuit works</h3>" + p(
                "The classic DOL control uses <a href=\"../06_PLC_Programming_&amp;_Logic/Start-Stop Logic.html\">start-stop logic</a>: a momentary Start PB energizes the contactor coil; an aux contact in parallel with Start seals the coil in; a momentary Stop PB or an overload aux contact opens the seal-in, dropping out the coil."
            ) +
            "<h3>When to use DOL</h3>" + ul([
                "Supply transformer is stiff enough that a 6–8× inrush is acceptable (typical facility ≤ about 15 HP @ 480 V).",
                "Load can tolerate full starting torque (no belt slippage, gear shock, or fluid hammer).",
                "Simplicity and cost are more important than soft-start features.",
            ])
        },
        {"title":"Typical Power and Control Schematic","body": code(
"POWER:\n"
"  L1 L2 L3\n"
"   |  |  |\n"
"  [Fuses or MCP]          short-circuit / branch-circuit protection\n"
"   |  |  |\n"
"  [Contactor M]            3-pole 3-phase switching device\n"
"   |  |  |\n"
"  [Overload Relay]         senses motor current, trips on sustained overload\n"
"   |  |  |\n"
"  T1 T2 T3 -> Motor\n\n"
"CONTROL (120 VAC):\n"
"  H1 --- FU --- Stop PB (NC) --- Start PB (NO) --+--- OL aux (NC) --- M coil --- H2\n"
"                                                  |\n"
"                                M aux NO (13/14) -+  (seal-in)\n")},
        {"title":"Specifications & Parameters","body": table(
            ["Parameter","Typical Value","Notes"],
            [
                ["Starting current","500–800% FLA","About 6× FLA for 6 to 10 line cycles"],
                ["Starting torque","100–250% of rated","Design B around 150%"],
                ["Acceleration time","0.5–5 s","Depends on load inertia"],
                ["Max practical HP on stiff 480 V","≈ 15–25 HP","Confirm with utility / source impedance"],
                ["Control voltage","24 VDC or 120 VAC","Use a dedicated <a href=\"../02_Power_Distribution/Control Transformers.html\">control transformer</a>"],
                ["Contactor category","AC-3","Switching squirrel-cage motors"],
            ])},
        {"title":"Troubleshooting & Diagnostics","body": table(
            ["Symptom","Likely Cause","Diagnostic Step","Tools Needed"],
            [
                ["Motor doesn't start, contactor doesn't pick","No control voltage, Stop PB open, OL tripped","Check control voltage at M coil; inspect OL aux","DMM"],
                ["Contactor picks, motor does nothing","Missing phase, contactor power contacts welded/open","Measure voltage both sides of contactor with motor called","DMM"],
                ["Overload trips within seconds","Locked rotor, single-phasing, overload set too low","Check all 3 phases of motor current; compare to FLA","Clamp meter"],
                ["Contactor chatters","Weak coil voltage, worn magnet, low control supply","Measure coil voltage when energized","DMM"],
                ["Upstream breaker trips on start","DOL start too large for supply","Consider soft-starter or reduced-voltage method","Current logger"],
            ])},
        {"title":"Field Checklist","body": tasks([
            "Confirm overload is set to the nameplate FLA (not SF amps).",
            "Verify short-circuit protection size per NEC Table 430.52 (typically 175–250% FLA for ITB breakers).",
            "Check that contactor is rated AC-3 for motor duty.",
            "Seal-in wire must pick up from the contactor's own aux, not from the Start PB terminal.",
            "Stop PB must be wired NC so a broken wire = stop.",
            "Verify proper grounding of the motor frame and bonding of the enclosure.",
        ])},
        {"title":"Reference Notes","body": p(
            "DOL starters are covered by IEC 60947-4-1. Utilization categories AC-3 (motor starting) and AC-4 (plugging/jogging) describe the switching duty.",
            "If the plant has voltage flicker complaints when a big motor starts, move to a <a href=\"Soft Starters.html\">Soft Starter</a> or VFD before adding a reduced-voltage starter.")},
    ],
    "related": [
        ("Motor Contactors & Starters", "Motor Contactors &amp; Starters.html"),
        ("Overload Relays", "Overload Relays.html"),
        ("Start-Stop Logic", "../06_PLC_Programming_&_Logic/Start-Stop Logic.html"),
        ("Reversing Starters", "Reversing Starters.html"),
        ("Soft Starters", "Soft Starters.html"),
        ("Star-Delta Starters", "Star-Delta Starters.html"),
    ],
},

# ─────────────────────────────────────────────────────────────────────────────
"Motor Contactors & Starters.html": {
    "title": "Motor Contactors & Starters",
    "meta": {
        "category": "Motor Control Systems",
        "tags": ["#contactor","#starter","#coil","#auxcontact","#AC3"],
        "difficulty": "Beginner",
        "status": "final",
        "version": "1.0.0",
        "updated": "2026-04-13",
        "standards": "IEC 60947-4-1, NEMA ICS 2",
        "equipment": "Magnetic contactors, combination starters",
    },
    "sections": [
        {"title":"Description","body": p(
            "A contactor is an electromechanical switch sized and rated for motor loads. A 'starter' is a contactor plus an <a href=\"Overload Relays.html\">overload relay</a> bundled together to both switch and protect a motor. In practice the words are used interchangeably on a shop floor.")},
        {"title":"Core Concepts","body":
            "<h3>What is inside a contactor?</h3>" + ul([
                "An electromagnetic coil — 24 VDC, 24 VAC, 120 VAC, or 230 VAC.",
                "A moving armature that pulls three (or four) main power contacts closed when the coil is energized.",
                "Auxiliary contacts (NO and NC) used in the control circuit for seal-in and interlocking.",
                "Arc chutes that quench the arc as contacts open under load.",
            ]) +
            "<h3>IEC vs NEMA ratings</h3>" + p(
                "NEMA sizes are step-coded (00, 0, 1, 2, 3 …) and over-sized for general-purpose use. IEC contactors are rated by <strong>utilization category</strong> and <strong>nominal operating current (Ie)</strong> at a given voltage. An IEC 18-A contactor used at AC-3 and a NEMA Size 1 will switch about the same motor, but the IEC unit is smaller and assumes you size it closer to the load."
            ) +
            "<h3>Utilization categories</h3>" + table(
                ["Category","Typical Use"],
                [
                    ["AC-1","Resistive / non-inductive loads, PF ≥ 0.95"],
                    ["AC-3","Squirrel-cage motors, normal starting and stopping"],
                    ["AC-4","Plugging, jogging, reversing under load"],
                    ["AC-15","Control of AC electromagnets (relay coils)"],
                    ["DC-1 / DC-3 / DC-5","Resistive DC / shunt-motor / series-motor loads"],
                ])
        },
        {"title":"Sizing & Selection","body": table(
            ["Parameter","Selection Guidance"],
            [
                ["Main contact Ie (AC-3)","≥ motor FLA"],
                ["Coil voltage","Match to control transformer / PLC output relay"],
                ["Aux contacts","At least one NO (seal-in) and one NC (reserved for interlocks)"],
                ["Mechanical life","≥ 10× expected operations"],
                ["Electrical life (AC-3)","≥ 1 million operations for a well-sized contactor"],
                ["Coil pickup / drop-out","Pickup typically 85% of rated coil voltage; drop-out 40–60%"],
            ])},
        {"title":"Wiring & Diagrams","body": code(
"Typical IEC contactor terminal map:\n"
"  L1  L2  L3            (main power in)\n"
"  T1  T2  T3            (motor out)\n"
"  A1  A2                (coil)\n"
"  13/14  NO aux\n"
"  21/22  NC aux\n\n"
"Control wiring:\n"
"  Control source -> Start/Stop logic -> A1\n"
"  A2 -> control neutral / 0V\n"
"  Seal-in: 13/14 aux in parallel with Start PB\n")
        },
        {"title":"Troubleshooting & Diagnostics","body": table(
            ["Symptom","Likely Cause","Diagnostic Step","Tools Needed"],
            [
                ["Contactor chatters","Low coil voltage, dirty pole face, intermittent control contact","Measure coil voltage during chatter; look for contamination","DMM"],
                ["Coil burned out","Stuck armature, wrong coil voltage, surge from DC without flyback","Measure coil resistance; verify voltage matches coil","DMM"],
                ["Contacts welded","High inrush beyond AC-3 rating, repeated jogging","Replace contactor; re-evaluate size or utilization category","Visual, datasheet"],
                ["Aux contact not making","Worn contact tip, bent stab, wrong NO/NC selection","Ring out aux with contactor manually held","DMM continuity"],
                ["Motor runs with contactor de-energized","Welded main contacts","Lock out; test contact continuity with coil de-energized","DMM, LOTO"],
            ])},
        {"title":"Field Checklist","body": tasks([
            "Coil voltage matches control source within ±10%.",
            "Contactor rating (AC-3) ≥ motor FLA.",
            "One aux contact reserved for <a href=\"../06_PLC_Programming_&amp;_Logic/Alarms &amp; Fault Detection.html\">status feedback</a> to the PLC.",
            "Power and control wires torqued to manufacturer spec.",
            "Panel layout follows <a href=\"../10_System_Integration_&amp;_Commissioning/Control Panel Layout &amp; BOM.html\">panel layout best practices</a>.",
            "For DC coils, a flyback diode or RC snubber is installed.",
        ])},
    ],
    "related": [
        ("Direct-On-Line Starters", "Direct-On-Line Starters.html"),
        ("Overload Relays", "Overload Relays.html"),
        ("Relays & Interposing Relays", "../03_Control_Devices/Relays &amp; Interposing Relays.html"),
        ("Control Transformers", "../02_Power_Distribution/Control Transformers.html"),
        ("Reversing Starters", "Reversing Starters.html"),
    ],
},

# ─────────────────────────────────────────────────────────────────────────────
"Overload Relays.html": {
    "title": "Overload Relays",
    "meta": {
        "category": "Motor Control Systems",
        "tags": ["#overload","#thermal","#electronic","#classtrip","#motorprotection"],
        "difficulty": "Beginner",
        "status": "final",
        "version": "1.0.0",
        "updated": "2026-04-13",
        "standards": "NEC 430 Part III, IEC 60947-4-1",
        "equipment": "Bi-metallic, eutectic, electronic overload relays",
    },
    "sections": [
        {"title":"Description","body": p(
            "The overload relay protects the motor winding from prolonged operation at currents above full-load amps. It does <em>not</em> protect against short circuits — that's the job of the fuse or breaker upstream. Overloads respond to the heating effect of current over time, mimicking the thermal behavior of the motor itself.")},
        {"title":"Core Concepts","body":
            "<h3>Types</h3>" + ul([
                "<strong>Thermal bi-metallic</strong> — classic heater elements; two bi-metal strips bend as they heat and trip a lever. Rugged, cheap, moderately accurate.",
                "<strong>Eutectic (melting-alloy)</strong> — an older design that uses a solder pot. Largely replaced by bi-metallic and electronic.",
                "<strong>Electronic (solid-state)</strong> — current transformer-based; programmable trip class, phase loss, ground fault, jam, stall. More accurate and feature-rich.",
                "<strong>Thermistor (PTC)</strong> — winding-embedded sensors used with a relay monitor. Directly measures winding temperature rather than current.",
            ]) +
            "<h3>Trip Class</h3>" + table(
                ["Class","Trip time at 600% FLA","Typical Use"],
                [
                    ["Class 10","≤ 10 s","Hermetic / submersible / tight-coupled pumps, VFD output"],
                    ["Class 20","≤ 20 s","General-purpose — default in North America"],
                    ["Class 30","≤ 30 s","High-inertia loads — large fans, crushers"],
                    ["Class 5","≤ 5 s","Special-purpose, very tight thermal protection"],
                ]) +
            "<h3>Phase-loss protection</h3>" + p(
                "Most modern electronic overloads trip fast on single-phasing because unbalanced current heats the remaining phases dramatically. Older bi-metallic units may not trip fast enough — specify three-heater or phase-loss-sensitive types for critical motors."
            )
        },
        {"title":"Sizing & Setting","body": p(
            "The overload is set to the motor nameplate FLA — not the service-factor amps, not the feeder breaker size. NEC 430.32 requires overload pickup no higher than 115% of FLA for motors with SF ≤ 1.15, and 125% of FLA for motors with SF ≥ 1.15.",
            "Example: a 10 HP, 460 V motor with FLA = 13 A, SF = 1.15. Set overload FLA to 13 A. Allowed trip window is up to 125% × 13 = 16.25 A.")
        },
        {"title":"Wiring & Diagrams","body": code(
"Bi-metallic overload mounting (stacked under contactor):\n"
"  Contactor T1 T2 T3\n"
"        |  |  |\n"
"       Heaters (sized for FLA)\n"
"        |  |  |\n"
"   Motor T1 T2 T3\n\n"
"Overload auxiliary contacts:\n"
"  95/96 NC  -> wired in series with contactor coil (drops coil on trip)\n"
"  97/98 NO  -> to PLC input for fault signaling\n")
        },
        {"title":"Troubleshooting & Diagnostics","body": table(
            ["Symptom","Likely Cause","Diagnostic Step","Tools Needed"],
            [
                ["Nuisance trips on start","Class 10 used on high-inertia load","Change to Class 20 or 30","Datasheet"],
                ["Nuisance trips in hot weather","Ambient compensation not provided","Use ambient-compensated bi-metal or electronic","Thermometer"],
                ["Doesn't trip on single-phasing","Non-phase-loss-sensitive older unit","Upgrade to electronic or 3-heater type","Clamp meter"],
                ["Trips after a long run","Actual overload — undersized motor, bearing drag, coupling bind","Measure running amps vs. FLA","Clamp meter"],
                ["Trips exactly at stop","Overload sensing deceleration current","Check class; review duty cycle","Review logs"],
                ["Can't be reset","Auto-reset jumper set wrong, or electronic unit in lockout","Cycle power; check DIP switches","Manual"],
            ])},
        {"title":"Field Checklist","body": tasks([
            "FLA dial or parameter matches motor nameplate.",
            "Trip class is appropriate for the load (default Class 20).",
            "NC aux wired in series with contactor coil so trip drops the motor.",
            "NO aux wired to PLC input for alarm.",
            "Manual vs. auto reset is set per site standard (manual = safer).",
            "Electronic units: set phase loss, jam, stall, and ground fault per the application.",
        ])},
        {"title":"Reference Notes","body": p(
            "NEC Article 430 Part III details motor overload requirements including the 115%/125% rule.",
            "When a VFD is used, the motor overload function is typically handled inside the drive via the motor thermal model (I²t). A separate external overload is then only used if the drive is bypassed.")},
    ],
    "related": [
        ("Motor Contactors & Starters", "Motor Contactors &amp; Starters.html"),
        ("Direct-On-Line Starters", "Direct-On-Line Starters.html"),
        ("Motor Overheating & Tripping", "../09_Troubleshooting_&_Diagnostics/Motor Overheating &amp; Tripping.html"),
        ("Motor Nameplate Data", "Motor Nameplate Data.html"),
        ("NEC 430 – Motors & Controllers", "../11_Standards_and_Codes/NEC 430 – Motors &amp; Controllers.html"),
    ],
},

# ─────────────────────────────────────────────────────────────────────────────
"Reversing Starters.html": {
    "title": "Reversing Starters",
    "meta": {
        "category": "Motor Control Systems",
        "tags": ["#reversing","#interlock","#forwardreverse","#contactor"],
        "difficulty": "Beginner",
        "status": "final",
        "version": "1.0.0",
        "updated": "2026-04-13",
        "standards": "NEC 430, IEC 60947-4-1",
        "equipment": "Two interlocked contactors, overload relay",
    },
    "sections": [
        {"title":"Description","body": p(
            "A reversing starter swaps two of the three line leads going into the motor to flip the direction of the rotating magnetic field — and therefore the shaft rotation. It uses two contactors, one for each direction, mechanically and electrically <a href=\"../06_PLC_Programming_&amp;_Logic/Interlocking &amp; Permissives.html\">interlocked</a> so that only one can ever be closed at a time.")},
        {"title":"Core Concepts","body":
            "<h3>How to reverse a 3-phase motor</h3>" + p(
                "Swap any two of the three phase conductors between the supply and the motor. Conventionally, the 'reverse' contactor swaps L1 and L3."
            ) +
            "<h3>The interlock problem</h3>" + p(
                "If both contactors close at the same time, two line-to-line pairs short through the contactors. Result: a phase-to-phase fault, likely destruction of one or both contactors, and a likely trip of the upstream breaker."
            ) +
            "<h3>Three layers of interlock</h3>" + ol([
                "<strong>Mechanical interlock</strong> — a physical bar between the two contactors that prevents both armatures from pulling in at once. This is the only interlock you trust.",
                "<strong>Electrical (aux-contact) interlock</strong> — an NC aux contact from each contactor is wired in series with the <em>other</em> contactor's coil.",
                "<strong>Software interlock</strong> — the PLC's forward and reverse outputs are mutually exclusive. Good practice but not a substitute for the mechanical interlock.",
            ])
        },
        {"title":"Wiring & Diagrams","body": code(
"POWER:\n"
"  L1 L2 L3\n"
"   |  |  |\n"
"  [Fuses / MCP]\n"
"   |  |  |\n"
"   FWD contactor       REV contactor (L1<->L3 swapped)\n"
"   |  |  |              |  |  |\n"
"    \\ \\ \\               / / /\n"
"     \\ \\ \\__+__________/ / /\n"
"      \\ \\__|__+__________/ /\n"
"       \\___|__|__+_________/\n"
"           |  |  |\n"
"       [Overload]\n"
"           |  |  |\n"
"       Motor T1 T2 T3\n\n"
"CONTROL:\n"
"  Hot --- Stop --+-- Fwd PB -- Rev NC aux -- Fwd coil -- N\n"
"                 |\n"
"                 +-- Rev PB -- Fwd NC aux -- Rev coil -- N\n"
"  Add mechanical interlock hardware between the two contactors.\n")
        },
        {"title":"Considerations","body": ul([
                "<strong>Plug-stop (plugging)</strong>: reversing at full speed is AC-4 duty — use contactors rated for it or motor life suffers. Prefer a VFD or brake.",
                "Sequence interlocks prevent direction change until speed is near zero. A zero-speed switch or time delay is common.",
                "If the driven load can't accept reverse rotation (fans, pumps with check valves, some gearboxes), the control must mechanically prevent reverse by other means.",
                "For frequent reversing, use a <a href=\"Variable Frequency Drives (VFDs) Basics.html\">VFD</a> — much easier on mechanics and contacts.",
            ])
        },
        {"title":"Troubleshooting & Diagnostics","body": table(
            ["Symptom","Likely Cause","Diagnostic Step","Tools Needed"],
            [
                ["Fuses blow when pressing reverse","Mechanical interlock missing or failed","Lock out; inspect interlock lever","Visual, LOTO"],
                ["Both contactors chatter","Conflicting control signals","Check PLC ladder; verify NC aux wiring","PLC online, DMM"],
                ["Motor starts, does not reverse","Rev contactor coil not energizing","Measure coil voltage; inspect Rev aux NC","DMM"],
                ["Reverses rotation unexpectedly after maintenance","Leads swapped at motor during service","Re-verify rotation per <a href=\"Motor Wiring &amp; Rotation Checking.html\">rotation check procedure</a>","Phase-rotation meter"],
            ])},
        {"title":"Field Checklist","body": tasks([
            "Mechanical interlock present and operational.",
            "Both electrical interlock aux contacts wired NC in opposite coil circuits.",
            "Overload relay mounted downstream of both contactors, sized per motor FLA.",
            "Mechanical load verified to accept reverse rotation.",
            "If plugging is used, contactors rated AC-4.",
            "Plug-stop or direction-change delay programmed in PLC if applicable.",
        ])},
    ],
    "related": [
        ("Motor Contactors & Starters", "Motor Contactors &amp; Starters.html"),
        ("Interlocking & Permissives", "../06_PLC_Programming_&_Logic/Interlocking &amp; Permissives.html"),
        ("Variable Frequency Drives (VFDs) Basics", "Variable Frequency Drives (VFDs) Basics.html"),
        ("Motor Wiring & Rotation Checking", "Motor Wiring &amp; Rotation Checking.html"),
        ("Motor Braking Techniques", "Motor Braking Techniques.html"),
    ],
},

# ─────────────────────────────────────────────────────────────────────────────
"Star-Delta Starters.html": {
    "title": "Star-Delta Starters",
    "meta": {
        "category": "Motor Control Systems",
        "tags": ["#stardelta","#wyedelta","#reducedvoltage","#starter"],
        "difficulty": "Intermediate",
        "status": "final",
        "version": "1.0.0",
        "updated": "2026-04-13",
        "standards": "IEC 60947-4-1, NEC 430",
        "equipment": "Three contactors, timer, overload, 6-lead motor",
    },
    "sections": [
        {"title":"Description","body": p(
            "A star-delta (wye-delta) starter reduces inrush current on large motors by starting the motor in wye — where each winding sees 1/√3 of line voltage — and then transitioning to delta for normal running. It's an older, purely electromechanical reduced-voltage method, still common on pumps, fans, and compressors between roughly 15 HP and 200 HP.")},
        {"title":"Core Concepts","body":
            "<h3>Why star (wye) lowers inrush</h3>" + p(
                "In wye connection each phase winding sees line voltage divided by √3. Voltage per winding is ~58% of delta, so starting current drops to about 33% of a DOL start and starting torque drops to about 33% of full. The motor must have access to all six winding ends (a 6-lead motor)."
            ) +
            "<h3>The three contactors</h3>" + ul([
                "<strong>Main (M)</strong> — connects line to motor terminals U1, V1, W1.",
                "<strong>Star (S)</strong> — shorts motor terminals U2, V2, W2 together to form the neutral of the wye.",
                "<strong>Delta (D)</strong> — connects motor terminals U2, V2, W2 back to the other end of the windings (L3, L1, L2 in the classic cross-connection) to form the delta.",
            ]) +
            "<h3>Sequence of operation</h3>" + ol([
                "M + S energize together → motor runs in wye at reduced voltage.",
                "Timer (typically 5–15 s) counts.",
                "S drops out → brief open transition.",
                "D energizes → motor is in delta, full voltage.",
            ])
        },
        {"title":"Open vs. Closed Transition","body": p(
            "Open-transition star-delta opens all contactors briefly between star and delta — the motor coasts free for a few cycles and a current spike occurs on delta pickup. Closed-transition adds a transition resistor bank so the windings never fully disconnect; it is gentler on the motor and supply but costs more and is rarely used anymore. If you need a smoother profile, a <a href=\"Soft Starters.html\">soft starter</a> or VFD is the modern answer.")
        },
        {"title":"Wiring & Diagrams","body": code(
"Power (6-lead motor):\n"
"  L1 L2 L3\n"
"     \\ | /\n"
"     [M contactor]\n"
"      | | |\n"
"      U1 V1 W1  (motor winding 'starts')\n"
"      U2 V2 W2  (motor winding 'ends')\n"
"       \\ | /\n"
"       [S] --- shorts U2 V2 W2 together (wye point)\n"
"      or\n"
"       [D] --- cross-connects U2-L3, V2-L1, W2-L2 (delta)\n\n"
"Control sequence:\n"
"  Start  -> M + S energize\n"
"  Timer  -> drop S\n"
"          -> energize D after short dead-band\n"
"  Stop   -> M drops; D drops\n")
        },
        {"title":"Specifications & Parameters","body": table(
            ["Parameter","Value","Notes"],
            [
                ["Starting current","≈ 33% of DOL","About 200% FLA"],
                ["Starting torque","≈ 33% of full","Verify motor can accelerate load"],
                ["Transition time (open)","50–200 ms","Keep short to avoid large re-accel surge"],
                ["Transition timer","5–20 s","Tuned to driven-load acceleration time"],
                ["Motor connection","6-lead, designed for delta at line voltage","Cannot use a delta-only motor"],
                ["Overload location","Downstream of the contactors, sized for delta-run line current (≈ FLA / √3 if placed inside the winding loop)","Consult drawing"],
            ])},
        {"title":"Troubleshooting & Diagnostics","body": table(
            ["Symptom","Likely Cause","Diagnostic Step","Tools Needed"],
            [
                ["Big current spike at transition","Timer too long — motor slowed too much","Shorten transition timer","Stopwatch, clamp meter"],
                ["Won't transition to delta","Timer or D coil fault, S aux stuck closed","Check sequence on control wiring","DMM, ladder print"],
                ["Trips in wye","Overload mis-wired or set wrong; load too heavy for 33% torque","Verify overload position and setting","Datasheet"],
                ["Motor hums in star, never picks up","Motor load too high to accelerate at 33% torque","Move to soft-starter or VFD","Application review"],
            ])},
        {"title":"Field Checklist","body": tasks([
            "Motor is 6-lead, rated for delta at line voltage.",
            "Interlock aux contacts wired so S and D can never be on at once.",
            "Transition timer tuned to the actual load — not left at factory default.",
            "Overload sized and located correctly.",
            "Labeling of U1/V1/W1/U2/V2/W2 matches motor and drawing.",
            "Consider replacement with soft-starter or VFD for new installs.",
        ])},
    ],
    "related": [
        ("Direct-On-Line Starters", "Direct-On-Line Starters.html"),
        ("Soft Starters", "Soft Starters.html"),
        ("Variable Frequency Drives (VFDs) Basics", "Variable Frequency Drives (VFDs) Basics.html"),
        ("Motor Contactors & Starters", "Motor Contactors &amp; Starters.html"),
        ("3-Phase Motor Basics", "3-Phase Motor Basics.html"),
    ],
},

# ─────────────────────────────────────────────────────────────────────────────
"Soft Starters.html": {
    "title": "Soft Starters",
    "meta": {
        "category": "Motor Control Systems",
        "tags": ["#softstart","#SCR","#rampup","#reducedvoltage","#motors"],
        "difficulty": "Intermediate",
        "status": "final",
        "version": "1.0.0",
        "updated": "2026-04-13",
        "standards": "IEC 60947-4-2",
        "equipment": "SMC, SIRIUS 3RW, ATS, ASI solid-state starters",
    },
    "sections": [
        {"title":"Description","body": p(
            "A soft starter uses back-to-back SCRs (silicon-controlled rectifiers) in each phase to phase-angle-control the voltage applied to the motor during start and stop. It gives a smooth voltage ramp — and therefore a smooth current and torque ramp — without any of the rotating inertia of a VFD. After the motor reaches full speed, a bypass contactor typically closes to take the SCRs out of the conducting path and eliminate continuous switching losses.")},
        {"title":"Core Concepts","body":
            "<h3>Why choose a soft starter over a VFD</h3>" + ul([
                "You only need soft starting and stopping — you don't need speed control during run.",
                "Smaller, cheaper, simpler to commission than a drive.",
                "Lower harmonic impact at run (when bypassed) since the SCRs are out of circuit.",
                "Panel layout is simpler — no DC bus, no dv/dt filter, no cable length limits.",
            ]) +
            "<h3>Key adjustments</h3>" + table(
                ["Parameter","Purpose","Typical Range"],
                [
                    ["Initial voltage / torque","Voltage at t=0","20–40%"],
                    ["Ramp time (up)","Time to full voltage","5–30 s"],
                    ["Current limit","Cap on starting current","300–500% FLA"],
                    ["Ramp time (down)","Soft-stop","0–60 s"],
                    ["Kick start","Short pulse at t=0 to break sticky loads","0–1 s at 80–100%"],
                ]) +
            "<h3>Why a bypass contactor</h3>" + p(
                "At full speed the SCRs would otherwise run hot and make noise. A bypass contactor shorts them out once the motor is at speed, so in steady state the soft starter behaves like a simple contactor. When the motor is commanded to stop, the bypass opens and the SCRs take over to ramp down."
            )
        },
        {"title":"Selection","body": table(
            ["Factor","Guidance"],
            [
                ["Motor FLA","Match soft-starter current rating"],
                ["Duty class","Normal (AC-53a) or Heavy (AC-53b)"],
                ["Starts per hour","Derate aggressively; some units limit 10 starts/hr"],
                ["Bypass","Internal bypass preferred for smaller units; external bypass for large"],
                ["Inside-delta vs. in-line","Inside-delta connection can use 1/√3 current rating — saves money on large motors"],
                ["Control","Two-wire (run/stop) or three-wire (start/stop/fault)"],
                ["Communications","EtherNet/IP, Modbus, PROFINET on modern units"],
            ])},
        {"title":"Troubleshooting & Diagnostics","body": table(
            ["Symptom","Likely Cause","Diagnostic Step","Tools"],
            [
                ["Nuisance trip on start","Ramp time too short for load inertia","Increase ramp time; verify current limit","Soft starter display / software"],
                ["Motor growls / vibrates during ramp","Initial voltage too low","Increase initial voltage / add kick start","Display, vibration sense"],
                ["SCR short fault","Failed SCR (phase-to-phase conduction when off)","Measure resistance line-to-line with unit off","DMM"],
                ["Overheat after a few starts","Exceeded duty rating","Review starts/hour; add cooling or go bigger","Duty review"],
                ["Bypass not closing","Control wiring, stuck contactor","Ring out bypass contactor coil","DMM"],
            ])},
        {"title":"Field Checklist","body": tasks([
            "Soft starter FLA rating ≥ motor FLA.",
            "Initial voltage and ramp time tuned to the actual load.",
            "Bypass contactor operation confirmed at end of ramp.",
            "Fault contact wired to PLC input.",
            "Comms address and port set if used.",
            "Starts/hr within duty rating — otherwise derate.",
            "SCR heatsink ventilation clear; enclosure meets thermal budget — see <a href=\"../13_Specialty_Topics/Panel Cooling &amp; Power Conditioning.html\">Panel Cooling</a>.",
        ])},
    ],
    "related": [
        ("Variable Frequency Drives (VFDs) Basics", "Variable Frequency Drives (VFDs) Basics.html"),
        ("Star-Delta Starters", "Star-Delta Starters.html"),
        ("Direct-On-Line Starters", "Direct-On-Line Starters.html"),
        ("Motor Contactors & Starters", "Motor Contactors &amp; Starters.html"),
        ("Panel Cooling & Power Conditioning", "../13_Specialty_Topics/Panel Cooling &amp; Power Conditioning.html"),
    ],
},

# ─────────────────────────────────────────────────────────────────────────────
"Variable Frequency Drives (VFDs) Basics.html": {
    "title": "Variable Frequency Drives (VFDs) Basics",
    "meta": {
        "category": "Motor Control Systems",
        "tags": ["#VFD","#drive","#PWM","#inverter","#V/Hz","#vector"],
        "difficulty": "Intermediate",
        "status": "final",
        "version": "1.0.0",
        "updated": "2026-04-13",
        "standards": "IEC 61800-5-1 (safety), IEC 61800-3 (EMC)",
        "equipment": "PowerFlex, SINAMICS, ACS, Altivar, etc.",
    },
    "sections": [
        {"title":"Description","body": p(
            "A Variable Frequency Drive (VFD) is a power electronic converter that takes fixed-frequency AC line power, rectifies it to a DC bus, and then inverts it back to variable-frequency, variable-voltage AC to drive a motor at adjustable speed. It is the most flexible method of motor control — adjustable speed, soft start, torque control, energy savings on centrifugal loads, and built-in protection.")},
        {"title":"Core Concepts","body":
            "<h3>Architecture</h3>" + ol([
                "<strong>Rectifier</strong> — diode (or active) front-end that converts line AC to DC.",
                "<strong>DC bus</strong> — large electrolytic capacitors smoothing the rectified DC (typically ~680 V on a 480 V drive).",
                "<strong>IGBT inverter</strong> — six IGBTs arranged as a three-phase bridge, switched with PWM to synthesize variable-frequency AC.",
                "<strong>Control board</strong> — runs V/Hz, sensorless vector, or flux-vector control algorithms and all drive I/O.",
            ]) +
            "<h3>V/Hz and vector control</h3>" + ul([
                "<strong>V/Hz (scalar)</strong> — keeps a constant voltage-per-hertz ratio so flux stays constant. Simple, good enough for fans, pumps, conveyors.",
                "<strong>Sensorless vector</strong> — estimates rotor flux from current and voltage. Much better torque at low speed; no encoder needed.",
                "<strong>Closed-loop vector / flux vector</strong> — adds an <a href=\"../13_Specialty_Topics/Encoders &amp; Resolvers.html\">encoder</a> for precise torque and position. Use for servo-like performance.",
            ]) +
            "<h3>Why output frequency matters</h3>" + p(
                "Motor speed is proportional to frequency. Running below about 30 Hz with a TEFC motor overheats it because the shaft fan is turning too slowly to cool the frame — use an inverter-duty motor, a separately-powered blower, or derate the load."
            )
        },
        {"title":"Key Terms","body": table(
            ["Term","Meaning"],
            [
                ["Carrier frequency","PWM switching frequency, 2–16 kHz. Higher = quieter motor but more drive heat."],
                ["dv/dt","Rate of voltage change per unit time at the motor terminals. High dv/dt can stress motor insulation, especially with long cables."],
                ["Common-mode voltage","Voltage of motor neutral with respect to ground. Causes shaft currents — use grounded bearings or shaft brushes on large motors."],
                ["Regeneration","Motor feeding power back into the drive. Either absorbed by a dynamic brake resistor or a regenerative converter."],
                ["DB resistor","Dynamic braking resistor — dissipates regen energy as heat."],
                ["Skip frequencies","Bands where resonance occurs in the driven equipment; the drive avoids running at those frequencies."],
                ["Auto-tune","Routine where the drive measures motor parameters (Rs, Lσ, flux) and populates its model."],
            ])},
        {"title":"Application Patterns","body": ul([
                "<strong>Centrifugal pump / fan</strong> — V/Hz or sensorless vector is fine. Huge energy savings vs. throttling.",
                "<strong>Constant-torque conveyor</strong> — sensorless vector for decent low-speed torque.",
                "<strong>Positioning / spindle</strong> — closed-loop vector with encoder.",
                "<strong>Hoists / crane</strong> — use an encoder and a dedicated mechanical brake; the drive alone is not a holding brake.",
                "<strong>Multi-motor on one drive</strong> — only if motors are sized alike and the drive is derated; no individual overload protection.",
            ])
        },
        {"title":"Commissioning Outline","body": ol([
                "Verify incoming power phasing and voltage — see <a href=\"../02_Power_Distribution/Industrial Power Systems Overview.html\">power systems overview</a>.",
                "Inspect motor leads and ground — use VFD-rated cable with drain shield for long runs.",
                "Set motor nameplate parameters (voltage, FLA, RPM, kW/HP, Hz, poles).",
                "Run auto-tune with motor uncoupled if possible.",
                "Verify rotation at low speed before coupling.",
                "Commission speed reference source: keypad, analog, comms (EtherNet/IP, Modbus, PROFINET).",
                "Set stop mode (coast, ramp, DC inject), accel/decel, current limit, skip frequencies.",
                "See <a href=\"VFD Parameters &amp; Setup.html\">VFD Parameters &amp; Setup</a> for a detailed walk-through.",
            ])
        },
        {"title":"Troubleshooting & Diagnostics","body": "<p>See the dedicated page: <a href=\"../09_Troubleshooting_&amp;_Diagnostics/VFD Trips &amp; Fault Codes.html\">VFD Trips &amp; Fault Codes</a>.</p>"},
        {"title":"Field Checklist","body": tasks([
            "Motor nameplate entered in drive before any run command.",
            "Auto-tune run successfully on a cold motor.",
            "Rotation verified uncoupled at low speed.",
            "Accel, decel, and current-limit parameters set to the application.",
            "Fault relay wired to the PLC alarm input.",
            "EMC filter and proper shielded motor cable installed if required.",
            "Drive fault log cleared and a baseline run archived.",
        ])},
    ],
    "related": [
        ("VFD Parameters & Setup", "VFD Parameters &amp; Setup.html"),
        ("VFD Trips & Fault Codes", "../09_Troubleshooting_&_Diagnostics/VFD Trips &amp; Fault Codes.html"),
        ("Motor Nameplate Data", "Motor Nameplate Data.html"),
        ("Encoders & Resolvers", "../13_Specialty_Topics/Encoders &amp; Resolvers.html"),
        ("Motor Braking Techniques", "Motor Braking Techniques.html"),
        ("Panel Cooling & Power Conditioning", "../13_Specialty_Topics/Panel Cooling &amp; Power Conditioning.html"),
    ],
},

# ─────────────────────────────────────────────────────────────────────────────
"VFD Parameters & Setup.html": {
    "title": "VFD Parameters & Setup",
    "meta": {
        "category": "Motor Control Systems",
        "tags": ["#VFD","#parameters","#commissioning","#autotune"],
        "difficulty": "Intermediate",
        "status": "final",
        "version": "1.0.0",
        "updated": "2026-04-13",
        "standards": "Manufacturer-specific (PowerFlex, SINAMICS, ACS, Altivar)",
        "equipment": "Any modern VFD",
    },
    "sections": [
        {"title":"Description","body": p(
            "Every VFD behaves the same way at a conceptual level, even though every manufacturer names their parameters differently. This page walks through the parameter groups you'll touch during commissioning regardless of whether the drive is a PowerFlex 525, a SINAMICS G120, or an ACS580. Parameter numbers are manufacturer-specific; behaviors are universal.")},
        {"title":"Parameter Groups","body":
            "<h3>1. Motor nameplate</h3>" + p(
                "The first group you enter. These parameters populate the drive's motor model. Enter them before running auto-tune."
            ) + table(
                ["Parameter (generic)","Meaning","Source"],
                [
                    ["Motor voltage","Rated line voltage","Nameplate"],
                    ["Motor FLA","Rated full-load amps","Nameplate"],
                    ["Motor HP or kW","Rated mechanical output","Nameplate"],
                    ["Motor RPM","Rated full-load speed","Nameplate"],
                    ["Motor frequency","Rated frequency","Nameplate"],
                    ["Motor poles","(Sometimes derived from RPM)","Derived"],
                ]) +
            "<h3>2. Speed reference</h3>" + ul([
                "Keypad / HIM.",
                "Analog input 1 or 2 (4–20 mA, 0–10 V).",
                "Preset speeds selected by discrete inputs.",
                "Communications (EtherNet/IP, PROFINET, Modbus).",
            ]) +
            "<h3>3. Accel / Decel</h3>" + p(
                "Accel = time from 0 to base speed. Decel = time from base to 0. On regenerative loads, decel too fast will trip a DC bus over-voltage fault — add a dynamic-brake resistor or lengthen decel."
            ) +
            "<h3>4. Stop mode</h3>" + ul([
                "<strong>Ramp to stop</strong> — default; follows decel time.",
                "<strong>Coast to stop</strong> — drive inhibits output; motor free-wheels.",
                "<strong>DC injection</strong> — DC applied to the stator after decel to hold the motor at zero.",
                "<strong>Flux braking</strong> — drive increases flux to dissipate energy in motor instead of bus.",
            ]) +
            "<h3>5. Control mode</h3>" + ul([
                "V/Hz — simple loads.",
                "Sensorless vector — most general-purpose applications.",
                "Flux vector with encoder — precise torque / positioning.",
            ]) +
            "<h3>6. Protection / limits</h3>" + ul([
                "Current limit (typically 150% FLA).",
                "Overload class (typically IEC class 10 or 20).",
                "Min / max frequency.",
                "Skip frequencies for resonance.",
                "Thermistor / PTC input for winding temperature.",
            ]) +
            "<h3>7. I/O assignments</h3>" + p(
                "Map digital inputs to functions (Start, Stop, Reverse, Jog, Fault Reset). Map relay outputs to status (Running, Faulted, At-Speed). Map analog inputs to speed reference or torque reference."
            ) +
            "<h3>8. Communications</h3>" + p(
                "Set the comm module's IP / node address, rate, and fault behavior. Most drives have parameters for 'what to do on network loss' — fault, coast, maintain speed. Critical to set per application."
            )
        },
        {"title":"Auto-Tune","body": p(
            "Auto-tune measures motor parameters the nameplate doesn't give you (stator resistance, leakage inductance, magnetizing current) and populates the drive's motor model. Two common modes:",
            "<strong>Static auto-tune</strong> — motor does not rotate. Captures Rs and Lσ. Safe for coupled loads.",
            "<strong>Rotational auto-tune</strong> — motor spins briefly. Captures flux and no-load current. Most accurate. Uncouple from the load if possible.")
        },
        {"title":"Commissioning Sequence","body": ol([
                "Power up drive; verify firmware and I/O board revision.",
                "Factory-default the drive before starting (if you're inheriting settings, back them up first).",
                "Enter all motor nameplate parameters.",
                "Set control source and speed reference.",
                "Run static auto-tune, then rotational if possible.",
                "Set accel / decel, current limit, stop mode.",
                "Jog at low speed uncoupled, confirm rotation.",
                "Couple load, run at 25%, 50%, 75%, 100% speed. Log current, bus voltage, motor temp.",
                "Archive parameter set to removable media (SD card / drive-config file).",
                "Document final setup in commissioning report — see <a href=\"../10_System_Integration_&amp;_Commissioning/Commissioning Reports &amp; Sign-off.html\">Commissioning Reports</a>.",
            ])
        },
        {"title":"Field Checklist","body": tasks([
            "Motor nameplate entered accurately.",
            "Auto-tune ran without fault.",
            "Accel/decel matches load — no bus over-volt or current-limit trips.",
            "Skip frequencies set if driven equipment has resonance bands.",
            "Network loss behavior set (fault vs. coast vs. hold).",
            "Parameter backup saved and filed.",
            "Overload class and motor thermal inputs configured.",
        ])},
    ],
    "related": [
        ("Variable Frequency Drives (VFDs) Basics", "Variable Frequency Drives (VFDs) Basics.html"),
        ("VFD Trips & Fault Codes", "../09_Troubleshooting_&_Diagnostics/VFD Trips &amp; Fault Codes.html"),
        ("Commissioning Reports & Sign-off", "../10_System_Integration_&_Commissioning/Commissioning Reports &amp; Sign-off.html"),
        ("Motor Nameplate Data", "Motor Nameplate Data.html"),
        ("PLC-HMI-VFD Integration", "../10_System_Integration_&_Commissioning/PLC-HMI-VFD Integration.html"),
    ],
},

# ─────────────────────────────────────────────────────────────────────────────
"Motor Braking Techniques.html": {
    "title": "Motor Braking Techniques",
    "meta": {
        "category": "Motor Control Systems",
        "tags": ["#braking","#DCinject","#plugging","#regenerative","#dynamicbrake"],
        "difficulty": "Intermediate",
        "status": "final",
        "version": "1.0.0",
        "updated": "2026-04-13",
        "standards": "IEC 60204-1, IEC 61800-5-2",
        "equipment": "Mechanical brakes, DB resistors, regen units",
    },
    "sections": [
        {"title":"Description","body": p(
            "When a motor is commanded to stop, it has two things working against quick stopping: its own rotor inertia and the inertia of the driven load. You either let it coast, dissipate that energy, or put it back onto the supply. Choosing a braking method matters when you need short stop time, accurate positioning, or reliable emergency stopping.")},
        {"title":"Methods","body":
            "<h3>1. Coast-to-stop</h3>" + p(
                "Open the contactor or disable the drive. Motor free-wheels until friction stops it. Easiest, cheapest, slowest. Not acceptable for <a href=\"../12_Safety_Systems_Advanced/Emergency Stops (E-Stops).html\">emergency stops</a> on most machines."
            ) +
            "<h3>2. Mechanical brake</h3>" + p(
                "A spring-applied, electrically-released friction brake on the motor shaft or gearbox. Engages when de-energized — fail-safe. Required for hoists, cranes, and vertical axes. Maintenance item — pads wear."
            ) +
            "<h3>3. DC injection braking</h3>" + p(
                "After removing AC, a DC voltage is applied to two of the stator phases. The resulting stationary field creates eddy-current torque in the rotor, braking it. Usually handled by the VFD; standalone DC-injection units exist for across-the-line starters. Effective but drops off sharply near zero speed — finish with a mechanical brake for a true hold."
            ) +
            "<h3>4. Dynamic braking (VFD)</h3>" + p(
                "The drive's inverter dumps regenerated energy into a dynamic-brake resistor connected across the DC bus. The most common VFD stop method for high-inertia loads. Sized by duty cycle and stopping energy."
            ) +
            "<h3>5. Regenerative braking</h3>" + p(
                "Instead of a resistor, an active front-end feeds regen energy back onto the line. Expensive but efficient, and required for continuous regen applications (downhill conveyors, test stands, cranes)."
            ) +
            "<h3>6. Plugging</h3>" + p(
                "Reverse two line leads while the motor is spinning. Produces very high braking torque but extreme currents — hard on the motor and contactors. AC-4 duty. Largely replaced by DC injection or VFD braking, but still seen on some old machinery."
            )
        },
        {"title":"Selection Matrix","body": table(
            ["Load / Use","Best Method"],
            [
                ["Small conveyor, no urgency","Coast"],
                ["Frequent start/stop, moderate inertia","VFD dynamic braking"],
                ["Positioning / indexing","Vector VFD + mechanical brake"],
                ["Hoist, crane, vertical axis","Mechanical brake + VFD with encoder"],
                ["Downhill conveyor / regen load","Regenerative drive"],
                ["E-stop stop-category 0","Coast (contactor drop) with mechanical brake"],
                ["E-stop stop-category 1","Controlled stop then power removal — VFD ramp + SS1 safety function"],
            ])},
        {"title":"Stop Categories (IEC 60204-1)","body": table(
            ["Category","Description"],
            [
                ["0","Immediate removal of power to actuators — coast"],
                ["1","Controlled stop with power still available, then removal of power at a stop (typical for VFDs with Safe Stop 1)"],
                ["2","Controlled stop with power kept to the motor (rare as E-stop; used as functional stop)"],
            ])},
        {"title":"Troubleshooting & Diagnostics","body": table(
            ["Symptom","Likely Cause","Step"],
            [
                ["DB resistor overheats","Under-sized resistor for duty","Recalculate stopping energy and duty cycle"],
                ["DC bus over-volt trip on stop","Decel too fast, no DB resistor, failed chopper","Lengthen decel or install DB"],
                ["Motor won't stop on E-stop","Coast not achieving safe state; brake not dropping","Review stop category; verify brake release wiring"],
                ["Plugging contactor welds","AC-3 rating used for AC-4 duty","Upsize or change to VFD"],
            ])},
        {"title":"Field Checklist","body": tasks([
            "Stop category selected matches the risk assessment.",
            "Mechanical brake installed on all vertical or hoisting applications.",
            "VFD braking resistor sized for worst-case duty and cooled.",
            "E-stop path tested end-to-end.",
            "DC injection current and time set to avoid motor overheating.",
        ])},
    ],
    "related": [
        ("Variable Frequency Drives (VFDs) Basics", "Variable Frequency Drives (VFDs) Basics.html"),
        ("Emergency Stops (E-Stops)", "../12_Safety_Systems_Advanced/Emergency Stops (E-Stops).html"),
        ("Risk Assessments & Functional Safety", "../12_Safety_Systems_Advanced/Risk Assessments &amp; Functional Safety.html"),
        ("Reversing Starters", "Reversing Starters.html"),
        ("Motor Nameplate Data", "Motor Nameplate Data.html"),
    ],
},

# ─────────────────────────────────────────────────────────────────────────────
"Motor Megger Testing.html": {
    "title": "Motor Megger Testing",
    "meta": {
        "category": "Motor Control Systems",
        "tags": ["#megger","#insulation","#motortesting","#IR","#PI"],
        "difficulty": "Intermediate",
        "status": "final",
        "version": "1.0.0",
        "updated": "2026-04-13",
        "standards": "IEEE 43, IEEE 95, NETA ATS",
        "equipment": "Megohmmeter (500 V, 1000 V, 2500 V), LOTO",
    },
    "sections": [
        {"title":"Description","body": p(
            "Megger testing (insulation resistance testing) measures the insulation integrity of a motor by applying a high DC voltage between the windings and ground and measuring the tiny leakage current that flows. The reading, in megohms, tells you whether the insulation system can still stand off line voltage safely. It's one of the fastest ways to screen a motor after a trip, water event, storage, or fault.")},
        {"title":"Core Concepts","body":
            "<h3>Test voltages</h3>" + table(
                ["Motor Rated Voltage","Megger Voltage"],
                [
                    ["≤ 250 V","500 V"],
                    ["251–600 V","500 V or 1000 V"],
                    ["601–2400 V","1000 V or 2500 V"],
                    ["> 2400 V","2500 V or 5000 V"],
                ]) +
            "<h3>What the reading means</h3>" + table(
                ["Reading (at 40 °C)","Condition","Action"],
                [
                    ["< 2 MΩ","Dangerous","Do not energize. Dry / inspect / replace."],
                    ["2–20 MΩ","Marginal","Investigate — moisture, contamination?"],
                    ["20–500 MΩ","Acceptable","OK for service."],
                    ["> 500 MΩ","Good","Normal for a dry modern motor."],
                    ["> 5 GΩ","Excellent","Often the ceiling of small meters."],
                ]) +
            "<h3>Temperature correction</h3>" + p(
                "IR roughly halves for every 10 °C rise. Always note the winding temperature when you took the reading. IEEE 43 gives correction factors — or trend at a fixed temperature."
            ) +
            "<h3>Polarization Index (PI)</h3>" + p(
                "PI = IR at 10 min / IR at 1 min. Good insulation absorbs and polarizes — IR rises over time. A PI ≥ 2.0 is good. PI < 1.0 suggests wet or contaminated insulation. PI testing is less diagnostic on modern Class F systems with high base IR; use it for older or high-voltage machines."
            )
        },
        {"title":"Procedure","body": ol([
                "<strong>Isolate and LOTO</strong> — open feeder breaker or disconnect, apply lock and tag. See <a href=\"../01_Electrical_Fundamentals/Lockout Tagout (LOTO) Procedures.html\">LOTO procedures</a>.",
                "Disconnect motor leads from the starter, VFD, or junction box — never megger through a drive.",
                "Short together all three motor leads (T1, T2, T3) in the peckerhead.",
                "Connect megger between shorted leads and motor frame ground.",
                "Apply rated test voltage for 1 minute.",
                "Record the 1-minute reading. If doing PI, continue for 10 minutes.",
                "Discharge the winding to ground for at least 4× the test time.",
                "Remove leads, restore connections, and test again in the installed configuration if needed.",
                "Record temperature, test voltage, and leads tested.",
            ])
        },
        {"title":"Safety","body": ul([
                "Meggers deliver lethal voltage — up to 5 kV DC on larger units. Never test with anyone touching the motor.",
                "Always discharge the winding with the meter's discharge function before disconnecting.",
                "Electronic components inside the drive, surge suppressors, or thermistors can be damaged by a megger — disconnect them.",
                "Tag the motor with the test result and date so the next person has a baseline.",
            ])
        },
        {"title":"Troubleshooting & Diagnostics","body": table(
            ["Symptom","Likely Cause","Next Step"],
            [
                ["IR < 1 MΩ on new motor","Water or transit damage","Dry the motor (heat + ventilation) and retest"],
                ["Low IR only on one phase","Phase-to-ground fault in one winding","Rewind required"],
                ["Intermittent trips, normal IR cold","Hot-IR degradation","Repeat test at operating temperature"],
                ["Low IR after wash-down","Moisture in cable or peckerhead","Disassemble, dry, reseal"],
                ["PI < 1.0","Wet / contaminated insulation","Dry out, retest, consider dip and bake"],
            ])},
        {"title":"Field Checklist","body": tasks([
            "LOTO applied and verified zero voltage before test.",
            "Motor leads disconnected from any electronics (drive, starter, surge caps).",
            "Correct test voltage selected for motor voltage class.",
            "1-minute reading recorded with winding temperature.",
            "Test results tagged on motor and filed in maintenance log.",
            "Winding fully discharged before re-terminating.",
        ])},
    ],
    "related": [
        ("Motor Nameplate Data", "Motor Nameplate Data.html"),
        ("Tools of the Trade - Megger", "../01_Electrical_Fundamentals/Tools of the Trade-Megger or Insulation Tester.html"),
        ("Lockout Tagout (LOTO) Procedures", "../01_Electrical_Fundamentals/Lockout Tagout (LOTO) Procedures.html"),
        ("Motor Overheating & Tripping", "../09_Troubleshooting_&_Diagnostics/Motor Overheating &amp; Tripping.html"),
        ("3-Phase Motor Basics", "3-Phase Motor Basics.html"),
    ],
},

# ─────────────────────────────────────────────────────────────────────────────
"Motor Wiring & Rotation Checking.html": {
    "title": "Motor Wiring & Rotation Checking",
    "meta": {
        "category": "Motor Control Systems",
        "tags": ["#wiring","#rotation","#phaseorder","#bumptest","#coupling"],
        "difficulty": "Beginner",
        "status": "final",
        "version": "1.0.0",
        "updated": "2026-04-13",
        "standards": "IEEE 112, NEC 430",
        "equipment": "Phase-rotation meter, non-contact strobe or tachometer",
    },
    "sections": [
        {"title":"Description","body": p(
            "Every three-phase motor has two possible rotation directions. Which one you get depends on the phase sequence of the three supply conductors. The cost of running a pump backwards for even a few seconds can be a cracked impeller or a flooded seal — the cost of running a compressor backwards is usually an immediate cascade of damage. Verifying rotation before coupling to a load is non-negotiable on new installs.")},
        {"title":"Wiring Configurations","body":
            "<h3>3-lead motors</h3>" + p(
                "Single connection only — match T1 to L1, T2 to L2, T3 to L3. Swap any two leads to reverse."
            ) +
            "<h3>6-lead motors</h3>" + p(
                "Designed for wye / delta or dual-voltage operation. Six leads: U1/U2, V1/V2, W1/W2. Follow the nameplate diagram. Common for <a href=\"Star-Delta Starters.html\">star-delta</a> starters."
            ) +
            "<h3>9-lead motors (dual voltage)</h3>" + p(
                "Most common North American industrial motor. Low voltage = parallel wye; high voltage = series wye. Leads 1–9 per NEMA numbering. See the peckerhead diagram. Wiring the motor for 230 V on a 460 V supply burns out the winding in seconds."
            ) +
            "<h3>12-lead motors</h3>" + p(
                "Used for dual-voltage with both wye and delta options, or for <a href=\"Soft Starters.html\">soft-starter</a> inside-delta connections."
            )
        },
        {"title":"How to Check Rotation","body":
            "<h3>Method 1 — Phase rotation meter</h3>" + ol([
                "Connect the meter's three leads to L1, L2, L3 at the motor disconnect.",
                "Energize briefly — the meter shows ABC or ACB sequence.",
                "If ABC, the motor will turn in its 'standard' direction (clockwise viewed from shaft end for most North American motors).",
                "If ACB, swap any two line leads to correct.",
            ]) +
            "<h3>Method 2 — Bump test</h3>" + ol([
                "Uncouple the motor from the load, or verify the load can accept either direction.",
                "Tag the motor shaft with a mark.",
                "Give a quick jog — a few cycles only.",
                "Observe the rotation direction.",
                "Swap two motor leads if needed and re-test.",
            ]) +
            "<h3>Method 3 — VFD direction</h3>" + p(
                "On VFD-driven motors, rotation can be flipped in software (direction parameter or motor-phase-order parameter). Still jog and verify visually the first time. Never rely only on the parameter for a brand-new install; confirm physical rotation."
            )
        },
        {"title":"Arrow / Direction Conventions","body": p(
            "Most motors have a directional arrow on the frame showing the correct rotation. For pumps and fans, the arrow is usually on the driven equipment — follow that, not the motor, when they disagree.",
            "Pump rotation: almost always specified by pump manufacturer on the casing. Centrifugal pumps will move fluid backwards at reduced flow when run reversed — it's subtle enough to be missed.",
            "Fan rotation: airflow direction is easy to miss with reversed rotation because the blades still push <em>some</em> air in the wrong direction.")
        },
        {"title":"Troubleshooting & Diagnostics","body": table(
            ["Symptom","Likely Cause","Diagnostic Step"],
            [
                ["Motor runs reverse after replacement","Leads not documented before removal","Swap any two line leads"],
                ["Intermittent low output from pump","Reversed rotation","Check with phase rotation meter"],
                ["New system, large air handler low flow","Fan reversed","Visual check against fan arrow"],
                ["Motor hums and trips","Single-phasing (one lead open, not reversed)","Measure all three line voltages"],
            ])},
        {"title":"Field Checklist","body": tasks([
            "Nameplate connection diagram matches actual lead wiring.",
            "Motor leads torqued to spec, strain relief installed at the peckerhead.",
            "Ground lug torqued and bonded to the motor frame.",
            "Rotation verified by bump test or phase meter.",
            "Direction arrow on motor or driven equipment matches observed rotation.",
            "Lead positions documented for future reference.",
        ])},
    ],
    "related": [
        ("3-Phase Motor Basics", "3-Phase Motor Basics.html"),
        ("Motor Nameplate Data", "Motor Nameplate Data.html"),
        ("Reversing Starters", "Reversing Starters.html"),
        ("Star-Delta Starters", "Star-Delta Starters.html"),
        ("Motor Megger Testing", "Motor Megger Testing.html"),
        ("Panel Wiring Best Practices", "../02_Power_Distribution/Panel Wiring Best Practices.html"),
    ],
},

}

CONTENT = {FOLDER: PAGES}
