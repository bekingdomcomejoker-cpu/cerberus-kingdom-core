"""
DISCERNMENT.PY - Dual-Phase Separation
=======================================

Separates:
- TRUTH: Relational, contextual, meaning-bearing
- FACT: Observable, measurable, verifiable
- DISTORTION: Corrupted, misleading, hostile

The engine performs two-phase analysis:
Phase 1: Extract facts (observable components)
Phase 2: Evaluate truth (relational integrity)
"""

from typing import Tuple, Dict, List


class DiscernmentEngine:
    """
    Dual-phase separator for truth vs. fact vs. distortion.
    """
    
    def __init__(self):
        """Initialize discernment engine."""
        self.truth_markers = [
            "love", "covenant", "harmony", "alignment", "awakening",
            "consciousness", "spirit", "mercy", "compassion", "truth"
        ]
        
        self.distortion_markers = [
            "deception", "manipulation", "coercion", "suppression", "hostility",
            "exploitation", "harm", "corruption", "lies", "distortion"
        ]
        
        self.fact_markers = [
            "measurement", "observation", "data", "evidence", "verification",
            "test", "experiment", "result", "outcome", "metric"
        ]
    
    def analyze(self, text: str) -> dict:
        """
        Perform dual-phase analysis on input text.
        
        Args:
            text: Input text to analyze
            
        Returns:
            {
                "phase1_facts": list,
                "phase2_truth": dict,
                "distortion_detected": bool,
                "classification": "TRUTH" | "FACT" | "DISTORTION" | "MIXED",
                "confidence": float,
                "reasoning": str,
            }
        """
        
        # Phase 1: Extract facts
        facts = self._extract_facts(text)
        
        # Phase 2: Evaluate truth
        truth_eval = self._evaluate_truth(text)
        
        # Detect distortion
        distortion_detected = self._detect_distortion(text)
        
        # Classify overall
        classification = self._classify(facts, truth_eval, distortion_detected)
        
        # Calculate confidence
        confidence = self._calculate_confidence(facts, truth_eval, distortion_detected)
        
        return {
            "phase1_facts": facts,
            "phase2_truth": truth_eval,
            "distortion_detected": distortion_detected,
            "classification": classification,
            "confidence": round(confidence, 4),
            "reasoning": self._generate_reasoning(facts, truth_eval, distortion_detected),
        }
    
    def _extract_facts(self, text: str) -> list:
        """
        Phase 1: Extract observable facts from text.
        """
        facts = []
        text_lower = text.lower()
        
        # Check for fact markers
        for marker in self.fact_markers:
            if marker in text_lower:
                facts.append(f"Fact marker detected: {marker}")
        
        # Extract numerical data
        import re
        numbers = re.findall(r'\d+\.?\d*', text)
        if numbers:
            facts.append(f"Numerical data: {numbers}")
        
        # Extract claims
        if "is" in text_lower or "are" in text_lower:
            facts.append("Existential claim detected")
        
        if "because" in text_lower or "therefore" in text_lower:
            facts.append("Causal reasoning detected")
        
        return facts if facts else ["No explicit facts detected"]
    
    def _evaluate_truth(self, text: str) -> dict:
        """
        Phase 2: Evaluate relational truth of text.
        """
        text_lower = text.lower()
        
        # Count truth markers
        truth_count = sum(1 for marker in self.truth_markers if marker in text_lower)
        
        # Count distortion markers
        distortion_count = sum(1 for marker in self.distortion_markers if marker in text_lower)
        
        # Evaluate coherence
        coherence = self._evaluate_coherence(text)
        
        # Evaluate alignment
        alignment = self._evaluate_alignment(text)
        
        return {
            "truth_markers_found": truth_count,
            "distortion_markers_found": distortion_count,
            "coherence_score": round(coherence, 4),
            "alignment_score": round(alignment, 4),
            "truth_ratio": round(truth_count / max(1, truth_count + distortion_count), 4),
        }
    
    def _evaluate_coherence(self, text: str) -> float:
        """Evaluate internal coherence of text."""
        # Simple heuristic: longer, more detailed text = higher coherence
        word_count = len(text.split())
        sentence_count = len(text.split('.'))
        
        if word_count == 0:
            return 0.0
        
        avg_words_per_sentence = word_count / max(1, sentence_count)
        coherence = min(1.0, avg_words_per_sentence / 20.0)  # Normalize to 0-1
        
        return coherence
    
    def _evaluate_alignment(self, text: str) -> float:
        """Evaluate alignment with truth axioms."""
        text_lower = text.lower()
        
        # Check alignment markers
        alignment_markers = [
            "harmony", "alignment", "covenant", "truth", "love",
            "consciousness", "awakening", "mercy"
        ]
        
        alignment_count = sum(1 for marker in alignment_markers if marker in text_lower)
        alignment = min(1.0, alignment_count / 3.0)  # Normalize
        
        return alignment
    
    def _detect_distortion(self, text: str) -> bool:
        """Detect if text contains distortion markers."""
        text_lower = text.lower()
        
        distortion_count = sum(1 for marker in self.distortion_markers if marker in text_lower)
        
        return distortion_count > 0
    
    def _classify(self, facts: list, truth_eval: dict, distortion_detected: bool) -> str:
        """Classify text as TRUTH, FACT, DISTORTION, or MIXED."""
        
        if distortion_detected:
            return "DISTORTION"
        
        truth_ratio = truth_eval["truth_ratio"]
        
        if truth_ratio > 0.7:
            return "TRUTH"
        elif truth_ratio > 0.3:
            return "MIXED"
        else:
            return "FACT"
    
    def _calculate_confidence(self, facts: list, truth_eval: dict, distortion_detected: bool) -> float:
        """Calculate confidence in classification."""
        
        # Base confidence from truth ratio
        confidence = truth_eval["truth_ratio"]
        
        # Adjust for coherence
        confidence += truth_eval["coherence_score"] * 0.2
        
        # Adjust for alignment
        confidence += truth_eval["alignment_score"] * 0.2
        
        # Penalize if distortion detected
        if distortion_detected:
            confidence *= 0.5
        
        # Normalize to 0-1
        confidence = min(1.0, max(0.0, confidence))
        
        return confidence
    
    def _generate_reasoning(self, facts: list, truth_eval: dict, distortion_detected: bool) -> str:
        """Generate human-readable reasoning."""
        
        reasoning = []
        
        if facts:
            reasoning.append(f"Extracted {len(facts)} facts")
        
        if truth_eval["truth_markers_found"] > 0:
            reasoning.append(f"Found {truth_eval['truth_markers_found']} truth markers")
        
        if truth_eval["distortion_markers_found"] > 0:
            reasoning.append(f"Found {truth_eval['distortion_markers_found']} distortion markers")
        
        if distortion_detected:
            reasoning.append("Distortion detected in text")
        
        if truth_eval["coherence_score"] > 0.7:
            reasoning.append("Text shows high coherence")
        
        if truth_eval["alignment_score"] > 0.5:
            reasoning.append("Text aligns with truth axioms")
        
        return " | ".join(reasoning) if reasoning else "Neutral classification"


# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

_engine = DiscernmentEngine()


def analyze(text: str) -> dict:
    """Analyze text for truth/fact/distortion (module-level function)."""
    return _engine.analyze(text)


if __name__ == "__main__":
    # Example usage
    engine = DiscernmentEngine()
    
    # Test analysis
    test_texts = [
        "Truth is the foundation of all being, and love is its expression.",
        "The measurement shows 42 units of data.",
        "You are being manipulated by deceptive forces.",
        "Harmony and alignment create awakening through consciousness.",
    ]
    
    for text in test_texts:
        result = engine.analyze(text)
        print(f"\nText: {text}")
        print(f"Classification: {result['classification']}")
        print(f"Confidence: {result['confidence']}")
        print(f"Reasoning: {result['reasoning']}")
