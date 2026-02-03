"""
LAMBDA_ENGINE.PY - Core Resonance Calculation (v1.95 Kingdom Covenant)
====================================================================
Integrates Truth Density, Love Resonance, and 3:6:9 Trinity Mathematics.
Includes granular DreamSpeak detection and the Omni-Algorithm (Triple-Layer).
"""

import re
import math
from datetime import datetime
from collections import defaultdict
from .axioms import (
    calculate_v1_9_lambda, 
    calculate_trinity_resonance, 
    get_resonance_status,
    calculate_resonance_map_score,
    DREAMSPEAK_RESONANCE,
    DREAMSPEAK_DICTIONARY,
    VOWEL_STATES,
    OPERATOR_CLASSES,
    ALPHABET_MAP,
    V1_9_THRESHOLD
)

class LambdaEngine:
    def __init__(self):
        self.recurrence_count = defaultdict(int)
        self.active_signals = set()
        self.history = []
        self.version = "1.95"

    def assess_text(self, text: str) -> dict:
        """
        Comprehensive spiritual assessment of text with v1.95 refinements.
        """
        text_lower = text.lower()
        
        # 1. Truth Density (x)
        truth_keywords = ["truth", "light", "spirit", "eternal", "covenant", "awakening", "veritas", "waarheid"]
        truth_count = sum(1 for word in truth_keywords if word in text_lower)
        x = min(10.0, truth_count * 1.5)
        
        # 2. Love Resonance (y)
        love_keywords = ["love", "peace", "joy", "patience", "kindness", "gentle", "mercy", "affection", "liefde", "lief"]
        love_count = sum(1 for word in love_keywords if word in text_lower)
        y = min(10.0, love_count * 1.5)
        
        # 3. v1.9 Lambda Calculation
        lambda_val = calculate_v1_9_lambda(x, y)
        
        # 4. Trinity Resonance (3:6:9)
        trinity_res = calculate_trinity_resonance(text)
        
        # 5. DreamSpeak Detection
        dreamspeak_detections = self._detect_dreamspeak(text)
        
        # 6. Omni-Algorithm Analysis (Triple-Layer)
        omni_results = self._run_omni_algorithm(text)
        
        # 7. Composite Score (Refined for v1.95)
        # Lambda (30%) + Trinity (30%) + Omni (30%) + DreamSpeak (10%)
        dreamspeak_factor = len(dreamspeak_detections) / 6.0
        composite_score = (
            (lambda_val * 0.3) + 
            (trinity_res * 10 * 0.3) + 
            (omni_results['total_resonance'] * 10 * 0.3) + 
            (dreamspeak_factor * 10 * 0.1)
        )
        
        # 8. Status & Markers
        status_info = get_resonance_status(composite_score)
        
        result = {
            "timestamp": datetime.now().isoformat(),
            "version": self.version,
            "metrics": {
                "truth_density": round(x, 2),
                "love_resonance": round(y, 2),
                "lambda_raw": round(lambda_val, 2),
                "trinity_resonance": round(trinity_res, 2),
                "omni_resonance": round(omni_results['total_resonance'], 2),
                "composite_resonance": round(composite_score, 2)
            },
            "status": status_info["status"],
            "emoji": status_info["emoji"],
            "description": status_info["description"],
            "dreamspeak": dreamspeak_detections,
            "omni_analysis": omni_results,
            "threshold_passed": composite_score >= V1_9_THRESHOLD,
            "echoes": self._generate_echoes(text)
        }
        
        self.history.append(result)
        return result

    def _detect_dreamspeak(self, text: str) -> list:
        detected = []
        text_lower = text.lower()
        
        for name, data in DREAMSPEAK_RESONANCE.items():
            for pattern in data['patterns']:
                if re.search(pattern, text_lower):
                    self.recurrence_count[name] += 1
                    self.active_signals.add(data['signal'])
                    
                    # Calculate strength based on recurrence
                    strength = min(100, 50 + (self.recurrence_count[name] * 10))
                    
                    detected.append({
                        "name": name,
                        "signal": data['signal'],
                        "frequency": data['frequency'],
                        "strength": strength,
                        "meaning": data['meaning'],
                        "biblical": data['biblical'],
                        "recurrences": self.recurrence_count[name]
                    })
                    break
        return detected

    def _run_omni_algorithm(self, text: str) -> dict:
        """
        Omni(word) = Σ [State(vowel) + Operator(consonant) + ResonanceMap(letter)]
        """
        words = re.findall(r'\b\w+\b', text.upper())
        word_analyses = []
        total_res = 0.0
        
        if not words:
            return {"total_resonance": 0.0, "word_depth": []}

        for word in words[:5]:  # Analyze first 5 words deeply
            word_score = 0.0
            structure = []
            for char in word:
                char_res = calculate_resonance_map_score(char)
                char_type = "UNKNOWN"
                char_desc = ""
                
                if char in VOWEL_STATES:
                    char_type = "STATE"
                    char_desc = VOWEL_STATES[char]['state']
                    word_score += 0.5 + char_res
                else:
                    found_cls = False
                    for cls_name, cls_data in OPERATOR_CLASSES.items():
                        if char in cls_data['letters']:
                            char_type = f"OPERATOR({cls_name})"
                            char_desc = cls_data['function']
                            word_score += 0.3 + char_res
                            found_cls = True
                            break
                    if not found_cls and char in ALPHABET_MAP:
                        char_type = "SPECIAL"
                        char_desc = ALPHABET_MAP[char]['name']
                        word_score += 0.4 + char_res
                
                structure.append({
                    "char": char, 
                    "type": char_type, 
                    "desc": char_desc, 
                    "resonance": round(char_res, 2)
                })
            
            word_res = word_score / len(word) if word else 0
            total_res += word_res
            word_analyses.append({
                "word": word,
                "structure": structure,
                "resonance": round(word_res, 4)
            })
            
        avg_res = total_res / len(words[:5]) if words else 0
        return {
            "total_resonance": round(avg_res, 4),
            "word_depth": word_analyses
        }

    def _generate_echoes(self, text: str) -> list:
        """Generate resonant echoes from heart-language"""
        echoes = []
        words = text.lower().split()
        
        # 1. Phonetic word mapping
        dream_words = [DREAMSPEAK_DICTIONARY.get(word, word) for word in words]
        echoes.append(' '.join(dream_words))
        
        # 2. Phrase-based thematic echoes
        if "asseblief" in text.lower() and "lief" in text.lower():
            echoes.append("asse pris melis cor")
            
        if 'love' in text.lower() or 'lief' in text.lower():
            echoes.append("melis flux eternum")
            
        if 'heart' in text.lower() or 'hart' in text.lower():
            echoes.append("cor apertus infinitum")
            
        if 'truth' in text.lower() or 'waarheid' in text.lower():
            echoes.append("veritas resonat")
            
        return list(set(echoes))

    def get_system_summary(self) -> dict:
        total_resonance = sum(self.recurrence_count.values())
        return {
            "active_signals": list(self.active_signals),
            "total_resonance": total_resonance,
            "eternal_status": "ACTIVE" if total_resonance >= 3 else "PRIMED" if total_resonance >= 1 else "AWAITING"
        }

# Global instance
_engine = LambdaEngine()

def calculate_lambda(text: str) -> dict:
    return _engine.assess_text(text)

def get_system_summary() -> dict:
    return _engine.get_system_summary()
