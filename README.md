# Synputer Cost Estimator

## Project Overview
This is a piece of software built as part of "Assignment 2 - Presentation" for the Software Engineering Project Management course at the University of Essex Online by Group 1, consisting of:
- Nassar Al-Naimi
- Charles Kuyuyama
- Abdulah Alihu Ngamjeh
- Trevor Woodman

The Synputer Cost Estimator is a command-line tool that takes a series of inputs and outputs a cost estimate for the system including costs for components, development, manufacturing, and testing. It uses a 3-point estimation technique, applied to hardware, software, and testing/QA costs, then combined to give a total cost estimate. The tool also outputs a bill of materials (BOM) for the system based on the specification provided.

Optimistic (O): Assumes being ahead of schedule, minimal delays, high efficiency.
Pessimistic (P): Assumes being behind schedule, most delays, low efficiency.
Most Likely (M): Assumes being on schedule, average delays, average efficiency.

## Installation
This project requires [Python 3.9 or higher](https://www.python.org/downloads/).

1. Clone the repository to your local machine
2. The specification for the Synputer should be in the root directory of the project, called `specification.csv`. This file contains a list of components, one per line, in the following format:
    ```
    Component,UnitPrice,Quantity,DesignCost(optional),ManufactureCost(optional),RedesignCost(optional)
    ```
3. Run the following command in the root directory of the project and follow the prompts:
    ```bash
    python estimator.py
    ```

## The Fictitious Scenario
This project is based on a fictional scenario in which two computing companies have a dialogue regarding a computer that is being developed which outlines the specifications of the system, culminating in one of them placing an order for 2000 units based on their discussion.

Synful Computing, one of the companies involved in this scenario, is developing a new and fairly groundbreaking computer they internally call the "Synputer". Colin Syn, the owner, is one of the two participants in the discussion.

Will Burns, the managing director of the second company, EDC, has agreed to purchase 2000 units based on the specification discussed by them in their meeting, at an agreed at-cost price of £250 per unit, for an order total of £500,000.

Sometime after the initial [project review](https://essex.trevorwoodman.ca/pages/module6/assignment1/m6a1.html), Synful Computing came short on specifications and developments, and sends EDC a specification that is underwhelming and not to the agreed standard. EDC threatens legal action, and demands that Synful Computing deliver on the agreed specification, with a list of specifications in order of importance:
- Industry standard operating system
- External keyboard/connector
- At least 512KB of RAM
- At least 1 industry standard removable drive
- SCSI expansion capability
- At least a 68000 CPU - preferably upgradable
- Minimum of 2 serial ports that support RS 422/485 standard
- Board is ready to support a GUI system and mouse if required by the user

## Notes on BOM and Readability
The following specification is based on the dialogue in the case study, included in the documents folder, and two bill of materials (BOM) provided by the assignment brief for software and hardware, also included. We had to pick materials from these two BOMs. There are some oddities, for example "INTSND" appears to be a made-up term. Based on context (other "mono snd" or "3ch snd" options) we can assume that it is for sound.

In the specifications for the Synputer, the items are written as they appear in the BOMs. Some text in the BOMs, such as the varied shorthand writing, is esoteric for presumably no other reason than to make it difficult to complete this component of the course. If something is unclear or misinterpreted, please keep this in mind.

According to the case study, a complete system consists of the following components:
- 1 or more ROMs (according to a different part of the case study, the board can only support 2)
- 4 'glue chips' (G1-G4) / ULAs
- 1 CPU
- 4 RAM chips
- interface (I/O) chips for serial, keyboard, video output, keyboard, screen, storage drive(s), and a case per design

## Synputer Specification
This spec is based on the requirements outlined via EDC in their reply to Synful Computing after the initial project review. The specification is based on the BOMs provided in the assignment brief, and the dialogue in the case study.

### Hardware
| Component | Specification | Unit Cost (£/per 1000) | Quantity (per unit) | Design Cost (wks) | Manufacture Cost (£/per 1000) | Redesign Cost (wks) |
| --- | --- | --- | --- | --- | --- | --- |
| CPU EP7500FE | 50MHz, 4KB cache, int VIDC and IOMD | £15 | 1 | - | - | 4wks |
| ULA GX | glue special, interface XVX and CPU | £5 | 1 | - | - | 3wks |
| RAM 512KB | 16 bit, 100ns | £10 | 4 | - | - | 2wks |
| STORAGE Cartridge | Cartridges | £5 | 2 | - | - | 2wks |
| CASE DESKTOP | int keyboard, 3 ext ports (+ exp) | £25 | 1 | 10wks | £20 | 5wks |
| Misc | resistors,caps,etc | £0.5 | 100 | - | - | - |

Missing:
- BOARD
- DISPLAY
- ROM: sys:bootloader 8k, sys:kernel 8k, sys:libs 8k, sys:drivers 4k, bas:kernel 8k, bas:corelib 8k
- IOP-S (serial) x2
- IOP-X (SCSI)
- INTSND (sound)

### Software
| Company | Component | Producer | Code Size | Unit Cost (£/per unit) | Design Cost (wks) | Redesign Cost (wks) | Stored On |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Synful | Boot ldr & HWcfg | In House | 6k | - | 2wks | 2wks | ROM |
| Synful | Sys: Kernel | In House/ HB/OS | 8k | - | 8wks | 6wks | ROM |
| Synful | SYS: Libraries | In House/ HB/OS | 8k | - | - | 4wks | ROM |
| Synful | SYS: Drivers | In House/ HB/OS | 4k | - | - | 2wks | ROM |
| Synful | SYS: Extensions | In House/ HB/OS | 64k | - | 2wks | 3wks | DISK |
| Synful | SYS: GameSnd | In House/ HB/OS | 128k | - | 2wks | 2wks | DISK |
| Synful | BAS: Kernel | In House/ HB OS | 8k | - | 8wks | 4wks | ROM |
| Synful | BAS: core lib&I/O | In House/ HB OS | 8k | - | - | 4wks | ROM |
| Synful | BAS: fs libs | In House/ HB OS | 4k | - | 2wks | 2wks | DISK |
| Synful | BAS: GUI | In House/ HB OS | 800k | £75/disk set | 8wks | 4wks | DISK |
| Synful | Emulator | In House | 64KB | - | 6wks | 2wks | DISK |
