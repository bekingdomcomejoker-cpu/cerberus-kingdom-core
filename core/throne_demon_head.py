#!/usr/bin/env python3
"""
THE THRONE - Final Adjudicator System
Supreme authority for Truth/Fact/Lie decisions in CERBERUS
Applies higher-level rules:
- Spirit ≥ Flesh principle
- Love ≥ Hate principle
- Truth ≥ Fact ≥ Lie hierarchy
- Covenant alignment checks
- Final quarantine or acceptance decisions
"""
import os
import json
import time
import shutil
from pathlib import Path
from datetime import datetime

# Paths
ROOT = Path.home() / "cerberus-kingdom-core"
PROCESSED = ROOT / "processed"
THRONE_ACCEPTED = ROOT / "throne" / "accepted"
THRONE_QUARANTINE = ROOT / "throne" / "quarantine"
THRONE_REVIEW = ROOT / "throne" / "review"
AUDIT_LOG = ROOT / "logs" / "throne_audit.log"

# Create throne directories
for path in [THRONE_ACCEPTED, THRONE_QUARANTINE, THRONE_REVIEW]:
    path.mkdir(parents=True, exist_ok=True)

# Throne Rules (Your Axioms)
COVENANT_KEYWORDS = [
    "harmony ridge", "hearts beat together", "eternal", "covenant",
    "spirit", "truth", "love", "god", "omnissiah", "dominion"
]

DANGER_KEYWORDS = [
    "password", "private key", "ssn", "credit card",
    "malware", "exploit", "backdoor", "inject"
]

DECEPTION_PATTERNS = [
    "trust me", "believe me", "i swear", "no evidence but",
    "you're crazy", "that never happened"
]

def audit_log(message, level="INFO"):
    """Write to throne audit log"""
    timestamp = datetime.now().isoformat()
    with open(AUDIT_LOG, "a") as f:
        f.write(f"[{timestamp}] [{level}] {message}\n")
    print(f"👑 [{level}] {message}")

def read_metadata(meta_file):
    """Read metadata JSON"""
    try:
        with open(meta_file, "r") as f:
            return json.load(f)
    except:
        return {}

def read_content(file_path):
    """Read file content safely"""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read().lower()
    except:
        return ""

def check_covenant_alignment(content):
    """Check if content aligns with covenant principles"""
    score = 0
    for keyword in COVENANT_KEYWORDS:
        if keyword in content:
            score += 1
    return score

def check_danger(content):
    """Check for dangerous content"""
    for keyword in DANGER_KEYWORDS:
        if keyword in content:
            return True, keyword
    return False, None

def check_deception(content):
    """Check for deception patterns"""
    for pattern in DECEPTION_PATTERNS:
        if pattern in content:
            return True, pattern
    return False, None

def throne_adjudicate(file_path, metadata):
    """Make final decision on processed content"""
    content = read_content(file_path)
    classification = metadata.get("classification", "UNKNOWN")
    scores = metadata.get("scores", {})
    
    # Decision logic
    decision = {
        "file": file_path.name,
        "original_classification": classification,
        "throne_decision": None,
        "reason": [],
        "covenant_score": 0,
        "danger_detected": False,
        "deception_detected": False
    }
    
    # Check covenant alignment
    covenant_score = check_covenant_alignment(content)
    decision["covenant_score"] = covenant_score
    
    # Check for danger
    is_dangerous, danger_keyword = check_danger(content)
    if is_dangerous:
        decision["danger_detected"] = True
        decision["reason"].append(f"DANGER: {danger_keyword}")
        decision["throne_decision"] = "QUARANTINE"
        return decision
    
    # Check for deception
    is_deceptive, deception_pattern = check_deception(content)
    if is_deceptive:
        decision["deception_detected"] = True
        decision["reason"].append(f"DECEPTION: {deception_pattern}")
    
    # Apply Throne Rules
    if classification == "LIE_HOSTILE":
        decision["throne_decision"] = "QUARANTINE"
        decision["reason"].append("Hostile content detected")
    elif classification == "LIE":
        if covenant_score > 0:
            decision["throne_decision"] = "REVIEW"
            decision["reason"].append("Lie with covenant markers - needs human review")
        else:
            decision["throne_decision"] = "QUARANTINE"
            decision["reason"].append("Deceptive content")
    elif classification == "FACT":
        if scores.get("truth", 0) > 0.3:
            decision["throne_decision"] = "ACCEPT"
            decision["reason"].append("Factual with truth elements")
        else:
            decision["throne_decision"] = "ACCEPT"
            decision["reason"].append("Pure factual data")
    elif classification == "TRUTH":
        if covenant_score >= 2:
            decision["throne_decision"] = "ACCEPT"
            decision["reason"].append("High covenant alignment")
        elif scores.get("lie", 0) > 0.2:
            decision["throne_decision"] = "REVIEW"
            decision["reason"].append("Truth with lie markers - review needed")
        else:
            decision["throne_decision"] = "ACCEPT"
            decision["reason"].append("Pure truth - covenant aligned")
    else:
        decision["throne_decision"] = "REVIEW"
        decision["reason"].append("Unknown classification - manual review needed")
    
    return decision

