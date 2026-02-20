# Home Network Security Audit — NIST CSF Based Assessment

**Role:** SOC Analyst (N1) — Lab / Home Environment  
**Date:** 2026-02-20  
**Scope:** 192.168.1.0/24 (LAN only)  
**Tools:** Nmap, Netcat (nc)  
**Framework:** NIST CSF (ID, PR, DE, RS, RC)

---

## Executive Summary
This repository documents a basic LAN security assessment using a NIST CSF structure.
It contains raw evidence (command outputs), findings with risk ratings, and an action plan.

**Key highlights**
- Asset inventory (host discovery) and exposed TCP services observed on the LAN
- Findings written in a SOC-friendly format (evidence → risk → recommendation)
- Practical hardening and monitoring roadmap (24h / 7d / 30d)

---

## Repository Map
- **docs/**: methodology, NIST mapping, risk matrix, action plan
- **evidence/**: raw outputs (immutable) + hashes
- **findings/**: one file per finding (ticket-style)
- **diagrams/**: topology diagram (.drawio + .png)
- **scripts/**: helpers to collect evidence and generate checksums
- **changelog/**: what changed per date

---

## Start Here
1. Read: [`docs/executive-summary.md`](docs/executive-summary.md)  
2. Review findings: [`findings/README.md`](findings/README.md)  
3. Validate evidence: [`evidence/README.md`](evidence/README.md)  

---

## Notes
- **Out of scope:** exploitation, credential testing, WAN exposure, UDP scanning, firmware extraction.
- Some ports may show as **tcpwrapped**, limiting service fingerprinting.
