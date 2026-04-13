---
title: "Basic Electrical Theory - AC vs DC"
version: "1.0.0"
status: "draft"
author: ["Yusuf Talan Saunders"]
editors: []
contributors: []
category: ["Electrical Fundamentals"]
tags: ["#electrical", "#ac", "#dc", "#power", "#basic-theory"]
difficulty: "Beginner"
related-topics: ["Basic Electrical Theory-Ohm’s Law, Power, Energy", "Basic Electrical Theory-Single-phase vs Three-phase"]
standards: ["NEC", "IEC Basics"]
equipment: ["none"]
to-be-completed-by: "2025-09-01"
last-updated: "2025-07-07"
reviewed: "2025-07-07"

---

# Basic Electrical Theory - AC vs DC

**Category:** `Electrical Fundamentals`  
**Tags:** `#electrical #ac #dc #power #basic-theory`  
**Difficulty:** `Beginner`  
**Last Updated:** `2025-07-07`  
**Version:** `1.0.0`  
**Status:** `Draft`  

---

## Description

This topic explains the difference between alternating current (AC) and direct current (DC), both of which are foundational to all electrical systems, from industrial automation and process control to power distribution. It includes what each is, a bit of history, why they’re used, and how their properties affect the design of controls and industrial systems.

---

## Core Concepts

### What is it?

#### DC (Direct Current)
Direct current is an electric current flowing in one constant direction.  
Typical sources are batteries, DC power supplies, or rectified AC systems. 

#### AC (Alternating Current)
Alternating current reverses direction periodically. It cycles in a waveform (typically sinusoidal), changing polarity and magnitude over time. In most countries, AC power is delivered at either 50 Hz or 60 Hz.

---

### How it works

```
Direct Current (DC)
-------------------
- Voltage is steady, does not change polarity.
- Example: A 24 VDC power supply feeding PLC inputs.

Graph: 
    Voltage
      |     _______     _______        _______
	24|____|       |___|       |______|       |_____
      |
      +----------------------------------------------> Time

Alternating Current (AC)
------------------------
- Voltage continuously rises and falls, crossing zero, changing polarity.

Graph:
    Voltage
   120|__________________________________________________
      |    /\      /\      /\      /\      /\      /\    |
      |   /  \    /  \    /  \    /  \    /  \    /  \   |
    0V|__/____\__/____\__/____\__/____\__/____\__/____\__|
      |
      +-------------------------------------------------> Time

At 60 Hz, the AC waveform completes 60 full cycles per second.
```

---

### A short history & practical reason why we have both

- **DC was first commercialized by Thomas Edison** for his electric light systems. It was simple to understand and build with.
- **AC was championed by Nikola Tesla and Westinghouse** because it allowed voltage to be easily stepped up or down with transformers, making long-distance power transmission practical.

Most modern grids use AC for transmission and distribution because it’s more efficient over long distances.  
However, most control systems (PLCs, sensors, drives) still internally operate on DC, supplied by onboard power supplies.

---

### When to Use


AC
--
- Powering large motors and industrial equipment.
- Long distance distribution (from the power company).
- Standard outlet voltage (120V, 240V, 480V).

DC
--
- PLC power supplies and control circuits (24 VDC is typical).
- Electronics, sensors, solid state relays.
- Motors requiring precise speed control (many VFDs rectify AC to DC internally).

Industrial panels often have both: 
AC incoming power, transformed or rectified to DC for controls.


---

## Specifications & Parameters

| Parameter      | AC Typical             | DC Typical                 |
|----------------|------------------------|----------------------------|
| Voltage        | 120/240/480 VAC         | 24 VDC common for controls |
| Frequency      | 50/60 Hz                | 0 Hz (steady)              |
| Polarity       | Alternates + / -        | Fixed + / -                |
| Transmission   | Efficient long distance| Short distance best        |

---

## Wiring & Diagrams

**AC vs DC Power Example in a Control Panel:**

```
Incoming AC:
L1 --[ Breaker ]--+--[ Control Relay (AC) ]
                  |
                  +--[ Power Supply ]--+24VDC--[ PLC Inputs ]-
                            |                                |
                            (-)[ 0VDC ]----------------------|
```

- The transformer drops line voltage (480/240 VAC) down to control levels (120 VAC).
- The power supply rectifies AC to DC for PLCs, sensors, and logic circuits.

---

## Troubleshooting & Diagnostics

| Symptom                | Likely Cause               | Diagnostic Step                      | Tool Needed |
|-------------------------|---------------------------|--------------------------------------|-------------|
| PLC won’t power up      | Blown DC power supply fuse| Measure 24 VDC output                 | Multimeter  |
| Motor hums but won’t turn| Lost AC phase or imbalance| Clamp all three phases for balance    | Clamp meter |
| Sensors fail intermittently| Noise on DC power lines | Check with oscilloscope if available | Oscilloscope|

---

## Field Checklist

- Confirm incoming AC line voltage and frequency matches nameplate.
- Check DC power supplies for steady output under load.
- Verify proper polarity on DC devices (many won’t tolerate reversed polarity).
- Inspect grounding and shielding to reduce AC noise coupling into DC signals.

---

## Reference Notes

- NEC Articles 210, 240, 250 for wiring & protection.
- IEC 60364 for global wiring standards.
- Historical context: The “War of Currents” (Edison vs Tesla).

---

## Related Topics

- [[Basic Electrical Theory-Ohm’s Law, Power, Energy]]
- [[Basic Electrical Theory-Single-phase vs Three-phase]]
- [[Tools of the Trade-Multimeter usage]]

---

## Local Changelog

| Date       | Version | Author                | Notes                                         |
|------------|---------|-----------------------|-----------------------------------------------|
| 2025-07-07 | 1.0.0   | Yusuf Talan Saunders  | Created first comprehensive draft of topic.   |

---
