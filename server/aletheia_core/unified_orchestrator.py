"""
UNIFIED_ORCHESTRATOR.PY - Comprehensive Analysis Orchestration Layer
====================================================================
Integrates all analysis engines into a unified, comprehensive analysis system.
Coordinates Lambda, DreamSpeak, Discernment, Pattern Recognition, and Temporal tracking.

Version: 2.0 (Enhanced Kingdom Covenant)
"""

import sys
from typing import Dict, List, Optional
from datetime import datetime
from dataclasses import dataclass, field
import json

# Import all engine modules
try:
    from lambda_engine import calculate_lambda, get_system_summary
    from throne_room import enter_throne_room, generate_prophecy, get_throne_status
    from axioms import COVENANT_MARKERS, verify_axiom_compliance
    from discernment_enhanced import analyze_discernment, get_discernment_statistics
    from pattern_recognition import analyze_patterns, get_pattern_statistics
    from temporal_coherence import analyze_temporal_coherence, get_temporal_statistics
except ImportError:
    # Try relative imports
    try:
        from .lambda_engine import calculate_lambda, get_system_summary
        from .throne_room import enter_throne_room, generate_prophecy, get_throne_status
        from .axioms import COVENANT_MARKERS, verify_axiom_compliance
        from .discernment_enhanced import analyze_discernment, get_discernment_statistics
        from .pattern_recognition import analyze_patterns, get_pattern_statistics
        from .temporal_coherence import analyze_temporal_coherence, get_temporal_statistics
    except ImportError:
        # Fallback for direct execution
        print("Warning: Some imports failed. Running in standalone mode.")
        COVENANT_MARKERS = {}

@dataclass
class ComprehensiveAnalysisResult:
    """Complete analysis result from all engines"""
    # Core identification
    analysis_id: str
    timestamp: str
    text: str
    text_length: int
    word_count: int
    
    # Lambda & Resonance Analysis
    lambda_analysis: Dict
    throne_room_access: Dict
    prophecy: Optional[Dict]
    
    # Discernment Analysis
    discernment_analysis: Dict
    
    # Pattern Recognition
    pattern_analysis: Dict
    
    # Temporal Coherence
    temporal_analysis: Dict
    
    # Unified Scores
    unified_scores: Dict
    
    # Overall Assessment
    overall_status: str
    overall_confidence: float
    risk_level: str
    
    # Recommendations & Actions
    recommendations: List[str]
    warnings: List[str]
    action_items: List[str]
    
    # System State
    system_summary: Dict
    covenant_markers: Dict
    
    # Metadata
    metadata: Dict = field(default_factory=dict)

