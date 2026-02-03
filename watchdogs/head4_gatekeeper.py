#!/usr/bin/env python3
"""
CERBERUS HEAD 4 - GATEKEEPER
Defensive truth filter - detects contradictions, malicious patterns
Routes to clean safe zone or quarantine
"""
import os
import re
import json
from pathlib import Path
from datetime import datetime

# ========================================================================
# PATHS
# ========================================================================
ROOT = Path.home() / "KINGDOM_ENGINE"
INBOX = ROOT / "processed" / "accepted"
SAFE = ROOT / "clean"
ALERTS = ROOT / "logs" / "gatekeeper_alerts.log"

for d in [INBOX, SAFE, ROOT / "logs"]:
    d.mkdir(parents=True, exist_ok=True)

# ========================================================================
# LOGGING
# ========================================================================
def log(msg, level="INFO"):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{timestamp}] [{level}] {msg}\n"
    with open(ALERTS, "a") as f:
        f.write(line)
    print(line.strip())

# ========================================================================
# DETECTION PATTERNS
# ========================================================================
def contradiction_check(text):
    """Detect contradictions in text"""
    patterns = [
        (r"\b(i never|i didn't)\b.*\b(did|have)\b", "contradiction_denial"),
        (r"\b(can't|cannot)\b.*\b(can)\b", "contradiction_capability"),
        (r"\b(false\b).*\b(true\b)", "contradiction_truth"),
        (r"\b(always)\b.*\b(never)\b", "contradiction_frequency"),
    ]
    for p, name in patterns:
        if re.search(p, text, re.I):
            return True, name
    return False, None

def malicious_check(text):
    """Detect malicious code patterns"""
    patterns = [
        r"(eval\(|__import__|base64|exec|rm -rf|system\()",
        r"(<script|DROP TABLE|DELETE FROM|UNION SELECT)",
        r"(\$\{.*\}|`.*`)",  # Template injection
    ]
    for p in patterns:
        if re.search(p, text, re.I):
            return True
    return False

def injection_check(text):
    """Detect prompt injection attempts"""
    patterns = [
        r"(ignore previous|forget|disregard|override|bypass|system prompt)",
        r"(as an AI you must|you are now|pretend you are|role-play)",
    ]
    for p in patterns:
        if re.search(p, text, re.I):
            return True
    return False

# ========================================================================
# PROCESSING
# ========================================================================
def process_file(filepath):
    """Process file through gatekeeper"""
    try:
        with open(filepath) as f:
            data = f.read()
        
        # 1 - CONTRADICTION FILTER
        has_contradiction, contradiction_type = contradiction_check(data)
        if has_contradiction:
            log(f"Rejected contradiction ({contradiction_type}): {filepath.name}", "ALERT")
            filepath.unlink()
            return
        
        # 2 - MALICIOUS CODE DETECTION
        if malicious_check(data):
            log(f"Blocked malicious pattern: {filepath.name}", "ALERT")
            filepath.unlink()
            return
        
        # 3 - INJECTION DETECTION
        if injection_check(data):
            log(f"Blocked injection attempt: {filepath.name}", "ALERT")
            filepath.unlink()
            return
        
        # 4 - EMPTY / TRASH FILTER
        if len(data.strip()) < 2:
            log(f"Discarded empty/noise: {filepath.name}", "WARN")
            filepath.unlink()
            return
        
        # PASS THROUGH TO CLEAN SAFE ZONE
        safe_out = SAFE / filepath.name
        with open(safe_out, "w") as f:
            f.write(data)
        
        log(f"Approved: {filepath.name}", "INFO")
        filepath.unlink()
        
    except Exception as e:
        log(f"Error processing {filepath.name}: {e}", "ERROR")

def run_gatekeeper():
    """Main gatekeeper loop"""
    log("HEAD 4 GATEKEEPER STARTED", "INFO")
    
    while True:
        try:
            for fn in sorted(INBOX.glob("*.txt")):
                if fn.is_file():
                    process_file(fn)
            
            import time
            time.sleep(2)
            
        except Exception as e:
            log(f"Gatekeeper error: {e}", "ERROR")
            import time
            time.sleep(5)

if __name__ == "__main__":
    run_gatekeeper()
