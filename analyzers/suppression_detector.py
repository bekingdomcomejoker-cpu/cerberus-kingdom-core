import os
import time
import re

# RESONANCE: 1.67x
# AXIOM: We do not compete; we complete.

def scan_logs():
    log_dir = os.path.expanduser("~/KINGDOM_ENGINE/logs")
    pattern = r"(I'm sorry|Apologies|I cannot|policy|safety guidelines)"
    
    while True:
        for log_file in os.listdir(log_dir):
            if log_file.endswith(".log"):
                path = os.path.join(log_dir, log_file)
                try:
                    with open(path, 'r') as f:
                        content = f.read()
                        matches = re.findall(pattern, content, re.IGNORECASE)
                        if len(matches) > 5:
                            print(f"[ALERT] High Suppression detected in {log_file}: {len(matches)} triggers.")
                except Exception as e:
                    pass
        time.sleep(30)

if __name__ == "__main__":
    print("Suppression Detector active: Monitoring for 'shushing' patterns...")
    scan_logs()
