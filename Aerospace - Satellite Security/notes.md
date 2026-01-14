# Overview

## Basic Satellite Systems
### Type Of Orbit

#### LEO
- ~160-2.000 km from earth
- Orbit Period: ~90-120 min

#### MEO (Medium Earth Orbit)
- ~2.000–35.000 km from earth (ex: GPS)
-

#### GEO (Geostationary)
- ~35.786 km from earth

> Satellite security learning = LEO + CubeSat

### OBC — On-Board Computer (TARGET UTAMA)
Fungsi:
- Otak satelit
- Menjalankan firmware
- Mengatur semua subsystem

### Biasanya:
ARM Cortex
RTOS / Embedded Linux

## Attack Surface OBC

Diserang via:
- Telecommand (TC)
- Firmware logic
- State machine

Jenis serangan:
- Command injection
- Buffer overflow
- Logic flaw
- Privilege escalation
- Debug mode abuse

Realita pahit
Banyak CubeSat:
- Hardcoded key
- No ASLR
- No stack 


EPS (Electrical Power System)
Fungsi:
- Solar panel
- Battery

- Power distribution

### Resources:
https://github.com/deptofdefense/hack-a-sat-library
https://forum.defcon.org/node/231910 
https://hackasat.com/moonlighter/ 
