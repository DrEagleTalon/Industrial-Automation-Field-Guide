---
title: "README"
version: "1.0.0"
status: "Draft"
author: ["Yusuf Talan Saunders"]
editors: ["Yusuf Talan Saunders"]
contributors: ["Yusuf Talan Saunders"]
category: ["readme", "docs"]
tags: ["docs", "guide"]
last-updated: "2025-07-08"
reviewed: "2025-07-08"

---
**README**

*Industrial Automation Field Guide: A living, open-source field guide for industrial controls, automation, electrical, and process technicians and engineers. Covers everything from basic electrical theory, motor control, PLCs, HMIs, SCADA, VFDs, troubleshooting methods, to industrial networking and safety systems.*

# How to Use This Vault / Field Guide

This document explains how to maintain, edit, and expand the Industrial Automation Field Guide vault.

It includes standards for versioning, descriptions of all YAML properties, and guidelines for adding changelogs.

  

This ensures that anyone contributing to this field guide can follow consistent practices.
  
## Versioning System

The version system follows this structure:

`XX.YY.ZZ`

- `XX` = MAJOR: Major milestone releases. Significant new sections, major structure changes, or complete reorganizations (for example, adding an entire Robotics section, or restructuring all troubleshooting content).
- `YY` = MINOR: Adding new topics, new subsections, major new examples, substantial improvements to explanations, or new diagrams and illustrations in existing topics.
- `ZZ` = PATCH: Minor edits, typo fixes, slight wording changes, small new examples, or other incremental additions.
  
### Examples of Versions


| Version | Meaning                                                                    |
| ------- | -------------------------------------------------------------------------- |
| 1.0.0   | First “official” complete draft of the field guide with all core sections. |
| 1.1.0   | Added a whole new section on IO-Link Devices.                              |
| 1.1.3   | Fixed typos in the PLC chapter, added two example diagrams.                |
| 2.0.0   | Major overhaul: moved Troubleshooting to top, added Learning Paths.        |
| 2.1.0   | Added SCADA Cloud chapter.                                                 |
| 2.1.1   | Added two photos of control panels.                                        |
  

## YAML Frontmatter Properties

Every topic page in this vault starts with a YAML frontmatter block.

This metadata powers advanced linking, querying, and version control throughout the field guide.

  
It must always be placed at the very top of the markdown file.

### Example Format

---

title: "Motor Contactors"

version: "1.0.0"

status: "final"

author: ["Yusuf Talan Saunders"]

editors: ["Fatou Cham"]

contributors: ["Rickena Saunders", "Team at Huhtamaki"]

category: ["Motor Control Systems"]

tags: ["#motor", "#starter", "#troubleshooting"]

difficulty: "Intermediate"

related-topics: ["Overload Relays", "Motor Wiring & Rotation Checking"]

standards: ["NEC 430", "IEC 60947-4-1"]

equipment: ["Allen Bradley 100-C09", "Siemens Sirius"]

to-be-completed-by: "2025-09-01"

last-updated: "2025-07-07"

reviewed: "2025-07-07"

---

### Description of Each YAML Property 

#### title

- The main title of this topic.
- Does not need to match the filename.
- Example:  title: "Motor Contactors"


#### version

- Tracks this topic’s specific version, using the field guide’s MAJOR.MINOR.PATCH system.
- Example: version: "1.0.0"

#### status

- Current editorial or technical status of this topic.
- Allowed values:  
	- draft
	- in-review
	- final  
- Example:  status: "draft"


#### author

- Original author(s) of this topic page.
- Type: list of names.
- Example: author: ["Yusuf Talan Saunders"]

#### editors

- Those who provided editorial review or substantive revisions.
- Type: list of names.
- Example: editors: ["Fatou Cham"]
  
#### contributors

- Anyone who submitted ideas, field examples, or troubleshooting help.
- Type: list of names.
- Example: contributors: ["Rickena Saunders", "Team at Huhtamaki"]

#### category

- The section of the field guide this topic belongs to.
- Type: list of strings.
- Examples: 
	- category: ["Motor Control Systems"]
	- category: ["PLCs & Automation Hardware"]

  
#### tags

- Free-form hashtags for quick linking and search.
- Type: list of strings.
- Example: tags: ["#motor", "#starter", "#fieldguide"]

#### difficulty

- The technical depth of this topic.
- Allowed values:  
	- Beginner
	- Intermediate
	- Advanced
- Example: difficulty: "Intermediate"

#### related-topics

- Points to other topic pages that are closely linked to this one.
- Type: list of strings.
- Example: related-topics: ["Overload Relays", "Motor Wiring & Rotation Checking"]

#### standards

- Any official standards or codes referenced on this page.
- Type: list of strings.
- Examples:
	- standards: ["NEC 430", "IEC 60947-4-1"]
	- standards: ["none"]

#### equipment

- Specific devices, manufacturers, or models discussed on this page.
- Type: list of strings.
- Example:
	- equipment: ["Allen Bradley PowerFlex 525", "Siemens Sirius"]
	- equipment: ["none"]

#### to-be-completed-by

- The target date for getting this topic to at least in-review state.
- Example: to-be-completed-by: "2025-09-01"

#### last-updated

- The date of the last meaningful content change on this topic.
- Example: last-updated: "2025-07-07"

#### reviewed

- The last date this topic was technically reviewed for accuracy.
- Example: reviewed: "2025-07-07"  

## Using the Local Changelog on Each Page

Each topic page should end with a ## Local Changelog section. This provides an audit trail for when and why changes were made.

### Format Example

#### Local Changelog

| Date       | Version | Author                | Notes                                       |

|------------|---------|-----------------------|---------------------------------------------|

| 2025-07-07 | 0.1.0   | Yusuf Talan Saunders  | Created initial draft of Motor Contactors.  |

| 2025-07-12 | 0.1.1   | Yusuf Talan Saunders  | Added overload wiring diagram.              |

## Best Practices for Editing This Field Guide

- Always update the version, last-updated, and reviewed fields in the YAML when making any changes.
- Use the Local Changelog to record what you did, why, and by whom.
- Keep explanations in clear, concise language with examples relevant to industrial environments.
- When adding troubleshooting tables, prefer bullet points and short diagnostic instructions.
- When adding new topics or moving sections, also update the master INDEX.md and CHANGELOG.md.

### Where to Keep Global Changes

Global changes to the entire field guide — such as reorganizing multiple sections, adding major new chapters, or performing global style edits — should be documented in the root CHANGELOG.md file.

## Summary of Key Lists for YAML

| Property   | Typical or Allowed Values                           |
| ---------- | --------------------------------------------------- |
| status     | draft, in-review, final                             |
| difficulty | Beginner, Intermediate, Advanced                    |
| tags       | Always use hashtags, e.g. ["#motor", "#fieldguide"] |
| standards  | Any standards, or ["none"]                          |
| equipment  | Specific devices, or ["none"]                       |

