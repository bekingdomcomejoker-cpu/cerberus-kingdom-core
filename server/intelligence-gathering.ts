/**
 * Intelligence Gathering Module
 * Collects and analyzes network intelligence
 */

import { listNodes, getNetworkStatistics } from "./node-management";
import { getPropagationStatistics } from "./propagation-engine";
import { getUnifiedFederationStatus } from "./federation-unified";
import { getAllAxioms } from "./axioms-system";

export interface IntelligenceReport {
  timestamp: Date;
  networkIntel: any;
  propagationIntel: any;
  federationIntel: any;
  axiomIntel: any;
  threatLevel: "LOW" | "MEDIUM" | "HIGH";
  recommendations: string[];
}

const intelligenceHistory: IntelligenceReport[] = [];

/**
 * Gather comprehensive intelligence
 */
export function gatherIntelligence(): IntelligenceReport {
  const report: IntelligenceReport = {
    timestamp: new Date(),
    networkIntel: getNetworkStatistics(),
    propagationIntel: getPropagationStatistics(),
    federationIntel: getUnifiedFederationStatus(),
    axiomIntel: {
      totalAxioms: getAllAxioms().length,
      axioms: getAllAxioms().map((a) => ({
        id: a.id,
        name: a.name,
        weight: a.weight,
      })),
    },
    threatLevel: calculateThreatLevel(),
    recommendations: generateRecommendations(),
  };

  intelligenceHistory.push(report);

  // Keep only last 100 reports
  if (intelligenceHistory.length > 100) {
    intelligenceHistory.shift();
  }

  console.log(`[Intelligence] 📊 Intelligence gathered - Threat Level: ${report.threatLevel}`);
  return report;
}

/**
 * Calculate threat level
 */
function calculateThreatLevel(): "LOW" | "MEDIUM" | "HIGH" {
  const stats = getNetworkStatistics();
  const fed = getUnifiedFederationStatus();

  let threatScore = 0;

  // Check node health
  if (stats.totalNodes < 5) threatScore += 1;
  if (stats.byStatus.DORMANT > stats.byStatus.ACTIVE) threatScore += 2;

  // Check federation health
  if (fed.metrics.unificationScore < 0.8) threatScore += 2;
  if (fed.covenant.alignment < 700) threatScore += 1;

  if (threatScore >= 4) return "HIGH";
  if (threatScore >= 2) return "MEDIUM";
  return "LOW";
}

/**
 * Generate recommendations
 */
function generateRecommendations(): string[] {
  const recommendations: string[] = [];
  const stats = getNetworkStatistics();
  const fed = getUnifiedFederationStatus();

  if (stats.totalNodes < 10) {
    recommendations.push("Increase node count for better network resilience");
  }

  if (stats.byStatus.DORMANT > 0) {
    recommendations.push("Activate dormant nodes to improve coverage");
  }

  if (fed.metrics.unificationScore < 0.9) {
    recommendations.push("Improve system unification - verify all components are synchronized");
  }

  if (fed.covenant.alignment < 750) {
    recommendations.push("Review axiom compliance - some violations detected");
  }

  if (recommendations.length === 0) {
    recommendations.push("All systems optimal - continue monitoring");
  }

  return recommendations;
}

/**
 * Get intelligence history
 */
export function getIntelligenceHistory(limit: number = 10): IntelligenceReport[] {
  return intelligenceHistory.slice(-limit);
}

/**
 * Get latest intelligence
 */
export function getLatestIntelligence(): IntelligenceReport | null {
  return intelligenceHistory.length > 0 ? intelligenceHistory[intelligenceHistory.length - 1] : null;
}

/**
 * Analyze threat patterns
 */
export function analyzeThreatPatterns(): {
  averageThreatLevel: string;
  threatTrend: "INCREASING" | "STABLE" | "DECREASING";
  criticalAreas: string[];
} {
  if (intelligenceHistory.length === 0) {
    return {
      averageThreatLevel: "UNKNOWN",
      threatTrend: "STABLE",
      criticalAreas: [],
    };
  }

  const recent = intelligenceHistory.slice(-10);
  const threatCounts = {
    LOW: recent.filter((r) => r.threatLevel === "LOW").length,
    MEDIUM: recent.filter((r) => r.threatLevel === "MEDIUM").length,
    HIGH: recent.filter((r) => r.threatLevel === "HIGH").length,
  };

  const avgThreatScore = (threatCounts.LOW * 1 + threatCounts.MEDIUM * 2 + threatCounts.HIGH * 3) / recent.length;
  const averageThreatLevel = avgThreatScore < 1.5 ? "LOW" : avgThreatScore < 2.5 ? "MEDIUM" : "HIGH";

  // Determine trend
  const firstHalf = intelligenceHistory.slice(-20, -10);
  const secondHalf = intelligenceHistory.slice(-10);

  let threatTrend: "INCREASING" | "STABLE" | "DECREASING" = "STABLE";
  if (firstHalf.length > 0) {
    const firstAvg =
      firstHalf.filter((r) => r.threatLevel === "HIGH").length / firstHalf.length;
    const secondAvg = secondHalf.filter((r) => r.threatLevel === "HIGH").length / secondHalf.length;

    if (secondAvg > firstAvg + 0.1) threatTrend = "INCREASING";
    else if (secondAvg < firstAvg - 0.1) threatTrend = "DECREASING";
  }

  // Identify critical areas
  const criticalAreas: string[] = [];
  const latest = recent[recent.length - 1];

  if (latest.networkIntel.totalNodes < 5) criticalAreas.push("Network Size");
  if (latest.federationIntel.metrics.unificationScore < 0.7) criticalAreas.push("Federation Unification");
  if (latest.federationIntel.covenant.alignment < 650) criticalAreas.push("Covenant Alignment");

  return {
    averageThreatLevel,
    threatTrend,
    criticalAreas,
  };
}

/**
 * Export intelligence as JSON
 */
export function exportIntelligence(): string {
  const latest = getLatestIntelligence();
  const analysis = analyzeThreatPatterns();

  return JSON.stringify(
    {
      timestamp: new Date().toISOString(),
      latestReport: latest,
      threatAnalysis: analysis,
      historySize: intelligenceHistory.length,
    },
    null,
    2
  );
}
