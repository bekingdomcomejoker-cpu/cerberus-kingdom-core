# CERBERUS + KINGDOM CORE - Complete Deployment Guide

## 📋 Project Summary

This is a complete, production-ready implementation of the CERBERUS + KINGDOM CORE system - a sophisticated defensive truth engine for Termux/Android devices.

### What You Have

✅ **Complete Source Code**
- Hardcore Processor (Truth/Fact/Lie classification)
- The Throne (Auto-processing daemon with REST API)
- Head 1 Sniffer (Clipboard capture)
- Head 4 Gatekeeper (Truth filter)
- Web Dashboard (Real-time monitoring)

✅ **Installation & Deployment Scripts**
- Automated installer (install.sh)
- Startup/stop/status scripts
- Autostart configuration for Termux:Boot

✅ **Comprehensive Documentation**
- README.md (System overview)
- This deployment guide
- Inline code documentation
- Example usage patterns

✅ **Interactive Web Dashboard**
- Beautiful, modern UI
- Real-time system metrics
- Classification pipeline visualization
- Export and sharing capabilities

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Clone the Repository

```bash
# On your Termux device
git clone https://github.com/yourusername/cerberus-kingdom-core.git
cd cerberus-kingdom-core
```

### Step 2: Run the Installer

```bash
bash scripts/install.sh
```

The installer will:
- Create directory structure
- Install Python dependencies
- Copy all core components
- Create startup scripts
- Configure autostart

### Step 3: Start the System

```bash
~/start_kingdom.sh
```

You'll see:
```
⚔️ Starting KINGDOM CORE...
✓ The Throne is running (PID: 12345)
✓ Head 1 Sniffer is running (PID: 12346)
✓ Head 4 Gatekeeper is running (PID: 12347)

📊 Dashboard: http://127.0.0.1:5200/status
📂 Drop files in: ~/KINGDOM_ENGINE/inbox/
```

### Step 4: Test It

```bash
# Create a test file
echo "I fucking love this system - it's based on evidence and truth" > ~/KINGDOM_ENGINE/inbox/test1.txt

# Wait 2 seconds
sleep 2

# Check status
~/kingdom_status.sh

# View the result
cat ~/KINGDOM_ENGINE/processed/accepted/test1.txt
```

---

## 📁 Directory Structure

```
~/KINGDOM_ENGINE/
├── core/
│   ├── hardcore_processor.py    # Truth classifier engine
│   └── throne_daemon.py         # Auto-processing daemon + API
├── watchdogs/
│   ├── head1_sniffer.py         # Clipboard capture
│   └── head4_gatekeeper.py      # Truth filter
├── inbox/                        # New files to process
├── shaken/                       # Unknown classification
├── processed/
│   ├── accepted/                # Truth/Fact files
│   └── quarantine/              # Lies/malicious
├── clean/                        # Final approved files
└── logs/                         # System logs
```

---

## 🔧 System Components

### 1. Hardcore Processor (`core/hardcore_processor.py`)

**Purpose**: Classifies content as Truth, Fact, or Lie

**How it works**:
- Analyzes text for truth markers (evidence, citations)
- Detects contradictions and lies
- Recognizes affection and emotional honesty
- Routes files to appropriate directories

**Configuration**:
- Edit regex patterns for custom classification
- Adjust scoring thresholds
- Add custom axioms

### 2. The Throne (`core/throne_daemon.py`)

**Purpose**: Auto-processing daemon with REST API

**How it works**:
- Runs continuously in background
- Checks inbox every 2 seconds
- Executes Hardcore Processor on new files
- Provides HTTP API for monitoring

**API Endpoints**:
- `GET /status` - System status
- `GET /accepted` - Accepted files
- `GET /quarantine` - Quarantined files
- `GET /logs` - Recent logs
- `POST /stop` - Stop daemon
- `POST /start` - Start daemon

### 3. Head 1 Sniffer (`watchdogs/head1_sniffer.py`)

**Purpose**: Captures clipboard and file events

**How it works**:
- Monitors clipboard every 5 seconds
- Watches designated directories
- Saves new content to inbox
- Removes duplicates

