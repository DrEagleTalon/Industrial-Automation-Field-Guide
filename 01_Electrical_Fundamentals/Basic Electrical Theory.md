---

title: "Basic Electrical Theory"

version: "1.0.0"

status: "final"

author: ["Yusuf Talan Saunders"]

editors: []

contributors: []

category: ["Electrical Fundamentals"]

tags: ["#electrical", "#ohmslaw", "#power", "#basic-theory"]

difficulty: "Beginner"

related-topics: ["Lockout Tagout (LOTO) Procedures", "Tools of the Trade"]

standards: ["NEC", "IEC Basics"]

equipment: ["none"]

to-be-completed-by: "2025-09-01"

last-updated: "2025-07-07"

reviewed: "2025-07-07"

---

# Basic Electrical Theory

**Category:** `Electrical Fundamentals`  

**Tags:** `#electrical #ohmslaw #power #basic-theory`  

**Difficulty:** `Beginner`  

**Last Updated:** `2025-07-07`  

**Version:** `1.0.0`  

**Status:** `Final`  

---

## Description

This topic lays the foundation of basic electrical concepts critical to any work in automation, controls, or industrial maintenance. It covers what electricity is, the fundamental relationships between voltage, current, and resistance (Ohm’s Law), power, energy, and the differences between AC and DC.  

It also introduces key ideas about single-phase and three-phase power systems, which are essential for understanding how industrial plants operate.  

---

## Core Concepts

  

### What is it?

Electricity is the movement of electrons (tiny charged particles) through a conductor like copper wire.

#### Core units:

- Voltage (V): electrical pressure, measured in volts (V). It pushes electrons.
- Current (I): flow of electrons, measured in amperes (A).
- Resistance (R): opposition to flow, measured in ohms (Ω).  

If you imagine water in a pipe:

- Voltage = water pressure
- Current = flow rate (gallons/min)
- Resistance = pipe restrictions

---

### How it works

#### Ohm’s Law

The fundamental equation that ties voltage, current, and resistance:

V = I × R

This means:

- Increase voltage -> current increases (if resistance is constant).
- Increase resistance -> current decreases (if voltage is constant).

Example:

If you have 120 volts across a 12 ohm heater coil:

I = V / R = 120V / 12Ω = 10A

#### Power

The rate of doing electrical work, measured in watts (W):

P = V × I

or for purely resistive loads:

P = I² × R

Example:

A 10 amp current at 120V:

P = 120V × 10A = 1200W (1.2 kW)

#### Energy

Power used over time, measured in kilowatt-hours (kWh):

Energy = Power × Time

Example:

A 2 kW motor running for 5 hours:

Energy = 2 kW × 5 h = 10 kWh

---

  

### When to Use

Basic electrical theory is used daily by technicians and engineers to:

- Calculate circuit current for wire sizing and overloads.
- Troubleshoot voltage drops causing machines to fault.
- Understand overheating wires or motors (overcurrent).
- Diagnose control circuits that under-voltage and fail to pull in contactors.

Without these basics, you’d never confidently size a starter, fuse, or wire run.

---

  

## Specifications & Parameters

  

| Parameter      | Typical Value / Range      | Notes                                  |

|----------------|---------------------------|----------------------------------------|

| Control Voltage| 24 VDC, 120 VAC            | Common for control circuits            |

| Line Voltage   | 120/240/480 VAC            | Typical industrial power supplies      |

| Current Ranges | Milliamps to hundreds of A | From sensors to large motors           |

| Resistance     | 0.1 Ω to MΩ                | Depends on load or insulation context  |

  

---

  

## Wiring & Diagrams

Basic DC Circuit Example:

  

+24VDC ––[ Fuse ]––[ Switch ]––[ Lamp ]–– 0VDC

  

- When the switch closes, voltage pushes current through the lamp’s resistance, lighting it up.
- The fuse protects against short circuits by melting if current is too high.

  

  

Simple AC Motor Circuit:

  

L1 ––[ Breaker ]––[ Contactor ]––[ Motor ]

N ––––––––––[ Contactor ]––[ Motor ]

  

- Breaker protects against overcurrent (shorts, overloads).
- Contactor is an electrically controlled switch.
- Motor is the load. N (neutral) provides return path.

  

  

Three-Phase Example (typical industrial motor):

  

L1 ––[ Overload ]––+

L2 ––[ Overload ]––+––[ Motor ]

L3 ––[ Overload ]––+

  

- Overload relay cuts the circuit if any phase draws too much current.

  

---

  

## Troubleshooting & Diagnostics

Common problems in simple circuits:

|   |   |   |   |
|---|---|---|---|
|Symptom|Likely Cause|Diagnostic Step|Tool Needed|
|No voltage at load|Open fuse, loose wire|Check continuity across fuse & wire|Multimeter|
|Motor won’t start|Contactor not pulling in|Verify coil voltage present|Multimeter|
|Overload tripping|Phase imbalance or dirt|Clamp each phase for imbalance|Clamp meter|
|Low voltage at load|Undersized wiring run|Measure voltage at source vs load|Multimeter|

Always check for voltage under load — an unloaded circuit might appear fine.

---

  

## Field Checklist

  

- Verify line voltage at incoming terminals.
- Confirm control circuit voltage (e.g. 24 VDC or 120 VAC) matches device spec.
- Ensure wire size matches load current draw.
- Inspect terminals for tight, clean connections.
- Perform voltage drop checks under full load.

  

---

  

## Reference Notes

Standards and references:

  

- NEC Article 210 (branch circuits)
- NEC 240 (overcurrent protection)
- NEC 250 (grounding & bonding)
- IEC 60364 series for global installations
- Manufacturer data sheets for motor, starter, or panel ratings

  

---

  

## Related Topics

  

- [[Lockout Tagout (LOTO) Procedures]]

- [[Tools of the Trade]]

- [[Wire Color Codes (US & IEC)]]

  

---

  

## Local Changelog

  

| Date       | Version | Author                | Notes                                       |

|------------|---------|-----------------------|---------------------------------------------|

| 2025-07-07 | 1.0.0   | Yusuf Talan Saunders  | Created complete first edition of topic.    |

  

---

