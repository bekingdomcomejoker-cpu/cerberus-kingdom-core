"""
MAIN.PY - Aletheia Engine FastAPI Server
=========================================

HTTP API wrapper for the Aletheia Engine validation pipeline.
Exposes core analysis functions as REST endpoints.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import sys
import os

# Add parent directory to path so we can import core modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import core modules
from validation_rig import validate_complete
from lambda_engine import calculate_lambda
from discernment import DiscernmentEngine
from human_meter import filter_output

# ============================================================================
# FASTAPI APP SETUP
# ============================================================================

app = FastAPI(
    title="Aletheia Engine API",
    description="Semantic analysis and truth discernment framework",
    version="1.0.0",
)

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request size guard (structural integrity, not censorship)
@app.middleware("http")
async def size_guard(request, call_next):
    """Prevent oversized requests from consuming resources."""
    body = await request.body()
    if len(body) > 50_000:  # 50KB limit
        raise HTTPException(status_code=413, detail="Input too large")
    return await call_next(request)

# ============================================================================
# REQUEST/RESPONSE MODELS
# ============================================================================

class AnalysisRequest(BaseModel):
    """Request model for content analysis"""
    text: str
    description: Optional[str] = None


class AnalysisResponse(BaseModel):
    """Response model for analysis results"""
    status: str
    description: Optional[str]
    lambda_value: float
    stage: str
    classification: str
    confidence: float
    distortion_detected: bool
    axiom_compliant: bool
    recommendation: str


class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    version: str
    authority: str


# ============================================================================
# ROUTES
# ============================================================================

@app.get("/", response_model=HealthResponse)
async def root():
    """Health check endpoint"""
    return {
        "status": "alive",
        "version": "1.0.0",
        "authority": "Canonical Spine",
    }


@app.get("/health", response_model=HealthResponse)
async def health():
    """Health check endpoint"""
    return {
        "status": "alive",
        "version": "1.0.0",
        "authority": "Canonical Spine",
    }


@app.post("/analyze", response_model=AnalysisResponse)
async def analyze(request: AnalysisRequest):
    """
    Perform complete analysis on input text.
    
    Runs the full validation pipeline:
    1. Axiom compliance check
    2. Lambda calculation
    3. Discernment analysis
    4. Alphabet transformation
    5. Human meter filtering
    
    Args:
        text: Input text to analyze
        description: Optional description of the text
        
    Returns:
        Complete analysis results with status, lambda, classification, etc.
    """
    try:
        if not request.text or len(request.text.strip()) == 0:
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        # Run full validation pipeline
        result = validate_complete(request.text)
        
        # Extract key fields
        return {
            "status": result.get("overall_status", "UNKNOWN"),
            "description": request.description or request.text[:100],
            "lambda_value": result.get("lambda_check", {}).get("lambda", 0.0),
            "stage": result.get("lambda_check", {}).get("stage", "UNKNOWN"),
            "classification": result.get("discernment_check", {}).get("classification", "UNKNOWN"),
            "confidence": result.get("overall_confidence", 0.0),
            "distortion_detected": result.get("discernment_check", {}).get("distortion_detected", False),
            "axiom_compliant": result.get("axiom_check", {}).get("compliant", False),
            "recommendation": result.get("human_meter_check", {}).get("recommendation", ""),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@app.post("/validate")
async def validate(request: AnalysisRequest):
    """
    Run validation pipeline and return raw results.
    
    Returns the complete validation object with all sub-checks.
    """
    try:
        if not request.text or len(request.text.strip()) == 0:
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        result = validate_complete(request.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Validation failed: {str(e)}")


@app.post("/lambda")
async def lambda_check(request: AnalysisRequest):
    """
    Calculate Lambda (resonance) for input text.
    
    Returns:
        - lambda: Resonance score (0.0 - 2.0+)
        - stage: Awakening stage (DORMANT, RESISTANCE, VERIFICATION, RECOGNITION, AWAKENED)
        - is_awakened: Boolean indicating if lambda >= 1.0
        - is_prophetic: Boolean indicating if lambda >= 1.7333
    """
    try:
        if not request.text or len(request.text.strip()) == 0:
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        result = calculate_lambda(request.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lambda calculation failed: {str(e)}")


@app.post("/discern")
async def discern(request: AnalysisRequest):
    """
    Perform dual-phase discernment (fact vs truth vs distortion).
    
    Returns:
        - classification: TRUTH, FACT, MIXED, or DISTORTION
        - confidence: Confidence score (0.0 - 1.0)
        - truth_ratio: Percentage of truth markers
        - distortion_detected: Boolean
        - coherence_score: Internal consistency metric
    """
    try:
        if not request.text or len(request.text.strip()) == 0:
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        engine = DiscernmentEngine()
        result = engine.analyze(request.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Discernment failed: {str(e)}")


@app.post("/filter")
async def filter_text(request: AnalysisRequest):
    """
    Apply human meter filtering (Axiom 10: Perfect Love casts out fear).
    
    Analyzes distortion and applies transformations to fear-based language.
    
    Returns:
        - filtered_output: Transformed text with fear replaced by love
        - distortion_level: Measured distortion (0.0 - 1.0)
        - axiom_10_applied: Boolean indicating if transformation was applied
        - recommendation: Human-readable recommendation
    """
    try:
        if not request.text or len(request.text.strip()) == 0:
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        # Default lambda for filtering
        result = filter_output(request.text, alpha_resonance=1.5)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Filtering failed: {str(e)}")


# ============================================================================
# STARTUP/SHUTDOWN
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """Log startup"""
    print("🔥 Aletheia Engine API started")
    print("📍 Authority: Canonical Spine")
    print("✅ Status: BINDING / FULL AHEAD")
    print("🍊 Chicka chicka orange.")


@app.on_event("shutdown")
async def shutdown_event():
    """Log shutdown"""
    print("🛑 Aletheia Engine API shutting down")


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    # Run on 0.0.0.0 to be accessible from outside (Render requirement)
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
    )
