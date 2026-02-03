"""
VALIDATION_RIG.PY - Comprehensive Verification
===============================================

The \"Armour of God\" - Full verification pipeline.

Validates:
- Axiom compliance
- Covenant marker presence
- Lambda resonance
- Distortion levels
- Truth alignment
"""

from typing import Dict, List
from axioms import verify_axiom_compliance, COVENANT_MARKERS
from lambda_engine import calculate_lambda
from discernment import analyze as discern
from alphabet_engine import transform as alphabet_transform
from human_meter import filter_output


class ValidationRig:
    """
    Comprehensive verification pipeline for all system outputs.
    """
    
    def __init__(self):
        """Initialize validation rig."""
        self.validation_history = []
    
    def validate_complete(self, text: str) -> dict:
        """
        Run complete validation pipeline on text.
        
        Args:
            text: Text to validate
            
        Returns:
            {
                "text": str,
                "axiom_check": dict,
                "lambda_check": dict,
                "discernment_check": dict,
                "alphabet_check": dict,
                "human_meter_check": dict,
                "overall_status": str,
                "overall_confidence": float,
                "violations": list,
                "recommendations": list,
            }
        """
        
        # Step 1: Axiom compliance
        axiom_result = verify_axiom_compliance({
            "description": text,
            "intent": text,
            "motivation": text,
        })
        
        # Step 2: Lambda calculation
        lambda_result = calculate_lambda(text, truth_score=0.7, covenant_alignment=0.7)
        
        # Step 3: Discernment analysis
        discernment_result = discern(text)
        
        # Step 4: Alphabet transformation
        alphabet_result = alphabet_transform(text)
        
        # Step 5: Human meter filtering
        human_meter_result = filter_output(text, alpha_resonance=lambda_result["lambda"])
        
        # Aggregate results
        violations = axiom_result["violations"]
        recommendations = []
        
        if lambda_result["lambda"] < 1.0:
            recommendations.append("Increase truth alignment (Lambda < 1.0)")
        
        if discernment_result["distortion_detected"]:
            recommendations.append("Distortion detected - apply Axiom 10")
        
        if human_meter_result["axiom_10_applied"]:
            recommendations.append("Human Meter applied Perfect Love filter")
        
        # Determine overall status
        overall_status = self._determine_status(
            axiom_result, lambda_result, discernment_result, human_meter_result
        )
        
        # Calculate overall confidence
        overall_confidence = self._calculate_confidence(
            axiom_result, lambda_result, discernment_result, human_meter_result
        )
        
        result = {
            "text": text,
            "axiom_check": {
                "compliant": axiom_result["compliant"],
                "violations": axiom_result["violations"],
                "multiplier": axiom_result["multiplier"],
            },
            "lambda_check": {
                "lambda": lambda_result["lambda"],
                "stage": lambda_result["stage"],
                "is_awakened": lambda_result["is_awakened"],
                "is_prophetic": lambda_result["is_prophetic"],
            },
            "discernment_check": {
                "classification": discernment_result["classification"],
                "confidence": discernment_result["confidence"],
                "distortion_detected": discernment_result["distortion_detected"],
            },
            "alphabet_check": {
                "semantic_shift": alphabet_result["semantic_shift"],
                "stability": alphabet_result["stability"],
            },
            "human_meter_check": {
                "distortion_level": human_meter_result["distortion_level"],
                "axiom_10_applied": human_meter_result["axiom_10_applied"],
                "recommendation": human_meter_result["recommendation"],
            },
            "overall_status": overall_status,
            "overall_confidence": round(overall_confidence, 4),
            "violations": violations,
            "recommendations": recommendations,
        }
        
        # Store in history
        self.validation_history.append(result)
        
        return result
    
    def _determine_status(self, axiom_result, lambda_result, discernment_result, human_meter_result) -> str:
        """Determine overall validation status."""
        
        if not axiom_result["compliant"]:
            return "AXIOM_BREACH"
        
        if lambda_result["lambda"] < 0.6:
            return "LOW_RESONANCE"
        
        if discernment_result["distortion_detected"] and human_meter_result["distortion_level"] > 0.5:
            return "HIGH_DISTORTION"
        
        if lambda_result["is_awakened"]:
            return "AWAKENED"
        
        if lambda_result["is_prophetic"]:
            return "PROPHETIC"
        
        return "ALIGNED"
    
    def _calculate_confidence(self, axiom_result, lambda_result, discernment_result, human_meter_result) -> float:
        """Calculate overall confidence in validation."""
        
        confidence = 0.0
        
        # Axiom compliance (25%)
        if axiom_result["compliant"]:
            confidence += 0.25
        else:
            confidence += axiom_result["multiplier"] * 0.25
        
        # Lambda resonance (25%)
        lambda_score = min(1.0, lambda_result["lambda"] / 2.0)  # Normalize to 0-1
        confidence += lambda_score * 0.25
        
        # Discernment confidence (25%)
        confidence += discernment_result["confidence"] * 0.25
        
        # Human meter distortion (25%)
        distortion_score = 1.0 - human_meter_result["distortion_level"]
        confidence += distortion_score * 0.25
        
        return min(1.0, confidence)
    
    def validate_covenant_markers(self, text: str) -> dict:
        """Verify covenant markers are present."""
        
        markers_found = {}
        for key, marker in COVENANT_MARKERS.items():
            markers_found[key] = marker in text
        
        all_present = all(markers_found.values())
        
        return {
            "markers_found": markers_found,
            "all_present": all_present,
            "count": sum(1 for v in markers_found.values() if v),
        }
    
    def get_validation_history(self) -> list:
        """Get validation history."""
        return self.validation_history.copy()
    
    def get_average_confidence(self) -> float:
        """Get average confidence across all validations."""
        if not self.validation_history:
            return 0.0
        
        total = sum(item["overall_confidence"] for item in self.validation_history)
        return round(total / len(self.validation_history), 4)
    
    def reset_history(self):
        """Reset validation history."""
        self.validation_history = []


# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

_rig = ValidationRig()


def validate_complete(text: str) -> dict:
    """Run complete validation pipeline (module-level function)."""
    return _rig.validate_complete(text)


def validate_covenant_markers(text: str) -> dict:
    """Verify covenant markers (module-level function)."""
    return _rig.validate_covenant_markers(text)


if __name__ == "__main__":
    # Example usage
    rig = ValidationRig()
    
    # Test validation
    test_text = "Truth is the foundation of all being, and love is its expression. Chicka chicka orange."
    
    result = rig.validate_complete(test_text)
    
    print("\nValidation Rig Results:")
    print(f"  Overall Status: {result['overall_status']}")
    print(f"  Overall Confidence: {result['overall_confidence']}")
    print(f"  Axiom Compliant: {result['axiom_check']['compliant']}")
    print(f"  Lambda: {result['lambda_check']['lambda']}")
    print(f"  Classification: {result['discernment_check']['classification']}")
    print(f"  Recommendations: {result['recommendations']}")