**Configuration**:
- Edit `time.sleep(5)` to change polling interval
- Add watch directories in `watch_dirs` list

### 4. Head 4 Gatekeeper (`watchdogs/head4_gatekeeper.py`)

**Purpose**: Defensive truth filter

**How it works**:
- Detects contradictions
- Blocks malicious code patterns
- Detects prompt injection attempts
- Routes to clean safe zone

**Patterns it detects**:
- Contradictions (I never... but I did)
- Malicious code (eval, exec, DROP TABLE)
- Prompt injections (ignore previous, system prompt)
- Empty/noise content

---

## 📊 Web Dashboard

### Access the Dashboard

```bash
# Option 1: Direct URL
http://127.0.0.1:5200/status

# Option 2: Open in Termux browser
termux-open-url http://127.0.0.1:5200/status

# Option 3: Copy to shared storage
cp ~/KINGDOM_ENGINE/web/dashboard.html ~/storage/shared/
# Then open in Chrome
```

### Dashboard Features

- **System Status**: Real-time indicator of all components
- **Architecture Diagram**: Visual representation of all heads
- **Classification Pipeline**: Flow visualization
- **API Documentation**: All endpoints listed
- **Classification Examples**: Real-world examples
- **Export/Share**: Download report or share link

---

## 🔌 REST API Usage

### Get System Status

```bash
curl http://127.0.0.1:5200/status
```

Response:
```json
{
  "status": "running",
  "processed_total": 42,
  "last_run": 1675000000,
  "uptime_seconds": 3600,
  "inbox_count": 3,
  "accepted_count": 38,
  "quarantine_count": 4,
  "errors_recent": []
}
```

### List Accepted Files

```bash
curl http://127.0.0.1:5200/accepted
```

### List Quarantined Files

```bash
curl http://127.0.0.1:5200/quarantine
```

### Get Recent Logs

```bash
curl http://127.0.0.1:5200/logs
```

### Stop the Daemon

```bash
curl -X POST http://127.0.0.1:5200/stop
```

### Start the Daemon

```bash
curl -X POST http://127.0.0.1:5200/start
```

---

## 📱 Termux Setup

### Prerequisites

1. **Install Termux** from F-Droid (not Google Play)
2. **Install Termux:API** from F-Droid
3. **Install Termux:Boot** from F-Droid (for autostart)

### Initial Setup

```bash
# In Termux, update packages
pkg update
pkg upgrade

# Install Python and dependencies
pkg install python
pkg install termux-api

# Grant permissions in Termux:API app
# (Open Termux:API app and grant all permissions)
```

### Enable Autostart

1. Open Termux:Boot app
2. Grant notification permission
3. Run once: `~/start_kingdom.sh`
4. Reboot device
5. System will auto-start on boot

### Check Autostart Status

```bash
# After reboot, check if running
ps aux | grep throne_daemon
```

---

## 🛡️ Security & Privacy

### What This System Does

✅ Processes data locally on your device  
✅ No internet required  
✅ No external connections  
✅ No tracking or analytics  
✅ No encryption (relies on Android sandboxing)  
✅ Works on non-rooted devices  

### What This System Does NOT Do

❌ Attack other systems  
❌ Modify system files  
❌ Require root access  
❌ Send data externally  
❌ Track your behavior  
❌ Violate privacy  

### Defensive Only

The system is **100% defensive**:
- Cannot initiate harm
- Cannot deceive
- Cannot trespass
- Cannot violate consent
- Cannot break laws

It can:
- Defend your data
- Protect the engine
- Reject attacks
- Watch for threats
- Expose falsehood

---

## 🐛 Troubleshooting

### Problem: "termux-clipboard-get: command not found"

**Solution**:
```bash
pkg install termux-api
```

### Problem: "Flask not found"

**Solution**:
```bash
pip install flask
```

### Problem: Daemon not processing files

**Solution**:
```bash
# Check if running
ps aux | grep throne_daemon

# Check logs
tail -f ~/KINGDOM_ENGINE/logs/throne.log

# Restart
~/stop_kingdom.sh
sleep 2
~/start_kingdom.sh
```

