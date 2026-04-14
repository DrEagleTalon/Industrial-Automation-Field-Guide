---
title: ""
version: ""
status: ""
author: [""]
editors: [""]
contributors: [""]
category: [""]
tags: [""]
difficulty: ""
related-topics: [""]
standards: [""]
equipment: [""]
to-be-completed-by: ""
last-updated: ""
reviewed: ""
---


## **Top-Level Folder Structure

> Recommended root folder name: `Industrial Automation Field Guide`

### `00_Index`

- `Master Topic Index.md` ← (The list we just built with topic links)
    
- `How to Use This Vault.md`
    
- `Glossary.md`
    
- `Quick Reference Symbols.md`
    

---

### `01_Electrical_Fundamentals`

Basic theory and safety.

- `Basic Electrical Theory.md`
    
- `Ohm's Law and Power.md`
    
- `AC vs DC.md`
    
- `Three-Phase Power.md`
    
- `PPE and Electrical Safety.md`
    
- `Lockout Tagout (LOTO).md`
    
- `Tool Basics – Multimeter, Clamp Meter, Megger.md`
    

---

### `02_Power_Distribution`

Incoming power and infrastructure.

- `Industrial Power Systems Overview.md`
    
- `Panel Wiring Best Practices.md`
    
- `Fuses vs Breakers.md`
    
- `Control Transformers.md`
    
- `Voltage Drop – Testing and Planning.md`
    
- `Conduit & Fittings.md`
    
- `Wire Color Codes.md`
    

---

### `03_Control_Devices`

Discrete devices used in control circuits.

- `Pushbuttons and Selector Switches.md`
    
- `Pilot Lights.md`
    
- `Limit Switches.md`
    
- `Proximity Sensors.md`
    
- `Photoelectric Sensors.md`
    
- `Relays and Interposing Relays.md`
    
- `Timers and Counters.md`
    
- `Latching and Seal-in Circuits.md`
    

---

### `04_Motor_Control`

Motor hardware and control components.

- `3-Phase Motor Basics.md`
    
- `Reading a Motor Nameplate.md`
    
- `Motor Contactors.md`
    
- `Motor Starters.md`
    
- `Overload Relays.md`
    
- `Reversing Starters.md`
    
- `Soft Starters.md`
    
- `Star-Delta Starters.md`
    
- `VFDs – Overview.md`
    
- `VFD Parameters and Setup.md`
    
- `Motor Braking Methods.md`
    
- `Motor Megger Testing.md`
    

---

### `05_PLCs_Hardware`

PLC hardware, wiring, and IO.

- `What is a PLC.md`
    
- `Discrete and Analog I/O.md`
    
- `Sinking vs Sourcing.md`
    
- `Wiring Inputs and Outputs.md`
    
- `Powering the PLC.md`
    
- `Safety Relays and Safety PLCs.md`
    
- `Common PLC Brands.md`
    

---

### `06_PLC_Programming`

Logic building and troubleshooting.

- `Ladder Logic Basics.md`
    
- `Start Stop Logic.md`
    
- `Timers.md`
    
- `Counters.md`
    
- `Set Reset Logic.md`
    
- `Interlocks and Permissives.md`
    
- `Alarm Logic and Fault Detection.md`
    
- `HMI Tagging Basics.md`
    
- `State Machine Programming.md`
    
- `Structured Text Overview.md`
    

---

### `07_HMI_SCADA`

Visualization and monitoring.

- `HMI Basics.md`
    
- `Screen Navigation and Input.md`
    
- `Tag Linking.md`
    
- `Alarms and Messaging.md`
    
- `HMI to PLC Communication.md`
    
- `SCADA Architecture Overview.md`
    
- `Data Logging and Trending.md`
    

---

### `08_Industrial_Networking`

Protocols and communications.

- `Industrial Ethernet vs Office Ethernet.md`
    
- `IP Addressing and Subnetting.md`
    
- `Modbus – RTU and TCP.md`
    
- `EtherNet/IP Basics.md`
    
- `Profinet Overview.md`
    
- `Network Switches and Cabling.md`
    
- `Network Troubleshooting Tools.md`
    

---

### `09_Troubleshooting`

Techniques and real-world diagnostics.

- `Troubleshooting Workflow.md`
    
- `Power Circuit Issues.md`
    
- `Control Circuit Failures.md`
    
- `VFD Fault Codes.md`
    
- `Motor Trips and Overloads.md`
    
- `PLC Input/Output Faults.md`
    
- `Sensor Troubleshooting.md`
    
- `Network Dropouts.md`
    

---

### `10_Commissioning_Integration`

System setup and handoff.

- `Control Panel BOM and Layout.md`
    
- `Loop Checks and I/O Checkout.md`
    
- `Startup Sequences.md`
    
- `PID Tuning Basics.md`
    
- `PLC-HMI-VFD Integration.md`
    
- `Documentation Best Practices.md`
    
- `Commissioning Reports.md`
    

---

### `11_Standards_and_Codes`

Reference standards and regulatory.

- `NEC 430 Overview.md`
    
- `UL 508A – Panel Requirements.md`
    
- `NFPA 79 Summary.md`
    
- `IEC 61131-3 Programming Standard.md`
    
- `Intro to Functional Safety.md`
    

---

### `12_Safety_Systems`

Machine safety design and diagnostics.

- `Emergency Stops.md`
    
- `Two-Hand Controls.md`
    
- `Safety Fencing and Interlocks.md`
    
- `Safety Relays and Circuits.md`
    
- `Safety PLCs.md`
    
- `Performing Risk Assessments.md`
    

---

### `13_Advanced_Systems`

Specialized and modern tech.

- `Servo Motors and Drives.md`
    
- `Encoders and Resolvers.md`
    
- `Robotic Integration.md`
    
- `IO-Link Overview.md`
    
- `Industrial Wireless Systems.md`
    
- `Energy Monitoring Systems.md`
    
- `IIoT and MQTT.md`
    
- `Remote PLC Access.md`
    

---

### `14_Soft_Skills_Workflow`

Real-world tools and habits.

- `Reading Schematics.md`
    
- `CAD Software Basics.md`
    
- `Project Handoff Docs.md`
    
- `Troubleshooting Reports.md`
    
- `Change Management and Backups.md`
    
- `Field Communication Tips.md`
    

---

## Suggested Folder Setup in Obsidian

```
Industrial Automation Field Guide/
├── 00_Index/
│   ├── Master Topic Index.md
│   └── How to Use This Vault.md
├── 01_Electrical_Fundamentals/
├── 02_Power_Distribution/
├── 03_Control_Devices/
├── 04_Motor_Control/
├── 05_PLCs_Hardware/
├── 06_PLC_Programming/
├── 07_HMI_SCADA/
├── 08_Industrial_Networking/
├── 09_Troubleshooting/
├── 10_Commissioning_Integration/
├── 11_Standards_and_Codes/
├── 12_Safety_Systems/
├── 13_Advanced_Systems/
├── 14_Soft_Skills_Workflow/
```

---
