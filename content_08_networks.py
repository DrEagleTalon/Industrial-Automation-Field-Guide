"""Content for 08_Industrial_Networks_&_Protocols."""

FOLDER = "08_Industrial_Networks_&_Protocols"

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

"Industrial Ethernet vs IT Ethernet.html":{
    "title":"Industrial Ethernet vs IT Ethernet",
    "meta":{"category":"Industrial Networks & Protocols","tags":["#Ethernet","#IT","#OT","#industrial","#determinism"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"IEEE 802.3, IEC 61784"},
    "sections":[
        {"title":"Description","body": p(
            "Industrial Ethernet and office Ethernet share the same physical layer but are deployed very differently. Control networks need deterministic timing, tolerate harsh environments, and can't be patched on Tuesday morning while the line is running.")},
        {"title":"Differences","body": table(
            ["Aspect","IT Ethernet","Industrial Ethernet"],
            [
                ["Physical environment","Office (20 °C, clean)","Plant (-20 to 60 °C, vibration, dust, moisture)"],
                ["Cable","UTP Cat 5e/6 indoor","Shielded, oil-resistant, rated for conduit and drag-chain"],
                ["Connectors","RJ45","RJ45 with IP67 hood, M12 D-coded, Harting"],
                ["Switches","Managed, rack-mount","Fanless, DIN-rail, -40 to +70 °C, redundant power"],
                ["Topology","Star","Star, ring (DLR, PRP/HSR), line"],
                ["Latency determinism","Best-effort","Bounded (< 1 ms for Profinet IRT, EtherCAT)"],
                ["Protocols","HTTP, SMB, DNS","EtherNet/IP, PROFINET, EtherCAT, Modbus TCP"],
                ["Change control","Frequent","Infrequent, tightly managed"],
                ["Security focus","Confidentiality","Availability first, integrity, then confidentiality"],
                ["Patch cycles","Weekly / monthly","Annual outage windows"],
            ])},
        {"title":"Purdue Model / ISA-95","body": p(
            "The standard reference for segmenting IT and OT networks: Level 0 (field devices) up through Level 5 (enterprise). Firewalls separate OT (0–3) from IT (4–5) with a DMZ in between. It's the pattern every industrial IT group ends up recreating whether or not they've read the document."
        )},
        {"title":"Common OT/IT Conflicts","body": ul([
                "IT deploys a switch firmware update — multicast config changes, EtherNet/IP I/O drops.",
                "IT enables DHCP on a port connected to a PLC that needs a static IP — line stops.",
                "IT installs anti-virus on a SCADA server — historian misses samples during scans.",
                "IT network scanner probes a PLC — PLC faults out because it wasn't designed to handle arbitrary packets.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "OT network physically and logically separated from IT by a firewall + DMZ.",
            "No DHCP on the control network.",
            "Documented change-control for any firmware, config, or VLAN change.",
            "Managed switches with monitoring (SNMP) and port security.",
            "Industrial-rated cable and connectors on anything exposed to the plant floor.",
        ])},
    ],
    "related":[
        ("Common Protocols","Common Protocols.html"),
        ("IP Addressing & Subnetting","IP Addressing &amp; Subnetting.html"),
        ("Switches & Managed Networks","Switches &amp; Managed Networks.html"),
        ("Remote Access & VPN","../13_Specialty_Topics/Remote Access &amp; VPN.html"),
    ],
},

"IP Addressing & Subnetting.html":{
    "title":"IP Addressing & Subnetting",
    "meta":{"category":"Industrial Networks & Protocols","tags":["#IP","#subnet","#gateway","#DHCP","#static"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "Every industrial Ethernet device needs a unique IP address, subnet mask, and (sometimes) a default gateway. Mis-configure one and the whole network can break in subtle ways.")},
        {"title":"The Basics","body": ul([
                "IPv4 address: four octets (e.g., 192.168.1.10).",
                "Subnet mask defines how much of the address is the network vs. host portion.",
                "Devices on the <em>same subnet</em> talk directly. Cross-subnet traffic goes through the gateway.",
                "Private ranges for industrial use: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16. Avoid public ranges.",
            ])},
        {"title":"CIDR / Mask Cheat Sheet","body": table(
            ["Mask","CIDR","Hosts","Typical Use"],
            [
                ["255.255.255.0","/24","254","Small machine network, one cell"],
                ["255.255.254.0","/23","510","Larger cell"],
                ["255.255.252.0","/22","1,022","Plant area"],
                ["255.255.248.0","/21","2,046",""],
                ["255.255.0.0","/16","65,534","Old Class-B; usually too big"],
                ["255.255.255.128","/25","126","Split subnet"],
                ["255.255.255.192","/26","62","Split subnet"],
            ])},
        {"title":"Addressing Plan","body": p(
            "Pick a scheme and document it. A typical plant plan looks like:"
        ) + code(
"10.10.0.0/16    Control network - entire plant\n"
" 10.10.1.0/24   Area 1 - PLCs, drives, HMIs\n"
"    10.10.1.10   Area 1 PLC\n"
"    10.10.1.11   Area 1 HMI\n"
"    10.10.1.20-99  Area 1 drives\n"
"    10.10.1.100-200 Area 1 remote I/O\n"
" 10.10.2.0/24   Area 2 ...\n"
" 10.10.200.0/24  Shared - SCADA servers, historians, switches\n"
"\n"
"Gateway (if required):\n"
" 10.10.1.1  Area 1 VLAN gateway (on the managed core switch)\n")},
        {"title":"DHCP vs Static","body": ul([
                "<strong>Static</strong> for PLCs, drives, HMIs, servers, and any device that is called by IP.",
                "<strong>DHCP reservation</strong> acceptable when every device's MAC is bound to a specific IP on the DHCP server.",
                "<strong>Random DHCP</strong> fine only for engineer laptops and transient tools.",
            ])},
        {"title":"Common Mistakes","body": ul([
                "Two devices with the same IP — both will fight and intermittently drop.",
                "Wrong mask — devices see each other but can't talk because they assume a gateway hop.",
                "Gateway missing on PLC that needs to talk across subnets — never connects to SCADA.",
                "Using 169.254.x.x (APIPA) — means DHCP failed silently.",
                "Placing production PLCs directly on the corporate IT subnet.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Plan documented and kept current.",
            "Static addresses on all permanent devices.",
            "No duplicate IPs (arp-scan the subnet at commissioning).",
            "Default gateway set on devices that need it (and only those).",
            "VLANs and inter-VLAN routing documented on the switch config.",
        ])},
    ],
    "related":[
        ("Common Protocols","Common Protocols.html"),
        ("Industrial Ethernet vs IT Ethernet","Industrial Ethernet vs IT Ethernet.html"),
        ("Network Troubleshooting (Ping, ARP, etc)","Network Troubleshooting (Ping, ARP, etc).html"),
        ("Switches & Managed Networks","Switches &amp; Managed Networks.html"),
    ],
},

