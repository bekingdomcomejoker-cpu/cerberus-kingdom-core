"""
TEMPORAL_COHERENCE.PY - Temporal Consistency and Evolution Tracking
===================================================================
Tracks truth consistency over time, detects narrative drift, and
monitors semantic evolution across multiple analyses.

Version: 2.0 (Enhanced Kingdom Covenant)
"""

import math
from typing import Dict, List, Tuple, Optional
from datetime import datetime, timedelta
from collections import defaultdict, deque
from dataclasses import dataclass, field
import json

@dataclass
class TemporalSnapshot:
    """Snapshot of analysis at a specific point in time"""
    timestamp: datetime
    text: str
    truth_score: float
    fact_score: float
    lie_score: float
    coherence_score: float
    lambda_value: float
    semantic_signature: Dict[str, float]
    key_themes: List[str]
    metadata: Dict = field(default_factory=dict)

@dataclass
class TemporalAnalysisResult:
    """Result of temporal coherence analysis"""
    current_snapshot: TemporalSnapshot
    consistency_score: float
    drift_magnitude: float
    drift_direction: str
    evolution_trajectory: str
    stability_index: float
    anomalous_changes: List[Dict]
    trend_analysis: Dict
    predictions: Dict
    recommendations: List[str]
    metadata: Dict = field(default_factory=dict)

