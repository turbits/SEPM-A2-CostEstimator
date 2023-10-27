# Synputer Cost Estimator

This is a piece of software built as part of "Assignment 2 - Presentation" for the Software Engineering Project Management course at the University of Essex Online by Group 1, consisting of:
- Nassar Al-Naimi
- Charles Kuyuyama
- Abdulah Alihu Ngamjeh
- Trevor Woodman

## The Fictitious Scenario

This project is based on a fictional scenario in which two computing companies have a dialogue regarding a computer that is being developed which outlines the specifications of the system, culminating in one of them placing an order for 2000 units based on their discussion.

Synful Computing, one of the companies involved in this scenario, is developing a new and fairly groundbreaking computer they internally call the "Synputer". Colin Syn, the owner, is one of the two participants in the discussion.

Will Burns, the managing director of the second company, EDC, has agreed to purchase 2000 units based on the specification discussed by them in their meeting, at an agreed at-cost price of £250 per unit, for an order total of £500,000.

The following specification is based on the dialogue in the case study, included in the documents folder, and two bill of materials (BOM) provided by the assignment brief for software and hardware, also included. We had to pick materials from these two BOMs. There are some oddities, for example "INTSND" appears to be a made-up term. Based on context ("mono snd" or "3ch snd" options) we can deduce that it is for sound. We assume this stands for something like "internal sound", although it is not defined anywhere.

In the specifications for the Syn Vectra, the items are written as they appear in the BOMs. Some text in the BOMs, such as the varied shorthand writing, is written esoterically and near unreadable for presumably no other reason than to make it difficult to complete this component of the course. If something is unclear or misinterpreted, please keep this in mind.

According to the case study, a complete system consists of the following components:
- 1 or more ROMs (according to a different part of the case study, the board can only support 2)
- 4 'glue chips' (G1-G4) / ULAs
- 1 CPU
- 4 RAM chips
- interface (I/O) chips for serial, keyboard, video output, keyboard, screen, storage drive(s), and a case per design


## SYN VECTRA SPECIFICATION
COST PRICE (EDC at-cost order): £250
SALE PRICE: £????

### HARDWARE
| Component | Model | Spec | Notes | Unit Cost £(per 1000) | Quantity (per board) | Design Cost (weeks) | Manufacture Cost £(unit per 1000) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CPU | 68k0 | 8MHz, 16/32, 16MB max RAM | | 8 | 1 | - | - |
| BOARD-SCKT | A83-S | All ICs have sockets | | 25 | 1 | 8 | 14 |
| ROM1 | 16K | 16 KB ROM chip | Boot ldr & HWcfg (6KB), SYS: Kernel (8KB) | 2 | 1 | 4 | - |
| ROM2 | 32K | 32 KB ROM chip | SYS: Libraries(8KB), Drivers(4KB) & BAS: Kernel (8KB), core lib&I/O (8KB), fs libs (4KB) | 4 | 1 | 4 | - |
| RAM1 | 512Kb | 16 bit, 100ns | | 10 | 4 | - | - |
| RAM2 | 512Kb | 16 bit, 100ns | | 10 | 4 | - | - |
| RAM3 | 512Kb | 16 bit, 100ns | | 10 | 4 | - | - |
| RAM4 | 512Kb | 16 bit, 100ns | | 10 | 4 | - | - |
| Pro Expansion | ProEx | CPU-Glue-SCSI - 4xRAM | Needed for SCSI | 15 | 1 | - | - |
| ULA1 | G1 | glue IOP-CPU | | 5 | 1 | 4 | - |
| ULA2 | G2 | glue RAM-CPU | | 5 | 1 | 4 | - |
| ULA3 | G3 | glue DISP-CPU | | 5 | 1 | 4 | - |
| ULA4 | G4 | glue SYSTEM | | 5 | 1 | 4 | - |
| INTSND | YM2149 | 3 ch snd, env, 2 8-bit ports | | 2.5 | 1 | - | - |
| IOP-S | 16550 UART | 1 ch serial port | | 5 | 1 | - | - |
| IOP-S (a second serial port)| 1655- UART | 1 ch serial port | | 5 | 1 | - | - |
| IOP-J | 16550 UART | 1 ch serial port | | 5 | 1 | - | - |
| IOP-X | SCSI | SCSI interface & terminator | | 5 | 1 | - | - |
| DISPLAY | ? | ? | ? | ? | ? | ? | ? |
| CASE | LUGGABLE | ext keyboard, 4 ext ports (+exp) | | 35 | 1 | 10 | 20 |
| KEYB | ext | ext keyboard for system | | 7.5 | 1 | - | - |
| Misc | resistors, caps, etc | - | | 0.5 | 100 | 0 | 0 |

Total Unit Cost: £179.50 (currently)

### SOFTWARE

*Note*: The "Coding Cost (person weeks)" column is empty in the software BOM, not sure why

| Company | Component | Producer | Code Size | Design Cost (weeks) | Core System | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Synful | Boot ldr & HWcfg | In House | 6k | 2 | yes | in ROM1 |
| Synful | SYS: Kernel | In House/HBOS | 8k | 8 | yes | in ROM1 |
| Synful | SYS: Libraries | In House/HBOS | 8k | - | yes | in ROM2 |
| Synful | SYS: Drivers | In House/HBOS | 4k | - | yes | in ROM2 |
| Synful | BAS:Kernel | In House/HBOS | 8k | 8 | yes | in ROM2 |
| Synful | BAS: core lib&I/O | In House/HBOS | 8k | - | yes | in ROM2 |
| Synful | BAS: fs libs | In House/HBOS | 4k | - | yes | in ROM2 |
| EZ-SYS | EZ-Suite | 3rd party | 520KB | 10 | no | on bundled disk, £25 per machine |
| EZ-SYS | HBConv | 3rd party | 128KB | 8 | no | converts TeleBasic to HyperBasic, £55 per license |

For whatever reason, the storage mediums are on the software BOM, and have a dollar sign $ instead of a pound sign £. I assume that this is yet another content error, and that the prices are in GBP.

| Component | Unformatted Size | Formatted Size | Cost |
| Floppy | 1MB | 720KB | $5 |
| Cartridge | 300KB | 160KB | $2 |





## Project Overview
The Synputer Cost Estimator is a software tool developed to facilitate cost estimation for the project.
