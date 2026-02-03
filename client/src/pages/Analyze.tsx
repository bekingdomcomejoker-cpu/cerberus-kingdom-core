/**
 * Analyze Page
 * Main analysis interface with text input and real-time scoring
 */

import { useState } from "react";
import { AletheiaLayout } from "@/components/AletheiaLayout";
import { AnalysisResults } from "@/components/AnalysisResults";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Badge } from "@/components/ui/badge";
import { Loader2, Send } from "lucide-react";
import { trpc } from "@/lib/trpc";
import { toast } from "sonner";

export default function Analyze() {
  const [text, setText] = useState("");
  const [result, setResult] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(false);

  const analyzeMutation = trpc.analysis.analyze.useMutation({
    onSuccess: (data) => {
      setResult(data);
      setIsLoading(false);
      toast.success("Analysis complete!");
    },
    onError: (error) => {
      setIsLoading(false);
      toast.error(`Analysis failed: ${error.message}`);
    },
  });

  const generateReportMutation = trpc.analysis.generateReport.useMutation({
    onSuccess: (data) => {
      // Create download link
      const element = document.createElement("a");
      const file = new Blob([data.content], { type: "text/plain" });
      element.href = URL.createObjectURL(file);
      element.download = data.filename;
      document.body.appendChild(element);
      element.click();
      document.body.removeChild(element);
      toast.success(`Report exported as ${data.format}!`);
    },
    onError: (error) => {
      toast.error(`Export failed: ${error.message}`);
    },
  });

  const handleAnalyze = async () => {
    if (text.trim().length < 10) {
      toast.error("Please enter at least 10 characters of text");
      return;
    }

    setIsLoading(true);
    setResult(null);
    analyzeMutation.mutate({ text });
  };

  const handleExport = (format: "markdown" | "html" | "json") => {
    if (!result) return;
    generateReportMutation.mutate({
      analysisId: result.analysisId,
      format,
    });
  };

  const handleClear = () => {
    setText("");
    setResult(null);
  };

  const characterCount = text.length;
  const maxCharacters = 50000;

  return (
    <AletheiaLayout currentPage="analyze">
      <div className="max-w-6xl mx-auto space-y-6">
        {/* Input Section */}
        {!result && (
          <Card className="border-2 border-accent/20">
            <CardHeader>
              <CardTitle>Text Analysis</CardTitle>
              <CardDescription>Enter text to analyze for truth, integrity, patterns, and coherence</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              {/* Textarea */}
              <div className="space-y-2">
                <Textarea
                  placeholder="Paste your text here for comprehensive analysis..."
                  value={text}
                  onChange={(e) => setText(e.target.value.slice(0, maxCharacters))}
                  className="min-h-64 bg-card border-border text-foreground placeholder:text-muted-foreground resize-none"
                  disabled={isLoading}
                />
                <div className="flex items-center justify-between text-xs text-muted-foreground">
                  <span>{characterCount} characters</span>
                  <span>{maxCharacters - characterCount} remaining</span>
                </div>
              </div>

              {/* Character Count Bar */}
              <div className="w-full bg-card rounded-full h-1.5 overflow-hidden border border-border">
                <div
                  className="h-full bg-gradient-to-r from-purple-600 to-violet-600 transition-all duration-300"
                  style={{ width: `${(characterCount / maxCharacters) * 100}%` }}
                />
              </div>

              {/* Action Buttons */}
              <div className="flex gap-3 pt-4">
                <Button
                  onClick={handleAnalyze}
                  disabled={isLoading || characterCount < 10}
                  className="flex-1 bg-gradient-to-r from-purple-600 to-violet-600 hover:from-purple-700 hover:to-violet-700"
                >
                  {isLoading ? (
                    <>
                      <Loader2 className="h-4 w-4 mr-2 animate-spin" />
                      Analyzing...
                    </>
                  ) : (
                    <>
                      <Send className="h-4 w-4 mr-2" />
                      Analyze Text
                    </>
                  )}
                </Button>
                <Button
                  onClick={handleClear}
                  variant="outline"
                  disabled={isLoading || characterCount === 0}
                >
                  Clear
                </Button>
              </div>

              {/* Tips */}
              <div className="bg-card border border-border rounded-lg p-4 space-y-2">
                <p className="text-xs font-medium text-accent">Tips for best results:</p>
                <ul className="text-xs text-muted-foreground space-y-1">
                  <li>• Provide sufficient context (minimum 10 characters)</li>
                  <li>• Include complete thoughts and statements</li>
                  <li>• Use clear, coherent language</li>
                  <li>• Longer texts provide more detailed analysis</li>
                </ul>
              </div>
            </CardContent>
          </Card>
        )}

        {/* Loading State */}
        {isLoading && (
          <Card className="border-2 border-accent/20">
            <CardContent className="py-12 flex flex-col items-center justify-center gap-4">
              <Loader2 className="h-8 w-8 animate-spin text-accent" />
              <div className="text-center">
                <p className="font-semibold text-foreground">Analyzing your text...</p>
                <p className="text-sm text-muted-foreground mt-1">This may take a few moments</p>
              </div>
            </CardContent>
          </Card>
        )}

        {/* Results Section */}
        {result && !isLoading && (
          <>
            <AnalysisResults
              result={result}
              onExport={handleExport}
            />
            <div className="flex gap-3 justify-center pt-4">
              <Button
                onClick={handleClear}
                variant="outline"
              >
                New Analysis
              </Button>
              <Button
                onClick={() => window.location.href = "/history"}
                variant="outline"
              >
                View History
              </Button>
            </div>
          </>
        )}
      </div>
    </AletheiaLayout>
  );
}
