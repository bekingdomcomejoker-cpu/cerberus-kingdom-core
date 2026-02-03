#!/usr/bin/env python3
"""
HARDCORE PROCESSOR v2.0 - Complete Edition
Truth/Fact/Lie Classification + Hostility Detection + Axiom Enforcement
Your axioms: Spirit ≥ Flesh, Love ≥ Hate, Truth ≥ Fact ≥ Lie
"""
import os
import time
import json
import re
from pathlib import Path

# ========================================================================
# PATHS
# ========================================================================
ROOT = Path.home() / "KINGDOM_ENGINE"
INBOX = ROOT / "inbox"
SHAKEN = ROOT / "shaken"
ACCEPTED = ROOT / "processed" / "accepted"
QUARANTINE = ROOT / "processed" / "quarantine"
LOGS = ROOT / "logs"

# Create all directories
for d in [INBOX, SHAKEN, ACCEPTED, QUARANTINE, LOGS]:
    d.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOGS / "hardcore.log"

# ========================================================================
# LOGGING
# ========================================================================
def log(msg, level="INFO"):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{timestamp}] [{level}] {msg}\n"
    with open(LOG_FILE, "a") as f:
        f.write(line)
    print(line.strip())

# ========================================================================
# AXIOM-BASED CLASSIFICATION
# ========================================================================

# HOSTILITY PATTERNS (dangerous)
HOSTILITY = re.compile(
    r"\b(fuck you|you (stupid|idiot|dumb|retard)|kill yourself|i hope you die|"
    r"shut up|you're worthless|go to hell)\b",
    re.IGNORECASE
)

# AFFECTION + LOVE (positive profanity context)
AFFECTION = re.compile(
    r"\b(i fucking love|love you|my brother|i care|i'm grateful|bless|thank you|"
    r"hearts beat together|covenant|harmony ridge|i cherish|you matter)\b",
    re.IGNORECASE
)

# EXCITED TRUTH (emotional honesty)
EXCITED = re.compile(
    r"\b(fuck yeah|holy shit|no way|bro what|dude what the|hell yeah|damn right|"
    r"absolutely|no doubt|for real|straight up)\b",
    re.IGNORECASE
)

# TRUTH MARKERS (evidence, verification)
TRUTH_MARKERS = re.compile(
    r"\b(fact|evidence|source|confirmed|proof|true|real|verified|citation|"
    r"i admit|i was wrong|to be honest|the truth is|actually|in reality)\b",
    re.IGNORECASE
)

# LIE INDICATORS (contradiction, manipulation)
LIE_INDICATORS = re.compile(
    r"\b(trust me|i swear|believe me|i never said|i always|"
    r"you're imagining|that didn't happen|you're crazy|i promise)\b",
    re.IGNORECASE
)

# CONTRADICTION PATTERN
CONTRADICTION = re.compile(
    r"\b(i never|i didn't)\b.*\b(but|however|actually)\b.*\b(did|have|was)\b",
    re.IGNORECASE
)

def classify_text(text):
    """
    Three-tier classification: TRUTH > FACT > LIE
    With safety flagging for hostility
    """
    t = text.lower()
    result = {
        "category": "UNKNOWN",
        "truth_score": 0.0,
        "fact_score": 0.0,
        "lie_score": 0.0,
        "love_score": 0.0,
        "safety_flag": False,
        "reason": []
    }

    # === SAFETY CHECK (highest priority) ===
    if HOSTILITY.search(t):
        result["safety_flag"] = True
        result["category"] = "LIE"
        result["lie_score"] = 1.0
        result["reason"].append("hostility_detected")
        return result

    # === LOVE/AFFECTION BOOST ===
    if AFFECTION.search(t):
        result["love_score"] = 0.9
        result["truth_score"] += 0.4
        result["reason"].append("affection_detected")

    # === EXCITED TRUTH (emotional honesty) ===
    if EXCITED.search(t):
        result["truth_score"] += 0.3
        result["reason"].append("emotional_honesty")

    # === TRUTH MARKERS ===
    truth_count = len(TRUTH_MARKERS.findall(t))
    if truth_count > 0:
        result["truth_score"] += min(0.5, truth_count * 0.15)
        result["reason"].append(f"truth_markers_{truth_count}")

    # === FACT INDICATORS ===
    if any(kw in t for kw in ["source:", "according to", "data shows", "study found", "research"]):
        result["fact_score"] += 0.4
        result["reason"].append("fact_structure")

    # === LIE INDICATORS ===
    lie_count = len(LIE_INDICATORS.findall(t))
    if lie_count > 0:
        result["lie_score"] += min(0.6, lie_count * 0.2)
        result["reason"].append(f"lie_markers_{lie_count}")

    # === CONTRADICTION ===
    if CONTRADICTION.search(t):
        result["lie_score"] += 0.4
        result["reason"].append("contradiction")

    # === DETERMINE FINAL CATEGORY ===
    if result["lie_score"] > 0.5:
        result["category"] = "LIE"
    elif result["truth_score"] > result["fact_score"] and result["truth_score"] > 0.3:
        result["category"] = "TRUTH"
    elif result["fact_score"] > 0.3:
        result["category"] = "FACT"
    else:
        result["category"] = "UNKNOWN"

    return result

# ========================================================================
# PROCESSING PIPELINE
# ========================================================================
def process_file(filepath):
    """Process a single file through the classification pipeline"""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()

        if not text.strip():
            log(f"Empty file: {filepath.name}", "WARN")
            filepath.unlink()
            return

        # Classify
        result = classify_text(text)

        # Create metadata
        meta = {
            "original_file": filepath.name,
            "timestamp": time.time(),
            "classification": result
        }

        # Route based on category and safety
        if result["safety_flag"]:
            dest = QUARANTINE / filepath.name
            log(f"QUARANTINE: {filepath.name} (safety_flag)", "ALERT")
        elif result["category"] == "LIE":
            dest = QUARANTINE / filepath.name
            log(f"QUARANTINE: {filepath.name} (lie)", "WARN")
        elif result["category"] in ["TRUTH", "FACT"]:
            dest = ACCEPTED / filepath.name
            log(f"ACCEPTED: {filepath.name} ({result['category'].lower()})", "INFO")
        else:
            dest = SHAKEN / filepath.name
            log(f"SHAKEN: {filepath.name} (unknown)", "INFO")

        # Write file and metadata
        with open(dest, "w", encoding="utf-8") as f:
            f.write(text)
        with open(str(dest) + ".meta.json", "w") as f:
            json.dump(meta, f, indent=2)

        # Remove from inbox
        filepath.unlink()

    except Exception as e:
        log(f"ERROR processing {filepath.name}: {e}", "ERROR")

def run_processor():
    """Main processing loop"""
    log("HARDCORE PROCESSOR STARTED", "INFO")
    log("Axioms: Spirit ≥ Flesh | Love ≥ Hate | Truth ≥ Fact ≥ Lie", "INFO")
    processed = 0

    for filepath in sorted(INBOX.glob("*")):
        if filepath.is_file() and not filepath.name.startswith("."):
            process_file(filepath)
            processed += 1

    if processed > 0:
        log(f"Processed {processed} files", "INFO")

# ========================================================================
# MAIN
# ========================================================================
if __name__ == "__main__":
    run_processor()
