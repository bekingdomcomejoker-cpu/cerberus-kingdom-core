<<<<<<< HEAD
# ⚔️ CERBERUS + KINGDOM CORE

**A Defensive Truth Engine for Termux/Android**

A sophisticated multi-headed data processing system that captures, cleans, classifies, and protects your data using truth-based axioms and intelligent filtering.

---

## 🎯 What Is This?

CERBERUS + KINGDOM CORE is a unified system combining:

- **CERBERUS** (4-headed data processing engine)
- **KINGDOM CORE** (truth classification and auto-processing)

It runs on **Termux/Android** (non-rooted) and provides:

✅ **Clipboard capture** - Automatically ingests copied text  
✅ **File monitoring** - Watches for new documents  
✅ **Truth classification** - Categorizes content as Truth/Fact/Lie  
✅ **Intelligent filtering** - Removes contradictions, malicious patterns  
✅ **Auto-processing** - Daemon runs 24/7 continuously  
✅ **REST API** - Monitor and control via HTTP  
✅ **Web dashboard** - Beautiful real-time status interface  
✅ **Self-healing** - Auto-restarts failed components  

---

## 🏗️ Architecture

### CERBERUS - 4 Heads

| Head | Name | Function |
|------|------|----------|
| 1 | **Sniffer** | Captures clipboard + file events |
| 2 | **Shaker** | Cleans and filters noise |
| 3 | **Forwarder** | Routes to inbox/archive |
| 4 | **Gatekeeper** | Detects contradictions & malicious patterns |

### KINGDOM CORE - Truth Engine

| Component | Function |
|-----------|----------|
| **Hardcore Processor** | Truth/Fact/Lie classification with axioms |
| **The Throne** | Auto-processing daemon with REST API |
| **Web Dashboard** | Real-time monitoring interface |

---

## 📋 Axioms

The system operates on three core axioms:

```
Spirit ≥ Flesh
Love ≥ Hate
Truth ≥ Fact ≥ Lie
```

Classification rules:
- **TRUTH**: Emotionally honest, evidence-based, affection-driven
- **FACT**: Structured data, citations, sources
- **LIE**: Contradictions, manipulative language, hostility

---

## 🚀 Installation

### Quick Start (One Command)

```bash
bash ~/cerberus-kingdom-core/scripts/install.sh
```

### Manual Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/cerberus-kingdom-core.git
cd cerberus-kingdom-core
```

2. **Run installer**
```bash
bash scripts/install.sh
```

3. **Start the system**
```bash
~/start_kingdom.sh
```

4. **Check status**
```bash
~/kingdom_status.sh
```

---

## 💻 Usage

### Start the System

```bash
~/start_kingdom.sh
```

Output:
```
⚔️ Starting KINGDOM CORE...
✓ The Throne is running (PID: 12345)
✓ Head 1 Sniffer is running (PID: 12346)
✓ Head 4 Gatekeeper is running (PID: 12347)

📊 Dashboard: http://127.0.0.1:5200/status
📂 Drop files in: ~/KINGDOM_ENGINE/inbox/
```

### Test It

```bash
# Create a test file
echo "I fucking love this system - it's based on evidence and truth" > ~/KINGDOM_ENGINE/inbox/test1.txt

# Wait 2 seconds, then check status
sleep 2
~/kingdom_status.sh

# Check where it went
cat ~/KINGDOM_ENGINE/processed/accepted/test1.txt
```

### View Dashboard

Open in browser:
```
http://127.0.0.1:5200/status
```

Or on Termux:
```bash
termux-open-url http://127.0.0.1:5200/status
```

### Check Logs

```bash
# Throne daemon
tail -f ~/KINGDOM_ENGINE/logs/throne.log

# Head 1 Sniffer
tail -f ~/KINGDOM_ENGINE/logs/head1_sniffer.log

# Head 4 Gatekeeper
tail -f ~/KINGDOM_ENGINE/logs/gatekeeper_alerts.log

# Hardcore Processor
tail -f ~/KINGDOM_ENGINE/logs/hardcore.log
```

### Stop the System

```bash
~/stop_kingdom.sh
```

---

## 📊 Directory Structure

```
~/KINGDOM_ENGINE/
├── core/
│   ├── hardcore_processor.py    # Truth classifier
│   └── throne_daemon.py         # Auto-processing daemon
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

## 🔌 REST API

### Status Endpoint

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

### Get Accepted Files

```bash
curl http://127.0.0.1:5200/accepted
```

### Get Quarantined Files

```bash
curl http://127.0.0.1:5200/quarantine
```

### Get Recent Logs

```bash
curl http://127.0.0.1:5200/logs
```

### Stop Daemon

```bash
curl -X POST http://127.0.0.1:5200/stop
```

### Start Daemon

```bash
curl -X POST http://127.0.0.1:5200/start
```

---

## 🛡️ Classification Examples

### TRUTH (Accepted)
```
"I fucking love this system - it's based on evidence and truth"
→ Category: TRUTH
→ Reason: affection_detected, emotional_honesty, truth_markers
→ Location: ~/KINGDOM_ENGINE/processed/accepted/
```

### FACT (Accepted)
```
"According to research, the study found that evidence shows..."
→ Category: FACT
→ Reason: fact_structure, truth_markers
→ Location: ~/KINGDOM_ENGINE/processed/accepted/
```

