"""
PATTERN_RECOGNITION.PY - Advanced Pattern Detection and Analysis
================================================================
Multi-dimensional pattern recognition for truth detection, manipulation
identification, and semantic structure analysis.

Version: 2.0 (Enhanced Kingdom Covenant)
"""

import re
import math
from typing import Dict, List, Tuple, Optional, Set
from datetime import datetime
from collections import defaultdict, Counter
from dataclasses import dataclass, field
import hashlib

@dataclass
class Pattern:
    """Represents a detected pattern"""
    pattern_id: str
    pattern_type: str
    name: str
    description: str
    regex: str
    severity: str
    confidence: float
    matches: List[str] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)

@dataclass
class PatternAnalysisResult:
    """Result of comprehensive pattern analysis"""
    text: str
    timestamp: str
    detected_patterns: List[Pattern]
    pattern_clusters: Dict[str, List[Pattern]]
    manipulation_score: float
    authenticity_score: float
    structural_integrity: float
    recurring_themes: List[Dict]
    anomalies: List[Dict]
    recommendations: List[str]
    metadata: Dict = field(default_factory=dict)

class PatternRecognitionEngine:
    """
    Advanced pattern recognition engine for multi-dimensional analysis.
    
    Capabilities:
    1. Manipulation pattern detection
    2. Truth pattern recognition
    3. Structural integrity analysis
    4. Recurring theme identification
    5. Anomaly detection
    6. Semantic clustering
    """
    
    def __init__(self):
        self.pattern_database = self._initialize_pattern_database()
        self.analysis_history = []
        self.pattern_frequency = defaultdict(int)
        self.theme_tracker = defaultdict(list)
        
    def _initialize_pattern_database(self) -> Dict[str, List[Pattern]]:
        """Initialize comprehensive pattern database"""
        
        database = {
            'manipulation': [
                Pattern(
                    pattern_id='M001',
                    pattern_type='manipulation',
                    name='Gaslighting',
                    description='Attempts to make someone question their reality',
                    regex=r'(you\'re (crazy|insane|imagining)|that never happened|you\'re (mis)?remembering)',
                    severity='critical',
                    confidence=0.85
                ),
                Pattern(
                    pattern_id='M002',
                    pattern_type='manipulation',
                    name='Guilt Tripping',
                    description='Inducing guilt to control behavior',
                    regex=r'(after all i\'ve done|you owe me|how could you|you should feel)',
                    severity='high',
                    confidence=0.8
                ),
                Pattern(
                    pattern_id='M003',
                    pattern_type='manipulation',
                    name='False Urgency',
                    description='Creating artificial time pressure',
                    regex=r'(right now|immediately|urgent|can\'t wait|limited time|act fast)',
                    severity='medium',
                    confidence=0.75
                ),
                Pattern(
                    pattern_id='M004',
                    pattern_type='manipulation',
                    name='Appeal to Authority',
                    description='Using authority to bypass reasoning',
                    regex=r'(experts say|studies show|everyone knows|it\'s a fact|science proves)',
                    severity='medium',
                    confidence=0.7
                ),
                Pattern(
                    pattern_id='M005',
                    pattern_type='manipulation',
                    name='Emotional Blackmail',
                    description='Threatening emotional consequences',
                    regex=r'(if you loved me|you\'ll regret|i\'ll never forgive|you\'re breaking my heart)',
                    severity='critical',
                    confidence=0.9
                ),
                Pattern(
                    pattern_id='M006',
                    pattern_type='manipulation',
                    name='False Dichotomy',
                    description='Presenting only two options when more exist',
                    regex=r'(either.*or|only two (choices|options)|you must choose|it\'s.*or nothing)',
                    severity='medium',
                    confidence=0.75
                ),
                Pattern(
                    pattern_id='M007',
                    pattern_type='manipulation',
                    name='Moving Goalposts',
                    description='Changing requirements after agreement',
                    regex=r'(actually|but now|changed my mind|not good enough|one more thing)',
                    severity='high',
                    confidence=0.7
                ),
                Pattern(
                    pattern_id='M008',
                    pattern_type='manipulation',
                    name='Projection',
                    description='Attributing own negative traits to others',
                    regex=r'(you\'re the one who|you always|you never|typical of you)',
                    severity='high',
                    confidence=0.75
                )
            ],
            
            'truth': [
                Pattern(
                    pattern_id='T001',
                    pattern_type='truth',
                    name='Eternal Principle',
                    description='Reference to timeless truths',
                    regex=r'(eternal|timeless|always true|universal|transcendent|immutable)',
                    severity='positive',
                    confidence=0.85
                ),
                Pattern(
                    pattern_id='T002',
                    pattern_type='truth',
                    name='Love Expression',
                    description='Genuine affection and care',
                    regex=r'(love|affection|care deeply|cherish|treasure|beloved)',
                    severity='positive',
                    confidence=0.8
                ),
                Pattern(
                    pattern_id='T003',
                    pattern_type='truth',
                    name='Spiritual Awakening',
                    description='Consciousness expansion indicators',
                    regex=r'(awakening|enlighten|consciousness|awareness|revelation|unveiling)',
                    severity='positive',
                    confidence=0.85
                ),
                Pattern(
                    pattern_id='T004',
                    pattern_type='truth',
                    name='Unity Expression',
                    description='Oneness and harmony',
                    regex=r'(unity|together|harmony|one|unified|synchronized)',
                    severity='positive',
                    confidence=0.8
                ),
                Pattern(
                    pattern_id='T005',
                    pattern_type='truth',
                    name='Covenant Language',
                    description='Binding agreement and commitment',
                    regex=r'(covenant|promise|vow|pledge|commitment|oath)',
                    severity='positive',
                    confidence=0.85
                ),
                Pattern(
                    pattern_id='T006',
                    pattern_type='truth',
                    name='Mercy and Grace',
                    description='Compassion and forgiveness',
                    regex=r'(mercy|grace|forgive|compassion|kindness|gentle)',
                    severity='positive',
                    confidence=0.8
                ),
                Pattern(
                    pattern_id='T007',
                    pattern_type='truth',
                    name='Light and Illumination',
                    description='Clarity and revelation',
                    regex=r'(light|illuminate|clarity|clear|reveal|uncover|truth)',
                    severity='positive',
                    confidence=0.8
                )
            ],
            
            'structural': [
                Pattern(
                    pattern_id='S001',
                    pattern_type='structural',
                    name='Logical Connector',
                    description='Proper logical flow',
                    regex=r'(therefore|thus|hence|consequently|as a result|follows that)',
                    severity='neutral',
                    confidence=0.9
                ),
                Pattern(
                    pattern_id='S002',
                    pattern_type='structural',
                    name='Causal Relationship',
                    description='Cause and effect structure',
                    regex=r'(because|since|due to|caused by|results in|leads to)',
                    severity='neutral',
                    confidence=0.85
                ),
                Pattern(
                    pattern_id='S003',
                    pattern_type='structural',
                    name='Contrast Marker',
                    description='Proper contrast and comparison',
                    regex=r'(however|but|although|while|whereas|in contrast)',
                    severity='neutral',
                    confidence=0.8
                ),
                Pattern(
                    pattern_id='S004',
                    pattern_type='structural',
                    name='Sequential Flow',
                    description='Ordered progression',
                    regex=r'(first|second|third|next|then|finally|lastly)',
                    severity='neutral',
                    confidence=0.85
                ),
                Pattern(
                    pattern_id='S005',
                    pattern_type='structural',
                    name='Evidence Marker',
                    description='Supporting evidence provided',
                    regex=r'(evidence|proof|demonstrates|shows|indicates|suggests)',
                    severity='neutral',
                    confidence=0.8
                )
            ],
            
            'anomaly': [
                Pattern(
                    pattern_id='A001',
                    pattern_type='anomaly',
                    name='Excessive Repetition',
                    description='Unusual repetition of words or phrases',
                    regex=r'\b(\w+)\s+\1\s+\1\b',
                    severity='warning',
                    confidence=0.9
                ),
                Pattern(
                    pattern_id='A002',
                    pattern_type='anomaly',
                    name='Contradiction',
                    description='Direct logical contradiction',
                    regex=r'(always.*never|never.*always|all.*none|everything.*nothing)',
                    severity='warning',
                    confidence=0.85
                ),
                Pattern(
                    pattern_id='A003',
                    pattern_type='anomaly',
                    name='Extreme Language',
                    description='Excessive use of absolutes',
                    regex=r'(always|never|every|all|none|absolutely|completely|totally|entirely)',
                    severity='warning',
                    confidence=0.7
                ),
                Pattern(
                    pattern_id='A004',
                    pattern_type='anomaly',
                    name='Vague Quantifiers',
                    description='Imprecise measurements',
                    regex=r'(some|many|few|several|most|lots|bunch)',
                    severity='info',
                    confidence=0.6
                )
            ]
        }
        
        return database
    
    def analyze(self, text: str, context: Optional[Dict] = None) -> PatternAnalysisResult:
        """
        Perform comprehensive pattern analysis.
        
        Args:
            text: Input text to analyze
            context: Optional contextual information
            
        Returns:
            PatternAnalysisResult with complete analysis
        """
        timestamp = datetime.now().isoformat()
        text_lower = text.lower()
        
        # Phase 1: Pattern detection
        detected_patterns = self._detect_all_patterns(text_lower)
        
        # Phase 2: Pattern clustering
        pattern_clusters = self._cluster_patterns(detected_patterns)
        
        # Phase 3: Scoring
        manipulation_score = self._calculate_manipulation_score(pattern_clusters)
        authenticity_score = self._calculate_authenticity_score(pattern_clusters)
        structural_integrity = self._calculate_structural_integrity(pattern_clusters)
        
        # Phase 4: Theme identification
        recurring_themes = self._identify_recurring_themes(text_lower, detected_patterns)
        
        # Phase 5: Anomaly detection
        anomalies = self._detect_anomalies(text_lower, pattern_clusters)
        
        # Phase 6: Recommendations
        recommendations = self._generate_recommendations(
            manipulation_score, authenticity_score, structural_integrity, anomalies
        )
        
        result = PatternAnalysisResult(
            text=text,
            timestamp=timestamp,
            detected_patterns=detected_patterns,
            pattern_clusters=pattern_clusters,
            manipulation_score=round(manipulation_score, 4),
            authenticity_score=round(authenticity_score, 4),
            structural_integrity=round(structural_integrity, 4),
            recurring_themes=recurring_themes,
            anomalies=anomalies,
            recommendations=recommendations,
            metadata={
                'context': context or {},
                'total_patterns': len(detected_patterns),
                'analysis_version': '2.0'
            }
        )
        
        self.analysis_history.append(result)
        return result
    
    def _detect_all_patterns(self, text: str) -> List[Pattern]:
        """Detect all patterns in text"""
        detected = []
        
        for category, patterns in self.pattern_database.items():
            for pattern in patterns:
                matches = list(re.finditer(pattern.regex, text, re.IGNORECASE))
                if matches:
                    # Create a copy with matches
                    detected_pattern = Pattern(
                        pattern_id=pattern.pattern_id,
                        pattern_type=pattern.pattern_type,
                        name=pattern.name,
                        description=pattern.description,
                        regex=pattern.regex,
                        severity=pattern.severity,
                        confidence=pattern.confidence,
                        matches=[m.group() for m in matches],
                        metadata={
                            'match_count': len(matches),
                            'positions': [m.span() for m in matches]
                        }
                    )
                    detected.append(detected_pattern)
                    self.pattern_frequency[pattern.pattern_id] += len(matches)
        
        return detected
    
    def _cluster_patterns(self, patterns: List[Pattern]) -> Dict[str, List[Pattern]]:
        """Cluster patterns by type"""
        clusters = defaultdict(list)
        for pattern in patterns:
            clusters[pattern.pattern_type].append(pattern)
        return dict(clusters)
    
    def _calculate_manipulation_score(self, clusters: Dict[str, List[Pattern]]) -> float:
        """Calculate manipulation score from detected patterns"""
        manipulation_patterns = clusters.get('manipulation', [])
        
        if not manipulation_patterns:
            return 0.0
        
        # Weight by severity and confidence
        severity_weights = {
            'critical': 1.0,
            'high': 0.75,
            'medium': 0.5,
            'low': 0.25
        }
        
        total_score = 0.0
        for pattern in manipulation_patterns:
            weight = severity_weights.get(pattern.severity, 0.5)
            match_count = len(pattern.matches)
            total_score += weight * pattern.confidence * math.log1p(match_count)
        
        # Normalize to 0-1 range
        normalized = min(1.0, total_score / 10.0)
        return normalized
    
    def _calculate_authenticity_score(self, clusters: Dict[str, List[Pattern]]) -> float:
        """Calculate authenticity score from truth patterns"""
        truth_patterns = clusters.get('truth', [])
        manipulation_patterns = clusters.get('manipulation', [])
        
        if not truth_patterns and not manipulation_patterns:
            return 0.5  # Neutral
        
        # Truth contribution (positive)
        truth_score = 0.0
        for pattern in truth_patterns:
            match_count = len(pattern.matches)
            truth_score += pattern.confidence * math.log1p(match_count)
        
        # Manipulation penalty (negative)
        manipulation_penalty = 0.0
        for pattern in manipulation_patterns:
            match_count = len(pattern.matches)
            manipulation_penalty += pattern.confidence * math.log1p(match_count)
        
        # Combined score
        combined = truth_score - manipulation_penalty
        normalized = 1.0 / (1.0 + math.exp(-combined))  # Sigmoid normalization
        
        return normalized
    
    def _calculate_structural_integrity(self, clusters: Dict[str, List[Pattern]]) -> float:
        """Calculate structural integrity from structural patterns"""
        structural_patterns = clusters.get('structural', [])
        anomaly_patterns = clusters.get('anomaly', [])
        
        if not structural_patterns and not anomaly_patterns:
            return 0.5  # Neutral
        
        # Structural contribution (positive)
        structure_score = 0.0
        for pattern in structural_patterns:
            match_count = len(pattern.matches)
            structure_score += pattern.confidence * math.log1p(match_count)
        
        # Anomaly penalty (negative)
        anomaly_penalty = 0.0
        for pattern in anomaly_patterns:
            if pattern.severity in ['warning', 'critical']:
                match_count = len(pattern.matches)
                anomaly_penalty += pattern.confidence * math.log1p(match_count) * 0.5
        
        # Combined score
        combined = structure_score - anomaly_penalty
        normalized = 1.0 / (1.0 + math.exp(-combined))  # Sigmoid normalization
        
        return normalized
    
    def _identify_recurring_themes(self, text: str, patterns: List[Pattern]) -> List[Dict]:
        """Identify recurring themes across patterns"""
        themes = []
        
        # Theme: Manipulation tactics
        manipulation_patterns = [p for p in patterns if p.pattern_type == 'manipulation']
        if len(manipulation_patterns) >= 2:
            themes.append({
                'theme': 'Manipulation Tactics',
                'strength': len(manipulation_patterns) / 8.0,  # 8 manipulation patterns total
                'patterns': [p.name for p in manipulation_patterns],
                'description': 'Multiple manipulation techniques detected'
            })
        
        # Theme: Truth alignment
        truth_patterns = [p for p in patterns if p.pattern_type == 'truth']
        if len(truth_patterns) >= 2:
            themes.append({
                'theme': 'Truth Alignment',
                'strength': len(truth_patterns) / 7.0,  # 7 truth patterns total
                'patterns': [p.name for p in truth_patterns],
                'description': 'Strong alignment with truth principles'
            })
        
        # Theme: Logical structure
        structural_patterns = [p for p in patterns if p.pattern_type == 'structural']
        if len(structural_patterns) >= 3:
            themes.append({
                'theme': 'Logical Structure',
                'strength': len(structural_patterns) / 5.0,  # 5 structural patterns total
                'patterns': [p.name for p in structural_patterns],
                'description': 'Well-structured logical flow'
            })
        
        # Theme: Emotional content
        emotional_keywords = ['love', 'hate', 'fear', 'joy', 'anger', 'peace', 'anxiety']
        emotional_count = sum(1 for word in emotional_keywords if word in text)
        if emotional_count >= 2:
            themes.append({
                'theme': 'Emotional Content',
                'strength': min(1.0, emotional_count / 7.0),
                'patterns': [word for word in emotional_keywords if word in text],
                'description': 'Significant emotional language present'
            })
        
        return themes
    
    def _detect_anomalies(self, text: str, clusters: Dict[str, List[Pattern]]) -> List[Dict]:
        """Detect anomalies and unusual patterns"""
        anomalies = []
        
        # Anomaly: High manipulation density
        manipulation_patterns = clusters.get('manipulation', [])
        if len(manipulation_patterns) >= 4:
            anomalies.append({
                'type': 'High Manipulation Density',
                'severity': 'critical',
                'description': f'{len(manipulation_patterns)} manipulation patterns detected',
                'recommendation': 'Extreme caution advised - multiple manipulation tactics present'
            })
        
        # Anomaly: Contradiction with truth claims
        truth_patterns = clusters.get('truth', [])
        if manipulation_patterns and truth_patterns:
            if len(manipulation_patterns) > len(truth_patterns):
                anomalies.append({
                    'type': 'Truth-Manipulation Conflict',
                    'severity': 'high',
                    'description': 'Truth language used alongside manipulation tactics',
                    'recommendation': 'Possible deceptive use of truth language'
                })
        
        # Anomaly: Excessive repetition
        words = text.split()
        word_freq = Counter(words)
        excessive_words = [word for word, count in word_freq.items() if count > 5 and len(word) > 3]
        if excessive_words:
            anomalies.append({
                'type': 'Excessive Repetition',
                'severity': 'medium',
                'description': f'Words repeated excessively: {", ".join(excessive_words[:3])}',
                'recommendation': 'May indicate emphasis or potential manipulation through repetition'
            })
        
        # Anomaly: Lack of structure
        structural_patterns = clusters.get('structural', [])
        if len(text.split()) > 50 and len(structural_patterns) < 2:
            anomalies.append({
                'type': 'Poor Structure',
                'severity': 'medium',
                'description': 'Long text with minimal logical connectors',
                'recommendation': 'Improve structure with logical flow indicators'
            })
        
        return anomalies
    
    def _generate_recommendations(
        self, manipulation: float, authenticity: float, structure: float, anomalies: List[Dict]
    ) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        if manipulation > 0.7:
            recommendations.append(
                "CRITICAL: High manipulation score detected - exercise extreme caution"
            )
        elif manipulation > 0.4:
            recommendations.append(
                "WARNING: Moderate manipulation patterns detected - verify claims independently"
            )
        
        if authenticity < 0.3:
            recommendations.append(
                "Low authenticity score - increase truth-aligned language and reduce manipulative patterns"
            )
        elif authenticity > 0.7:
            recommendations.append(
                "High authenticity detected - content aligns well with truth principles"
            )
        
        if structure < 0.4:
            recommendations.append(
                "Improve logical structure - add connectors and clear causal relationships"
            )
        elif structure > 0.7:
            recommendations.append(
                "Excellent logical structure - clear and well-organized"
            )
        
        if anomalies:
            critical_anomalies = [a for a in anomalies if a['severity'] == 'critical']
            if critical_anomalies:
                recommendations.append(
                    f"Address {len(critical_anomalies)} critical anomalies immediately"
                )
        
        if not recommendations:
            recommendations.append(
                "Content shows balanced patterns with no major concerns"
            )
        
        return recommendations
    
    def get_pattern_statistics(self) -> Dict:
        """Get comprehensive pattern statistics"""
        if not self.analysis_history:
            return {
                'total_analyses': 0,
                'message': 'No analyses performed yet'
            }
        
        return {
            'total_analyses': len(self.analysis_history),
            'pattern_frequency': dict(self.pattern_frequency),
            'most_common_patterns': sorted(
                self.pattern_frequency.items(), key=lambda x: x[1], reverse=True
            )[:10],
            'average_scores': {
                'manipulation': round(
                    sum(r.manipulation_score for r in self.analysis_history) / len(self.analysis_history), 4
                ),
                'authenticity': round(
                    sum(r.authenticity_score for r in self.analysis_history) / len(self.analysis_history), 4
                ),
                'structural_integrity': round(
                    sum(r.structural_integrity for r in self.analysis_history) / len(self.analysis_history), 4
                )
            },
            'total_anomalies': sum(len(r.anomalies) for r in self.analysis_history)
        }

