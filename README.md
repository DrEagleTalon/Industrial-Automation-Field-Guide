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

# Industrial Automation Field Guide

A living, open-source field guide for industrial controls, automation, electrical, process, and systems technicians and engineers.

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

- **[Master Table of Contents](markdown/00_Index/Index.md)** — full index of every topic, rendered in markdown for GitHub.
- **[HTML Site Index](00_Index/Index.html)** — same TOC, rendered for the website.
- **[Site Landing Page](index.html)** — quick-browse landing page (HTML).
- **[Markdown Source Mirror](markdown/)** — every `.md` file in a parallel tree, ready to be extracted as a standalone repo.

### Sections at a Glance

The guide is organized into 14 sections. Each row links to the markdown source (best for reading directly on GitHub) and the rendered HTML pages.

| # | Section | Source (Markdown) | Rendered (HTML) |
|---|---------|-------------------|-----------------|
| I    | Electrical Fundamentals             | [markdown/01_Electrical_Fundamentals/](markdown/01_Electrical_Fundamentals/)                       | [01_Electrical_Fundamentals/](01_Electrical_Fundamentals/)                       |
| II   | Power Distribution & Wiring         | [markdown/02_Power_Distribution/](markdown/02_Power_Distribution/)                                 | [02_Power_Distribution/](02_Power_Distribution/)                                 |
| III  | Control Devices & Circuits          | [markdown/03_Control_Devices/](markdown/03_Control_Devices/)                                       | [03_Control_Devices/](03_Control_Devices/)                                       |
| IV   | Motor Control Systems               | [markdown/04_Motor_Control/](markdown/04_Motor_Control/)                                           | [04_Motor_Control/](04_Motor_Control/)                                           |
| V    | PLCs & Automation Hardware          | [markdown/05_PLCs & Automation Hardware/](markdown/05_PLCs%20%26%20Automation%20Hardware/)         | [05_PLCs & Automation Hardware/](05_PLCs%20%26%20Automation%20Hardware/)         |
| VI   | PLC Programming & Logic             | [markdown/06_PLC_Programming_&_Logic/](markdown/06_PLC_Programming_%26_Logic/)                     | [06_PLC_Programming_&_Logic/](06_PLC_Programming_%26_Logic/)                     |
| VII  | HMI / SCADA Systems                 | [markdown/07_HMI_SCADA_Systems/](markdown/07_HMI_SCADA_Systems/)                                   | [07_HMI_SCADA_Systems/](07_HMI_SCADA_Systems/)                                   |
| VIII | Industrial Networks & Protocols     | [markdown/08_Industrial_Networks_&_Protocols/](markdown/08_Industrial_Networks_%26_Protocols/)     | [08_Industrial_Networks_&_Protocols/](08_Industrial_Networks_%26_Protocols/)     |
| IX   | Troubleshooting & Diagnostics       | [markdown/09_Troubleshooting_&_Diagnostics/](markdown/09_Troubleshooting_%26_Diagnostics/)         | [09_Troubleshooting_&_Diagnostics/](09_Troubleshooting_%26_Diagnostics/)         |
| X    | System Integration & Commissioning  | [markdown/10_System_Integration_&_Commissioning/](markdown/10_System_Integration_%26_Commissioning/) | [10_System_Integration_&_Commissioning/](10_System_Integration_%26_Commissioning/) |
| XI   | Standards & Codes                   | [markdown/11_Standards_and_Codes/](markdown/11_Standards_and_Codes/)                               | [11_Standards_and_Codes/](11_Standards_and_Codes/)                               |
| XII  | Safety Systems (Advanced)           | [markdown/12_Safety_Systems_Advanced/](markdown/12_Safety_Systems_Advanced/)                       | [12_Safety_Systems_Advanced/](12_Safety_Systems_Advanced/)                       |
| XIII | Specialty Topics                    | [markdown/13_Specialty_Topics/](markdown/13_Specialty_Topics/)                                     | [13_Specialty_Topics/](13_Specialty_Topics/)                                     |
| XIV  | Soft Skills & Workflow              | [markdown/14_Soft_Skills_Workflow/](markdown/14_Soft_Skills_Workflow/)                             | [14_Soft_Skills_Workflow/](14_Soft_Skills_Workflow/)                             |

> For the full per-topic list with every page linked, open the **[Master Table of Contents](markdown/00_Index/Index.md)**.

---

## Repository Layout

```
.
├── 00_Index/                   Table of Contents (HTML, rendered for the site)
├── 01_Electrical_Fundamentals/ … through …
├── 14_Soft_Skills_Workflow/    Section folders — rendered HTML pages for the site
├── instructions/               Vault guide, folder structure doc, page templates (HTML)
├── markdown/                   Full mirror of every .md file (standalone-repo ready)
│   ├── 00_Index/Index.md       Master TOC (markdown)
│   ├── instructions/           Markdown copies of the four guide documents
│   └── 01_… 14_…/              Section folders with all topic markdown files
├── scripts/                    Python generators (convert_to_html.py, generate_pages.py, content_*.py)
├── index.html                  Site landing page
├── README.md / README.html     This file
├── CHANGELOG.md / CHANGELOG.html
├── LICENSE                    CC BY-SA 4.0 (docs, prose, diagrams)
└── LICENSE-CODE               GPL-3.0 (code samples and scripts)
```

