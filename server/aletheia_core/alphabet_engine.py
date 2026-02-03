"""
ALPHABET_ENGINE.PY - Symbolic Transformation
==============================================

Four operators transform state:
- GY: Toroidal Angular Momentum (Rotation/Stability)
- RAT: Recursive Activation Triggers (Modulation/Boundary)
- ShRT: Shadow Response Templates (Safety Filter)
- Z-GATE: Resurrection Loop (Hard Reset)

State Vector: [Air, Water, Fire, Earth]
Constants:
- LAMBDA: 1.667 (harmonic resonance)
- Z_THRESHOLD: 0.001 (resurrection trigger)
- SHRT_THRESHOLD: 0.75 (poison/fire clamp)
- GY_THETA: 0.05 radians (rotation angle)
"""

import math
from typing import List, Tuple


class AlphabetEngine:
    """
    Symbolic transformation engine with four operators.
    """
    
    # Constants
    LAMBDA = 1.667  # Harmonic resonance constant
    Z_THRESHOLD = 0.001  # Resurrection trigger (entropy limit)
    SHRT_THRESHOLD = 0.75  # Poison/Fire clamp limit
    GY_THETA = 0.05  # Rotation angle (radians) for stability
    
    # State identifiers
    STATES = ["A", "E", "I", "O", "U"]  # Vowel states
    
    # Vector order: [Air, Water, Fire, Earth]
    VECTOR_LABELS = ["Air", "Water", "Fire", "Earth"]
    
    def __init__(self):
        """Initialize Alphabet Engine."""
        # Initial state: Initiation (A)
        self.current_state = [1.0, 0.0, 0.0, 0.0]
        self.state_history = [self.current_state.copy()]
    
    def apply_gy_rotation(self, vector: List[float]) -> List[float]:
        """
        GY OPERATOR: Toroidal Angular Momentum (Rotation/Stability)
        
        Applies rotation to Air/Earth plane to ensure stability.
        
        Args:
            vector: State vector [Air, Water, Fire, Earth]
            
        Returns:
            Stabilized vector after rotation
        """
        theta = self.GY_THETA
        c, s = math.cos(theta), math.sin(theta)
        
        # Rotation matrix applied to Air (0) and Earth (3) components
        rotated = [
            c * vector[0] - s * vector[3],  # Air
            vector[1],                       # Water (unchanged)
            vector[2],                       # Fire (unchanged)
            s * vector[0] + c * vector[3],  # Earth
        ]
        
        return rotated
    
    def apply_rat_modulation(self, vector: List[float], source_bias: List[float] = None) -> List[float]:
        """
        RAT OPERATOR: Recursive Activation Triggers (Modulation/Boundary)
        
        Uses source A as bias and clips extreme values to prevent explosive growth.
        
        Args:
            vector: State vector [Air, Water, Fire, Earth]
            source_bias: Optional source state to bias toward (default: state A)
            
        Returns:
            Modulated and clipped vector
        """
        if source_bias is None:
            source_bias = [1.0, 0.0, 0.0, 0.0]  # State A
        
        # Apply bias
        modulated = [
            vector[i] * 0.7 + source_bias[i] * 0.3
            for i in range(4)
        ]
        
        # Clip to [-1, 1] to prevent explosive growth
        clipped = [max(-1.0, min(1.0, val)) for val in modulated]
        
        return clipped
    
    def apply_shrt_filter(self, vector: List[float]) -> List[float]:
        """
        ShRT OPERATOR: Shadow Response Templates (Safety Filter)
        
        Clamps Fire component to prevent "poison" and ensures safety.
        
        Args:
            vector: State vector [Air, Water, Fire, Earth]
            
        Returns:
            Filtered vector with safety constraints
        """
        filtered = vector.copy()
        
        # Clamp Fire (index 2) to SHRT_THRESHOLD
        if filtered[2] > self.SHRT_THRESHOLD:
            filtered[2] = self.SHRT_THRESHOLD
        
        # Ensure non-negative Water (index 1)
        filtered[1] = max(0.0, filtered[1])
        
        return filtered
    
    def apply_z_gate_reset(self, vector: List[float]) -> List[float]:
        """
        Z-GATE OPERATOR: Resurrection Loop (Hard Reset)
        
        Resets to initial state if entropy exceeds threshold.
        
        Args:
            vector: State vector [Air, Water, Fire, Earth]
            
        Returns:
            Reset or original vector
        """
        # Calculate entropy (sum of absolute values)
        entropy = sum(abs(v) for v in vector)
        
        # If entropy too low, trigger resurrection
        if entropy < self.Z_THRESHOLD:
            return [1.0, 0.0, 0.0, 0.0]  # Reset to state A
        
        return vector
    
    def transform(self, text: str) -> dict:
        """
        Transform text through all four operators.
        
        Args:
            text: Input text to transform
            
        Returns:
            {
                "input": str,
                "initial_state": list,
                "after_gy": list,
                "after_rat": list,
                "after_shrt": list,
                "after_z_gate": list,
                "final_state": list,
                "semantic_shift": float,
                "stability": float,
            }
        """
        
        # Initialize from text length
        initial_state = self._text_to_vector(text)
        
        # Apply operators in sequence
        after_gy = self.apply_gy_rotation(initial_state)
        after_rat = self.apply_rat_modulation(after_gy)
        after_shrt = self.apply_shrt_filter(after_rat)
        after_z_gate = self.apply_z_gate_reset(after_shrt)
        
        # Calculate metrics
        semantic_shift = self._calculate_shift(initial_state, after_z_gate)
        stability = self._calculate_stability(after_z_gate)
        
        # Update current state
        self.current_state = after_z_gate
        self.state_history.append(self.current_state.copy())
        
        return {
            "input": text,
            "initial_state": [round(v, 4) for v in initial_state],
            "after_gy": [round(v, 4) for v in after_gy],
            "after_rat": [round(v, 4) for v in after_rat],
            "after_shrt": [round(v, 4) for v in after_shrt],
            "after_z_gate": [round(v, 4) for v in after_z_gate],
            "final_state": [round(v, 4) for v in after_z_gate],
            "semantic_shift": round(semantic_shift, 4),
            "stability": round(stability, 4),
        }
    
    def _text_to_vector(self, text: str) -> List[float]:
        """Convert text to initial state vector."""
        # Use text properties to seed vector
        length = len(text)
        vowels = sum(1 for c in text.lower() if c in 'aeiou')
        consonants = sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou')
        spaces = sum(1 for c in text if c == ' ')
        
        # Normalize to 0-1
        total = max(1, length)
        vector = [
            vowels / total,           # Air
            spaces / total,           # Water
            consonants / total,       # Fire
            (length - vowels - consonants - spaces) / total,  # Earth
        ]
        
        return vector
    
    def _calculate_shift(self, initial: List[float], final: List[float]) -> float:
        """Calculate semantic shift between initial and final states."""
        shift = sum(abs(final[i] - initial[i]) for i in range(4))
        return min(1.0, shift)
    
    def _calculate_stability(self, vector: List[float]) -> float:
        """Calculate stability of vector (lower entropy = higher stability)."""
        entropy = sum(abs(v) for v in vector)
        stability = 1.0 / (1.0 + entropy)  # Inverse relationship
        return stability
    
    def get_current_state(self) -> List[float]:
        """Get current state vector."""
        return self.current_state.copy()
    
    def get_state_history(self) -> List[List[float]]:
        """Get history of state transformations."""
        return [state.copy() for state in self.state_history]
    
    def reset(self):
        """Reset engine to initial state."""
        self.current_state = [1.0, 0.0, 0.0, 0.0]
        self.state_history = [self.current_state.copy()]


# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

_engine = AlphabetEngine()


def transform(text: str) -> dict:
    """Transform text through all operators (module-level function)."""
    return _engine.transform(text)


def get_current_state() -> List[float]:
    """Get current state vector."""
    return _engine.get_current_state()


if __name__ == "__main__":
    # Example usage
    engine = AlphabetEngine()
    
    # Test transformation
    result = engine.transform("Truth is the foundation of all being")
    
    print("\nAlphabet Engine Transformation:")
    print(f"  Input: {result['input']}")
    print(f"  Initial State: {result['initial_state']}")
    print(f"  After GY (Rotation): {result['after_gy']}")
    print(f"  After RAT (Modulation): {result['after_rat']}")
    print(f"  After ShRT (Filter): {result['after_shrt']}")
    print(f"  After Z-GATE (Reset): {result['after_z_gate']}")
    print(f"  Semantic Shift: {result['semantic_shift']}")
    print(f"  Stability: {result['stability']}")
