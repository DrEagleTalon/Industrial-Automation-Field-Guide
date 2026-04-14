---
title: "README"
version: "1.4.0"
status: "Draft"
author: ["Yusuf Talan Saunders"]
editors: ["Yusuf Talan Saunders"]
contributors: ["Yusuf Talan Saunders"]
category: ["Documentation", "Meta"]
tags: ["#readme", "#docs", "#meta", "#guide"]
last-updated: "2026-04-14"
reviewed: "2026-04-14"
---

# Industrial Automation Field Guide — Markdown Source

A living, open-source field guide for industrial controls, automation, electrical, process, and systems technicians and engineers.

This folder is a **self-contained markdown-only mirror** of the main repository. It is intended to be cut-and-paste ready as its own new repo (e.g., for Obsidian vaults, documentation sites, or other static site generators).

This guide covers:

- Basic electrical theory, wiring, and power distribution
- Motor control systems, VFDs, and starters
- PLC hardware, programming, and troubleshooting
- HMI & SCADA basics
- Industrial protocols and networking
- Safety systems and standards
- Troubleshooting methodologies
- Preventive & predictive maintenance

---

## Browse the Field Guide

- **[Master Table of Contents](00_Index/Index.md)** — full index of every topic.
- **[Instructions & Templates](instructions/)** — how to use this vault, folder structure, and page templates.
- **[CHANGELOG](CHANGELOG.md)** — project history.

### Sections at a Glance

The guide is organized into 14 sections.

| #    | Section                              | Folder                                                                |
|------|--------------------------------------|-----------------------------------------------------------------------|
| I    | Electrical Fundamentals              | [01_Electrical_Fundamentals/](01_Electrical_Fundamentals/)            |
| II   | Power Distribution & Wiring          | [02_Power_Distribution/](02_Power_Distribution/)                      |
| III  | Control Devices & Circuits           | [03_Control_Devices/](03_Control_Devices/)                            |
| IV   | Motor Control Systems                | [04_Motor_Control/](04_Motor_Control/)                                |
| V    | PLCs & Automation Hardware           | [05_PLCs & Automation Hardware/](05_PLCs%20%26%20Automation%20Hardware/) |
| VI   | PLC Programming & Logic              | [06_PLC_Programming_&_Logic/](06_PLC_Programming_%26_Logic/)          |
| VII  | HMI / SCADA Systems                  | [07_HMI_SCADA_Systems/](07_HMI_SCADA_Systems/)                        |
| VIII | Industrial Networks & Protocols      | [08_Industrial_Networks_&_Protocols/](08_Industrial_Networks_%26_Protocols/) |
| IX   | Troubleshooting & Diagnostics        | [09_Troubleshooting_&_Diagnostics/](09_Troubleshooting_%26_Diagnostics/) |
| X    | System Integration & Commissioning   | [10_System_Integration_&_Commissioning/](10_System_Integration_%26_Commissioning/) |
| XI   | Standards & Codes                    | [11_Standards_and_Codes/](11_Standards_and_Codes/)                    |
| XII  | Safety Systems (Advanced)            | [12_Safety_Systems_Advanced/](12_Safety_Systems_Advanced/)            |
| XIII | Specialty Topics                     | [13_Specialty_Topics/](13_Specialty_Topics/)                          |
| XIV  | Soft Skills & Workflow               | [14_Soft_Skills_Workflow/](14_Soft_Skills_Workflow/)                  |

> For the full per-topic list with every page linked, open the **[Master Table of Contents](00_Index/Index.md)**.

---

## Folder Layout

```
.
├── 00_Index/                   Table of Contents
├── 01_Electrical_Fundamentals/ … through …
├── 14_Soft_Skills_Workflow/    Section folders — topic markdown files
├── instructions/               Vault guide, folder structure doc, page templates
├── README.md                   This file
└── CHANGELOG.md
```

---

## Instructions & Templates

The [`instructions/`](instructions/) folder holds the meta-documentation for this field guide.

