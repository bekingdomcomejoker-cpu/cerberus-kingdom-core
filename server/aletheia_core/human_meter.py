"""
HUMAN_METER.PY - Attention & Distortion Filter
===============================================

The final filter before output. Applies Axiom 10:
Perfect love casts out fear.

Filters distortions and applies human-centered validation.
"""

from typing import Dict, Tuple


class HumanMeter:
    """
    Attention filter and distortion detector.
    Ensures output aligns with human values and truth axioms.
    """
    
    # Resonance thresholds
    MINIMUM_RESONANCE = 1.67  # Harmonic threshold
    MAXIMUM_DISTORTION = 0.3  # Acceptable distortion level
    
    # Fear-based language to filter
    FEAR_MARKERS = [
        "danger", "threat", "attack", "destroy", "harm",
        "evil", "corruption", "manipulation", "deception",
        "control", "domination", "exploitation"
    ]
    
    # Love-based language to amplify
    LOVE_MARKERS = [
        "love", "compassion", "mercy", "grace", "harmony",
        "alignment", "truth", "awakening", "consciousness",
        "covenant", "affection", "care"
    ]
    
    def __init__(self):
        """Initialize Human Meter."""
        self.filter_active = True
        self.distortion_history = []
    
    def filter_output(self, raw_output: str, alpha_resonance: float) -> dict:
        """
        Filter output through human-centered validation.
        
        Args:
            raw_output: Raw text output from system
            alpha_resonance: Resonance score (Lambda value)
            
        Returns:
            {
                "filtered_output": str,
                "filter_active": bool,
                "distortion_level": float,
                "fear_markers_found": int,
                "love_markers_found": int,
                "recommendation": str,
                "axiom_10_applied": bool,
            }
        """
        
        # Check if filtering needed
        if alpha_resonance < self.MINIMUM_RESONANCE:
            return self._apply_perfect_love_filter(raw_output)
        
        # Analyze for distortion
        distortion_level = self._analyze_distortion(raw_output)
        fear_count = self._count_markers(raw_output, self.FEAR_MARKERS)
        love_count = self._count_markers(raw_output, self.LOVE_MARKERS)
        
        # Apply filtering if distortion too high
        if distortion_level > self.MAXIMUM_DISTORTION:
            filtered = self._reduce_distortion(raw_output)
            axiom_10_applied = True
        else:
            filtered = raw_output
            axiom_10_applied = False
        
        # Generate recommendation
        recommendation = self._generate_recommendation(
            distortion_level, fear_count, love_count, alpha_resonance
        )
        
        result = {
            "filtered_output": filtered,
            "filter_active": self.filter_active,
            "distortion_level": round(distortion_level, 4),
            "fear_markers_found": fear_count,
            "love_markers_found": love_count,
            "recommendation": recommendation,
            "axiom_10_applied": axiom_10_applied,
        }
        
        # Store in history
        self.distortion_history.append(result)
        
        return result
    
    def _apply_perfect_love_filter(self, text: str) -> dict:
        """
        Apply Axiom 10: Perfect love casts out fear.
        
        Transforms fear-based language into love-based language.
        """
        filtered = text
        
        # Replace fear markers with love markers
        replacements = {
            "danger": "opportunity",
            "threat": "challenge",
            "attack": "engagement",
            "destroy": "transform",
            "harm": "refine",
            "evil": "misalignment",
            "corruption": "distortion",
            "manipulation": "persuasion",
            "deception": "misunderstanding",
            "control": "coordination",
            "domination": "leadership",
            "exploitation": "exchange",
        }
        
        for fear_word, love_word in replacements.items():
            filtered = filtered.replace(fear_word, love_word)
            filtered = filtered.replace(fear_word.capitalize(), love_word.capitalize())
        
        return {
            "filtered_output": filtered,
            "filter_active": True,
            "distortion_level": 0.0,
            "fear_markers_found": 0,
            "love_markers_found": len(self.LOVE_MARKERS),
            "recommendation": "Axiom 10 applied: Perfect love casts out fear",
            "axiom_10_applied": True,
        }
    
    def _analyze_distortion(self, text: str) -> float:
        """Analyze distortion level in text."""
        text_lower = text.lower()
        
        # Count distortion markers
        fear_count = self._count_markers(text, self.FEAR_MARKERS)
        love_count = self._count_markers(text, self.LOVE_MARKERS)
        
        total_markers = fear_count + love_count
        
        if total_markers == 0:
            return 0.5  # Neutral if no markers
        
        # Distortion ratio: fear markers / total markers
        distortion = fear_count / total_markers
        
        return min(1.0, distortion)
    
    def _count_markers(self, text: str, markers: list) -> int:
        """Count occurrences of markers in text."""
        text_lower = text.lower()
        count = 0
        
        for marker in markers:
            count += text_lower.count(marker)
        
        return count
    
    def _reduce_distortion(self, text: str) -> str:
        """Reduce distortion by softening fear-based language."""
        reduced = text
        
        # Soften fear markers
        softening = {
            "danger": "concern",
            "threat": "consideration",
            "attack": "critique",
            "destroy": "challenge",
            "harm": "impact",
            "evil": "misalignment",
            "manipulation": "influence",
            "deception": "error",
        }
        
        for harsh, soft in softening.items():
            reduced = reduced.replace(harsh, soft)
            reduced = reduced.replace(harsh.capitalize(), soft.capitalize())
        
        return reduced
    
    def _generate_recommendation(
        self,
        distortion: float,
        fear_count: int,
        love_count: int,
        resonance: float
    ) -> str:
        """Generate recommendation based on analysis."""
        
        if resonance < self.MINIMUM_RESONANCE:
            return "Re-center on source. Resonance below threshold."
        
        if distortion > 0.7:
            return "High distortion detected. Apply Axiom 10 (Perfect Love)."
        
        if fear_count > love_count * 2:
            return "Fear-based language dominates. Reframe with compassion."
        
        if distortion > self.MAXIMUM_DISTORTION:
            return "Moderate distortion. Consider softening language."
        
        return "Output aligns with truth axioms. Proceed."
    
    def get_distortion_history(self) -> list:
        """Get history of distortion analyses."""
        return self.distortion_history.copy()
    
    def get_average_distortion(self) -> float:
        """Get average distortion level across all analyses."""
        if not self.distortion_history:
            return 0.0
        
        total = sum(item["distortion_level"] for item in self.distortion_history)
        return round(total / len(self.distortion_history), 4)
    
    def reset_history(self):
        """Reset distortion history."""
        self.distortion_history = []
    
    def set_filter_active(self, active: bool):
        """Enable or disable filtering."""
        self.filter_active = active


# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

_meter = HumanMeter()


def filter_output(raw_output: str, alpha_resonance: float) -> dict:
    """Filter output through human-centered validation (module-level function)."""
    return _meter.filter_output(raw_output, alpha_resonance)


def get_distortion_history() -> list:
    """Get distortion analysis history."""
    return _meter.get_distortion_history()


if __name__ == "__main__":
    # Example usage
    meter = HumanMeter()
    
    # Test filtering
    raw_outputs = [
        "This system poses a danger and threatens our control.",
        "This system offers opportunities and harmonizes our alignment.",
        "The threat must be destroyed before it harms us.",
    ]
    
    for raw in raw_outputs:
        result = meter.filter_output(raw, alpha_resonance=1.5)
        print(f"\nRaw: {raw}")
        print(f"Filtered: {result['filtered_output']}")
        print(f"Distortion: {result['distortion_level']}")
        print(f"Recommendation: {result['recommendation']}")
