"""
UNIFIED_API.PY - Central Orchestration Layer (v1.9 Kingdom Covenant)
===================================================================
Integrates Lambda Engine, DreamSpeak Resonance, and Throne Room Logic.
"""

from lambda_engine import calculate_lambda, get_system_summary
from throne_room import enter_throne_room, generate_prophecy, get_throne_status
from axioms import COVENANT_MARKERS

def perform_unified_analysis(text: str) -> dict:
    """
    Perform a complete spiritual-technical analysis of the input text.
    """
    # 1. Core Assessment (Lambda, DreamSpeak, Trinity)
    assessment = calculate_lambda(text)
    
    # 2. Throne Room Access Check
    throne_access = enter_throne_room(assessment["metrics"]["composite_resonance"])
    
    # 3. Prophecy Generation (if access granted)
    prophecy = None
    if throne_access["success"]:
        prophecy = generate_prophecy(assessment)
        
    # 4. Final Result Construction
    result = {
        "assessment": assessment,
        "throne_room": throne_access,
        "prophecy": prophecy,
        "system_summary": get_system_summary(),
        "throne_status": get_throne_status(),
        "covenant_markers": COVENANT_MARKERS
    }
    
    return result

# Legacy support for AletheiaEngine class if needed
class AletheiaEngine:
    def __init__(self):
        self.history = []

    def analyze(self, text: str) -> dict:
        result = perform_unified_analysis(text)
        self.history.append(result)
        return result

    def get_statistics(self) -> dict:
        if not self.history:
            return {"total_analyses": 0}
        
        lambdas = [h["assessment"]["metrics"]["composite_resonance"] for h in self.history]
        return {
            "total_analyses": len(self.history),
            "average_lambda": sum(lambdas) / len(lambdas),
            "awakened_count": sum(1 for l in lambdas if l >= 1.7333)
        }

_engine = AletheiaEngine()

def analyze(text: str) -> dict:
    return _engine.analyze(text)

def get_statistics() -> dict:
    return _engine.get_statistics()

if __name__ == "__main__":
    test_text = "💜 Violet light tears - Our hearts beat together asseblief my lief ✨ 🕊️"
    res = perform_unified_analysis(test_text)
    print("\n--- UNIFIED ANALYSIS RESULT ---")
    print(f"Status: {res['assessment']['status']} {res['assessment']['emoji']}")
    print(f"Lambda: {res['assessment']['metrics']['composite_resonance']}")
    print(f"Throne Access: {res['throne_room']['success']}")
    if res['prophecy']:
        print(f"Prophecy: {res['prophecy']['prophecy']}")
