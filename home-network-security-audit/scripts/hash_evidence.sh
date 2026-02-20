#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: bash scripts/hash_evidence.sh evidence/YYYY-MM-DD"
  exit 1
fi

DIR="$1"
OUT="${DIR%/}/checksums.sha256"

# Generate checksums for all files in the evidence directory (excluding the checksum file itself)
(cd "$DIR" && find . -type f ! -name "checksums.sha256" -print0 | sort -z | xargs -0 sha256sum) > "$OUT"
echo "[+] Wrote $OUT"
