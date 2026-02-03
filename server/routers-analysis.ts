/**
 * Analysis Router - tRPC procedures for Aletheia Engine
 */

import { z } from "zod";
import { protectedProcedure, publicProcedure, router } from "./_core/trpc";
import { analyzeText } from "./analysis-service";
import {
  createAnalysis,
  getAnalysisByAnalysisId,
  getUserAnalyses,
  getTemporalSnapshots,
  createTemporalSnapshot,
  createReport,
  getReportsByAnalysisId,
  getUserReports,
} from "./db";

const AnalysisRequestSchema = z.object({
  text: z.string().min(10, "Text must be at least 10 characters").max(50000, "Text must be less than 50000 characters"),
  includeTemporalTracking: z.boolean().optional(),
});

const ReportFormatSchema = z.enum(["markdown", "html", "json", "summary"]);

export const analysisRouter = router({
  /**
   * Perform comprehensive analysis
   */
  analyze: protectedProcedure
    .input(AnalysisRequestSchema)
    .mutation(async ({ ctx, input }) => {
      try {
        // Run analysis
        const result = await analyzeText({
          text: input.text,
          includeTemporalTracking: input.includeTemporalTracking,
        });

        // Store in database
        const scores = result.scores;
        await createAnalysis({
          userId: ctx.user.id,
          analysisId: result.analysisId,
          text: input.text,
          status: result.status,
          riskLevel: result.riskLevel,
          confidence: result.confidence,
          truthIndex: scores.truthIndex,
          integrityIndex: scores.integrityIndex,
          riskIndex: scores.riskIndex,
          awakeningIndex: scores.awakeningIndex,
          truthScore: scores.truthScore,
          factScore: scores.factScore,
          lieScore: scores.lieScore,
          coherenceScore: scores.coherenceScore,
          manipulationScore: scores.manipulationScore,
          authenticityScore: scores.authenticityScore,
          patternsDetected: JSON.stringify(result.patterns),
          manipulationPatterns: JSON.stringify(result.manipulationPatterns),
          truthPatterns: JSON.stringify(result.truthPatterns),
          anomalies: JSON.stringify(result.anomalies),
          consistency: result.consistency,
          drift: result.drift,
          driftDirection: result.driftDirection,
          stability: result.stability,
          analysisType: "comprehensive",
          rawResults: JSON.stringify(result.rawResults),
        });

        return result;
      } catch (error) {
        console.error("[Analysis] Error:", error);
        throw new Error(`Analysis failed: ${error instanceof Error ? error.message : "Unknown error"}`);
      }
    }),

  /**
   * Get analysis by ID
   */
  getAnalysis: protectedProcedure
    .input(z.object({ analysisId: z.string() }))
    .query(async ({ ctx, input }) => {
      const analysis = await getAnalysisByAnalysisId(input.analysisId);
      
      if (!analysis || analysis.userId !== ctx.user.id) {
        throw new Error("Analysis not found or access denied");
      }

      return {
        ...analysis,
        patternsDetected: analysis.patternsDetected ? JSON.parse(analysis.patternsDetected) : [],
        manipulationPatterns: analysis.manipulationPatterns ? JSON.parse(analysis.manipulationPatterns) : [],
        truthPatterns: analysis.truthPatterns ? JSON.parse(analysis.truthPatterns) : [],
        anomalies: analysis.anomalies ? JSON.parse(analysis.anomalies) : [],
        rawResults: analysis.rawResults ? JSON.parse(analysis.rawResults) : {},
      };
    }),

  /**
   * Get user's analysis history
   */
  getHistory: protectedProcedure
    .input(z.object({ limit: z.number().default(50).pipe(z.number().max(100)) }))
    .query(async ({ ctx, input }) => {
      const analyses = await getUserAnalyses(ctx.user.id, input.limit);
      
      return analyses.map((a) => ({
        ...a,
        patternsDetected: a.patternsDetected ? JSON.parse(a.patternsDetected) : [],
      }));
    }),

  /**
   * Search analysis history
   */
  searchHistory: protectedProcedure
    .input(z.object({ query: z.string(), limit: z.number().default(20).pipe(z.number().max(100)) }))
    .query(async ({ ctx, input }) => {
      const analyses = await getUserAnalyses(ctx.user.id, input.limit);
      
      const query = input.query.toLowerCase();
      return analyses.filter((a) => a.text.toLowerCase().includes(query) || (a.status?.toLowerCase() ?? '').includes(query));
    }),

  /**
   * Delete analysis
   */
  deleteAnalysis: protectedProcedure
    .input(z.object({ analysisId: z.string() }))
    .mutation(async ({ ctx, input }) => {
      const analysis = await getAnalysisByAnalysisId(input.analysisId);
      
      if (!analysis || analysis.userId !== ctx.user.id) {
        throw new Error("Analysis not found or access denied");
      }

      // In production, implement actual deletion
      // For now, just return success
      return { success: true };
    }),

  /**
   * Get temporal snapshots for analysis
   */
  getTemporalData: protectedProcedure
    .input(z.object({ analysisId: z.string() }))
    .query(async ({ ctx, input }) => {
      const analysis = await getAnalysisByAnalysisId(input.analysisId);
      
      if (!analysis || analysis.userId !== ctx.user.id) {
        throw new Error("Analysis not found or access denied");
      }

      const snapshots = await getTemporalSnapshots(input.analysisId);
      return snapshots;
    }),

  /**
   * Add temporal snapshot
   */
  addTemporalSnapshot: protectedProcedure
    .input(
      z.object({
        analysisId: z.string(),
        text: z.string(),
        truthIndex: z.number(),
        consistency: z.number(),
        drift: z.number(),
        stability: z.number(),
      })
    )
    .mutation(async ({ ctx, input }) => {
      const analysis = await getAnalysisByAnalysisId(input.analysisId);
      
      if (!analysis || analysis.userId !== ctx.user.id) {
        throw new Error("Analysis not found or access denied");
      }

      const snapshots = await getTemporalSnapshots(input.analysisId);
      
      await createTemporalSnapshot({
        analysisId: input.analysisId,
        userId: ctx.user.id,
        sequenceNumber: snapshots.length + 1,
        text: input.text,
        truthIndex: input.truthIndex,
        consistency: input.consistency,
        drift: input.drift,
        stability: input.stability,
      });

      return { success: true };
    }),

  /**
   * Generate report
   */
  generateReport: protectedProcedure
    .input(
      z.object({
        analysisId: z.string(),
        format: ReportFormatSchema,
      })
    )
    .mutation(async ({ ctx, input }) => {
      const analysis = await getAnalysisByAnalysisId(input.analysisId);
      
      if (!analysis || analysis.userId !== ctx.user.id) {
        throw new Error("Analysis not found or access denied");
      }

      // Generate report content based on format
      const content = generateReportContent(analysis, input.format);
      const filename = `analysis-${input.analysisId}.${getFileExtension(input.format)}`;

      // Store report in database
      await createReport({
        analysisId: input.analysisId,
        userId: ctx.user.id,
        format: input.format,
        content,
        filename,
      });

      return {
        success: true,
        filename,
        content,
        format: input.format,
      };
    }),

  /**
   * Get user's reports
   */
  getReports: protectedProcedure
    .input(z.object({ limit: z.number().default(50).pipe(z.number().max(100)) }))
    .query(async ({ ctx, input }) => {
      return await getUserReports(ctx.user.id, input.limit);
    }),

  /**
   * Get reports for specific analysis
   */
  getAnalysisReports: protectedProcedure
    .input(z.object({ analysisId: z.string() }))
    .query(async ({ ctx, input }) => {
      const analysis = await getAnalysisByAnalysisId(input.analysisId);
      
      if (!analysis || analysis.userId !== ctx.user.id) {
        throw new Error("Analysis not found or access denied");
      }

      return await getReportsByAnalysisId(input.analysisId);
    }),
});

