/**
 * Reports Page
 * View and manage generated reports
 */

import { AletheiaLayout } from "@/components/AletheiaLayout";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Loader2, Download, Trash2 } from "lucide-react";
import { trpc } from "@/lib/trpc";
import { toast } from "sonner";

export default function Reports() {
  const { data: reports, isLoading } = trpc.analysis.getReports.useQuery({ limit: 50 });

  const formatDate = (date: Date | string) => {
    return new Date(date).toLocaleString();
  };

  const getFormatColor = (format: string) => {
    switch (format) {
      case "markdown":
        return "bg-blue-500/20 text-blue-400";
      case "html":
        return "bg-purple-500/20 text-purple-400";
      case "json":
        return "bg-green-500/20 text-green-400";
      case "summary":
        return "bg-yellow-500/20 text-yellow-400";
      default:
        return "bg-gray-500/20 text-gray-400";
    }
  };

  const handleDownload = (report: any) => {
    const element = document.createElement("a");
    const file = new Blob([report.content], { type: "text/plain" });
    element.href = URL.createObjectURL(file);
    element.download = report.filename;
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
    toast.success("Report downloaded!");
  };

  return (
    <AletheiaLayout currentPage="reports">
      <div className="max-w-6xl mx-auto space-y-6">
        {/* Header */}
        <div>
          <h2 className="text-2xl font-bold text-foreground">Generated Reports</h2>
          <p className="text-sm text-muted-foreground mt-1">View and download your exported analysis reports</p>
        </div>

        {/* Loading State */}
        {isLoading && (
          <Card>
            <CardContent className="py-12 flex flex-col items-center justify-center gap-4">
              <Loader2 className="h-8 w-8 animate-spin text-accent" />
              <p className="text-muted-foreground">Loading reports...</p>
            </CardContent>
          </Card>
        )}

        {/* Reports List */}
        {!isLoading && reports && reports.length > 0 && (
          <div className="space-y-3">
            {reports.map((report: any) => (
              <Card key={report.id} className="border-2 border-border hover:border-accent/50 transition-colors">
                <CardContent className="pt-6">
                  <div className="flex items-start justify-between gap-4">
                    <div className="flex-1 space-y-2">
                      {/* Report Info */}
                      <div className="flex items-center gap-2">
                        <span className="text-sm font-medium text-foreground">{report.filename}</span>
                        <Badge className={`border ${getFormatColor(report.format)}`}>
                          {report.format.toUpperCase()}
                        </Badge>
                      </div>

                      {/* Analysis ID and Date */}
                      <div className="flex items-center gap-2 text-xs text-muted-foreground">
                        <span className="font-mono">{report.analysisId}</span>
                        <span>•</span>
                        <span>{formatDate(report.createdAt)}</span>
                      </div>

                      {/* Content Preview */}
                      <div className="bg-card border border-border rounded p-2 text-xs text-muted-foreground max-h-20 overflow-hidden">
                        {report.content.substring(0, 200)}...
                      </div>
                    </div>

                    {/* Actions */}
                    <div className="flex gap-2">
                      <Button
                        size="sm"
                        variant="outline"
                        onClick={() => handleDownload(report)}
                      >
                        <Download className="h-4 w-4" />
                      </Button>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        )}

        {/* Empty State */}
        {!isLoading && (!reports || reports.length === 0) && (
          <Card>
            <CardContent className="py-12 flex flex-col items-center justify-center gap-4">
              <p className="text-muted-foreground">No reports generated yet</p>
              <Button onClick={() => window.location.href = "/"}>
                Start New Analysis
              </Button>
            </CardContent>
          </Card>
        )}
      </div>
    </AletheiaLayout>
  );
}