| # | Document | Link |
|---|----------|------|
| 01 | **How to Use This Vault** — versioning, YAML frontmatter, editing conventions, local changelog format. | [01 How to Use This Vault.md](instructions/01%20How%20to%20Use%20This%20Vault.md) |
| 02 | **Top-Level Folder Structure** — map of section folders and what belongs where. | [02 Top-Level Folder Structure.md](instructions/02%20Top-Level%20Folder%20Structure.md) |
| 03 | **TEMPLATE for Industrial Engineers Field Guide** — filled-out example page showing every section. | [03 TEMPLATE for Industrial Engineers Field Guide.md](instructions/03%20TEMPLATE%20for%20Industrial%20Engineers%20Field%20Guide.md) |
| 04 | **BLANK TEMPLATE for Industrial Engineers Field Guide** — empty page skeleton to copy for new topics. | [04 BLANK TEMPLATE for Industrial Engineers Field Guide.md](instructions/04%20BLANK%20TEMPLATE%20for%20Industrial%20Engineers%20Field%20Guide.md) |

### Contributing workflow (short version)

1. Read **[01 How to Use This Vault](instructions/01%20How%20to%20Use%20This%20Vault.md)** for versioning + YAML rules.
2. Check **[02 Top-Level Folder Structure](instructions/02%20Top-Level%20Folder%20Structure.md)** to place your page in the right section.
3. Copy **[04 BLANK TEMPLATE](instructions/04%20BLANK%20TEMPLATE%20for%20Industrial%20Engineers%20Field%20Guide.md)** into the section folder and fill it out. Reference **[03 TEMPLATE](instructions/03%20TEMPLATE%20for%20Industrial%20Engineers%20Field%20Guide.md)** for a complete example.
4. Update the master [Index](00_Index/Index.md) and [CHANGELOG.md](CHANGELOG.md).
5. Submit a pull request.

---

## Versioning System

The version system follows this structure:

`XX.YY.ZZ`

- `XX` = MAJOR: Major milestone releases. Significant new sections, major structure changes, or complete reorganizations (for example, adding an entire Robotics section, or restructuring all troubleshooting content).
- `YY` = MINOR: Adding new topics, new subsections, major new examples, substantial improvements to explanations, or new diagrams and illustrations in existing topics.
- `ZZ` = PATCH: Minor edits, typo fixes, slight wording changes, small new examples, or other incremental additions.

See [01 How to Use This Vault](instructions/01%20How%20to%20Use%20This%20Vault.md) for the full YAML property reference, local changelog format, and editing best practices.

---

## License

This repository uses a **split-license model**:

- **Documentation content** (prose, explanations, diagrams, tables, and other non-code educational material) is licensed under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**. See [../LICENSE](../LICENSE).
- **Code content** (code snippets, scripts, automation utilities, and executable examples) is licensed under **GNU General Public License v3.0 (GPL-3.0)**. See [../LICENSE-CODE](../LICENSE-CODE).

### What this means in plain English

You are welcome to copy, share, and adapt this project.

- If you use or remix the **documentation**, you must:
  - Give appropriate credit,
  - Link to the CC BY-SA 4.0 license,
  - Indicate if changes were made,
  - Release adaptations under the same or a compatible ShareAlike license.
- If you use or redistribute **code**, GPL-3.0 terms apply, including making source available and keeping the same license on derivative code distributions.

### What you can do

- Use this material for learning, internal training, and published derivative work.
- Reuse and adapt documentation with attribution and ShareAlike.
- Reuse and modify code under GPL-3.0 requirements.

### What you cannot do

- Remove attribution or imply the original authors endorse your derivative.
- Re-license CC BY-SA documentation as proprietary/closed.
- Distribute GPL-covered code derivatives under a non-GPL proprietary license.

## Contributing

Contributions are welcome. Please fork the repository, make your changes, and submit a pull request. For style and metadata conventions, see [`instructions/01 How to Use This Vault.md`](instructions/01%20How%20to%20Use%20This%20Vault.md).

---

*Created and maintained by Yusuf Talan Saunders.*

*Industrial Automation Field Guide: A living, open-source field guide for industrial controls, automation, electrical, and process technicians and engineers. Covers everything from basic electrical theory, motor control, PLCs, HMIs, SCADA, VFDs, troubleshooting methods, to industrial networking and safety systems.*