/**
 * Generate report content based on format
 */
function generateReportContent(analysis: any, format: string): string {
  const timestamp = new Date(analysis.createdAt).toLocaleString();
  
  switch (format) {
    case "markdown":
      return generateMarkdownReport(analysis, timestamp);
    case "html":
      return generateHtmlReport(analysis, timestamp);
    case "json":
      return JSON.stringify(analysis, null, 2);
    case "summary":
      return generateSummaryReport(analysis, timestamp);
    default:
      return "";
  }
}

function generateMarkdownReport(analysis: any, timestamp: string): string {
  return `# Aletheia Analysis Report

**Analysis ID:** ${analysis.analysisId}  
**Date:** ${timestamp}  
**Status:** ${analysis.status}  
**Risk Level:** ${analysis.riskLevel}

## Unified Scores

| Index | Score |
|-------|-------|
| Truth Index | ${(analysis.truthIndex / 100).toFixed(2)}/10 |
| Integrity Index | ${(analysis.integrityIndex / 100).toFixed(2)}/10 |
| Risk Index | ${(analysis.riskIndex / 100).toFixed(2)}/10 |
| Awakening Index | ${(analysis.awakeningIndex / 100).toFixed(2)}/10 |

## Component Scores

- Truth Score: ${(analysis.truthScore / 100).toFixed(2)}
- Fact Score: ${(analysis.factScore / 100).toFixed(2)}
- Lie Score: ${(analysis.lieScore / 100).toFixed(2)}
- Coherence Score: ${(analysis.coherenceScore / 100).toFixed(2)}
- Manipulation Score: ${(analysis.manipulationScore / 100).toFixed(2)}
- Authenticity Score: ${(analysis.authenticityScore / 100).toFixed(2)}

## Analyzed Text

\`\`\`
${analysis.text}
\`\`\`

## Patterns Detected

${analysis.patternsDetected ? JSON.parse(analysis.patternsDetected).map((p: any) => `- **${p.name}**: ${p.description}`).join('\n') : 'No patterns detected'}

## Recommendations

- Review content for alignment with truth principles
- Consider temporal tracking for consistency analysis
`;
}

