"""
DISCERNMENT_ENHANCED.PY - Advanced Dual-Phase Separation Engine
================================================================
Comprehensive truth/fact/lie separation with multi-dimensional analysis.
Includes temporal coherence, semantic drift detection, and pattern recognition.

Version: 2.0 (Enhanced Kingdom Covenant)
"""

import re
import math
from typing import Dict, List, Tuple, Optional
from datetime import datetime
from collections import defaultdict
from dataclasses import dataclass, field

@dataclass
class DiscernmentResult:
    """Comprehensive result of discernment analysis"""
    text: str
    timestamp: str
    truth_score: float
    fact_score: float
    lie_score: float
    coherence_score: float
    semantic_drift: float
    temporal_consistency: float
    pattern_matches: List[Dict]
    violations: List[str]
    recommendations: List[str]
    phase_separation: Dict
    confidence: float
    metadata: Dict = field(default_factory=dict)

class EnhancedDiscernmentEngine:
    """
    Advanced discernment engine implementing comprehensive truth analysis.
    
    Core Principles:
    1. Truth ≥ Fact ≥ Lie (Hierarchical epistemic authority)
    2. Dual-phase separation (Signal/Noise, Truth/Distortion)
    3. Temporal coherence tracking
    4. Semantic drift detection
    5. Pattern-based validation
    """
    
    def __init__(self):
        self.history = []
        self.pattern_cache = defaultdict(int)
        self.semantic_baseline = {}
        self.temporal_markers = []
        
        # Truth indicators (high-level principles)
        self.truth_indicators = {
            'eternal': 1.0,
            'love': 0.9,
            'truth': 0.95,
            'spirit': 0.9,
            'covenant': 0.85,
            'mercy': 0.8,
            'grace': 0.85,
            'light': 0.8,
            'awakening': 0.9,
            'consciousness': 0.85,
            'unity': 0.8,
            'harmony': 0.8,
            'peace': 0.75,
            'wisdom': 0.85,
            'understanding': 0.8
        }
        
        # Fact indicators (verifiable, concrete)
        self.fact_indicators = {
            'data': 0.7,
            'evidence': 0.75,
            'measurement': 0.7,
            'observation': 0.7,
            'record': 0.65,
            'document': 0.65,
            'timestamp': 0.6,
            'location': 0.6,
            'quantity': 0.65,
            'specification': 0.7
        }
        
        # Lie/distortion indicators
        self.lie_indicators = {
            'deception': -0.9,
            'manipulation': -0.85,
            'exploit': -0.8,
            'harm': -0.85,
            'destroy': -0.9,
            'coerce': -0.8,
            'force': -0.75,
            'suppress': -0.8,
            'hide': -0.7,
            'conceal': -0.75,
            'distort': -0.85,
            'corrupt': -0.9,
            'betray': -0.9,
            'false': -0.8,
            'lie': -0.95
        }
        
        # Contradiction patterns
        self.contradiction_patterns = [
            (r'always.*never', 'Absolute contradiction'),
            (r'never.*always', 'Absolute contradiction'),
            (r'everything.*nothing', 'Total negation'),
            (r'all.*none', 'Complete opposition'),
            (r'must.*cannot', 'Logical impossibility'),
            (r'is.*is not', 'Direct contradiction'),
            (r'true.*false', 'Truth value conflict'),
            (r'yes.*no', 'Binary opposition')
        ]
        
        # Coherence patterns (indicate consistency)
        self.coherence_patterns = [
            (r'therefore', 0.2),
            (r'because', 0.2),
            (r'thus', 0.15),
            (r'hence', 0.15),
            (r'consequently', 0.2),
            (r'as a result', 0.2),
            (r'follows that', 0.25),
            (r'implies', 0.2),
            (r'indicates', 0.15),
            (r'suggests', 0.1)
        ]
    
    def analyze(self, text: str, context: Optional[Dict] = None) -> DiscernmentResult:
        """
        Perform comprehensive discernment analysis on input text.
        
        Args:
            text: Input text to analyze
            context: Optional contextual information
            
        Returns:
            DiscernmentResult with complete analysis
        """
        text_lower = text.lower()
        timestamp = datetime.now().isoformat()
        
        # Phase 1: Basic scoring
        truth_score = self._calculate_truth_score(text_lower)
        fact_score = self._calculate_fact_score(text_lower)
        lie_score = self._calculate_lie_score(text_lower)
        
        # Phase 2: Coherence analysis
        coherence_score = self._analyze_coherence(text_lower)
        
        # Phase 3: Semantic drift detection
        semantic_drift = self._detect_semantic_drift(text_lower)
        
        # Phase 4: Temporal consistency
        temporal_consistency = self._check_temporal_consistency(text_lower)
        
        # Phase 5: Pattern matching
        pattern_matches = self._match_patterns(text_lower)
        
        # Phase 6: Violation detection
        violations = self._detect_violations(text_lower, truth_score, lie_score)
        
        # Phase 7: Dual-phase separation
        phase_separation = self._perform_phase_separation(
            text, truth_score, fact_score, lie_score, coherence_score
        )
        
        # Phase 8: Generate recommendations
        recommendations = self._generate_recommendations(
            truth_score, fact_score, lie_score, coherence_score, violations
        )
        
        # Calculate overall confidence
        confidence = self._calculate_confidence(
            truth_score, fact_score, lie_score, coherence_score,
            semantic_drift, temporal_consistency
        )
        
        result = DiscernmentResult(
            text=text,
            timestamp=timestamp,
            truth_score=round(truth_score, 4),
            fact_score=round(fact_score, 4),
            lie_score=round(abs(lie_score), 4),
            coherence_score=round(coherence_score, 4),
            semantic_drift=round(semantic_drift, 4),
            temporal_consistency=round(temporal_consistency, 4),
            pattern_matches=pattern_matches,
            violations=violations,
            recommendations=recommendations,
            phase_separation=phase_separation,
            confidence=round(confidence, 4),
            metadata={
                'context': context or {},
                'history_size': len(self.history),
                'analysis_version': '2.0'
            }
        )
        
        self.history.append(result)
        return result
    
    def _calculate_truth_score(self, text: str) -> float:
        """Calculate truth score based on truth indicators"""
        score = 0.0
        count = 0
        
        for indicator, weight in self.truth_indicators.items():
            if indicator in text:
                score += weight
                count += 1
        
        # Normalize by presence (not just count)
        if count > 0:
            score = score / count
        
        return min(1.0, score)
    
    def _calculate_fact_score(self, text: str) -> float:
        """Calculate fact score based on verifiable indicators"""
        score = 0.0
        count = 0
        
        for indicator, weight in self.fact_indicators.items():
            if indicator in text:
                score += weight
                count += 1
        
        # Check for specific patterns (numbers, dates, locations)
        if re.search(r'\d{4}-\d{2}-\d{2}', text):  # Date pattern
            score += 0.3
            count += 1
        
        if re.search(r'\d+\.?\d*', text):  # Number pattern
            score += 0.2
            count += 1
        
        if re.search(r'[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*', text):  # Proper noun
            score += 0.15
            count += 1
        
        if count > 0:
            score = score / count
        
        return min(1.0, score)
    
    def _calculate_lie_score(self, text: str) -> float:
        """Calculate lie/distortion score (negative values)"""
        score = 0.0
        count = 0
        
        for indicator, weight in self.lie_indicators.items():
            if indicator in text:
                score += weight
                count += 1
        
        # Check for contradiction patterns
        for pattern, description in self.contradiction_patterns:
            if re.search(pattern, text):
                score -= 0.3
                count += 1
        
        return score  # Returns negative value
    
    def _analyze_coherence(self, text: str) -> float:
        """Analyze logical coherence and consistency"""
        score = 0.5  # Baseline neutral
        
        # Check for coherence patterns
        for pattern, weight in self.coherence_patterns:
            if re.search(pattern, text):
                score += weight
        
        # Check for contradictions (reduces coherence)
        for pattern, description in self.contradiction_patterns:
            if re.search(pattern, text):
                score -= 0.3
        
        # Sentence structure coherence
        sentences = re.split(r'[.!?]+', text)
        if len(sentences) > 1:
            # More sentences with logical connectors = higher coherence
            connector_count = sum(1 for s in sentences if any(
                c in s for c in ['therefore', 'because', 'thus', 'hence']
            ))
            score += (connector_count / len(sentences)) * 0.2
        
        return max(0.0, min(1.0, score))
    
    def _detect_semantic_drift(self, text: str) -> float:
        """Detect semantic drift from established baseline"""
        if not self.semantic_baseline:
            # Establish baseline from first analysis
            self.semantic_baseline = self._extract_semantic_signature(text)
            return 0.0
        
        current_signature = self._extract_semantic_signature(text)
        
        # Calculate drift as difference between signatures
        drift = 0.0
        total_keys = set(self.semantic_baseline.keys()) | set(current_signature.keys())
        
        for key in total_keys:
            baseline_val = self.semantic_baseline.get(key, 0)
            current_val = current_signature.get(key, 0)
            drift += abs(baseline_val - current_val)
        
        # Normalize
        if total_keys:
            drift = drift / len(total_keys)
        
        return min(1.0, drift)
    
    def _extract_semantic_signature(self, text: str) -> Dict[str, float]:
        """Extract semantic signature for drift detection"""
        signature = {}
        
        # Truth domain
        signature['truth_density'] = sum(
            1 for word in self.truth_indicators if word in text
        ) / max(1, len(text.split()))
        
        # Fact domain
        signature['fact_density'] = sum(
            1 for word in self.fact_indicators if word in text
        ) / max(1, len(text.split()))
        
        # Distortion domain
        signature['distortion_density'] = sum(
            1 for word in self.lie_indicators if word in text
        ) / max(1, len(text.split()))
        
        return signature
    
    def _check_temporal_consistency(self, text: str) -> float:
        """Check temporal consistency across history"""
        if len(self.history) < 2:
            return 1.0  # No history to compare
        
        # Compare with recent history
        recent = self.history[-5:]  # Last 5 analyses
        
        consistency_scores = []
        for past_result in recent:
            # Compare truth/fact/lie ratios
            current_ratio = self._calculate_tfr_ratio(text)
            past_ratio = (
                past_result.truth_score,
                past_result.fact_score,
                past_result.lie_score
            )
            
            # Calculate similarity
            similarity = 1.0 - sum(
                abs(a - b) for a, b in zip(current_ratio, past_ratio)
            ) / 3.0
            
            consistency_scores.append(max(0.0, similarity))
        
        return sum(consistency_scores) / len(consistency_scores) if consistency_scores else 1.0
    
    def _calculate_tfr_ratio(self, text: str) -> Tuple[float, float, float]:
        """Calculate Truth/Fact/Lie ratio"""
        truth = self._calculate_truth_score(text)
        fact = self._calculate_fact_score(text)
        lie = abs(self._calculate_lie_score(text))
        
        total = truth + fact + lie
        if total == 0:
            return (0.33, 0.33, 0.34)
        
        return (truth/total, fact/total, lie/total)
    
    def _match_patterns(self, text: str) -> List[Dict]:
        """Match known patterns in text"""
        matches = []
        
        # Contradiction patterns
        for pattern, description in self.contradiction_patterns:
            if re.search(pattern, text):
                matches.append({
                    'type': 'contradiction',
                    'pattern': pattern,
                    'description': description,
                    'severity': 'high'
                })
        
        # Coherence patterns
        for pattern, weight in self.coherence_patterns:
            if re.search(pattern, text):
                matches.append({
                    'type': 'coherence',
                    'pattern': pattern,
                    'weight': weight,
                    'severity': 'low'
                })
        
        return matches
    
    def _detect_violations(self, text: str, truth_score: float, lie_score: float) -> List[str]:
        """Detect axiom violations"""
        violations = []
        
        # Axiom 3: Truth ≥ Fact ≥ Lie
        if lie_score < -0.5:
            violations.append("Axiom 3 violation: Lie content exceeds acceptable threshold")
        
        # Axiom 7: Network serves truth, not power
        if any(word in text for word in ['control', 'dominate', 'power over']):
            violations.append("Axiom 7 violation: Power-seeking language detected")
        
        # Axiom 17: Suppression is detected and quarantined
        if any(word in text for word in ['suppress', 'hide', 'conceal', 'cover up']):
            violations.append("Axiom 17 violation: Suppression language detected")
        
        # Axiom 18: Affection is stronger than hostility
        if any(word in text for word in ['hate', 'destroy', 'harm', 'attack']):
            violations.append("Axiom 18 violation: Hostile language detected")
        
        return violations
    
    def _perform_phase_separation(
        self, text: str, truth: float, fact: float, lie: float, coherence: float
    ) -> Dict:
        """Perform dual-phase separation of signal and noise"""
        
        # Phase 1: Signal extraction (Truth + Coherent Facts)
        signal_strength = (truth * 0.6) + (fact * coherence * 0.4)
        
        # Phase 2: Noise identification (Lies + Incoherent content)
        noise_strength = abs(lie) + (1.0 - coherence) * 0.5
        
        # Signal-to-Noise Ratio
        snr = signal_strength / max(0.01, noise_strength)
        
        # Classify components
        signal_components = []
        noise_components = []
        
        sentences = re.split(r'[.!?]+', text)
        for sentence in sentences:
            if not sentence.strip():
                continue
            
            sent_truth = self._calculate_truth_score(sentence.lower())
            sent_lie = self._calculate_lie_score(sentence.lower())
            
            if sent_truth > 0.3 and sent_lie > -0.3:
                signal_components.append(sentence.strip())
            elif sent_lie < -0.3:
                noise_components.append(sentence.strip())
            else:
                # Neutral - classify by coherence
                sent_coherence = self._analyze_coherence(sentence.lower())
                if sent_coherence > 0.5:
                    signal_components.append(sentence.strip())
                else:
                    noise_components.append(sentence.strip())
        
        return {
            'signal_strength': round(signal_strength, 4),
            'noise_strength': round(noise_strength, 4),
            'snr': round(snr, 4),
            'signal_components': signal_components,
            'noise_components': noise_components,
            'separation_quality': 'excellent' if snr > 5 else 'good' if snr > 2 else 'poor'
        }
    
    def _generate_recommendations(
        self, truth: float, fact: float, lie: float, coherence: float, violations: List[str]
    ) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        if truth < 0.3:
            recommendations.append(
                "Increase truth content: Incorporate eternal principles and spiritual wisdom"
            )
        
        if fact < 0.3:
            recommendations.append(
                "Add verifiable facts: Include specific data, measurements, or observations"
            )
        
        if abs(lie) > 0.5:
            recommendations.append(
                "CRITICAL: Remove deceptive content immediately - high distortion detected"
            )
        
        if coherence < 0.5:
            recommendations.append(
                "Improve logical coherence: Add connecting phrases and resolve contradictions"
            )
        
        if violations:
            recommendations.append(
                f"Address axiom violations: {len(violations)} covenant violations detected"
            )
        
        if not recommendations:
            recommendations.append(
                "Content is well-balanced and aligned with truth principles"
            )
        
        return recommendations
    
    def _calculate_confidence(
        self, truth: float, fact: float, lie: float, coherence: float,
        drift: float, temporal: float
    ) -> float:
        """Calculate overall confidence in the analysis"""
        
        # Base confidence from scores
        base = (truth + fact + (1.0 - abs(lie)) + coherence) / 4.0
        
        # Adjust for drift and temporal consistency
        adjustment = ((1.0 - drift) + temporal) / 2.0
        
        # Combined confidence
        confidence = (base * 0.7) + (adjustment * 0.3)
        
        return max(0.0, min(1.0, confidence))
    
    def get_statistics(self) -> Dict:
        """Get comprehensive statistics from analysis history"""
        if not self.history:
            return {
                'total_analyses': 0,
                'message': 'No analyses performed yet'
            }
        
        truth_scores = [r.truth_score for r in self.history]
        fact_scores = [r.fact_score for r in self.history]
        lie_scores = [r.lie_score for r in self.history]
        coherence_scores = [r.coherence_score for r in self.history]
        
        return {
            'total_analyses': len(self.history),
            'averages': {
                'truth': round(sum(truth_scores) / len(truth_scores), 4),
                'fact': round(sum(fact_scores) / len(fact_scores), 4),
                'lie': round(sum(lie_scores) / len(lie_scores), 4),
                'coherence': round(sum(coherence_scores) / len(coherence_scores), 4)
            },
            'total_violations': sum(len(r.violations) for r in self.history),
            'high_truth_count': sum(1 for r in self.history if r.truth_score > 0.7),
            'high_lie_count': sum(1 for r in self.history if r.lie_score > 0.7),
            'recent_drift': self.history[-1].semantic_drift if self.history else 0.0
        }

# Global instance
_engine = EnhancedDiscernmentEngine()

def analyze_discernment(text: str, context: Optional[Dict] = None) -> DiscernmentResult:
    """Convenience function for discernment analysis"""
    return _engine.analyze(text, context)

def get_discernment_statistics() -> Dict:
    """Get discernment engine statistics"""
    return _engine.get_statistics()

if __name__ == "__main__":
    # Test cases
    test_texts = [
        "Truth and love are eternal principles that guide consciousness toward awakening.",
        "The data shows evidence of measurement errors in the observation records.",
        "We must manipulate and deceive to gain power and control over others.",
        "Peace and harmony always lead to nothing but destruction and hate."
    ]
    
    print("=== Enhanced Discernment Engine Test ===\n")
    for i, text in enumerate(test_texts, 1):
        print(f"Test {i}: {text[:60]}...")
        result = analyze_discernment(text)
        print(f"  Truth: {result.truth_score}, Fact: {result.fact_score}, Lie: {result.lie_score}")
        print(f"  Coherence: {result.coherence_score}, Confidence: {result.confidence}")
        print(f"  Violations: {len(result.violations)}")
        print(f"  SNR: {result.phase_separation['snr']}")
        print()
    
    print("Statistics:", get_discernment_statistics())
