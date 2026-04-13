---
title: "Wire Color Codes (US & IEC)"  
version: "0.1.1"  
status: "Draft"  
author: ["Yusuf Talan Saunders"]  
editors: []  
contributors: []  
category: ["Power Distribution & Wiring"]  
tags: ["#wiring", "#colorcodes", "#us", "#iec"]  
difficulty: "Beginner"  
related-topics: ["Panel Wiring Best Practices", "Industrial Power Systems Overview"]  
standards: ["NEC Article 200", "IEC 60446", "IEC 61131-3"]  
equipment: ["Multimeter"]  
to-be-completed-by: "2025-09-15"  
last-updated: "2025-07-10"  
reviewed: ""

---

# Wire Color Codes (US & IEC)

**Category:** `Power Distribution & Wiring`  
**Tags:** `#wiring #colorcodes #us #iec`  
**Difficulty:** `Beginner`  
**Last Updated:** `2025-07-10`  
**Version:** `0.1.1`  
**Status:** `Draft`

---

## Description

This topic covers standard wire color codes used in electrical wiring for industrial systems, comparing US (NEC/NFPA) and IEC international standards. Clear identification of wires using standard colors is crucial for safety, maintenance, and troubleshooting.

---

## Core Concepts

### What is it?

Wire color codes are standardized colors assigned to wires based on their electrical function. They ensure clarity and safety during installation, maintenance, and troubleshooting.

### How it works

Wires are assigned specific colors based on their function (e.g., phase conductors, neutral, grounding, control circuits). Consistency prevents confusion and errors.

### When to Use

Use color coding anytime wiring or rewiring circuits, especially in industrial and automation control panels.

---

## Specifications & Parameters

|Function|US Standard (NEC/NFPA)|IEC Standard (IEC 60446)|
|---|---|---|
|Ground|Green or Green/Yellow|Green/Yellow|
|Neutral|White or Grey|Blue|
|Phase 1|Black|Brown|
|Phase 2|Red|Black|
|Phase 3|Blue|Grey|
|DC Positive|Red|Brown or Red|
|DC Negative|Black|Blue or Grey|
|Control circuits|Usually Blue or Yellow|Usually Orange or Yellow|

---

## Wiring & Diagrams

### Example of US Standard (Three-Phase):

```
L1 (Black)
L2 (Red)
L3 (Blue)
Neutral (White)
Ground (Green)
```

### Example of IEC Standard (Three-Phase):

```
L1 (Brown)
L2 (Black)
L3 (Grey)
Neutral (Blue)
Ground (Green/Yellow)
```

### Typical Control and DC Wiring:

**US Standard:**

```
Control Circuits: Blue or Yellow
DC Positive: Red
DC Negative: Black
Ground: Green or Green/Yellow
```

**IEC Standard:**

```
Control Circuits: Orange or Yellow
DC Positive: Brown or Red
DC Negative: Blue or Grey
Ground: Green/Yellow
```

---

## Troubleshooting & Diagnostics

|Symptom|Likely Cause|Diagnostic Step|Tool(s) Needed|
|---|---|---|---|
|Incorrect voltage|Incorrect wire connections|Verify correct color coding matches function|Multimeter|
|Grounding issues|Misidentified ground wire|Verify continuity to earth ground|Multimeter|

---

## Field Checklist

-  Verify wire color coding during installation.
    
-  Ensure clear labeling in control panels.
    
-  Check wiring diagrams for compliance with local standards.
    
-  Regularly inspect and maintain wire integrity.
    

---

## Reference Notes

- Always adhere to local electrical codes.
    
- IEC standards generally preferred internationally.
    
- Use wire labels if deviations from standard occur.
    

---

## Related Topics

- [[Panel Wiring Best Practices]]
    
- [[Industrial Power Systems Overview]]
    

---

## Local Changelog

|Date|Version|Author|Notes|
|---|---|---|---|
|2025-07-10|0.1.0|Yusuf Talan Saunders|Initial draft created.|
|2025-07-10|0.1.1|Yusuf Talan Saunders|Expanded with control and DC wiring.|

---