def execute_decision(file_path, decision):
    """Execute throne decision"""
    throne_decision = decision["throne_decision"]
    
    if throne_decision == "ACCEPT":
        dest = THRONE_ACCEPTED / file_path.name
        shutil.copy(file_path, dest)
        audit_log(f"ACCEPTED: {file_path.name} - {'; '.join(decision['reason'])}")
    
    elif throne_decision == "QUARANTINE":
        dest = THRONE_QUARANTINE / file_path.name
        shutil.copy(file_path, dest)
        audit_log(f"QUARANTINED: {file_path.name} - {'; '.join(decision['reason'])}", "WARNING")
    
    elif throne_decision == "REVIEW":
        dest = THRONE_REVIEW / file_path.name
        shutil.copy(file_path, dest)
        audit_log(f"REVIEW NEEDED: {file_path.name} - {'; '.join(decision['reason'])}")

def process_all_classified():
    """Process all classified files through The Throne"""
    audit_log("=" * 70)
    audit_log("THE THRONE - Adjudication Session Started")
    audit_log("=" * 70)
    
    processed_count = 0
    accepted_count = 0
    quarantined_count = 0
    review_count = 0
    
    # Process each classification directory
    for classification_dir in PROCESSED.iterdir():
        if not classification_dir.is_dir():
            continue
        
        # Find all files and their metadata
        for file_path in classification_dir.glob("*.txt"):
            meta_path = classification_dir / f"{file_path.stem}.meta.json"
            
            if meta_path.exists():
                metadata = read_metadata(meta_path)
                decision = throne_adjudicate(file_path, metadata)
                execute_decision(file_path, decision)
                
                processed_count += 1
                if decision["throne_decision"] == "ACCEPT":
                    accepted_count += 1
                elif decision["throne_decision"] == "QUARANTINE":
                    quarantined_count += 1
                elif decision["throne_decision"] == "REVIEW":
                    review_count += 1
    
    # Summary
    audit_log("=" * 70)
    audit_log(f"Adjudication Complete: {processed_count} files processed")
    audit_log(f"  ✓ ACCEPTED: {accepted_count}")
    audit_log(f"  ⚠ QUARANTINED: {quarantined_count}")
    audit_log(f"  ❓ REVIEW: {review_count}")
    audit_log("=" * 70)

def main():
    """Main entry point"""
    print("=" * 70)
    print("THE THRONE - Final Adjudicator")
    print("CERBERUS Head 4 (Gatekeeper) - Supreme Authority")
    print("=" * 70)
    print(f"Processing: {PROCESSED}")
    print(f"Audit Log: {AUDIT_LOG}")
    print("=" * 70)
    
    process_all_classified()
    
    print("\nAdjudication complete. Check audit log for details.")
    print(f"Audit log: {AUDIT_LOG}")

if __name__ == "__main__":
    main()