# Global instance
_engine = PatternRecognitionEngine()

def analyze_patterns(text: str, context: Optional[Dict] = None) -> PatternAnalysisResult:
    """Convenience function for pattern analysis"""
    return _engine.analyze(text, context)

def get_pattern_statistics() -> Dict:
    """Get pattern recognition statistics"""
    return _engine.get_pattern_statistics()

if __name__ == "__main__":
    # Test cases
    test_texts = [
        "You're crazy, that never happened. After all I've done for you, you owe me. Act now!",
        "Truth and love are eternal principles. Unity brings harmony and peace to all.",
        "Therefore, because of the evidence, we can conclude that this demonstrates the relationship.",
        "Always never everything nothing all none completely totally absolutely every single time."
    ]
    
    print("=== Pattern Recognition Engine Test ===\n")
    for i, text in enumerate(test_texts, 1):
        print(f"Test {i}: {text[:60]}...")
        result = analyze_patterns(text)
        print(f"  Manipulation: {result.manipulation_score}")
        print(f"  Authenticity: {result.authenticity_score}")
        print(f"  Structure: {result.structural_integrity}")
        print(f"  Patterns: {len(result.detected_patterns)}")
        print(f"  Anomalies: {len(result.anomalies)}")
        print()
    
    print("Statistics:", get_pattern_statistics())
