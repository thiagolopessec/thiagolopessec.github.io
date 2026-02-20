# Methodology

## In scope
- Host discovery on 192.168.1.0/24 (LAN only)
- Fast TCP port scan on selected hosts
- Targeted validation for observed ports (service detection, basic probes)

## Out of scope
- Exploitation and vulnerability testing
- Credential testing (default passwords, brute force)
- Router admin login review
- WAN/Internet exposure validation
- UDP scanning and full-port scanning for all hosts

## Evidence handling
- Raw outputs are stored under `evidence/YYYY-MM-DD/`
- A checksum file is generated to support integrity verification
