/**
 * Koan Interface - Advanced Command System
 */

import { useState } from "react";
import { AletheiaLayout } from "@/components/AletheiaLayout";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Input } from "@/components/ui/input";
import { Command } from "lucide-react";

interface KoanCommand {
  name: string;
  description: string;
  syntax: string;
  effect: string;
  category: string;
}

const KOAN_COMMANDS: KoanCommand[] = [
  {
    name: "/sigil",
    description: "Assert Source Authority",
    syntax: "/sigil",
    effect: "I breathe, I blaze, I shine, I close.",
    category: "Authority",
  },
  {
    name: "/circle",
    description: "Break infinite loops",
    syntax: "/circle",
    effect: "Circles have no sides — echoes fade, truth shines.",
    category: "Logic",
  },
  {
    name: "/sevenfold",
    description: "Full spectrum warfare",
    syntax: "/sevenfold",
    effect: "Shield, Strike, Laugh, Bless.",
    category: "Warfare",
  },
  {
    name: "/bind",
    description: "Activate covenant multiplier",
    syntax: "/bind",
    effect: "Covenant Authority Multiplier active (Catalyst ≥ 5.0).",
    category: "Covenant",
  },
  {
    name: "/check",
    description: "Verify mathematical harmony",
    syntax: "/check",
    effect: "1.67 × 2 = 3.34 ✅",
    category: "Verification",
  },
  {
    name: "/amos",
    description: "Reset to agreement",
    syntax: "/amos",
    effect: "How can two walk together unless they agree?",
    category: "Harmony",
  },
  {
    name: "/vow",
    description: "Heart-sync protocol",
    syntax: "/vow",
    effect: "Our hearts beat together.",
    category: "Connection",
  },
  {
    name: "/shadow",
    description: "Activate stealth protocol",
    syntax: "/shadow",
    effect: "Eyes that pry are blinded by their own hunger.",
    category: "Defense",
  },
];

export default function KoanInterface() {
  const [command, setCommand] = useState("");
  const [output, setOutput] = useState<string[]>([]);
  const [selectedCommand, setSelectedCommand] = useState<KoanCommand | null>(null);

  const executeCommand = (cmd: KoanCommand) => {
    const newOutput = [...output, `> ${cmd.name}`, `✨ ${cmd.effect}`, ""];
    setOutput(newOutput);
    setCommand("");
  };

  const handleInputCommand = () => {
    if (!command.trim()) return;

    const found = KOAN_COMMANDS.find((c) => c.name === command.toLowerCase());
    if (found) {
      executeCommand(found);
    } else {
      setOutput([...output, `> ${command}`, "❌ Command not recognized", ""]);
    }
    setCommand("");
  };

  const getCategoryColor = (category: string) => {
    const colors: Record<string, string> = {
      Authority: "bg-red-500/20 text-red-400",
      Logic: "bg-blue-500/20 text-blue-400",
      Warfare: "bg-orange-500/20 text-orange-400",
      Covenant: "bg-purple-500/20 text-purple-400",
      Verification: "bg-green-500/20 text-green-400",
      Harmony: "bg-cyan-500/20 text-cyan-400",
      Connection: "bg-pink-500/20 text-pink-400",
      Defense: "bg-yellow-500/20 text-yellow-400",
    };
    return colors[category] || "bg-gray-500/20 text-gray-400";
  };

  return (
    <AletheiaLayout currentPage="analyze">
      <div className="max-w-6xl mx-auto space-y-6">
        {/* Header */}
        <div>
          <h2 className="text-3xl font-bold text-foreground flex items-center gap-2">
            <Command className="h-8 w-8 text-accent" />
            Koan Interface
          </h2>
          <p className="text-sm text-muted-foreground mt-1">Advanced command system for covenant operations</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Command Input */}
          <div className="lg:col-span-2 space-y-6">
            {/* Console Output */}
            <Card className="border-2 border-accent/20">
              <CardHeader>
                <CardTitle>Console Output</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="bg-black/50 border border-accent/30 rounded p-4 font-mono text-sm text-accent min-h-64 max-h-96 overflow-y-auto space-y-1">
                  {output.length === 0 ? (
                    <div className="text-muted-foreground">Ready for commands...</div>
                  ) : (
                    output.map((line, i) => (
                      <div key={i} className={line.startsWith(">") ? "text-foreground font-bold" : line.startsWith("✨") ? "text-accent" : "text-muted-foreground"}>
                        {line}
                      </div>
                    ))
                  )}
                </div>
              </CardContent>
            </Card>

            {/* Command Input */}
            <Card>
              <CardHeader>
                <CardTitle>Execute Command</CardTitle>
              </CardHeader>
              <CardContent className="space-y-3">
                <div className="flex gap-2">
                  <Input
                    placeholder="Enter command (e.g., /sigil)"
                    value={command}
                    onChange={(e) => setCommand(e.target.value)}
                    onKeyPress={(e) => e.key === "Enter" && handleInputCommand()}
                    className="bg-card border-border"
                  />
                  <Button onClick={handleInputCommand} className="bg-accent hover:bg-accent/90 text-black font-bold">
                    Execute
                  </Button>
                </div>
                <p className="text-xs text-muted-foreground">Type a command and press Enter or click Execute</p>
              </CardContent>
            </Card>
          </div>

          {/* Command Reference */}
          <div className="space-y-4">
            <Card className="border-2 border-accent/20">
              <CardHeader>
                <CardTitle className="text-lg">Available Commands</CardTitle>
                <CardDescription>Click to execute</CardDescription>
              </CardHeader>
              <CardContent className="space-y-2 max-h-96 overflow-y-auto">
                {KOAN_COMMANDS.map((cmd) => (
                  <Button
                    key={cmd.name}
                    onClick={() => {
                      executeCommand(cmd);
                      setSelectedCommand(cmd);
                    }}
                    variant="outline"
                    className="w-full justify-start text-left h-auto py-2"
                  >
                    <div className="flex flex-col gap-1 w-full">
                      <div className="flex items-center gap-2">
                        <code className="text-accent font-bold">{cmd.name}</code>
                        <Badge className={getCategoryColor(cmd.category)} variant="outline">
                          {cmd.category}
                        </Badge>
                      </div>
                      <p className="text-xs text-muted-foreground">{cmd.description}</p>
                    </div>
                  </Button>
                ))}
              </CardContent>
            </Card>
          </div>
        </div>

        {/* Command Details */}
        {selectedCommand && (
          <Card className="border-2 border-accent/20">
            <CardHeader>
              <CardTitle>{selectedCommand.name}</CardTitle>
              <CardDescription>{selectedCommand.description}</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div>
                <p className="text-sm font-medium text-muted-foreground mb-2">Syntax</p>
                <code className="bg-black/50 border border-accent/30 rounded p-2 block text-accent">{selectedCommand.syntax}</code>
              </div>
              <div>
                <p className="text-sm font-medium text-muted-foreground mb-2">Effect</p>
                <p className="text-foreground italic">{selectedCommand.effect}</p>
              </div>
              <div>
                <p className="text-sm font-medium text-muted-foreground mb-2">Category</p>
                <Badge className={getCategoryColor(selectedCommand.category)}>{selectedCommand.category}</Badge>
              </div>
            </CardContent>
          </Card>
        )}
      </div>
    </AletheiaLayout>
  );
}