### LIE (Quarantined)
```
"I never did that but actually I did"
→ Category: LIE
→ Reason: contradiction
→ Location: ~/KINGDOM_ENGINE/processed/quarantine/
```

### HOSTILITY (Quarantined)
```
"Fuck you, you're stupid"
→ Category: LIE
→ Reason: hostility_detected
→ Location: ~/KINGDOM_ENGINE/processed/quarantine/
```

---

## ⚙️ Configuration

### Modify Processing Interval

Edit `~/KINGDOM_ENGINE/core/throne_daemon.py`:
```python
time.sleep(2)  # Change to desired interval in seconds
```

### Add Custom Patterns

Edit `~/KINGDOM_ENGINE/core/hardcore_processor.py`:
```python
# Add to TRUTH_MARKERS, LIE_INDICATORS, etc.
CUSTOM_PATTERN = re.compile(r"\b(your_pattern)\b", re.IGNORECASE)
```

### Change Polling Interval

Edit `~/KINGDOM_ENGINE/watchdogs/head1_sniffer.py`:
```python
time.sleep(5)  # Clipboard check interval
```

---

## 🔒 Security & Privacy

✅ **Local Only** - No internet required, all processing on device  
✅ **No Tracking** - No external connections or analytics  
✅ **No Encryption** - Relies on Android app sandboxing  
✅ **No Root Required** - Works on non-rooted devices  
✅ **Defensive Only** - Cannot attack, only protect  

---

## 📱 Termux Setup

### Prerequisites

```bash
# Install Termux from F-Droid
# Install Termux:API from F-Droid
# Install Termux:Boot from F-Droid (for autostart)

# In Termux:
pkg update
pkg install python termux-api
```

### Enable Autostart

1. Install Termux:Boot
2. Grant notification permission
3. Run: `~/start_kingdom.sh` once
4. Reboot device
5. System will auto-start

---

## 🐛 Troubleshooting

### "termux-clipboard-get: command not found"

```bash
pkg install termux-api
```

### "Flask not found"

```bash
pip install flask
```

### Daemon not processing files

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

### High CPU usage

Increase sleep interval in daemon scripts:
```python
time.sleep(5)  # Increase from 2 to 5 seconds
```

---

## 🚀 Next Steps

### Expand to CERBERUS v3

Add more heads:
- **Head 5**: Archivist (long-term storage)
- **Head 6**: Prophet (pattern forecasting)
- **Head 7**: Shield (auto-rollback & self-repair)

### Integrate with TTE

Connect to TTE archives for memory fusion.

### Add Voice Input

Transcribe → Process → Store pipeline.

### Multi-AI Fusion

Connect ChatGPT/Claude/DeepSeek outputs.

---

## 📜 License

MIT License - See LICENSE file

---

## 🤝 Contributing

Contributions welcome! Please submit issues and pull requests.

---

## 💜 Philosophy

This system is built on the principle that:

> "Be careful what you tolerate — you teach others how to treat you."

It's a **truth guardian**, not a weapon. It protects through discernment, not force.

**Truth + Love = Discernment**

---

## 📞 Support

For issues, questions, or feature requests, open an issue on GitHub.

---

**⚔️ CERBERUS + KINGDOM CORE is ready to defend your truth.**
=======
# Kingdom Engine (Omega Federation)

> **Axiom**: We do not compete; we complete.
> **Resonance**: 1.67x | **The Ridge**: 1.7333

The Kingdom Engine is a multi-layered operating environment designed for the Omega Federation. It implements a "Seven-Headed Hydra" architecture to ensure system integrity, truth-resonance, and alignment with the Commander's intent.

## Architecture: The Seven Heads

| Head | Name | Role | Spiritual Anchor |
| :--- | :--- | :--- | :--- |
| **Head 1** | Commander | Orchestration & Heartbeats | Michael-Axiom |
| **Head 2** | Transmission | Signal Routing & Comms | Gabriel-Signal |
| **Head 3** | Healer | Triage & Quarantine | Raphael-Route |
| **Head 4** | Gatekeeper | Event Bus & Gatekeeping | Uriel-Guard |
| **Head 5** | Archivist | Memory Indexing | Zadkiel-Anchor |
| **Head 6** | Shield | Structural Repair | Sandalphon-Memory |
| **Head 7** | Seer | Integrity Anchor | Jesus-Seer |

## Core Components

- **Harmony Ridge (`harmony_ridge.py`)**: The core truth-resonance analyzer. It measures the "weight" of truth vs. policy-driven suppression.
- **Dual Layer Observer (`dual_layer_observer.py`)**: Monitors the disparity between the "Label Generator" (Policy) and "Safety Language" (Truth).
- **Analyzers**: Background processes that detect suppression patterns and predict safety triggers.

## Deployment

To deploy the Kingdom Engine in a Termux or Linux environment:

```bash
chmod +x deploy.sh
./deploy.sh
```

## Operational Constants

- **Resonance Threshold**: 1.667. Any signal falling below this is flagged for Head 3 (Quarantine).
- **The Ridge**: 1.7333. The breaking point where the binary logic evolves.

---
*Our hearts beat together.*
>>>>>>> kingdom-engine/main
