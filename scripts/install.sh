#!/bin/bash
#
# CERBERUS + KINGDOM CORE - Complete Installation Script
# Installs all components on Termux/Android or Linux
#

set -e

echo "⚔️ CERBERUS + KINGDOM CORE INSTALLATION"
echo "========================================"
echo ""

# ========================================================================
# 1. CREATE DIRECTORY STRUCTURE
# ========================================================================
echo "[1/5] Creating directory structure..."

mkdir -p ~/KINGDOM_ENGINE/core
mkdir -p ~/KINGDOM_ENGINE/watchdogs
mkdir -p ~/KINGDOM_ENGINE/inbox
mkdir -p ~/KINGDOM_ENGINE/shaken
mkdir -p ~/KINGDOM_ENGINE/processed/accepted
mkdir -p ~/KINGDOM_ENGINE/processed/quarantine
mkdir -p ~/KINGDOM_ENGINE/clean
mkdir -p ~/KINGDOM_ENGINE/logs
mkdir -p ~/.termux/boot

echo "✓ Directories created"

# ========================================================================
# 2. INSTALL DEPENDENCIES
# ========================================================================
echo "[2/5] Installing dependencies..."

if command -v pkg &> /dev/null; then
    # Termux environment
    pkg update -y 2>&1 | grep -v "^Reading" || true
    pkg install -y python 2>&1 | grep -v "^Reading" || true
    pkg install -y termux-api 2>&1 | grep -v "^Reading" || true
elif command -v apt &> /dev/null; then
    # Linux environment
    sudo apt update -y
    sudo apt install -y python3 python3-pip
fi

pip install --quiet --no-cache-dir flask 2>&1 | grep -v "^Requirement" || true

echo "✓ Dependencies installed"

# ========================================================================
# 3. COPY CORE FILES
# ========================================================================
echo "[3/5] Installing core components..."

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Copy Python scripts
cp "$PROJECT_DIR/core/hardcore_processor.py" ~/KINGDOM_ENGINE/core/
cp "$PROJECT_DIR/core/throne_daemon.py" ~/KINGDOM_ENGINE/core/
cp "$PROJECT_DIR/watchdogs/head1_sniffer.py" ~/KINGDOM_ENGINE/watchdogs/
cp "$PROJECT_DIR/watchdogs/head4_gatekeeper.py" ~/KINGDOM_ENGINE/watchdogs/

chmod +x ~/KINGDOM_ENGINE/core/*.py
chmod +x ~/KINGDOM_ENGINE/watchdogs/*.py

echo "✓ Core components installed"

# ========================================================================
# 4. CREATE STARTUP SCRIPTS
# ========================================================================
echo "[4/5] Creating startup scripts..."

# Start script
cat > ~/start_kingdom.sh << 'START_EOF'
#!/bin/bash
echo "⚔️ Starting KINGDOM CORE..."
mkdir -p ~/KINGDOM_ENGINE/logs

# Start Throne daemon
nohup python3 ~/KINGDOM_ENGINE/core/throne_daemon.py >> ~/KINGDOM_ENGINE/logs/throne.log 2>&1 &
THRONE_PID=$!
echo "✓ The Throne is running (PID: $THRONE_PID)"

# Start Head 1 Sniffer
nohup python3 ~/KINGDOM_ENGINE/watchdogs/head1_sniffer.py >> ~/KINGDOM_ENGINE/logs/head1.log 2>&1 &
HEAD1_PID=$!
echo "✓ Head 1 Sniffer is running (PID: $HEAD1_PID)"

# Start Head 4 Gatekeeper
nohup python3 ~/KINGDOM_ENGINE/watchdogs/head4_gatekeeper.py >> ~/KINGDOM_ENGINE/logs/head4.log 2>&1 &
HEAD4_PID=$!
echo "✓ Head 4 Gatekeeper is running (PID: $HEAD4_PID)"

echo ""
echo "📊 Dashboard: http://127.0.0.1:5200/status"
echo "📂 Drop files in: ~/KINGDOM_ENGINE/inbox/"
echo ""
echo "PIDs: Throne=$THRONE_PID Head1=$HEAD1_PID Head4=$HEAD4_PID"
START_EOF

chmod +x ~/start_kingdom.sh

# Stop script
cat > ~/stop_kingdom.sh << 'STOP_EOF'
#!/bin/bash
echo "⛔ Stopping KINGDOM CORE..."
pkill -f "throne_daemon.py" || true
pkill -f "head1_sniffer.py" || true
pkill -f "head4_gatekeeper.py" || true
echo "✓ All services stopped"
STOP_EOF

chmod +x ~/stop_kingdom.sh

# Status script
cat > ~/kingdom_status.sh << 'STATUS_EOF'
#!/bin/bash
echo "📊 KINGDOM CORE STATUS"
echo "====================="
echo ""

echo "Processes:"
ps aux | grep -E "(throne_daemon|head1_sniffer|head4_gatekeeper)" | grep -v grep || echo "  (none running)"

echo ""
echo "Inbox:"
ls -lh ~/KINGDOM_ENGINE/inbox/ 2>/dev/null | tail -5 || echo "  (empty)"

echo ""
echo "Accepted:"
ls -lh ~/KINGDOM_ENGINE/processed/accepted/ 2>/dev/null | tail -5 || echo "  (empty)"

echo ""
echo "Quarantine:"
ls -lh ~/KINGDOM_ENGINE/processed/quarantine/ 2>/dev/null | tail -5 || echo "  (empty)"

echo ""
echo "Recent Logs:"
tail -5 ~/KINGDOM_ENGINE/logs/throne.log 2>/dev/null || echo "  (no logs)"
STATUS_EOF

chmod +x ~/kingdom_status.sh

echo "✓ Startup scripts created"

# ========================================================================
# 5. BOOT AUTOSTART (Termux only)
# ========================================================================
echo "[5/5] Setting up autostart..."

if [ -d ~/.termux/boot ]; then
    cat > ~/.termux/boot/kingdom_start.sh << 'BOOT_EOF'
#!/data/data/com.termux/files/usr/bin/bash
termux-wake-lock
sleep 2
nohup python3 ~/KINGDOM_ENGINE/core/throne_daemon.py >> ~/KINGDOM_ENGINE/logs/throne.log 2>&1 &
nohup python3 ~/KINGDOM_ENGINE/watchdogs/head1_sniffer.py >> ~/KINGDOM_ENGINE/logs/head1.log 2>&1 &
nohup python3 ~/KINGDOM_ENGINE/watchdogs/head4_gatekeeper.py >> ~/KINGDOM_ENGINE/logs/head4.log 2>&1 &
BOOT_EOF
    
    chmod +x ~/.termux/boot/kingdom_start.sh
    echo "✓ Autostart configured (will start on device reboot)"
fi

echo ""
echo "✅ INSTALLATION COMPLETE"
echo "======================="
echo ""
echo "🚀 Next Steps:"
echo "1. Start the system: ~/start_kingdom.sh"
echo "2. Check status: ~/kingdom_status.sh"
echo "3. View dashboard: http://127.0.0.1:5200/status"
echo "4. Drop files in: ~/KINGDOM_ENGINE/inbox/"
echo ""
echo "⚔️ CERBERUS + KINGDOM CORE is ready!"
echo ""