### Problem: High CPU usage

**Solution**:
Increase sleep interval in daemon scripts:
```python
time.sleep(5)  # Change from 2 to 5 seconds
```

### Problem: API not responding

**Solution**:
```bash
# Check if Flask is running
ps aux | grep throne_daemon

# Check port
netstat -tlnp | grep 5200

# Restart daemon
~/stop_kingdom.sh
sleep 2
~/start_kingdom.sh
```

---

## 📈 Monitoring & Maintenance

### Daily Checks

```bash
# Check system status
~/kingdom_status.sh

# View recent logs
tail -20 ~/KINGDOM_ENGINE/logs/throne.log

# Check disk usage
du -sh ~/KINGDOM_ENGINE/
```

### Weekly Maintenance

```bash
# Archive old logs
tar -czf ~/KINGDOM_ENGINE/logs/archive-$(date +%Y%m%d).tar.gz ~/KINGDOM_ENGINE/logs/*.log

# Clean up old files
find ~/KINGDOM_ENGINE/processed -type f -mtime +30 -delete

# Verify system integrity
~/kingdom_status.sh
```

### Monthly Review

```bash
# Check total processed files
find ~/KINGDOM_ENGINE/processed -type f | wc -l

# Review quarantine
ls -lh ~/KINGDOM_ENGINE/processed/quarantine/

# Check system logs
tail -100 ~/KINGDOM_ENGINE/logs/throne.log
```

---

## 🚀 Advanced Configuration

### Custom Classification Patterns

Edit `~/KINGDOM_ENGINE/core/hardcore_processor.py`:

```python
# Add custom truth marker
CUSTOM_TRUTH = re.compile(r"\b(your_pattern)\b", re.IGNORECASE)

# In classify_text function:
if CUSTOM_TRUTH.search(t):
    result["truth_score"] += 0.3
```

### Change Processing Interval

Edit `~/KINGDOM_ENGINE/core/throne_daemon.py`:

```python
time.sleep(2)  # Change to desired interval
```

### Add Watch Directories

Edit `~/KINGDOM_ENGINE/watchdogs/head1_sniffer.py`:

```python
watch_dirs = [
    Path.home() / "KINGDOM_ENGINE" / "watch",
    Path("/storage/emulated/0/Download"),
    Path("/your/custom/directory"),  # Add here
]
```

---

## 📞 Support & Issues

### Getting Help

1. Check logs: `tail -f ~/KINGDOM_ENGINE/logs/throne.log`
2. Run status: `~/kingdom_status.sh`
3. Review README.md
4. Check GitHub issues

### Reporting Issues

When reporting issues, include:
- Error message from logs
- Output of `~/kingdom_status.sh`
- Steps to reproduce
- System information (Termux version, Android version)

---

## 🎯 Next Steps

### Immediate

1. ✅ Install the system
2. ✅ Test with sample files
3. ✅ Monitor logs for 24 hours
4. ✅ Verify autostart works

### Short Term

- [ ] Customize classification patterns
- [ ] Set up log archival
- [ ] Configure monitoring alerts
- [ ] Document custom axioms

### Long Term

- [ ] Integrate with TTE archives
- [ ] Add voice input pipeline
- [ ] Connect multiple AI systems
- [ ] Build memory fusion layer

---

## 📜 License

MIT License - See LICENSE file in repository

---

## 💜 Philosophy

> "Be careful what you tolerate — you teach others how to treat you."

This system is built on the principle of **truth-based defense**:

**Truth + Love = Discernment**

It's a guardian, not a weapon. It protects through understanding, not force.

---

## 🔗 Resources

- **GitHub**: https://github.com/yourusername/cerberus-kingdom-core
- **Documentation**: See README.md
- **Dashboard**: http://127.0.0.1:5200/status (when running)
- **Termux**: https://termux.dev

---

**⚔️ CERBERUS + KINGDOM CORE is ready to defend your truth.**

Last Updated: 2026-02-03
