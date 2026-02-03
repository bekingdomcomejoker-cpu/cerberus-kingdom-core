/**
 * Score Card Component
 * Displays individual score with visual representation
 */

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { cn } from "@/lib/utils";

interface ScoreCardProps {
  title: string;
  description?: string;
  score: number; // 0-1000 (displayed as 0-10)
  maxScore?: number;
  icon?: React.ReactNode;
  className?: string;
  variant?: "truth" | "integrity" | "risk" | "awakening";
}

export function ScoreCard({
  title,
  description,
  score,
  maxScore = 1000,
  icon,
  className,
  variant = "truth",
}: ScoreCardProps) {
  const displayScore = (score / maxScore) * 10;
  const percentage = (score / maxScore) * 100;

  const getVariantColor = (variant: string) => {
    switch (variant) {
      case "truth":
        return "from-purple-600 to-purple-400";
      case "integrity":
        return "from-violet-600 to-violet-400";
      case "risk":
        return "from-red-600 to-red-400";
      case "awakening":
        return "from-amber-600 to-amber-400";
      default:
        return "from-purple-600 to-purple-400";
    }
  };

  const getVariantBg = (variant: string) => {
    switch (variant) {
      case "truth":
        return "bg-purple-500/10 border-purple-500/20";
      case "integrity":
        return "bg-violet-500/10 border-violet-500/20";
      case "risk":
        return "bg-red-500/10 border-red-500/20";
      case "awakening":
        return "bg-amber-500/10 border-amber-500/20";
      default:
        return "bg-purple-500/10 border-purple-500/20";
    }
  };

  return (
    <Card className={cn("border-2", getVariantBg(variant), className)}>
      <CardHeader className="pb-3">
        <div className="flex items-start justify-between">
          <div>
            <CardTitle className="text-base">{title}</CardTitle>
            {description && <CardDescription className="text-xs">{description}</CardDescription>}
          </div>
          {icon && <div className="text-accent">{icon}</div>}
        </div>
      </CardHeader>
      <CardContent>
        <div className="space-y-3">
          {/* Score Display */}
          <div className="flex items-baseline gap-1">
            <span className={`text-4xl font-bold bg-gradient-to-r ${getVariantColor(variant)} bg-clip-text text-transparent`}>
              {displayScore.toFixed(1)}
            </span>
            <span className="text-sm text-muted-foreground">/10</span>
          </div>

          {/* Progress Bar */}
          <div className="w-full bg-card rounded-full h-2 overflow-hidden border border-border">
            <div
              className={`h-full bg-gradient-to-r ${getVariantColor(variant)} transition-all duration-500`}
              style={{ width: `${percentage}%` }}
            />
          </div>

          {/* Percentage */}
          <p className="text-xs text-muted-foreground">{percentage.toFixed(0)}% Complete</p>
        </div>
      </CardContent>
    </Card>
  );
}
