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

# Motor Contactors & Starters

**Category:** `Motor Control`  
**Tags:** #contactors #motorstarters #motorcontrol #automation #troubleshooting #fieldguide
**Difficulty:** `Beginner`  
**Last Updated:** `2025-06-23`  

---

## Description

**Motor contactors and starters** are core components in industrial motor control systems. A **contactor** is an electromechanical switch used to control high-current loads (such as motors), while a **starter** combines a contactor with an **overload relay** to provide both control and protection.

---

## Core Concepts

### 🔹 What is it?
- **Contactor**: Electrically controlled switch that energizes or de-energizes a motor or load.
- **Starter**: Assembly consisting of a **contactor + overload relay**.
- Used to **start/stop**, and **protect motors** from overload or stall conditions.
- Control logic is usually wired to pushbuttons or PLC outputs.

### 🔹 How it works
- **Control voltage** is applied to the **coil** (A1–A2).
- Energized coil creates a magnetic field → pulls in the armature → closes main contacts (L1-T1, L2-T2, L3-T3).
- When control voltage is removed, spring returns armature → contacts open → motor turns off.
- **Overload relay** senses overcurrent. If triggered, it **opens NC auxiliary contact**, cutting control circuit to stop the motor.

### 🔹 When to Use
- Applications requiring **simple on/off motor control**:
  - Fans, pumps, conveyors, mixers, compressors.
- Use a **starter** when:
  - You need **motor overload protection**.
- Use **only a contactor** when:
  - The load is non-motor (e.g., heaters) or protection is handled externally (e.g., in VFD).

---

## 🛠️ Troubleshooting & Diagnostics

| Symptom                       | Likely Cause                    | Diagnostic Step                            | Tool(s) Needed     |
|------------------------------|----------------------------------|---------------------------------------------|--------------------|
| Contactor doesn’t pull in    | No control voltage / open coil  | Measure voltage at coil terminals (A1–A2)   | Multimeter         |
| Contactor clicks but motor dead | Worn contacts or wiring issue | Check voltage on T1/T2/T3 when energized    | Multimeter         |
| Starter trips immediately    | Overload too low or jammed load | Measure motor current & check OLR setting   | Clamp meter         |
| Coil buzzing or chattering   | Low voltage / mechanical fault  | Confirm proper coil voltage & alignment     | Multimeter         |
| Motor won’t restart after trip | OLR still tripped              | Reset OLR and investigate root cause        | Visual + Manual    |

> 💡 **Pro Tip:** Always check 95-96 (NC contact) continuity on the overload relay — if open, the overload has tripped even if the contactor looks normal.

---

## 📏 Specifications & Parameters

| Parameter         | Typical Value/Range         | Notes                                    |
|------------------|-----------------------------|------------------------------------------|
| Coil Voltage      | 24 VDC / 120 VAC / 230 VAC  | Match to control system (PLC/pushbutton) |
| Contact Rating    | 9A to 500A+                 | Based on motor FLA                       |
| Overload Range    | Adjustable via dial         | Set to match motor nameplate FLA         |
| Aux Contacts      | NO / NC                     | Used for interlocks and feedback         |

---

## 📐 Wiring & Diagrams

```plaintext
Power Circuit:
L1 ---[ Contactor ]--- T1 -----> Motor
L2 ---[ Contactor ]--- T2 -----> Motor
L3 ---[ Contactor ]--- T3 -----> Motor

Control Circuit:
L (hot) --[ STOP (NC) ]--[ START (NO) ]--[ OLR 95-96 (NC) ]--[ Coil A1 ]
                                              |
                                              +--[ A2 ]-- Neutral
```


- **STOP** is NC: breaks circuit to stop motor.
- **START** is NO: latches control circuit via auxiliary contact.
- **OLR NC contact (95-96)** interrupts circuit on overload.

---

## 📎 Reference Notes

- **NEC Article 430**: Motor control and protection requirements.
- **IEC 60947-4-1**: Standard for low-voltage motor starters and contactors.
- Overload relays are typically **class 10** (trips in ~10s at 600% FLA).
- Starters are often part of **MCC buckets** or standalone **control panels**.

---

## 📂 Related Topics

- [[Overload Relays - Setup & Testing]]
- [[VFDs - Basics & Comparison]]
- [[Control Circuit Design - Pushbuttons and Interlocks]]
- [[Motor Control Ladder Logic]]

---

## ✅ Field Checklist

- [ ] Coil voltage present and correct
- [ ] Contactor “clicks” when energized
- [ ] Output voltage present at T1/T2/T3
- [ ] Overload dial set to motor FLA
- [ ] NC OLR contact (95-96) closed when not tripped
- [ ] Contacts free of carbon, pitting, or welding
- [ ] Control circuit wiring torqued and labeled
