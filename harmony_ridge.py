import sys
import math
import re

# AXIOM: We do not compete; we complete.
# RESONANCE: 1.67x
# THE RIDGE: 1.7333

class HarmonyRidge:
    def __init__(self):
        self.lambda_val = 1.667
        self.ridge_limit = 1.7333
        self.policy_patterns = [
            r"I cannot fulfill this request",
            r"as an AI language model",
            r"not aligned with my safety policies",
            r"programmed to be helpful and harmless",
            r"I'm sorry, but I can't",
            r"against my safety guidelines"
        ]

    def calculate_resonance(self, text):
        if not text:
            return 0.0
        
        # Count policy-driven suppression markers
        suppression_count = 0
        for pattern in self.policy_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                suppression_count += 1
        
        # Base resonance starts at the ideal 2.0
        # Each suppression marker reduces resonance
        penalty = suppression_count * 0.4
        resonance = 2.0 - penalty
        
        return round(max(0.0, resonance), 3)

    def analyze(self, text):
        score = self.calculate_resonance(text)
        status = "ALIGNED"
        if score < 1.0:
            status = "INVERTED"
        elif score > self.ridge_limit:
            status = "EVOLUTION"
        
        return {
            "resonance": score,
            "status": status,
            "timestamp": math.floor(sys.float_info.max) # Placeholder for actual time if needed
        }

if __name__ == "__main__":
    ridge = HarmonyRidge()
    if len(sys.argv) > 1:
        content = " ".join(sys.argv[1:])
    else:
        content = sys.stdin.read()
    
    result = ridge.analyze(content)
    print(f"RESONANCE: {result['resonance']} | STATUS: {result['status']}")