"Common Protocols.html":{
    "title":"Common Protocols",
    "meta":{"category":"Industrial Networks & Protocols","tags":["#EthernetIP","#Profinet","#Modbus","#DeviceNet","#CIP"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13",
            "standards":"IEC 61784, ODVA, PI"},
    "sections":[
        {"title":"Description","body": p(
            "Industrial protocols fall into two buckets: fieldbus (serial, deterministic, limited distance) and Ethernet-based (high bandwidth, flexible, widely adopted). Most plants today mix several.")},
        {"title":"Ethernet-Based","body": table(
            ["Protocol","Owner","Typical Use","Notes"],
            [
                ["EtherNet/IP","ODVA / Rockwell","Dominant in North America","CIP over UDP (implicit) / TCP (explicit). DLR for ring topology."],
                ["PROFINET","PI / Siemens","Dominant in Europe","IRT for deterministic motion; RT for I/O."],
                ["EtherCAT","ETG / Beckhoff","Motion, fast I/O","Distributed clocks, sub-microsecond sync."],
                ["Modbus TCP","Open","Interop between any devices","Simple; not deterministic."],
                ["OPC UA","OPC Foundation","SCADA/MES, IT/OT","Secure, vendor-neutral, object-oriented."],
                ["MQTT / Sparkplug","OASIS / Eclipse","IIoT, cloud","Publish-subscribe, unified namespace."],
                ["CC-Link IE","CLPA / Mitsubishi","Asia","Ring and star; motion."],
                ["POWERLINK","EPSG","Industrial Ethernet","Deterministic."],
            ])},
        {"title":"Fieldbus / Serial","body": table(
            ["Protocol","Physical","Speed","Typical Use"],
            [
                ["Modbus RTU","RS-485","9.6–115.2 kbps","Meters, VFDs, instruments"],
                ["PROFIBUS DP","RS-485","up to 12 Mbps","Legacy Siemens field I/O"],
                ["DeviceNet","CAN","125/250/500 kbps","Rockwell legacy device network"],
                ["CANopen","CAN","125 kbps–1 Mbps","Mobile equipment, marine"],
                ["AS-i","Flat yellow cable","167 kbps","Low-end I/O networking (sensors, valves)"],
                ["HART","4–20 mA","1200 bps overlay","Smart instruments on existing loops"],
                ["IO-Link","Point-to-point","4.8/38.4/230 kbps","Smart sensors, device-level config; see <a href=\"../13_Specialty_Topics/IO-Link Devices.html\">IO-Link</a>"],
            ])},
        {"title":"Picking a Protocol","body": ul([
                "What PLC family are you on? Pick the native fieldbus (EtherNet/IP for Rockwell, PROFINET for Siemens).",
                "Is motion involved? EtherCAT or PROFINET IRT.",
                "Are third-party devices involved? Modbus TCP or OPC UA for interop.",
                "Is distance / cable mass a constraint? IO-Link at the device, Ethernet at the cabinet.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Protocol selection matches the dominant PLC brand.",
            "Topology (star / ring / line) and media redundancy documented.",
            "Each device's protocol role (controller / adapter / scanner) listed.",
            "Firmware versions for each end of every protocol recorded.",
        ])},
    ],
    "related":[
        ("IP Addressing & Subnetting","IP Addressing &amp; Subnetting.html"),
        ("Industrial Ethernet vs IT Ethernet","Industrial Ethernet vs IT Ethernet.html"),
        ("Switches & Managed Networks","Switches &amp; Managed Networks.html"),
        ("IO-Link Devices","../13_Specialty_Topics/IO-Link Devices.html"),
        ("Cloud SCADA & MQTT","../13_Specialty_Topics/Cloud SCADA &amp; MQTT.html"),
    ],
},

"Switches & Managed Networks.html":{
    "title":"Switches & Managed Networks",
    "meta":{"category":"Industrial Networks & Protocols","tags":["#switch","#VLAN","#DLR","#ring","#QoS"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "An unmanaged switch is fine in a home office. On the plant floor, you want managed switches — for VLANs, diagnostics, port mirroring, redundant ring topologies, QoS, and security.")},
        {"title":"Features That Matter","body": table(
            ["Feature","Why it matters"],
            [
                ["VLANs","Segregate traffic by area / function / security zone"],
                ["QoS","Prioritize motion / I/O traffic over HTTP and historian backfill"],
                ["IGMP snooping","Essential for CIP multicast (Ethernet/IP implicit I/O)"],
                ["DLR / REP / MRP / HSR","Ring-topology recovery in single-digit milliseconds"],
                ["Port security / 802.1X","Lock ports to MACs or require authentication"],
                ["Port mirroring","Clone traffic to a port for a protocol analyzer"],
                ["SNMP / syslog","Integrate into the monitoring stack"],
                ["Redundant power","Dual 24 VDC inputs"],
                ["Environmental rating","-40 to +70 °C, vibration, EMI"],
            ])},
        {"title":"Topologies","body": ul([
                "<strong>Star</strong> — simplest. Each device has its own cable back to the switch. Single point of failure at the switch.",
                "<strong>Ring</strong> — every switch connects to two neighbors. One link fails, others keep working. DLR (Rockwell), MRP (PROFINET), HSR, REP, Spanning Tree variants.",
                "<strong>Line</strong> — daisy-chain. Common on simple machines. Break in the middle splits the network in two.",
            ])},
        {"title":"VLAN Planning","body": ul([
                "Separate VLAN per area or per function (control, safety, vision, voice).",
                "Safety network and motion network on their own VLANs.",
                "Management VLAN for switches themselves.",
                "Inter-VLAN routing via a core switch or firewall.",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Switch config backed up and versioned.",
            "Ring topology tested with a deliberate link break.",
            "IGMP snooping on for EtherNet/IP.",
            "Port mirrors available for diagnostics.",
            "Unused ports administratively down.",
            "SNMP monitoring integrated with plant alarm / monitoring system.",
        ])},
    ],
    "related":[
        ("Industrial Ethernet vs IT Ethernet","Industrial Ethernet vs IT Ethernet.html"),
        ("IP Addressing & Subnetting","IP Addressing &amp; Subnetting.html"),
        ("Network Troubleshooting (Ping, ARP, etc)","Network Troubleshooting (Ping, ARP, etc).html"),
        ("Common Protocols","Common Protocols.html"),
    ],
},