---

## Instructions & Templates

The [`instructions/`](instructions/) folder holds the meta-documentation that used to live at the root of the repo. Each document is available as both HTML (rendered for the site) and Markdown (in [`markdown/instructions/`](markdown/instructions/), best for reading on GitHub).

| # | Document | Markdown (GitHub) | HTML (site) |
|---|----------|-------------------|-------------|
| 01 | **How to Use This Vault** — versioning, YAML frontmatter, editing conventions, local changelog format. | [MD](markdown/instructions/01%20How%20to%20Use%20This%20Vault.md) | [HTML](instructions/01%20How%20to%20Use%20This%20Vault.html) |
| 02 | **Top-Level Folder Structure** — map of section folders and what belongs where. | [MD](markdown/instructions/02%20Top-Level%20Folder%20Structure.md) | [HTML](instructions/02%20Top-Level%20Folder%20Structure.html) |
| 03 | **TEMPLATE for Industrial Engineers Field Guide** — filled-out example page showing every section. | [MD](markdown/instructions/03%20TEMPLATE%20for%20Industrial%20Engineers%20Field%20Guide.md) | [HTML](instructions/03%20TEMPLATE%20for%20Industrial%20Engineers%20Field%20Guide.html) |
| 04 | **BLANK TEMPLATE for Industrial Engineers Field Guide** — empty page skeleton to copy for new topics. | [MD](markdown/instructions/04%20BLANK%20TEMPLATE%20for%20Industrial%20Engineers%20Field%20Guide.md) | [HTML](instructions/04%20BLANK%20TEMPLATE%20for%20Industrial%20Engineers%20Field%20Guide.html) |

### Contributing workflow (short version)

1. Read **[01 How to Use This Vault](markdown/instructions/01%20How%20to%20Use%20This%20Vault.md)** for versioning + YAML rules.
2. Check **[02 Top-Level Folder Structure](markdown/instructions/02%20Top-Level%20Folder%20Structure.md)** to place your page in the right section.
3. Copy **[04 BLANK TEMPLATE](markdown/instructions/04%20BLANK%20TEMPLATE%20for%20Industrial%20Engineers%20Field%20Guide.md)** into the right [`markdown/`](markdown/) section folder and fill it out. Reference **[03 TEMPLATE](markdown/instructions/03%20TEMPLATE%20for%20Industrial%20Engineers%20Field%20Guide.md)** for a complete example.
4. Run `python scripts/convert_to_html.py` to regenerate the HTML output.
5. Update the master [Index](markdown/00_Index/Index.md) and [CHANGELOG.md](CHANGELOG.md).
6. Submit a pull request.

---

## Versioning System

The version system follows this structure:

`XX.YY.ZZ`

- `XX` = MAJOR: Major milestone releases. Significant new sections, major structure changes, or complete reorganizations (for example, adding an entire Robotics section, or restructuring all troubleshooting content).
- `YY` = MINOR: Adding new topics, new subsections, major new examples, substantial improvements to explanations, or new diagrams and illustrations in existing topics.
- `ZZ` = PATCH: Minor edits, typo fixes, slight wording changes, small new examples, or other incremental additions.

### Examples of Versions

| Version | Meaning                                                                    |
| ------- | -------------------------------------------------------------------------- |
| 1.0.0   | First "official" complete draft of the field guide with all core sections. |
| 1.1.0   | Added a whole new section on IO-Link Devices.                              |
| 1.1.3   | Fixed typos in the PLC chapter, added two example diagrams.                |
| 2.0.0   | Major overhaul: moved Troubleshooting to top, added Learning Paths.        |
| 2.1.0   | Added SCADA Cloud chapter.                                                 |
| 2.1.1   | Added two photos of control panels.                                        |

See the full instructions in [01 How to Use This Vault](markdown/instructions/01%20How%20to%20Use%20This%20Vault.md) for YAML property reference, local changelog format, and editing best practices.

For project-wide history, see [CHANGELOG.md](CHANGELOG.md).

---

## License

This repository uses a **split-license model**:

- **Documentation content** (prose, explanations, diagrams, tables, and other non-code educational material) is licensed under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**. See [LICENSE](LICENSE).
- **Code content** (code snippets, scripts, automation utilities, and executable examples) is licensed under **GNU General Public License v3.0 (GPL-3.0)**. See [LICENSE-CODE](LICENSE-CODE).

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

Contributions are welcome. Please fork the repository, make your changes, and submit a pull request. For style and metadata conventions, see [`markdown/instructions/01 How to Use This Vault.md`](markdown/instructions/01%20How%20to%20Use%20This%20Vault.md).

---

*Created and maintained by Yusuf Talan Saunders.*

*Industrial Automation Field Guide: A living, open-source field guide for industrial controls, automation, electrical, and process technicians and engineers. Covers everything from basic electrical theory, motor control, PLCs, HMIs, SCADA, VFDs, troubleshooting methods, to industrial networking and safety systems.*