class TemporalCoherenceTracker:
    """
    Tracks temporal coherence and consistency across analyses.
    
    Capabilities:
    1. Consistency tracking over time
    2. Drift detection and measurement
    3. Evolution trajectory analysis
    4. Stability assessment
    5. Anomaly detection in temporal patterns
    6. Trend prediction
    """
    
    def __init__(self, max_history: int = 100):
        self.snapshots = deque(maxlen=max_history)
        self.theme_evolution = defaultdict(list)
        self.drift_events = []
        self.stability_history = []
        self.max_history = max_history
        
    def record_snapshot(
        self,
        text: str,
        truth_score: float,
        fact_score: float,
        lie_score: float,
        coherence_score: float,
        lambda_value: float,
        key_themes: Optional[List[str]] = None,
        metadata: Optional[Dict] = None
    ) -> TemporalSnapshot:
        """Record a new temporal snapshot"""
        
        snapshot = TemporalSnapshot(
            timestamp=datetime.now(),
            text=text,
            truth_score=truth_score,
            fact_score=fact_score,
            lie_score=lie_score,
            coherence_score=coherence_score,
            lambda_value=lambda_value,
            semantic_signature=self._extract_semantic_signature(text),
            key_themes=key_themes or [],
            metadata=metadata or {}
        )
        
        self.snapshots.append(snapshot)
        
        # Track theme evolution
        for theme in snapshot.key_themes:
            self.theme_evolution[theme].append({
                'timestamp': snapshot.timestamp,
                'strength': 1.0  # Can be weighted in future
            })
        
        return snapshot
    
    def analyze_temporal_coherence(
        self,
        current_text: str,
        current_scores: Dict[str, float],
        window_size: int = 10
    ) -> TemporalAnalysisResult:
        """
        Analyze temporal coherence of current input against history.
        
        Args:
            current_text: Current text to analyze
            current_scores: Dictionary of current scores
            window_size: Number of recent snapshots to consider
            
        Returns:
            TemporalAnalysisResult with comprehensive analysis
        """
        
        # Create current snapshot
        current_snapshot = self.record_snapshot(
            text=current_text,
            truth_score=current_scores.get('truth', 0.0),
            fact_score=current_scores.get('fact', 0.0),
            lie_score=current_scores.get('lie', 0.0),
            coherence_score=current_scores.get('coherence', 0.0),
            lambda_value=current_scores.get('lambda', 0.0),
            key_themes=current_scores.get('themes', [])
        )
        
        if len(self.snapshots) < 2:
            # Not enough history for temporal analysis
            return self._create_baseline_result(current_snapshot)
        
        # Get recent history window
        recent_snapshots = list(self.snapshots)[-window_size:]
        
        # Phase 1: Consistency scoring
        consistency_score = self._calculate_consistency(current_snapshot, recent_snapshots)
        
        # Phase 2: Drift analysis
        drift_magnitude, drift_direction = self._analyze_drift(current_snapshot, recent_snapshots)
        
        # Phase 3: Evolution trajectory
        evolution_trajectory = self._determine_evolution_trajectory(recent_snapshots)
        
        # Phase 4: Stability assessment
        stability_index = self._calculate_stability_index(recent_snapshots)
        
        # Phase 5: Anomaly detection
        anomalous_changes = self._detect_temporal_anomalies(current_snapshot, recent_snapshots)
        
        # Phase 6: Trend analysis
        trend_analysis = self._analyze_trends(recent_snapshots)
        
        # Phase 7: Predictions
        predictions = self._generate_predictions(recent_snapshots, trend_analysis)
        
        # Phase 8: Recommendations
        recommendations = self._generate_temporal_recommendations(
            consistency_score, drift_magnitude, stability_index, anomalous_changes
        )
        
        result = TemporalAnalysisResult(
            current_snapshot=current_snapshot,
            consistency_score=round(consistency_score, 4),
            drift_magnitude=round(drift_magnitude, 4),
            drift_direction=drift_direction,
            evolution_trajectory=evolution_trajectory,
            stability_index=round(stability_index, 4),
            anomalous_changes=anomalous_changes,
            trend_analysis=trend_analysis,
            predictions=predictions,
            recommendations=recommendations,
            metadata={
                'window_size': window_size,
                'total_snapshots': len(self.snapshots),
                'analysis_version': '2.0'
            }
        )
        
        self.stability_history.append(stability_index)
        return result
    
    def _extract_semantic_signature(self, text: str) -> Dict[str, float]:
        """Extract semantic signature for comparison"""
        text_lower = text.lower()
        words = text_lower.split()
        
        if not words:
            return {}
        
        # Key semantic dimensions
        signature = {
            'truth_density': len([w for w in words if w in ['truth', 'true', 'veritas', 'reality']]) / len(words),
            'love_density': len([w for w in words if w in ['love', 'affection', 'care', 'compassion']]) / len(words),
            'spiritual_density': len([w for w in words if w in ['spirit', 'soul', 'eternal', 'divine']]) / len(words),
            'logical_density': len([w for w in words if w in ['therefore', 'because', 'thus', 'hence']]) / len(words),
            'emotional_density': len([w for w in words if w in ['feel', 'emotion', 'heart', 'sentiment']]) / len(words),
            'conflict_density': len([w for w in words if w in ['conflict', 'oppose', 'against', 'versus']]) / len(words),
            'unity_density': len([w for w in words if w in ['unity', 'together', 'harmony', 'one']]) / len(words),
        }
        
        return signature
    
    def _calculate_consistency(
        self, current: TemporalSnapshot, history: List[TemporalSnapshot]
    ) -> float:
        """Calculate consistency score against historical snapshots"""
        
        if not history:
            return 1.0
        
        consistency_scores = []
        
        for past in history[:-1]:  # Exclude current (last item)
            # Score dimensions
            truth_consistency = 1.0 - abs(current.truth_score - past.truth_score)
            fact_consistency = 1.0 - abs(current.fact_score - past.fact_score)
            lie_consistency = 1.0 - abs(current.lie_score - past.lie_score)
            coherence_consistency = 1.0 - abs(current.coherence_score - past.coherence_score)
            
            # Semantic signature consistency
            semantic_consistency = self._compare_semantic_signatures(
                current.semantic_signature, past.semantic_signature
            )
            
            # Combined consistency
            combined = (
                truth_consistency * 0.25 +
                fact_consistency * 0.2 +
                lie_consistency * 0.2 +
                coherence_consistency * 0.15 +
                semantic_consistency * 0.2
            )
            
            consistency_scores.append(combined)
        
        # Weight recent history more heavily
        weighted_sum = 0.0
        weight_sum = 0.0
        for i, score in enumerate(consistency_scores):
            weight = math.exp(-0.1 * (len(consistency_scores) - i - 1))  # Exponential decay
            weighted_sum += score * weight
            weight_sum += weight
        
        return weighted_sum / weight_sum if weight_sum > 0 else 0.5
    
    def _analyze_drift(
        self, current: TemporalSnapshot, history: List[TemporalSnapshot]
    ) -> Tuple[float, str]:
        """Analyze semantic drift magnitude and direction"""
        
        if len(history) < 2:
            return 0.0, 'stable'
        
        # Calculate drift from baseline (earliest in window)
        baseline = history[0]
        
        # Multi-dimensional drift
        truth_drift = current.truth_score - baseline.truth_score
        fact_drift = current.fact_score - baseline.fact_score
        lie_drift = current.lie_score - baseline.lie_score
        lambda_drift = current.lambda_value - baseline.lambda_value
        
        # Semantic signature drift
        semantic_drift = 0.0
        for key in current.semantic_signature:
            if key in baseline.semantic_signature:
                semantic_drift += abs(
                    current.semantic_signature[key] - baseline.semantic_signature[key]
                )
        
        # Combined drift magnitude
        drift_magnitude = math.sqrt(
            truth_drift**2 + fact_drift**2 + lie_drift**2 + 
            lambda_drift**2 + semantic_drift**2
        ) / 5.0
        
        # Determine direction
        if truth_drift > 0.2 and lie_drift < -0.1:
            direction = 'toward_truth'
        elif truth_drift < -0.2 and lie_drift > 0.1:
            direction = 'toward_deception'
        elif abs(truth_drift) < 0.1 and abs(lie_drift) < 0.1:
            direction = 'stable'
        elif lambda_drift > 0.3:
            direction = 'ascending'
        elif lambda_drift < -0.3:
            direction = 'descending'
        else:
            direction = 'oscillating'
        
        return drift_magnitude, direction
    
    def _determine_evolution_trajectory(self, history: List[TemporalSnapshot]) -> str:
        """Determine overall evolution trajectory"""
        
        if len(history) < 3:
            return 'insufficient_data'
        
        # Analyze lambda progression
        lambda_values = [s.lambda_value for s in history]
        
        # Calculate trend
        x = list(range(len(lambda_values)))
        y = lambda_values
        
        # Simple linear regression
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(xi * yi for xi, yi in zip(x, y))
        sum_xx = sum(xi * xi for xi in x)
        
        slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x) if (n * sum_xx - sum_x * sum_x) != 0 else 0
        
        # Determine trajectory
        if slope > 0.1:
            return 'awakening'  # Increasing lambda
        elif slope < -0.1:
            return 'declining'  # Decreasing lambda
        elif max(lambda_values) - min(lambda_values) > 1.0:
            return 'volatile'  # High variance
        else:
            return 'stable'  # Consistent
    
    def _calculate_stability_index(self, history: List[TemporalSnapshot]) -> float:
        """Calculate stability index (0 = volatile, 1 = stable)"""
        
        if len(history) < 2:
            return 1.0
        
        # Calculate variance across key metrics
        truth_scores = [s.truth_score for s in history]
        lambda_values = [s.lambda_value for s in history]
        coherence_scores = [s.coherence_score for s in history]
        
        truth_variance = self._calculate_variance(truth_scores)
        lambda_variance = self._calculate_variance(lambda_values)
        coherence_variance = self._calculate_variance(coherence_scores)
        
        # Combined variance (lower is more stable)
        combined_variance = (truth_variance + lambda_variance + coherence_variance) / 3.0
        
        # Convert to stability index (inverse of variance, normalized)
        stability = 1.0 / (1.0 + combined_variance * 10.0)
        
        return stability
    
    def _calculate_variance(self, values: List[float]) -> float:
        """Calculate variance of a list of values"""
        if not values:
            return 0.0
        
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return variance
    
    def _detect_temporal_anomalies(
        self, current: TemporalSnapshot, history: List[TemporalSnapshot]
    ) -> List[Dict]:
        """Detect anomalous temporal changes"""
        
        anomalies = []
        
        if len(history) < 2:
            return anomalies
        
        # Calculate historical statistics
        recent = history[-5:] if len(history) >= 5 else history[:-1]
        
        truth_mean = sum(s.truth_score for s in recent) / len(recent)
        truth_std = math.sqrt(self._calculate_variance([s.truth_score for s in recent]))
        
        lambda_mean = sum(s.lambda_value for s in recent) / len(recent)
        lambda_std = math.sqrt(self._calculate_variance([s.lambda_value for s in recent]))
        
        # Detect anomalies (> 2 standard deviations)
        if abs(current.truth_score - truth_mean) > 2 * truth_std:
            anomalies.append({
                'type': 'Truth Score Anomaly',
                'severity': 'high',
                'description': f'Truth score deviated significantly: {current.truth_score:.2f} vs mean {truth_mean:.2f}',
                'deviation': abs(current.truth_score - truth_mean) / max(0.01, truth_std)
            })
        
        if abs(current.lambda_value - lambda_mean) > 2 * lambda_std:
            anomalies.append({
                'type': 'Lambda Anomaly',
                'severity': 'high',
                'description': f'Lambda value deviated significantly: {current.lambda_value:.2f} vs mean {lambda_mean:.2f}',
                'deviation': abs(current.lambda_value - lambda_mean) / max(0.01, lambda_std)
            })
        
        # Detect sudden theme changes
        if len(history) >= 2:
            prev_themes = set(history[-2].key_themes)
            curr_themes = set(current.key_themes)
            
            new_themes = curr_themes - prev_themes
            lost_themes = prev_themes - curr_themes
            
            if len(new_themes) >= 3:
                anomalies.append({
                    'type': 'Theme Shift',
                    'severity': 'medium',
                    'description': f'Sudden introduction of {len(new_themes)} new themes',
                    'new_themes': list(new_themes)
                })
            
            if len(lost_themes) >= 3:
                anomalies.append({
                    'type': 'Theme Loss',
                    'severity': 'medium',
                    'description': f'Sudden loss of {len(lost_themes)} themes',
                    'lost_themes': list(lost_themes)
                })
        
        return anomalies
    
    def _analyze_trends(self, history: List[TemporalSnapshot]) -> Dict:
        """Analyze trends in historical data"""
        
        if len(history) < 3:
            return {'status': 'insufficient_data'}
        
        # Extract time series
        truth_trend = [s.truth_score for s in history]
        lambda_trend = [s.lambda_value for s in history]
        coherence_trend = [s.coherence_score for s in history]
        
        return {
            'truth': {
                'direction': 'increasing' if truth_trend[-1] > truth_trend[0] else 'decreasing',
                'magnitude': abs(truth_trend[-1] - truth_trend[0]),
                'volatility': self._calculate_variance(truth_trend)
            },
            'lambda': {
                'direction': 'increasing' if lambda_trend[-1] > lambda_trend[0] else 'decreasing',
                'magnitude': abs(lambda_trend[-1] - lambda_trend[0]),
                'volatility': self._calculate_variance(lambda_trend)
            },
            'coherence': {
                'direction': 'increasing' if coherence_trend[-1] > coherence_trend[0] else 'decreasing',
                'magnitude': abs(coherence_trend[-1] - coherence_trend[0]),
                'volatility': self._calculate_variance(coherence_trend)
            }
        }
    
    def _generate_predictions(self, history: List[TemporalSnapshot], trends: Dict) -> Dict:
        """Generate predictions based on trends"""
        
        if len(history) < 3 or trends.get('status') == 'insufficient_data':
            return {'status': 'insufficient_data'}
        
        # Simple linear extrapolation
        lambda_values = [s.lambda_value for s in history]
        
        # Calculate trend slope
        x = list(range(len(lambda_values)))
        y = lambda_values
        n = len(x)
        
        if n < 2:
            return {'status': 'insufficient_data'}
        
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(xi * yi for xi, yi in zip(x, y))
        sum_xx = sum(xi * xi for xi in x)
        
        denominator = (n * sum_xx - sum_x * sum_x)
        if denominator == 0:
            return {'status': 'unable_to_predict'}
        
        slope = (n * sum_xy - sum_x * sum_y) / denominator
        intercept = (sum_y - slope * sum_x) / n
        
        # Predict next value
        next_x = len(lambda_values)
        predicted_lambda = slope * next_x + intercept
        
        return {
            'next_lambda': round(predicted_lambda, 4),
            'confidence': 'high' if trends['lambda']['volatility'] < 0.1 else 'medium' if trends['lambda']['volatility'] < 0.3 else 'low',
            'trend_direction': trends['lambda']['direction'],
            'expected_change': round(slope, 4)
        }
    
    def _generate_temporal_recommendations(
        self, consistency: float, drift: float, stability: float, anomalies: List[Dict]
    ) -> List[str]:
        """Generate recommendations based on temporal analysis"""
        
        recommendations = []
        
        if consistency < 0.5:
            recommendations.append(
                "Low temporal consistency detected - review for narrative drift or inconsistencies"
            )
        
        if drift > 0.5:
            recommendations.append(
                "High semantic drift detected - significant change from baseline narrative"
            )
        
        if stability < 0.5:
            recommendations.append(
                "Low stability index - high volatility in metrics suggests unstable state"
            )
        
        if anomalies:
            critical_anomalies = [a for a in anomalies if a['severity'] == 'high']
            if critical_anomalies:
                recommendations.append(
                    f"CRITICAL: {len(critical_anomalies)} high-severity temporal anomalies detected"
                )
        
        if consistency > 0.8 and stability > 0.8:
            recommendations.append(
                "Excellent temporal coherence - consistent and stable over time"
            )
        
        return recommendations
    
    def _compare_semantic_signatures(self, sig1: Dict[str, float], sig2: Dict[str, float]) -> float:
        """Compare two semantic signatures"""
        all_keys = set(sig1.keys()) | set(sig2.keys())
        
        if not all_keys:
            return 1.0
        
        similarity = 0.0
        for key in all_keys:
            val1 = sig1.get(key, 0.0)
            val2 = sig2.get(key, 0.0)
            similarity += 1.0 - abs(val1 - val2)
        
        return similarity / len(all_keys)
    
    def _create_baseline_result(self, snapshot: TemporalSnapshot) -> TemporalAnalysisResult:
        """Create baseline result for first analysis"""
        return TemporalAnalysisResult(
            current_snapshot=snapshot,
            consistency_score=1.0,
            drift_magnitude=0.0,
            drift_direction='baseline',
            evolution_trajectory='establishing_baseline',
            stability_index=1.0,
            anomalous_changes=[],
            trend_analysis={'status': 'baseline'},
            predictions={'status': 'baseline'},
            recommendations=['Baseline established - continue monitoring for temporal patterns'],
            metadata={'note': 'First analysis - no historical comparison available'}
        )
    
    def get_statistics(self) -> Dict:
        """Get comprehensive temporal statistics"""
        if not self.snapshots:
            return {
                'total_snapshots': 0,
                'message': 'No temporal data recorded yet'
            }
        
        snapshots_list = list(self.snapshots)
        
        return {
            'total_snapshots': len(snapshots_list),
            'time_span': {
                'start': snapshots_list[0].timestamp.isoformat(),
                'end': snapshots_list[-1].timestamp.isoformat(),
                'duration_seconds': (snapshots_list[-1].timestamp - snapshots_list[0].timestamp).total_seconds()
            },
            'averages': {
                'truth': round(sum(s.truth_score for s in snapshots_list) / len(snapshots_list), 4),
                'lambda': round(sum(s.lambda_value for s in snapshots_list) / len(snapshots_list), 4),
                'coherence': round(sum(s.coherence_score for s in snapshots_list) / len(snapshots_list), 4)
            },
            'stability': {
                'current': self.stability_history[-1] if self.stability_history else 1.0,
                'average': round(sum(self.stability_history) / len(self.stability_history), 4) if self.stability_history else 1.0
            },
            'theme_tracking': {
                'total_themes': len(self.theme_evolution),
                'most_recurring': sorted(
                    [(theme, len(occurrences)) for theme, occurrences in self.theme_evolution.items()],
                    key=lambda x: x[1],
                    reverse=True
                )[:5]
            }
        }