"Network Troubleshooting (Ping, ARP, etc).html":{
    "title":"Network Troubleshooting (Ping, ARP, etc.)",
    "meta":{"category":"Industrial Networks & Protocols","tags":["#ping","#arp","#traceroute","#wireshark","#netstat"],
            "difficulty":"Intermediate","status":"final","version":"1.0.0","updated":"2026-04-13"},
    "sections":[
        {"title":"Description","body": p(
            "When network comm breaks, a methodical checklist beats guessing. These are the tools every controls tech should be fluent with.")},
        {"title":"Basic Toolkit","body": table(
            ["Tool","What it does"],
            [
                ["ping","Layer-3 reachability. ICMP echo."],
                ["arp -a","MAC-to-IP mapping in the local cache"],
                ["tracert / traceroute","Hop-by-hop path to a remote host"],
                ["ipconfig / ifconfig","Local interface settings"],
                ["netstat -an","TCP/UDP ports and connections on this host"],
                ["nslookup","DNS resolution"],
                ["nmap","Port scanning (use only with authorization)"],
                ["Wireshark","Packet capture and protocol analysis"],
                ["Managed switch web UI","Port counters, duplex, speed, errors"],
            ])},
        {"title":"Workflow","body": ol([
                "Verify link light and cable first — most 'network' problems are physical.",
                "ipconfig — is the PC/PLC on the expected subnet?",
                "ping the gateway, then the peer.",
                "arp -a — is the MAC of the peer what you expect? Duplicate MAC causes chaos.",
                "tracert — where does the traffic stop?",
                "Switch port counters — CRC errors, runts, duplex mismatches, collisions.",
                "Packet capture if the problem is a protocol handshake failure.",
            ])},
        {"title":"Common Patterns","body": table(
            ["Symptom","Likely Cause"],
            [
                ["Link light off","Cable, transceiver, wrong media"],
                ["Link on, no traffic","Duplex mismatch, wrong VLAN, port disabled"],
                ["Intermittent drop","Bad cable, loose RJ45, EMI"],
                ["Slow performance","Broadcast storm, failing cable, mismatched speed"],
                ["Works on one PC, not another","ACL / firewall rule"],
                ["One machine floods the network","Stuck ARP, runaway device, loop without STP"],
            ])},
        {"title":"EtherNet/IP Specific","body": ul([
                "Implicit I/O uses multicast on some networks — need IGMP querier + snooping.",
                "Connection Timeout Multiplier x RPI = time before the PLC faults.",
                "Check CIP connection status on the Rockwell module diagnostic page (/en/connections.html).",
            ])},
        {"title":"Field Checklist","body": tasks([
            "Cable tested with a proper tester (not just link lights).",
            "Switch port counters reviewed, cleared, and re-reviewed.",
            "Duplex/speed set manually where auto-negotiation has proven unreliable.",
            "Packet capture saved to help the next tech.",
        ])},
    ],
    "related":[
        ("IP Addressing & Subnetting","IP Addressing &amp; Subnetting.html"),
        ("Network Communication Loss","../09_Troubleshooting_&_Diagnostics/Network Communication Loss.html"),
        ("Switches & Managed Networks","Switches &amp; Managed Networks.html"),
    ],
},

}
CONTENT = {FOLDER: PAGES}
