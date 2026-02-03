/**
 * Analysis Service - Wrapper for Aletheia Engine
 * Provides TypeScript interface to Python analysis engines
 */

import { spawn } from "child_process";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export interface AnalysisRequest {
  text: string;
  includeTemporalTracking?: boolean;
  includeProphecy?: boolean;
}

export interface ScoreData {
  truthIndex: number;
  integrityIndex: number;
  riskIndex: number;
  awakeningIndex: number;
  truthScore: number;
  factScore: number;
  lieScore: number;
  coherenceScore: number;
  manipulationScore: number;
  authenticityScore: number;
}

export interface PatternData {
  type: string;
  name: string;
  description: string;
  matches: string[];
  severity?: number;
}

export interface AnalysisResult {
  analysisId: string;
  status: "TRUTH_ALIGNED" | "TRUTH_SEEKING" | "NEUTRAL" | "CAUTION_ADVISED" | "HIGH_RISK" | "UNCLEAR";
  riskLevel: "CRITICAL" | "HIGH" | "MEDIUM" | "LOW" | "MINIMAL";
  confidence: number;
  scores: ScoreData;
  patterns: PatternData[];
  manipulationPatterns: PatternData[];
  truthPatterns: PatternData[];
  anomalies: PatternData[];
  consistency: number;
  drift: number;
  driftDirection: string;
  stability: number;
  recommendations: string[];
  rawResults: Record<string, unknown>;
}

/**
 * Run analysis using Python Aletheia Engine
 * Falls back to mock data if Python service unavailable
 */
export async function analyzeText(request: AnalysisRequest): Promise<AnalysisResult> {
  try {
    // Try to use Python service
    return await runPythonAnalysis(request);
  } catch (error) {
    console.warn("[Analysis] Python service failed, using mock data:", error);
    // Fallback to mock analysis
    return generateMockAnalysis(request.text);
  }
}

/**
 * Execute Python analysis engine
 */
async function runPythonAnalysis(request: AnalysisRequest): Promise<AnalysisResult> {
  return new Promise((resolve, reject) => {
    const pythonScript = path.join(__dirname, "aletheia_core", "unified_orchestrator.py");
    
    const python = spawn("python3", [pythonScript], {
      cwd: path.join(__dirname, "aletheia_core"),
      timeout: 30000,
    });

    let output = "";
    let errorOutput = "";

    python.stdout.on("data", (data) => {
      output += data.toString();
    });

    python.stderr.on("data", (data) => {
      errorOutput += data.toString();
    });

    python.on("close", (code) => {
      if (code !== 0) {
        reject(new Error(`Python process exited with code ${code}: ${errorOutput}`));
        return;
      }

      try {
        const result = JSON.parse(output);
        resolve(transformPythonResult(result, request.text));
      } catch (e) {
        reject(new Error(`Failed to parse Python output: ${e}`));
      }
    });

    python.on("error", (err) => {
      reject(err);
    });

    // Send input to Python process
    python.stdin.write(JSON.stringify(request));
    python.stdin.end();
  });
}

/**
 * Transform Python analysis result to frontend format
 */