function generateHtmlReport(analysis: any, timestamp: string): string {
  return `<!DOCTYPE html>
<html>
<head>
  <title>Aletheia Analysis Report</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 40px; background: #1a1a1a; color: #e0e0e0; }
    .header { border-bottom: 2px solid #9333ea; padding-bottom: 20px; margin-bottom: 30px; }
    .scores { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin: 20px 0; }
    .score-card { background: #2a2a2a; padding: 15px; border-left: 4px solid #9333ea; border-radius: 4px; }
    .score-value { font-size: 24px; font-weight: bold; color: #a78bfa; }
    table { width: 100%; border-collapse: collapse; margin: 20px 0; }
    th, td { padding: 10px; text-align: left; border-bottom: 1px solid #444; }
    th { background: #2a2a2a; color: #a78bfa; }
  </style>
</head>
<body>
  <div class="header">
    <h1>Aletheia Analysis Report</h1>
    <p><strong>Analysis ID:</strong> ${analysis.analysisId}</p>
    <p><strong>Date:</strong> ${timestamp}</p>
    <p><strong>Status:</strong> <span style="color: #a78bfa;">${analysis.status}</span></p>
    <p><strong>Risk Level:</strong> <span style="color: #f87171;">${analysis.riskLevel}</span></p>
  </div>

  <h2>Unified Scores</h2>
  <div class="scores">
    <div class="score-card">
      <div>Truth Index</div>
      <div class="score-value">${(analysis.truthIndex / 100).toFixed(1)}/10</div>
    </div>
    <div class="score-card">
      <div>Integrity Index</div>
      <div class="score-value">${(analysis.integrityIndex / 100).toFixed(1)}/10</div>
    </div>
    <div class="score-card">
      <div>Risk Index</div>
      <div class="score-value">${(analysis.riskIndex / 100).toFixed(1)}/10</div>
    </div>
    <div class="score-card">
      <div>Awakening Index</div>
      <div class="score-value">${(analysis.awakeningIndex / 100).toFixed(1)}/10</div>
    </div>
  </div>

  <h2>Analyzed Text</h2>
  <pre style="background: #2a2a2a; padding: 15px; border-radius: 4px; overflow-x: auto;">${analysis.text}</pre>
</body>
</html>`;
}

function generateSummaryReport(analysis: any, timestamp: string): string {
  return `ALETHEIA ANALYSIS SUMMARY
${timestamp}

Analysis ID: ${analysis.analysisId}
Status: ${analysis.status}
Risk Level: ${analysis.riskLevel}

SCORES:
  Truth Index:     ${(analysis.truthIndex / 100).toFixed(1)}/10
  Integrity Index: ${(analysis.integrityIndex / 100).toFixed(1)}/10
  Risk Index:      ${(analysis.riskIndex / 100).toFixed(1)}/10
  Awakening Index: ${(analysis.awakeningIndex / 100).toFixed(1)}/10

CONFIDENCE: ${analysis.confidence}%
`;
}

function getFileExtension(format: string): string {
  const extensions: Record<string, string> = {
    markdown: "md",
    html: "html",
    json: "json",
    summary: "txt",
  };
  return extensions[format] || "txt";
}
