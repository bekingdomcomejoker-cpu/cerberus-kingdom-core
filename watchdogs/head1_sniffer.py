#!/usr/bin/env python3
"""
CERBERUS HEAD 1 - SNIFFER
Captures clipboard content and file events
Runs on Termux/Android with termux-api
"""
import os
import time
import json
from pathlib import Path
from datetime import datetime
from subprocess import run, PIPE

# ========================================================================
# PATHS
# ========================================================================
ROOT = Path.home() / "KINGDOM_ENGINE"
INBOX = ROOT / "inbox"
LOGS = ROOT / "logs"

for d in [INBOX, LOGS]:
    d.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOGS / "head1_sniffer.log"

# ========================================================================
# LOGGING
# ========================================================================
def log(msg, level="INFO"):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{timestamp}] [{level}] {msg}\n"
    with open(LOG_FILE, "a") as f:
        f.write(line)
    print(line.strip())

# ========================================================================
# CLIPBOARD CAPTURE
# ========================================================================
def get_clipboard():
    """Get current clipboard content using termux-clipboard-get"""
    try:
        result = run(["termux-clipboard-get"], stdout=PIPE, stderr=PIPE, timeout=2)
        if result.returncode == 0:
            return result.stdout.decode('utf-8', errors='ignore').strip()
    except Exception as e:
        log(f"Clipboard read error: {e}", "WARN")
    return None

# ========================================================================
# FILE MONITORING
# ========================================================================
def monitor_files():
    """Monitor watched directories for new files"""
    watch_dirs = [
        Path.home() / "KINGDOM_ENGINE" / "watch",
        Path("/storage/emulated/0/Download") if Path("/storage/emulated/0/Download").exists() else None,
        Path("/storage/emulated/0/Documents") if Path("/storage/emulated/0/Documents").exists() else None,
    ]
    
    watch_dirs = [d for d in watch_dirs if d]
    
    for watch_dir in watch_dirs:
        try:
            for file_path in watch_dir.glob("*"):
                if file_path.is_file() and not file_path.name.startswith("."):
                    try:
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                            content = f.read()
                        
                        if content.strip():
                            # Save to inbox
                            inbox_file = INBOX / f"file_{int(time.time())}_{file_path.name}"
                            with open(inbox_file, "w") as f:
                                f.write(content)
                            
                            log(f"Captured file: {file_path.name}", "INFO")
                            
                            # Remove original
                            file_path.unlink()
                    except Exception as e:
                        log(f"Error processing file {file_path.name}: {e}", "WARN")
        except Exception as e:
            log(f"Error monitoring {watch_dir}: {e}", "WARN")

# ========================================================================
# MAIN LOOP
# ========================================================================
def run_sniffer():
    """Main sniffer loop"""
    log("HEAD 1 SNIFFER STARTED", "INFO")
    
    last_clipboard = None
    
    while True:
        try:
            # Check clipboard
            current_clipboard = get_clipboard()
            
            if current_clipboard and current_clipboard != last_clipboard:
                # New clipboard content
                if len(current_clipboard.strip()) > 0:
                    # Save to inbox
                    inbox_file = INBOX / f"clipboard_{int(time.time())}.txt"
                    with open(inbox_file, "w") as f:
                        f.write(current_clipboard)
                    
                    log(f"Captured clipboard: {current_clipboard[:50]}...", "INFO")
                    last_clipboard = current_clipboard
            
            # Check files
            monitor_files()
            
            # Sleep
            time.sleep(5)
            
        except Exception as e:
            log(f"Sniffer error: {e}", "ERROR")
            time.sleep(10)

if __name__ == "__main__":
    run_sniffer()