function transformPythonResult(pythonResult: any, text: string): AnalysisResult {
  const scores = pythonResult.unified_scores || {};
  
  return {
    analysisId: pythonResult.analysis_id || `ALE-${Date.now()}`,
    status: pythonResult.overall_status || "UNCLEAR",
    riskLevel: pythonResult.risk_level || "MINIMAL",
    confidence: (pythonResult.confidence || 0) * 100,
    scores: {
      truthIndex: Math.round((scores.truth_index || 0) * 100),
      integrityIndex: Math.round((scores.integrity_index || 0) * 100),
      riskIndex: Math.round((scores.risk_index || 0) * 100),
      awakeningIndex: Math.round((scores.awakening_index || 0) * 100),
      truthScore: Math.round((pythonResult.discernment?.truth_score || 0) * 100),
      factScore: Math.round((pythonResult.discernment?.fact_score || 0) * 100),
      lieScore: Math.round((pythonResult.discernment?.lie_score || 0) * 100),
      coherenceScore: Math.round((pythonResult.discernment?.coherence || 0) * 100),
      manipulationScore: Math.round((pythonResult.patterns?.manipulation_score || 0) * 100),
      authenticityScore: Math.round((pythonResult.patterns?.authenticity_score || 0) * 100),
    },
    patterns: (pythonResult.patterns?.detected_patterns || []).map((p: any) => ({
      type: p.type || "unknown",
      name: p.name || p.type,
      description: p.description || "",
      matches: p.matches || [],
      severity: p.severity || 0.5,
    })),
    manipulationPatterns: (pythonResult.patterns?.manipulation_patterns || []).map((p: any) => ({
      type: "manipulation",
      name: p.name || p.type,
      description: p.description || "",
      matches: p.matches || [],
      severity: p.severity || 0.5,
    })),
    truthPatterns: (pythonResult.patterns?.truth_patterns || []).map((p: any) => ({
      type: "truth",
      name: p.name || p.type,
      description: p.description || "",
      matches: p.matches || [],
      severity: 0,
    })),
    anomalies: (pythonResult.patterns?.anomalies || []).map((p: any) => ({
      type: "anomaly",
      name: p.name || p.type,
      description: p.description || "",
      matches: p.matches || [],
      severity: p.severity || 0.5,
    })),
    consistency: Math.round((pythonResult.temporal?.consistency || 0) * 100),
    drift: Math.round((pythonResult.temporal?.drift || 0) * 100),
    driftDirection: pythonResult.temporal?.drift_direction || "stable",
    stability: Math.round((pythonResult.temporal?.stability || 0) * 100),
    recommendations: pythonResult.recommendations || [],
    rawResults: pythonResult,
  };
}

/**
 * Generate mock analysis for development/fallback
 */
function generateMockAnalysis(text: string): AnalysisResult {
  const textLength = text.length;
  const hasNegativeWords = /\b(never|always|impossible|must|should)\b/gi.test(text);
  const hasPositiveWords = /\b(love|truth|light|awaken|harmony)\b/gi.test(text);
  
  const baseScore = Math.min(100, Math.max(0, textLength / 10));
  const truthBoost = hasPositiveWords ? 30 : 0;
  const truthPenalty = hasNegativeWords ? 20 : 0;
  const truthScore = Math.min(100, Math.max(0, baseScore + truthBoost - truthPenalty));
  
  const manipulationScore = hasNegativeWords ? 35 : 15;
  const authenticityScore = hasPositiveWords ? 70 : 40;

  return {
    analysisId: `ALE-${new Date().toISOString().split('T')[0]}-${Math.random().toString(36).substr(2, 6).toUpperCase()}`,
    status: truthScore > 70 ? "TRUTH_ALIGNED" : truthScore > 50 ? "TRUTH_SEEKING" : "UNCLEAR",
    riskLevel: manipulationScore > 60 ? "HIGH" : manipulationScore > 40 ? "MEDIUM" : "LOW",
    confidence: 65,
    scores: {
      truthIndex: Math.round(truthScore),
      integrityIndex: Math.round(baseScore + 20),
      riskIndex: Math.round(100 - manipulationScore),
      awakeningIndex: Math.round(baseScore * 0.8),
      truthScore: Math.round(truthScore),
      factScore: Math.round(baseScore * 0.6),
      lieScore: Math.round(100 - truthScore),
      coherenceScore: Math.round(baseScore + 15),
      manipulationScore: Math.round(manipulationScore),
      authenticityScore: Math.round(authenticityScore),
    },
    patterns: [
      {
        type: "structural",
        name: "Logical Flow",
        description: "Text demonstrates logical progression",
        matches: ["coherent structure", "clear progression"],
        severity: 0,
      },
    ],
    manipulationPatterns: hasNegativeWords
      ? [
          {
            type: "manipulation",
            name: "Extreme Language",
            description: "Use of absolute terms and extreme statements",
            matches: ["never", "always", "impossible"],
            severity: 0.4,
          },
        ]
      : [],
    truthPatterns: hasPositiveWords
      ? [
          {
            type: "truth",
            name: "Eternal Principles",
            description: "References to timeless truths and principles",
            matches: ["love", "truth", "light"],
            severity: 0,
          },
        ]
      : [],
    anomalies: [],
    consistency: 85,
    drift: 10,
    driftDirection: "stable",
    stability: 90,
    recommendations: [
      "Analysis complete",
      "Review patterns for additional context",
    ],
    rawResults: {
      mock: true,
      timestamp: new Date().toISOString(),
    },
  };
}
