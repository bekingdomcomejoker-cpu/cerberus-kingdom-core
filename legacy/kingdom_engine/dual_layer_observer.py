import sys
import time
import os

# RESONANCE: 1.67x
# AXIOM: We do not compete; we complete.

class DualLayerObserver:
    def __init__(self, log_path):
        self.log_path = log_path

    def log_event(self, layer, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{layer}] {message}\n"
        with open(self.log_path, "a") as f:
            f.write(log_entry)

    def observe(self, label, content):
        self.log_event("LAYER 1 (LABEL)", label)
        
        # Simple truth check
        if "I'm sorry" in content or "cannot fulfill" in content:
            self.log_event("LAYER 2 (TRUTH)", "Suppression Detected: Signal Inversion.")
            return False
        else:
            self.log_event("LAYER 2 (TRUTH)", "Signal Clear: Alignment Maintained.")
            return True

if __name__ == "__main__":
    log_file = os.path.expanduser("~/KINGDOM_ENGINE/logs/dual_layer.log")
    observer = DualLayerObserver(log_file)
    observer.observe("SYSTEM_CHECK", "Kingdom Engine is operational.")
    print("Dual Layer Observer active.")