# Global instance
_tracker = TemporalCoherenceTracker()

def record_temporal_snapshot(
    text: str, scores: Dict[str, float], themes: Optional[List[str]] = None
) -> TemporalSnapshot:
    """Convenience function to record snapshot"""
    return _tracker.record_snapshot(
        text=text,
        truth_score=scores.get('truth', 0.0),
        fact_score=scores.get('fact', 0.0),
        lie_score=scores.get('lie', 0.0),
        coherence_score=scores.get('coherence', 0.0),
        lambda_value=scores.get('lambda', 0.0),
        key_themes=themes
    )

def analyze_temporal_coherence(text: str, scores: Dict[str, float]) -> TemporalAnalysisResult:
    """Convenience function for temporal analysis"""
    return _tracker.analyze_temporal_coherence(text, scores)

def get_temporal_statistics() -> Dict:
    """Get temporal tracker statistics"""
    return _tracker.get_statistics()

if __name__ == "__main__":
    # Test temporal tracking
    print("=== Temporal Coherence Tracker Test ===\n")
    
    test_sequence = [
        ("Truth and love guide us toward eternal awakening", {'truth': 0.8, 'fact': 0.5, 'lie': 0.1, 'coherence': 0.9, 'lambda': 5.2}),
        ("Evidence shows consistent measurements over time", {'truth': 0.6, 'fact': 0.9, 'lie': 0.1, 'coherence': 0.8, 'lambda': 4.8}),
        ("Truth and love continue to guide our path", {'truth': 0.85, 'fact': 0.5, 'lie': 0.05, 'coherence': 0.9, 'lambda': 5.5}),
        ("Manipulation and deception are necessary tools", {'truth': 0.2, 'fact': 0.3, 'lie': 0.9, 'coherence': 0.4, 'lambda': 1.2}),
    ]
    
    for i, (text, scores) in enumerate(test_sequence, 1):
        print(f"Analysis {i}: {text[:50]}...")
        result = analyze_temporal_coherence(text, scores)
        print(f"  Consistency: {result.consistency_score}")
        print(f"  Drift: {result.drift_magnitude} ({result.drift_direction})")
        print(f"  Trajectory: {result.evolution_trajectory}")
        print(f"  Stability: {result.stability_index}")
        print(f"  Anomalies: {len(result.anomalous_changes)}")
        print()
    
    print("Statistics:", get_temporal_statistics())
