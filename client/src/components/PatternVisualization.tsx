/**
 * Pattern Visualization Component
 * Displays detected patterns with categorization and details
 */

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { AlertTriangle, CheckCircle2, AlertCircle } from "lucide-react";
import { cn } from "@/lib/utils";

interface Pattern {
  type: string;
  name: string;
  description: string;
  matches: string[];
  severity?: number;
}

interface PatternVisualizationProps {
  manipulationPatterns: Pattern[];
  truthPatterns: Pattern[];
  anomalies: Pattern[];
  className?: string;
}

export function PatternVisualization({
  manipulationPatterns,
  truthPatterns,
  anomalies,
  className,
}: PatternVisualizationProps) {
  const PatternItem = ({ pattern, type }: { pattern: Pattern; type: "manipulation" | "truth" | "anomaly" }) => {
    const getIcon = () => {
      switch (type) {
        case "manipulation":
          return <AlertTriangle className="h-4 w-4 text-red-500" />;
        case "truth":
          return <CheckCircle2 className="h-4 w-4 text-green-500" />;
        case "anomaly":
          return <AlertCircle className="h-4 w-4 text-yellow-500" />;
      }
    };

    const getBgColor = () => {
      switch (type) {
        case "manipulation":
          return "bg-red-500/10 border-red-500/20";
        case "truth":
          return "bg-green-500/10 border-green-500/20";
        case "anomaly":
          return "bg-yellow-500/10 border-yellow-500/20";
      }
    };

    const getBadgeVariant = () => {
      switch (type) {
        case "manipulation":
          return "destructive";
        case "truth":
          return "default";
        case "anomaly":
          return "secondary";
      }
    };

    return (
      <div className={cn("border-2 rounded-lg p-4 space-y-2", getBgColor())}>
        <div className="flex items-start gap-3">
          <div className="mt-1">{getIcon()}</div>
          <div className="flex-1">
            <h4 className="font-semibold text-sm text-foreground">{pattern.name}</h4>
            <p className="text-xs text-muted-foreground mt-1">{pattern.description}</p>
          </div>
        </div>

        {/* Matches */}
        {pattern.matches && pattern.matches.length > 0 && (
          <div className="mt-3 pt-3 border-t border-border">
            <p className="text-xs font-medium text-muted-foreground mb-2">Detected Matches:</p>
            <div className="flex flex-wrap gap-1">
              {pattern.matches.slice(0, 3).map((match, idx) => (
                <Badge key={idx} variant="outline" className="text-xs">
                  {match}
                </Badge>
              ))}
              {pattern.matches.length > 3 && (
                <Badge variant="outline" className="text-xs">
                  +{pattern.matches.length - 3} more
                </Badge>
              )}
            </div>
          </div>
        )}

        {/* Severity */}
        {pattern.severity !== undefined && pattern.severity > 0 && (
          <div className="mt-2 pt-2 border-t border-border">
            <div className="flex items-center justify-between">
              <span className="text-xs text-muted-foreground">Severity</span>
              <div className="w-24 bg-card rounded h-1.5 overflow-hidden border border-border">
                <div
                  className="h-full bg-gradient-to-r from-yellow-500 to-red-500"
                  style={{ width: `${pattern.severity * 100}%` }}
                />
              </div>
            </div>
          </div>
        )}
      </div>
    );
  };

  return (
    <Card className={className}>
      <CardHeader>
        <CardTitle className="text-lg">Pattern Recognition</CardTitle>
        <CardDescription>Detected manipulation tactics, truth patterns, and anomalies</CardDescription>
      </CardHeader>
      <CardContent className="space-y-6">
        {/* Manipulation Patterns */}
        {manipulationPatterns.length > 0 && (
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <AlertTriangle className="h-4 w-4 text-red-500" />
              <h3 className="font-semibold text-sm">Manipulation Tactics ({manipulationPatterns.length})</h3>
            </div>
            <div className="space-y-2">
              {manipulationPatterns.map((pattern, idx) => (
                <PatternItem key={idx} pattern={pattern} type="manipulation" />
              ))}
            </div>
          </div>
        )}

        {/* Truth Patterns */}
        {truthPatterns.length > 0 && (
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <CheckCircle2 className="h-4 w-4 text-green-500" />
              <h3 className="font-semibold text-sm">Truth Patterns ({truthPatterns.length})</h3>
            </div>
            <div className="space-y-2">
              {truthPatterns.map((pattern, idx) => (
                <PatternItem key={idx} pattern={pattern} type="truth" />
              ))}
            </div>
          </div>
        )}

        {/* Anomalies */}
        {anomalies.length > 0 && (
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <AlertCircle className="h-4 w-4 text-yellow-500" />
              <h3 className="font-semibold text-sm">Anomalies ({anomalies.length})</h3>
            </div>
            <div className="space-y-2">
              {anomalies.map((pattern, idx) => (
                <PatternItem key={idx} pattern={pattern} type="anomaly" />
              ))}
            </div>
          </div>
        )}

        {/* No Patterns */}
        {manipulationPatterns.length === 0 && truthPatterns.length === 0 && anomalies.length === 0 && (
          <div className="text-center py-8">
            <p className="text-muted-foreground text-sm">No patterns detected in this analysis</p>
          </div>
        )}
      </CardContent>
    </Card>
  );
}
