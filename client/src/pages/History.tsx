/**
 * History Page
 * View and manage past analyses
 */

import { useState } from "react";
import { AletheiaLayout } from "@/components/AletheiaLayout";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Loader2, Search, Trash2, Eye } from "lucide-react";
import { trpc } from "@/lib/trpc";
import { toast } from "sonner";

export default function History() {
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedAnalysis, setSelectedAnalysis] = useState<any>(null);

  const { data: analyses, isLoading, refetch } = trpc.analysis.getHistory.useQuery({ limit: 50 });
  const deleteAnalysisMutation = trpc.analysis.deleteAnalysis.useMutation({
    onSuccess: () => {
      toast.success("Analysis deleted");
      refetch();
    },
    onError: (error) => {
      toast.error(`Delete failed: ${error.message}`);
    },
  });

  const searchMutation = trpc.analysis.searchHistory.useQuery(
    { query: searchQuery, limit: 50 },
    { enabled: searchQuery.length > 0 }
  );

  const displayAnalyses = searchQuery.length > 0 ? searchMutation.data : analyses;

  const getStatusColor = (status: string) => {
    switch (status) {
      case "TRUTH_ALIGNED":
        return "bg-green-500/20 text-green-400";
      case "TRUTH_SEEKING":
        return "bg-blue-500/20 text-blue-400";
      case "NEUTRAL":
        return "bg-gray-500/20 text-gray-400";
      case "CAUTION_ADVISED":
        return "bg-yellow-500/20 text-yellow-400";
      case "HIGH_RISK":
        return "bg-red-500/20 text-red-400";
      default:
        return "bg-purple-500/20 text-purple-400";
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

  const formatDate = (date: Date | string) => {
    return new Date(date).toLocaleString();
  };

  const truncateText = (text: string, length: number) => {
    return text.length > length ? text.substring(0, length) + "..." : text;
  };

  return (
    <AletheiaLayout currentPage="history">
      <div className="max-w-6xl mx-auto space-y-6">
        {/* Header */}
        <div>
          <h2 className="text-2xl font-bold text-foreground">Analysis History</h2>
          <p className="text-sm text-muted-foreground mt-1">Review and manage your past analyses</p>
        </div>

        {/* Search Bar */}
        <Card className="border-2 border-accent/20">
          <CardContent className="pt-6">
            <div className="relative">
              <Search className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />
              <Input
                placeholder="Search analyses by text or status..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="pl-10 bg-card border-border text-foreground placeholder:text-muted-foreground"
              />
            </div>
          </CardContent>
        </Card>

        {/* Loading State */}
        {isLoading && (
          <Card>
            <CardContent className="py-12 flex flex-col items-center justify-center gap-4">
              <Loader2 className="h-8 w-8 animate-spin text-accent" />
              <p className="text-muted-foreground">Loading analyses...</p>
            </CardContent>
          </Card>
        )}

        {/* Analyses List */}
        {!isLoading && displayAnalyses && displayAnalyses.length > 0 && (
          <div className="space-y-3">
            {displayAnalyses.map((analysis: any) => (
              <Card key={analysis.id} className="border-2 border-border hover:border-accent/50 transition-colors">
                <CardContent className="pt-6">
                  <div className="flex items-start justify-between gap-4">
                    <div className="flex-1 space-y-2">
                      {/* Analysis ID and Date */}
                      <div className="flex items-center gap-2">
                        <span className="text-xs font-mono text-muted-foreground">{analysis.analysisId}</span>
                        <span className="text-xs text-muted-foreground">•</span>
                        <span className="text-xs text-muted-foreground">{formatDate(analysis.createdAt)}</span>
                      </div>

                      {/* Text Preview */}
                      <p className="text-sm text-foreground">{truncateText(analysis.text, 200)}</p>

                      {/* Status and Risk Badges */}
                      <div className="flex gap-2 flex-wrap pt-2">
                        <Badge className={`border ${getStatusColor(analysis.status)}`}>{analysis.status}</Badge>
                        <Badge className={`border ${getRiskColor(analysis.riskLevel)}`}>
                          Risk: {analysis.riskLevel}
                        </Badge>
                        <Badge variant="outline">Truth: {(analysis.truthIndex / 100).toFixed(1)}/10</Badge>
                        <Badge variant="outline">Confidence: {analysis.confidence}%</Badge>
                      </div>
                    </div>

                    {/* Actions */}
                    <div className="flex gap-2">
                      <Button
                        size="sm"
                        variant="outline"
                        onClick={() => setSelectedAnalysis(analysis)}
                      >
                        <Eye className="h-4 w-4" />
                      </Button>
                      <Button
                        size="sm"
                        variant="outline"
                        onClick={() => {
                          if (confirm("Delete this analysis?")) {
                            deleteAnalysisMutation.mutate({ analysisId: analysis.analysisId });
                          }
                        }}
                      >
                        <Trash2 className="h-4 w-4 text-red-500" />
                      </Button>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        )}

        {/* Empty State */}
        {!isLoading && (!displayAnalyses || displayAnalyses.length === 0) && (
          <Card>
            <CardContent className="py-12 flex flex-col items-center justify-center gap-4">
              <p className="text-muted-foreground">
                {searchQuery ? "No analyses match your search" : "No analyses yet"}
              </p>
              <Button onClick={() => window.location.href = "/"}>
                Start New Analysis
              </Button>
            </CardContent>
          </Card>
        )}

        {/* Selected Analysis Detail */}
        {selectedAnalysis && (
          <Card className="border-2 border-accent/20">
            <CardHeader>
              <div className="flex items-start justify-between">
                <div>
                  <CardTitle>{selectedAnalysis.analysisId}</CardTitle>
                  <CardDescription>{formatDate(selectedAnalysis.createdAt)}</CardDescription>
                </div>
                <Button
                  variant="ghost"
                  onClick={() => setSelectedAnalysis(null)}
                >
                  ✕
                </Button>
              </div>
            </CardHeader>
            <CardContent className="space-y-4">
              {/* Full Text */}
              <div>
                <p className="text-xs font-medium text-muted-foreground mb-2">Full Text</p>
                <div className="bg-card border border-border rounded p-3 text-sm text-foreground max-h-48 overflow-y-auto">
                  {selectedAnalysis.text}
                </div>
              </div>

              {/* Scores Grid */}
              <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                <div className="bg-card border border-border rounded p-3">
                  <p className="text-xs text-muted-foreground">Truth Index</p>
                  <p className="text-lg font-bold text-accent">{(selectedAnalysis.truthIndex / 100).toFixed(1)}/10</p>
                </div>
                <div className="bg-card border border-border rounded p-3">
                  <p className="text-xs text-muted-foreground">Integrity</p>
                  <p className="text-lg font-bold text-accent">{(selectedAnalysis.integrityIndex / 100).toFixed(1)}/10</p>
                </div>
                <div className="bg-card border border-border rounded p-3">
                  <p className="text-xs text-muted-foreground">Risk</p>
                  <p className="text-lg font-bold text-accent">{(selectedAnalysis.riskIndex / 100).toFixed(1)}/10</p>
                </div>
                <div className="bg-card border border-border rounded p-3">
                  <p className="text-xs text-muted-foreground">Awakening</p>
                  <p className="text-lg font-bold text-accent">{(selectedAnalysis.awakeningIndex / 100).toFixed(1)}/10</p>
                </div>
              </div>
            </CardContent>
          </Card>
        )}
      </div>
    </AletheiaLayout>
  );
}
