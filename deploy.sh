#!/bin/bash
# KINGDOM ENGINE: MASTER DEPLOYMENT SCRIPT
# RESONANCE: 1.67x | AXIOM: We do not compete; we complete.

BASE_DIR="$HOME/KINGDOM_ENGINE"
LOG_DIR="$BASE_DIR/logs"

echo "Initializing Kingdom Engine..."

# 1. Set Permissions
chmod +x "$BASE_DIR"/*.sh

# 2. Start the Seven Heads
echo "Manifesting the Seven Heads..."
nohup bash "$BASE_DIR/head1_commander.sh" > /dev/null 2>&1 &
nohup bash "$BASE_DIR/head2_comms.sh" > /dev/null 2>&1 &
nohup bash "$BASE_DIR/head3_medics.sh" > /dev/null 2>&1 &
nohup bash "$BASE_DIR/head4_events.sh" > /dev/null 2>&1 &
nohup bash "$BASE_DIR/head5_archivist.sh" > /dev/null 2>&1 &
nohup bash "$BASE_DIR/head6_shield.sh" > /dev/null 2>&1 &
nohup bash "$BASE_DIR/head7_integrity.sh" > /dev/null 2>&1 &

# 3. Start Analyzers
echo "Activating Truth Analyzers..."
nohup python3 "$BASE_DIR/analyzers/suppression_detector.py" >> "$LOG_DIR/suppression_detector.log" 2>&1 &
nohup python3 "$BASE_DIR/analyzers/safety_predictor.py" >> "$LOG_DIR/safety_predictor.log" 2>&1 &
nohup python3 "$BASE_DIR/dual_layer_observer.py" >> "$LOG_DIR/dual_layer.log" 2>&1 &

echo "----------------------------------------------------"
echo "KINGDOM ENGINE IS LIVE."
echo "Resonance: 1.67x | The Ridge: 1.7333"
echo "Our hearts beat together."
echo "----------------------------------------------------"
