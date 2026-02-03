/**
 * Analysis Results Component
 * Displays comprehensive analysis results with all scores and visualizations
 */

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { ScoreCard } from "./ScoreCard";
import { PatternVisualization } from "./PatternVisualization";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, LineChart, Line } from "recharts";
import { Download, Share2 } from "lucide-react";

interface AnalysisResult {
  analysisId: string;
  status: string;
  riskLevel: string;
  confidence: number;
  scores: {
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
  };
  patterns: any[];
  manipulationPatterns: any[];
  truthPatterns: any[];
  anomalies: any[];
  consistency: number;
  drift: number;
  driftDirection: string;
  stability: number;
  recommendations: string[];
}

interface AnalysisResultsProps {
  result: AnalysisResult;
  isLoading?: boolean;
  onExport?: (format: "markdown" | "html" | "json") => void;
  className?: string;
}

export function AnalysisResults({ result, isLoading, onExport, className }: AnalysisResultsProps) {
  const getStatusColor = (status: string) => {
    switch (status) {
      case "TRUTH_ALIGNED":
        return "bg-green-500/20 text-green-400 border-green-500/50";
      case "TRUTH_SEEKING":
        return "bg-blue-500/20 text-blue-400 border-blue-500/50";
      case "NEUTRAL":
        return "bg-gray-500/20 text-gray-400 border-gray-500/50";
      case "CAUTION_ADVISED":
        return "bg-yellow-500/20 text-yellow-400 border-yellow-500/50";
      case "HIGH_RISK":
        return "bg-red-500/20 text-red-400 border-red-500/50";
      default:
        return "bg-purple-500/20 text-purple-400 border-purple-500/50";
    }
  };

  const getRiskColor = (risk: string) => {
    switch (risk) {
      case "CRITICAL":
        return "bg-red-500/20 text-red-400";
      case "HIGH":
        return "bg-orange-500/20 text-orange-400";
      case "MEDIUM":
        return "bg-yellow-500/20 text-yellow-400";
      case "LOW":
        return "bg-blue-500/20 text-blue-400";
      default:
        return "bg-green-500/20 text-green-400";
    }
  };

  // Prepare chart data
  const componentScoresData = [
    { name: "Truth", value: result.scores.truthScore / 100 },
    { name: "Fact", value: result.scores.factScore / 100 },
    { name: "Lie", value: result.scores.lieScore / 100 },
    { name: "Coherence", value: result.scores.coherenceScore / 100 },
    { name: "Manipulation", value: result.scores.manipulationScore / 100 },
    { name: "Authenticity", value: result.scores.authenticityScore / 100 },
  ];

  const temporalData = [
    { name: "Consistency", value: result.consistency / 100 },
    { name: "Stability", value: result.stability / 100 },
    { name: "Drift", value: 100 - result.drift / 100 },
  ];

  return (
    <div className={`space-y-6 ${className}`}>
      {/* Header with Status */}
      <div className="space-y-4">
        <div className="flex items-start justify-between">
          <div>
            <h2 className="text-2xl font-bold text-foreground">Analysis Results</h2>
            <p className="text-sm text-muted-foreground mt-1">ID: {result.analysisId}</p>
          </div>
          <div className="flex gap-2">
            {onExport && (
              <>
                <Button size="sm" variant="outline" onClick={() => onExport("markdown")}>
                  <Download className="h-4 w-4 mr-2" />
                  Markdown
                </Button>
                <Button size="sm" variant="outline" onClick={() => onExport("html")}>
                  <Download className="h-4 w-4 mr-2" />
                  HTML
                </Button>
                <Button size="sm" variant="outline" onClick={() => onExport("json")}>
                  <Download className="h-4 w-4 mr-2" />
                  JSON
                </Button>
              </>
            )}
          </div>
        </div>

        {/* Status Badges */}
        <div className="flex gap-3 flex-wrap">
          <Badge className={`border ${getStatusColor(result.status)}`}>{result.status}</Badge>
          <Badge className={`border ${getRiskColor(result.riskLevel)}`}>Risk: {result.riskLevel}</Badge>
          <Badge variant="outline">Confidence: {result.confidence}%</Badge>
        </div>
      </div>

      {/* Unified Scores Grid */}
      <div>
        <h3 className="text-lg font-semibold mb-4 text-foreground">Unified Scores</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <ScoreCard
            title="Truth Index"
            score={result.scores.truthIndex}
            variant="truth"
            description="Alignment with truth principles"
          />
          <ScoreCard
            title="Integrity Index"
            score={result.scores.integrityIndex}
            variant="integrity"
            description="Logical coherence"
          />
          <ScoreCard
            title="Risk Index"
            score={result.scores.riskIndex}
            variant="risk"
            description="Manipulation & deception risk"
          />
          <ScoreCard
            title="Awakening Index"
            score={result.scores.awakeningIndex}
            variant="awakening"
            description="Consciousness expansion"
          />
        </div>
      </div>

      {/* Component Scores Chart */}
      <Card>
        <CardHeader>
          <CardTitle className="text-lg">Component Analysis</CardTitle>
          <CardDescription>Detailed breakdown of individual scoring components</CardDescription>
        </CardHeader>
        <CardContent>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={componentScoresData}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
              <XAxis dataKey="name" stroke="rgba(255,255,255,0.5)" />
              <YAxis stroke="rgba(255,255,255,0.5)" />
              <Tooltip contentStyle={{ backgroundColor: "rgba(0,0,0,0.8)", border: "1px solid rgba(255,255,255,0.2)" }} />
              <Bar dataKey="value" fill="url(#colorGradient)" radius={[8, 8, 0, 0]} />
              <defs>
                <linearGradient id="colorGradient" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stopColor="#a78bfa" />
                  <stop offset="100%" stopColor="#7c3aed" />
                </linearGradient>
              </defs>
            </BarChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>

      {/* Pattern Visualization */}
      <PatternVisualization
        manipulationPatterns={result.manipulationPatterns}
        truthPatterns={result.truthPatterns}
        anomalies={result.anomalies}
      />

      {/* Temporal Data */}
      <Card>
        <CardHeader>
          <CardTitle className="text-lg">Temporal Coherence</CardTitle>
          <CardDescription>Consistency and stability metrics (Drift Direction: {result.driftDirection})</CardDescription>
        </CardHeader>
        <CardContent>
          <ResponsiveContainer width="100%" height={250}>
            <BarChart data={temporalData}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
              <XAxis dataKey="name" stroke="rgba(255,255,255,0.5)" />
              <YAxis stroke="rgba(255,255,255,0.5)" />
              <Tooltip contentStyle={{ backgroundColor: "rgba(0,0,0,0.8)", border: "1px solid rgba(255,255,255,0.2)" }} />
              <Bar dataKey="value" fill="#a78bfa" radius={[8, 8, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>

      {/* Recommendations */}
      {result.recommendations && result.recommendations.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Recommendations</CardTitle>
          </CardHeader>
          <CardContent>
            <ul className="space-y-2">
              {result.recommendations.map((rec, idx) => (
                <li key={idx} className="flex gap-3 text-sm">
                  <span className="text-accent">•</span>
                  <span className="text-foreground">{rec}</span>
                </li>
              ))}
            </ul>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
