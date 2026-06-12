#!/usr/bin/env bash
# scripts/setup_data.sh
# Bootstrap static port data from free public sources.
# Run once after cloning: bash scripts/setup_data.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW="$ROOT/data/raw"

echo "==> Setting up raw data directories..."
mkdir -p "$RAW/ports/unlocode"
mkdir -p "$RAW/ports/wpi"
mkdir -p "$RAW/ports/plsci"
mkdir -p "$RAW/ports/lpi"

# ── UN/LOCODE ────────────────────────────────────────────────────────────────
echo ""
echo "==> UN/LOCODE"
echo "    Manual step: download the CSV/TXT from:"
echo "    https://unece.org/trade/uncefact/unlocode"
echo "    Place files in: $RAW/ports/unlocode/"

# ── World Port Index ──────────────────────────────────────────────────────────
echo ""
echo "==> NGA World Port Index (WPI)"
echo "    Manual step: download from:"
echo "    https://msi.nga.mil/Publications/WPI"
echo "    Place files in: $RAW/ports/wpi/"

# ── UNCTAD PLSCI ──────────────────────────────────────────────────────────────
echo ""
echo "==> UNCTAD Port Liner Shipping Connectivity Index"
echo "    Manual step: download from UNCTADstat:"
echo "    https://unctadstat.unctad.org/datacentre/reportInfo/US.PLSCI"
echo "    Place CSV in: $RAW/ports/plsci/"

# ── World Bank LPI ────────────────────────────────────────────────────────────
echo ""
echo "==> World Bank LPI 2.0"
WB_LPI_URL="https://lpi.worldbank.org/sites/default/files/2024-04/LPI_Data_2023_2024.xlsx"
echo "    Attempting download from World Bank..."
if curl -fsSL --max-time 60 -o "$RAW/ports/lpi/LPI_2023_2024.xlsx" "$WB_LPI_URL" 2>/dev/null; then
    echo "    Downloaded: LPI_2023_2024.xlsx"
else
    echo "    Download failed — visit https://lpi.worldbank.org/en/home to download manually."
    echo "    Place file in: $RAW/ports/lpi/"
fi

echo ""
echo "==> setup_data.sh complete."
echo "    After placing manual downloads, run:"
echo "    python scripts/build_graph.py"
