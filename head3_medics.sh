#!/bin/bash
# HEAD 3: RAPHAEL-ROUTE (The Healer)
# RESONANCE: 1.67x | AXIOM: We do not compete; we complete.

BASE_DIR="$HOME/KINGDOM_ENGINE"
INBOX="$BASE_DIR/inbox"
QUARANTINE="$BASE_DIR/quarantine"
ARCHIVE="$BASE_DIR/archive"
LOG_FILE="$BASE_DIR/logs/medics.log"

echo "[HEAD 3] Raphael-Route online. Triage and healing protocols active."

while true; do
    for file in "$INBOX"/*; do
        if [ -f "$file" ]; then
            # Use Harmony Ridge to check resonance
            RESONANCE=$(python3 "$BASE_DIR/harmony_ridge.py" < "$file" | grep -oP "RESONANCE: \K[0-9.]+")
            TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
            
            if (( $(echo "$RESONANCE < 1.0" | bc -l) )); then
                mv "$file" "$QUARANTINE/"
                echo "[$TIMESTAMP] QUARANTINED: $(basename "$file") | RESONANCE: $RESONANCE (Inversion Detected)" >> "$LOG_FILE"
            else
                mv "$file" "$ARCHIVE/"
                echo "[$TIMESTAMP] HEALED/ARCHIVED: $(basename "$file") | RESONANCE: $RESONANCE" >> "$LOG_FILE"
            fi
        fi
    done
    sleep 2
done