class UnifiedOrchestrator:
    """
    Unified orchestration layer coordinating all analysis engines.
    
    Provides:
    1. Comprehensive multi-engine analysis
    2. Score unification and normalization
    3. Risk assessment and classification
    4. Actionable recommendations
    5. System state monitoring
    """
    
    def __init__(self):
        self.analysis_history = []
        self.analysis_count = 0
        
    def analyze_comprehensive(
        self,
        text: str,
        context: Optional[Dict] = None,
        include_prophecy: bool = True,
        temporal_window: int = 10
    ) -> ComprehensiveAnalysisResult:
        """
        Perform comprehensive analysis using all available engines.
        
        Args:
            text: Input text to analyze
            context: Optional contextual information
            include_prophecy: Whether to generate prophecy (requires throne access)
            temporal_window: Size of temporal analysis window
            
        Returns:
            ComprehensiveAnalysisResult with complete multi-engine analysis
        """
        
        self.analysis_count += 1
        analysis_id = f"ALE-{datetime.now().strftime('%Y%m%d')}-{self.analysis_count:06d}"
        timestamp = datetime.now().isoformat()
        
        # Basic text metrics
        word_count = len(text.split())
        text_length = len(text)
        
        print(f"[Orchestrator] Starting comprehensive analysis {analysis_id}...")
        
        # ========================================================================
        # PHASE 1: Lambda & Resonance Analysis
        # ========================================================================
        print("[Orchestrator] Phase 1: Lambda & Resonance Analysis...")
        try:
            lambda_result = calculate_lambda(text)
            composite_resonance = lambda_result['metrics']['composite_resonance']
        except Exception as e:
            print(f"[Orchestrator] Lambda analysis failed: {e}")
            lambda_result = self._create_fallback_lambda()
            composite_resonance = 0.0
        
        # ========================================================================
        # PHASE 2: Throne Room Access Check
        # ========================================================================
        print("[Orchestrator] Phase 2: Throne Room Access...")
        try:
            throne_access = enter_throne_room(composite_resonance)
        except Exception as e:
            print(f"[Orchestrator] Throne room check failed: {e}")
            throne_access = {'success': False, 'reason': 'Error in access check'}
        
        # ========================================================================
        # PHASE 3: Prophecy Generation (if authorized)
        # ========================================================================
        prophecy = None
        if include_prophecy and throne_access.get('success'):
            print("[Orchestrator] Phase 3: Generating Prophecy...")
            try:
                prophecy = generate_prophecy(lambda_result)
            except Exception as e:
                print(f"[Orchestrator] Prophecy generation failed: {e}")
        
        # ========================================================================
        # PHASE 4: Enhanced Discernment Analysis
        # ========================================================================
        print("[Orchestrator] Phase 4: Discernment Analysis...")
        try:
            discernment_result = analyze_discernment(text, context)
            discernment_dict = {
                'truth_score': discernment_result.truth_score,
                'fact_score': discernment_result.fact_score,
                'lie_score': discernment_result.lie_score,
                'coherence_score': discernment_result.coherence_score,
                'semantic_drift': discernment_result.semantic_drift,
                'temporal_consistency': discernment_result.temporal_consistency,
                'violations': discernment_result.violations,
                'phase_separation': discernment_result.phase_separation,
                'confidence': discernment_result.confidence,
                'recommendations': discernment_result.recommendations
            }
        except Exception as e:
            print(f"[Orchestrator] Discernment analysis failed: {e}")
            discernment_dict = self._create_fallback_discernment()
        
        # ========================================================================
        # PHASE 5: Pattern Recognition
        # ========================================================================
        print("[Orchestrator] Phase 5: Pattern Recognition...")
        try:
            pattern_result = analyze_patterns(text, context)
            pattern_dict = {
                'detected_patterns': len(pattern_result.detected_patterns),
                'pattern_types': {
                    ptype: len(patterns) 
                    for ptype, patterns in pattern_result.pattern_clusters.items()
                },
                'manipulation_score': pattern_result.manipulation_score,
                'authenticity_score': pattern_result.authenticity_score,
                'structural_integrity': pattern_result.structural_integrity,
                'recurring_themes': pattern_result.recurring_themes,
                'anomalies': pattern_result.anomalies,
                'recommendations': pattern_result.recommendations
            }
        except Exception as e:
            print(f"[Orchestrator] Pattern recognition failed: {e}")
            pattern_dict = self._create_fallback_pattern()
        
        # ========================================================================
        # PHASE 6: Temporal Coherence Analysis
        # ========================================================================
        print("[Orchestrator] Phase 6: Temporal Coherence...")
        try:
            temporal_scores = {
                'truth': discernment_dict.get('truth_score', 0.0),
                'fact': discernment_dict.get('fact_score', 0.0),
                'lie': discernment_dict.get('lie_score', 0.0),
                'coherence': discernment_dict.get('coherence_score', 0.0),
                'lambda': composite_resonance
            }
            temporal_result = analyze_temporal_coherence(text, temporal_scores, temporal_window)
            temporal_dict = {
                'consistency_score': temporal_result.consistency_score,
                'drift_magnitude': temporal_result.drift_magnitude,
                'drift_direction': temporal_result.drift_direction,
                'evolution_trajectory': temporal_result.evolution_trajectory,
                'stability_index': temporal_result.stability_index,
                'anomalous_changes': temporal_result.anomalous_changes,
                'trend_analysis': temporal_result.trend_analysis,
                'predictions': temporal_result.predictions,
                'recommendations': temporal_result.recommendations
            }
        except Exception as e:
            print(f"[Orchestrator] Temporal analysis failed: {e}")
            temporal_dict = self._create_fallback_temporal()
        
        # ========================================================================
        # PHASE 7: Score Unification
        # ========================================================================
        print("[Orchestrator] Phase 7: Unifying Scores...")
        unified_scores = self._unify_scores(
            lambda_result, discernment_dict, pattern_dict, temporal_dict
        )
        
        # ========================================================================
        # PHASE 8: Overall Assessment
        # ========================================================================
        print("[Orchestrator] Phase 8: Overall Assessment...")
        overall_status, overall_confidence, risk_level = self._assess_overall(
            unified_scores, discernment_dict, pattern_dict, temporal_dict
        )
        
        # ========================================================================
        # PHASE 9: Recommendations & Warnings
        # ========================================================================
        print("[Orchestrator] Phase 9: Generating Recommendations...")
        recommendations, warnings, action_items = self._generate_comprehensive_recommendations(
            unified_scores, discernment_dict, pattern_dict, temporal_dict, risk_level
        )
        
        # ========================================================================
        # PHASE 10: System State Collection
        # ========================================================================
        print("[Orchestrator] Phase 10: Collecting System State...")
        try:
            system_summary = get_system_summary()
        except Exception as e:
            print(f"[Orchestrator] System summary failed: {e}")
            system_summary = {'status': 'unavailable'}
        
        # ========================================================================
        # Final Result Assembly
        # ========================================================================
        result = ComprehensiveAnalysisResult(
            analysis_id=analysis_id,
            timestamp=timestamp,
            text=text,
            text_length=text_length,
            word_count=word_count,
            lambda_analysis=lambda_result,
            throne_room_access=throne_access,
            prophecy=prophecy,
            discernment_analysis=discernment_dict,
            pattern_analysis=pattern_dict,
            temporal_analysis=temporal_dict,
            unified_scores=unified_scores,
            overall_status=overall_status,
            overall_confidence=overall_confidence,
            risk_level=risk_level,
            recommendations=recommendations,
            warnings=warnings,
            action_items=action_items,
            system_summary=system_summary,
            covenant_markers=COVENANT_MARKERS,
            metadata={
                'context': context or {},
                'analysis_version': '2.0',
                'engines_used': [
                    'lambda_engine',
                    'throne_room',
                    'discernment_enhanced',
                    'pattern_recognition',
                    'temporal_coherence'
                ]
            }
        )
        
        self.analysis_history.append(result)
        print(f"[Orchestrator] Analysis {analysis_id} complete!")
        
        return result
    
    def _unify_scores(
        self, lambda_res: Dict, discern: Dict, pattern: Dict, temporal: Dict
    ) -> Dict:
        """Unify scores from all engines into a coherent assessment"""
        
        # Extract key scores
        lambda_score = lambda_res.get('metrics', {}).get('composite_resonance', 0.0)
        truth_score = discern.get('truth_score', 0.0)
        authenticity_score = pattern.get('authenticity_score', 0.0)
        coherence_score = discern.get('coherence_score', 0.0)
        consistency_score = temporal.get('consistency_score', 0.0)
        
        # Manipulation and lie detection (negative indicators)
        lie_score = discern.get('lie_score', 0.0)
        manipulation_score = pattern.get('manipulation_score', 0.0)
        
        # Unified Truth Index (0-10 scale)
        truth_index = (
            (truth_score * 3.0) +
            (authenticity_score * 2.5) +
            (lambda_score * 0.3) +
            (coherence_score * 2.0) +
            (consistency_score * 2.0) -
            (lie_score * 2.0) -
            (manipulation_score * 3.0)
        )
        truth_index = max(0.0, min(10.0, truth_index))
        
        # Unified Integrity Index (0-10 scale)
        integrity_index = (
            (coherence_score * 3.0) +
            (pattern.get('structural_integrity', 0.5) * 3.0) +
            (consistency_score * 2.0) +
            (temporal.get('stability_index', 0.5) * 2.0)
        )
        integrity_index = max(0.0, min(10.0, integrity_index))
        
        # Unified Risk Index (0-10 scale, higher = more risk)
        risk_index = (
            (manipulation_score * 4.0) +
            (lie_score * 3.0) +
            (1.0 - authenticity_score) * 2.0 +
            (temporal.get('drift_magnitude', 0.0) * 1.0)
        )
        risk_index = max(0.0, min(10.0, risk_index))
        
        # Unified Awakening Index (0-10 scale)
        awakening_index = lambda_score * 0.6  # Lambda is primary awakening metric
        
        return {
            'truth_index': round(truth_index, 4),
            'integrity_index': round(integrity_index, 4),
            'risk_index': round(risk_index, 4),
            'awakening_index': round(awakening_index, 4),
            'component_scores': {
                'lambda': round(lambda_score, 4),
                'truth': round(truth_score, 4),
                'authenticity': round(authenticity_score, 4),
                'coherence': round(coherence_score, 4),
                'consistency': round(consistency_score, 4),
                'manipulation': round(manipulation_score, 4),
                'lie': round(lie_score, 4)
            }
        }
    
    def _assess_overall(
        self, unified: Dict, discern: Dict, pattern: Dict, temporal: Dict
    ) -> tuple:
        """Assess overall status, confidence, and risk level"""
        
        truth_index = unified['truth_index']
        risk_index = unified['risk_index']
        integrity_index = unified['integrity_index']
        
        # Determine overall status
        if truth_index >= 8.0 and risk_index < 2.0:
            status = "TRUTH_ALIGNED"
        elif truth_index >= 6.0 and risk_index < 3.0:
            status = "TRUTH_SEEKING"
        elif truth_index >= 4.0 and risk_index < 5.0:
            status = "NEUTRAL"
        elif risk_index >= 7.0:
            status = "HIGH_RISK"
        elif risk_index >= 5.0:
            status = "CAUTION_ADVISED"
        else:
            status = "UNCLEAR"
        
        # Calculate overall confidence
        discern_confidence = discern.get('confidence', 0.5)
        temporal_stability = temporal.get('stability_index', 0.5)
        
        overall_confidence = (
            (discern_confidence * 0.4) +
            (temporal_stability * 0.3) +
            ((1.0 - (risk_index / 10.0)) * 0.3)
        )
        
        # Determine risk level
        if risk_index >= 7.0:
            risk_level = "CRITICAL"
        elif risk_index >= 5.0:
            risk_level = "HIGH"
        elif risk_index >= 3.0:
            risk_level = "MEDIUM"
        elif risk_index >= 1.0:
            risk_level = "LOW"
        else:
            risk_level = "MINIMAL"
        
        return status, round(overall_confidence, 4), risk_level
    
    def _generate_comprehensive_recommendations(
        self, unified: Dict, discern: Dict, pattern: Dict, temporal: Dict, risk_level: str
    ) -> tuple:
        """Generate comprehensive recommendations, warnings, and action items"""
        
        recommendations = []
        warnings = []
        action_items = []
        
        # Risk-based warnings
        if risk_level == "CRITICAL":
            warnings.append("⚠️ CRITICAL RISK: Multiple severe issues detected - immediate action required")
        elif risk_level == "HIGH":
            warnings.append("⚠️ HIGH RISK: Significant concerns identified - careful review needed")
        
        # Truth index recommendations
        truth_index = unified['truth_index']
        if truth_index < 4.0:
            recommendations.append("Increase truth content: Incorporate eternal principles and verifiable facts")
            action_items.append("Review content for truth alignment")
        elif truth_index >= 8.0:
            recommendations.append("Excellent truth alignment maintained")
        
        # Manipulation warnings
        manipulation_score = unified['component_scores']['manipulation']
        if manipulation_score > 0.7:
            warnings.append("⚠️ High manipulation score - multiple manipulation tactics detected")
            action_items.append("Remove manipulative language immediately")
        elif manipulation_score > 0.4:
            warnings.append("Moderate manipulation patterns detected")
            action_items.append("Review for manipulative language")
        
        # Discernment recommendations
        if discern.get('violations'):
            warnings.append(f"⚠️ {len(discern['violations'])} covenant violations detected")
            action_items.append("Address covenant violations")
        
        # Pattern-based recommendations
        pattern_recommendations = pattern.get('recommendations', [])
        recommendations.extend(pattern_recommendations[:2])  # Top 2
        
        # Temporal recommendations
        temporal_recommendations = temporal.get('recommendations', [])
        recommendations.extend(temporal_recommendations[:2])  # Top 2
        
        # Drift warnings
        drift_magnitude = temporal.get('drift_magnitude', 0.0)
        if drift_magnitude > 0.5:
            warnings.append("⚠️ High semantic drift detected - significant change from baseline")
            action_items.append("Review narrative consistency")
        
        # Anomaly warnings
        anomalies = temporal.get('anomalous_changes', [])
        if anomalies:
            critical_anomalies = [a for a in anomalies if a.get('severity') == 'high']
            if critical_anomalies:
                warnings.append(f"⚠️ {len(critical_anomalies)} critical temporal anomalies detected")
        
        return recommendations, warnings, action_items
    
    def _create_fallback_lambda(self) -> Dict:
        """Create fallback lambda result"""
        return {
            'metrics': {
                'composite_resonance': 0.0,
                'truth_density': 0.0,
                'love_resonance': 0.0
            },
            'status': 'ERROR',
            'emoji': '⚠️'
        }
    
    def _create_fallback_discernment(self) -> Dict:
        """Create fallback discernment result"""
        return {
            'truth_score': 0.0,
            'fact_score': 0.0,
            'lie_score': 0.0,
            'coherence_score': 0.5,
            'semantic_drift': 0.0,
            'temporal_consistency': 0.5,
            'violations': [],
            'phase_separation': {'snr': 1.0},
            'confidence': 0.0,
            'recommendations': ['Analysis unavailable']
        }
    
    def _create_fallback_pattern(self) -> Dict:
        """Create fallback pattern result"""
        return {
            'detected_patterns': 0,
            'pattern_types': {},
            'manipulation_score': 0.0,
            'authenticity_score': 0.5,
            'structural_integrity': 0.5,
            'recurring_themes': [],
            'anomalies': [],
            'recommendations': ['Analysis unavailable']
        }
    
    def _create_fallback_temporal(self) -> Dict:
        """Create fallback temporal result"""
        return {
            'consistency_score': 0.5,
            'drift_magnitude': 0.0,
            'drift_direction': 'unknown',
            'evolution_trajectory': 'unknown',
            'stability_index': 0.5,
            'anomalous_changes': [],
            'trend_analysis': {},
            'predictions': {},
            'recommendations': ['Analysis unavailable']
        }
    
    def get_statistics(self) -> Dict:
        """Get comprehensive orchestrator statistics"""
        if not self.analysis_history:
            return {
                'total_analyses': 0,
                'message': 'No analyses performed yet'
            }
        
        return {
            'total_analyses': len(self.analysis_history),
            'risk_distribution': {
                'CRITICAL': sum(1 for a in self.analysis_history if a.risk_level == 'CRITICAL'),
                'HIGH': sum(1 for a in self.analysis_history if a.risk_level == 'HIGH'),
                'MEDIUM': sum(1 for a in self.analysis_history if a.risk_level == 'MEDIUM'),
                'LOW': sum(1 for a in self.analysis_history if a.risk_level == 'LOW'),
                'MINIMAL': sum(1 for a in self.analysis_history if a.risk_level == 'MINIMAL')
            },
            'status_distribution': {
                status: sum(1 for a in self.analysis_history if a.overall_status == status)
                for status in set(a.overall_status for a in self.analysis_history)
            },
            'average_scores': {
                'truth_index': round(
                    sum(a.unified_scores['truth_index'] for a in self.analysis_history) / len(self.analysis_history), 4
                ),
                'risk_index': round(
                    sum(a.unified_scores['risk_index'] for a in self.analysis_history) / len(self.analysis_history), 4
                ),
                'integrity_index': round(
                    sum(a.unified_scores['integrity_index'] for a in self.analysis_history) / len(self.analysis_history), 4
                )
            },
            'total_warnings': sum(len(a.warnings) for a in self.analysis_history),
            'total_action_items': sum(len(a.action_items) for a in self.analysis_history)
        }
    
    def export_result_json(self, result: ComprehensiveAnalysisResult) -> str:
        """Export result as JSON string"""
        # Convert dataclass to dict
        result_dict = {
            'analysis_id': result.analysis_id,
            'timestamp': result.timestamp,
            'text': result.text,
            'text_length': result.text_length,
            'word_count': result.word_count,
            'lambda_analysis': result.lambda_analysis,
            'throne_room_access': result.throne_room_access,
            'prophecy': result.prophecy,
            'discernment_analysis': result.discernment_analysis,
            'pattern_analysis': result.pattern_analysis,
            'temporal_analysis': result.temporal_analysis,
            'unified_scores': result.unified_scores,
            'overall_status': result.overall_status,
            'overall_confidence': result.overall_confidence,
            'risk_level': result.risk_level,
            'recommendations': result.recommendations,
            'warnings': result.warnings,
            'action_items': result.action_items,
            'system_summary': result.system_summary,
            'covenant_markers': result.covenant_markers,
            'metadata': result.metadata
        }
        
        return json.dumps(result_dict, indent=2, default=str)

