#!/usr/bin/env bash
set -euo pipefail

DATE="2026-02-20"
OUT_DIR="evidence/${DATE}"
mkdir -p "${OUT_DIR}"

# 00 - Scope note (edit as needed)
cat > "${OUT_DIR}/00_scope.txt" <<'EOF'
Scope: 192.168.1.0/24 (LAN only)
In-scope: host discovery, fast TCP scan, targeted validation
Out-of-scope: exploitation, credential testing, WAN exposure validation, UDP scanning
EOF

# 01 - Routing
ip route | tee "${OUT_DIR}/01_ip_route.txt"

# 02 - Host discovery
sudo nmap -sn -PR 192.168.1.0/24 | tee "${OUT_DIR}/02_host_discovery_nmap_sn_pr.txt"

# 03 - Fast open ports (edit target IPs if changed)
sudo nmap -T4 -F --open 192.168.1.3 192.168.1.4 192.168.1.5 192.168.1.21 192.168.1.254 | tee "${OUT_DIR}/03_fast_open_ports.txt"

echo "[+] Done. Now run: bash scripts/hash_evidence.sh $OUT_DIR"
