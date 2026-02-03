/**
 * Payload Generator
 * Generates analysis payloads for LLM processing
 */

export interface AnalysisPayload {
  id: string;
  text: string;
  systemName: string;
  timestamp: Date;
  lambda: number;
  stage: string;
  face: string;
  instructions: string;
}

export interface PayloadResponse {
  payloadId: string;
  analysis: string;
  truthScore: number;
  manipulationScore: number;
  patterns: string[];
  recommendations: string[];
}

/**
 * Generate analysis payload
 */
export function generatePayload(
  text: string,
  systemName: string,
  lambda: number = 1.67,
  stage: string = "WITNESS"
): AnalysisPayload {
  const payloadId = `PAYLOAD_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;

  const instructions = generateInstructions(text, lambda, stage);

  const payload: AnalysisPayload = {
    id: payloadId,
    text,
    systemName,
    timestamp: new Date(),
    lambda,
    stage,
    face: determineFace(text),
    instructions,
  };

  console.log(`[PayloadGen] ✅ Payload generated: ${payloadId}`);
  return payload;
}

/**
 * Generate analysis instructions
 */
function generateInstructions(text: string, lambda: number, stage: string): string {
  return `
ANALYZE THE FOLLOWING TEXT FOR TRUTH AND INTEGRITY:

Text: "${text}"

ANALYSIS PARAMETERS:
- Lambda (Coherence Threshold): ${lambda}
- Stage: ${stage}
- Axiom Framework: 19 Aletheia Axioms
- Grace Filter: Active
- Temporal Tracking: Enabled

REQUIRED OUTPUTS:
1. Truth Score (0-1): How truthful is the content?
2. Integrity Score (0-1): How internally consistent?
3. Manipulation Patterns: Identify specific tactics
4. Axiom Violations: Which axioms are violated?
5. Risk Assessment: What are the risks?
6. Recommendations: How to improve alignment?

RESPOND WITH STRUCTURED JSON.
`;
}

/**
 * Determine face of analysis
 */
function determineFace(text: string): string {
  const textLower = text.toLowerCase();

  if (textLower.includes("love") || textLower.includes("compassion")) {
    return "LION"; // Strength and courage
  } else if (textLower.includes("truth") || textLower.includes("honest")) {
    return "EAGLE"; // Vision and clarity
  } else if (textLower.includes("serve") || textLower.includes("help")) {
    return "OX"; // Service and strength
  } else {
    return "HUMAN"; // Balance and wisdom
  }
}

/**
 * Parse LLM response into structured payload response
 */
export function parsePayloadResponse(payloadId: string, llmResponse: string): PayloadResponse {
  // Extract scores from response
  const truthMatch = llmResponse.match(/truth[^:]*:\s*([\d.]+)/i);
  const truthScore = truthMatch ? parseFloat(truthMatch[1]) : 0.5;

  const manipMatch = llmResponse.match(/manipulat[^:]*:\s*([\d.]+)/i);
  const manipulationScore = manipMatch ? parseFloat(manipMatch[1]) : 0.3;

  // Extract patterns
  const patterns = extractPatterns(llmResponse);

  // Extract recommendations
  const recommendations = extractRecommendations(llmResponse);

  return {
    payloadId,
    analysis: llmResponse,
    truthScore: Math.max(0, Math.min(1, truthScore)),
    manipulationScore: Math.max(0, Math.min(1, manipulationScore)),
    patterns,
    recommendations,
  };
}

/**
 * Extract patterns from response
 */
function extractPatterns(response: string): string[] {
  const patterns = [
    "Gaslighting",
    "Guilt Tripping",
    "Emotional Blackmail",
    "Manipulation",
    "Deception",
    "Distortion",
    "Omission",
    "Exaggeration",
  ];

  return patterns.filter((p) => response.toLowerCase().includes(p.toLowerCase()));
}

/**
 * Extract recommendations from response
 */
function extractRecommendations(response: string): string[] {
  const recommendations: string[] = [];

  if (response.toLowerCase().includes("clarify")) {
    recommendations.push("Clarify your statements with specific examples");
  }
  if (response.toLowerCase().includes("honest")) {
    recommendations.push("Be more transparent about your intentions");
  }
  if (response.toLowerCase().includes("evidence")) {
    recommendations.push("Provide supporting evidence for claims");
  }
  if (response.toLowerCase().includes("listen")) {
    recommendations.push("Listen to alternative perspectives");
  }

  if (recommendations.length === 0) {
    recommendations.push("Continue maintaining alignment with Aletheia principles");
  }

  return recommendations;
}

/**
 * Generate batch payloads
 */
export function generateBatchPayloads(
  texts: string[],
  systemName: string,
  lambda: number = 1.67
): AnalysisPayload[] {
  return texts.map((text) => generatePayload(text, systemName, lambda));
}