# Global instance
_orchestrator = UnifiedOrchestrator()

def analyze_comprehensive(
    text: str,
    context: Optional[Dict] = None,
    include_prophecy: bool = True
) -> ComprehensiveAnalysisResult:
    """Convenience function for comprehensive analysis"""
    return _orchestrator.analyze_comprehensive(text, context, include_prophecy)

def get_orchestrator_statistics() -> Dict:
    """Get orchestrator statistics"""
    return _orchestrator.get_statistics()

def export_analysis_json(result: ComprehensiveAnalysisResult) -> str:
    """Export analysis result as JSON"""
    return _orchestrator.export_result_json(result)

if __name__ == "__main__":
    # Test comprehensive analysis
    print("=== Unified Orchestrator Test ===\n")
    
    test_text = "💜 Truth and love are eternal principles that guide consciousness toward awakening. Our hearts beat together in harmony and unity. ✨"
    
    print(f"Analyzing: {test_text}\n")
    result = analyze_comprehensive(test_text)
    
    print(f"\nAnalysis ID: {result.analysis_id}")
    print(f"Overall Status: {result.overall_status}")
    print(f"Risk Level: {result.risk_level}")
    print(f"Confidence: {result.overall_confidence}")
    print(f"\nUnified Scores:")
    print(f"  Truth Index: {result.unified_scores['truth_index']}/10")
    print(f"  Integrity Index: {result.unified_scores['integrity_index']}/10")
    print(f"  Risk Index: {result.unified_scores['risk_index']}/10")
    print(f"  Awakening Index: {result.unified_scores['awakening_index']}/10")
    print(f"\nWarnings: {len(result.warnings)}")
    print(f"Recommendations: {len(result.recommendations)}")
    print(f"Action Items: {len(result.action_items)}")
