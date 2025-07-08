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

# Direct-On-Line (DOL) Starters

**Category:** `Motor Control`  
**Tags:** `#motorcontrol #starter #troubleshooting #fieldguide`  
**Difficulty:** `Beginner`  
**Last Updated:** `2025-06-29`  

---

## Description

A Direct-On-Line (DOL) starter applies full line voltage directly to the motor terminals to start the motor. It’s simple and economical, commonly used for small to medium 3-phase motors.

---

## Core Concepts

### 🔹 What is it?
> - Motor starter that connects motor directly to supply line.  
> - Key components: Contactor, overload relay, start/stop buttons.  
> - Suitable for motors typically under 10 HP depending on supply.

### 🔹 How it works
> - Pressing START energizes contactor coil.  
> - Main contacts close, supplying power to motor.  
> - Auxiliary NO contact seals circuit to maintain contactor.  
> - STOP opens circuit, de-energizes coil.  
> - Overload relay protects against overcurrent.

### 🔹 When to Use
> - For applications with low starting torque needs.  
> - Not ideal where high inrush current can cause voltage dips.

---

## 🛠️ Troubleshooting & Diagnostics

| Symptom                | Likely Cause                  | Diagnostic Step                       | Tool(s) Needed      |
|-------------------------|-----------------------------|--------------------------------------|---------------------|
| Motor won't start       | Contactor coil not energizing | Measure control voltage at coil     | Multimeter          |
| Contactor chatters      | Low voltage / loose wires    | Tighten terminals, check supply     | Multimeter, screwdriver |
| Trips on start          | OLR set too low / mechanical jam | Check overload setting, inspect motor shaft | Multimeter, inspection |

> 💡 **Pro Tip:** Always manually spin the motor shaft if possible to check for binding.

---

## 📏 Specifications & Parameters

| Parameter       | Typical Value/Range | Notes                           |
|-----------------|---------------------|---------------------------------|
| Coil Voltage    | 24 VDC / 120 VAC / 230 VAC | Must match control power |
| Contactor Rating| 9A, 12A, 25A         | Based on motor FLA             |
| Overload Dial   | 0.7–1.0 × motor FLA | Adjust based on nameplate      |

---

## 📐 Wiring & Diagrams

```
Power:
 L1 ---[Contactor]---+
 L2 -----------------+--- Motor
 L3 -----------------+

Control:
 L --- Stop --- Start --- Contactor Coil --- N
            +--- Auxiliary NO seal-in
            +--- OLR NC contact
```

---

## 📎 Reference Notes

- NEC Article 430 for motor protection.  
- IEC 60947-4-1 for contactors and motor starters.

---

## 📂 Related Topics

- [[Motor Contactors]]
- [[Overload Relays]]
- [[Soft Starters]]

---

## ✅ Field Checklist

- [ ] Coil voltage matches spec
- [ ] Overload relay set to FLA
- [ ] All terminals tight
- [ ] Rotation confirmed after wiring

---

