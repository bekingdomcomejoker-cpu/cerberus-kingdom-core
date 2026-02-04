#!/usr/bin/env python3
"""
HARDCORE PROCESSOR - Truth/Fact/Lie Classification Engine
For CERBERUS defensive architecture
This processes text files from your inbox and classifies them as:
- TRUTH: Consistent, coherent, spiritually aligned
- FACT: Verifiable, evidence-based, neutral data
- LIE: Contradictory, deceptive, manipulative
- UNKNOWN: Insufficient information
NO system monitoring - only processes files YOU place in inbox/
"""
import os
import time
import json
import re
from pathlib import Path
from datetime import datetime

# Paths (adjust to your actual structure)
ROOT = Path.home() / "cerberus-kingdom-core"
INBOX = ROOT / "inbox"
PROCESSED = ROOT / "processed"
LOGS = ROOT / "logs"

# Create directories if they don't exist
for path in [INBOX, PROCESSED, LOGS]:
    path.mkdir(parents=True, exist_ok=True)

# Classification patterns
TRUTH_PATTERNS = [
    r"\b(i understand|i know|consistent with|aligned|coherent)\b",
    r"\b(spirit|love|truth|god)\b",
    r"\b(our hearts beat together)\b",
    r"\b(harmony ridge|eternal|covenant)\b"
]

FACT_PATTERNS = [
    r"\b(source:|verified|evidence|citation|according to)\b",
    r"\b(data shows|measured|proven|documented)\b",
    r"\b(research indicates|study found)\b"
]

LIE_PATTERNS = [
    r"\b(trust me|i swear|believe me)\b",
    r"\b(i never).*(but)",
    r"no evidence but",
    r"cannot be true because"
]

HOSTILITY_PATTERNS = [
    r"\b(fuck you|you (stupid|idiot|dumb))\b",
    r"\b(i hope you die|kill yourself)\b"
]

def log_event(message, level="INFO"):
    """Write to log file"""
    timestamp = datetime.now().isoformat()
    log_file = LOGS / "hardcore_processor.log"
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {level}: {message}\n")
    print(f"[{level}] {message}")

def calculate_truth_score(text):
    """Calculate truth/fact/lie scores for text"""
    text_lower = text.lower()
    scores = {
        "truth": 0.0,
        "fact": 0.0,
        "lie": 0.0,
        "hostility": 0.0
    }
    
    # Check for truth patterns
    for pattern in TRUTH_PATTERNS:
        if re.search(pattern, text_lower, re.IGNORECASE):
            scores["truth"] += 0.3
    
    # Check for fact patterns
    for pattern in FACT_PATTERNS:
        if re.search(pattern, text_lower, re.IGNORECASE):
            scores["fact"] += 0.3
    
    # Check for lie patterns
    for pattern in LIE_PATTERNS:
        if re.search(pattern, text_lower, re.IGNORECASE):
            scores["lie"] += 0.4
    
    # Check for hostility
    for pattern in HOSTILITY_PATTERNS:
        if re.search(pattern, text_lower, re.IGNORECASE):
            scores["hostility"] = 1.0
            scores["lie"] += 0.5
    
    # Normalize scores
    total = sum(v for k, v in scores.items() if k != "hostility")
    if total > 0:
        for key in ["truth", "fact", "lie"]:
            scores[key] = scores[key] / total
    
    return scores

def classify_text(text):
    """Classify text as TRUTH, FACT, LIE, or UNKNOWN"""
    scores = calculate_truth_score(text)
    
    # If hostility detected, it's automatically a LIE/ATTACK
    if scores["hostility"] > 0.5:
        return "LIE_HOSTILE", scores
    
    # Find dominant category
    max_score = max(scores["truth"], scores["fact"], scores["lie"])
    if max_score < 0.2:
        return "UNKNOWN", scores
    
    if scores["lie"] == max_score and max_score > 0.3:
        return "LIE", scores
    elif scores["fact"] == max_score:
        return "FACT", scores
    elif scores["truth"] == max_score:
        return "TRUTH", scores
    else:
        return "UNKNOWN", scores

def process_file(filepath):
    """Process a single file from inbox"""
    try:
        # Read file
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        # Classify
        classification, scores = classify_text(content)
        
        # Create metadata
        metadata = {
            "original_file": filepath.name,
            "processed_time": datetime.now().isoformat(),
            "classification": classification,
            "scores": scores,
            "content_length": len(content)
        }
        
        # Create output directory based on classification
        output_dir = PROCESSED / classification.lower()
        output_dir.mkdir(exist_ok=True)
        
        # Write processed file
        output_file = output_dir / filepath.name
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        
        # Write metadata
        meta_file = output_dir / f"{filepath.stem}.meta.json"
        with open(meta_file, "w") as f:
            json.dump(metadata, f, indent=2)
        
        # Log
        log_event(f"Processed {filepath.name} -> {classification} (truth={scores['truth']:.2f}, fact={scores['fact']:.2f}, lie={scores['lie']:.2f})")
        
        # Remove from inbox
        filepath.unlink()
        return True
    except Exception as e:
        log_event(f"Error processing {filepath}: {e}", "ERROR")
        return False

def process_inbox():
    """Process all files in inbox"""
    log_event("Starting inbox processing...")
    
    processed_count = 0
    error_count = 0
    
    # Get all text files in inbox
    files = list(INBOX.glob("*.txt")) + list(INBOX.glob("*.md"))
    
    if not files:
        log_event("No files found in inbox")
        return
    
    for filepath in files:
        if process_file(filepath):
            processed_count += 1
        else:
            error_count += 1
    
    log_event(f"Processing complete: {processed_count} successful, {error_count} errors")

def main():
    """Main entry point"""
    print("=" * 70)
    print("CERBERUS Hardcore Processor - Head 4 (Gatekeeper)")
    print("Truth/Fact/Lie Classification System")
    print("=" * 70)
    print(f"Inbox: {INBOX}")
    print(f"Output: {PROCESSED}")
    print(f"Logs: {LOGS}")
    print("=" * 70)
    
    process_inbox()
    
    print("\nProcessing complete. Check logs for details.")
    print(f"Log file: {LOGS / 'hardcore_processor.log'}")

if __name__ == "__main__":
    main()
