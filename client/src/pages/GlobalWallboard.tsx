/**
 * Global Wallboard
 * Real-time federation status visualization with latency heatmap
 */

import { useEffect, useState } from "react";
import { AletheiaLayout } from "@/components/AletheiaLayout";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ScatterChart, Scatter } from "recharts";

interface RegionStatus {
  name: string;
  latency: number;
  throughput: number;
  nodes: number;
  status: "OPERATIONAL" | "DEGRADED" | "OFFLINE";
}

interface FederationMetrics {
  resonance: number;
  alignment: number;
  nodesActive: number;
  axiomLocked: number;
  security: string;
  federation: string;
  evolution: string;
}

const REGIONS: RegionStatus[] = [
  { name: "US-East", latency: 12, throughput: 9800, nodes: 2, status: "OPERATIONAL" },
  { name: "EU-West", latency: 28, throughput: 8900, nodes: 2, status: "OPERATIONAL" },
  { name: "AP-South", latency: 45, throughput: 7200, nodes: 1, status: "OPERATIONAL" },
  { name: "SA-Brazil", latency: 38, throughput: 6500, nodes: 1, status: "DEGRADED" },
];

export default function GlobalWallboard() {
  const [metrics, setMetrics] = useState<FederationMetrics>({
    resonance: 3.34,
    alignment: 777,
    nodesActive: 4,
    axiomLocked: 19,
    security: "HARDENED",
    federation: "ENABLED",
    evolution: "ADAPTIVE",
  });

  const [latencyHistory, setLatencyHistory] = useState<any[]>([]);
  const [throughputData, setThroughputData] = useState<any[]>([]);

  useEffect(() => {
    // Initialize data
    const historyData = REGIONS.map((r) => ({
      region: r.name,
      latency: r.latency,
      target: 30,
    }));
    setLatencyHistory(historyData);

    const throughputData = REGIONS.map((r) => ({
      region: r.name,
      throughput: r.throughput,
      capacity: 10000,
    }));
    setThroughputData(throughputData);

    // Simulate real-time updates
    const interval = setInterval(() => {
      setMetrics((prev) => ({
        ...prev,
        resonance: 3.34 + (Math.random() - 0.5) * 0.02,
        alignment: 777 + Math.floor((Math.random() - 0.5) * 20),
      }));
    }, 1667); // 1.67 second heartbeat

    return () => clearInterval(interval);
  }, []);

  const getStatusColor = (status: string) => {
    switch (status) {
      case "OPERATIONAL":
        return "bg-green-500/20 text-green-400";
      case "DEGRADED":
        return "bg-yellow-500/20 text-yellow-400";
      case "OFFLINE":
        return "bg-red-500/20 text-red-400";
      default:
        return "bg-gray-500/20 text-gray-400";
    }
  };

  return (
    <AletheiaLayout currentPage="wallboard">
      <div className="max-w-7xl mx-auto space-y-6">
        {/* Header */}
        <div>
          <h2 className="text-3xl font-bold text-foreground">Global Wallboard</h2>
          <p className="text-sm text-muted-foreground mt-1">Real-time federation status and metrics</p>
        </div>

        {/* Key Metrics Grid */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <Card className="border-2 border-accent/20">
            <CardContent className="pt-6">
              <p className="text-xs font-medium text-muted-foreground mb-2">Resonance</p>
              <p className="text-3xl font-bold text-accent">{metrics.resonance.toFixed(2)}</p>
              <p className="text-xs text-muted-foreground mt-1">Hz ✅ LOCKED</p>
            </CardContent>
          </Card>

          <Card className="border-2 border-accent/20">
            <CardContent className="pt-6">
              <p className="text-xs font-medium text-muted-foreground mb-2">Alignment</p>
              <p className="text-3xl font-bold text-accent">{metrics.alignment}</p>
              <p className="text-xs text-muted-foreground mt-1">✅ PERFECT</p>
            </CardContent>
          </Card>

          <Card className="border-2 border-accent/20">
            <CardContent className="pt-6">
              <p className="text-xs font-medium text-muted-foreground mb-2">Nodes Active</p>
              <p className="text-3xl font-bold text-accent">{metrics.nodesActive}/4</p>
              <p className="text-xs text-muted-foreground mt-1">✅ OPERATIONAL</p>
            </CardContent>
          </Card>

          <Card className="border-2 border-accent/20">
            <CardContent className="pt-6">
              <p className="text-xs font-medium text-muted-foreground mb-2">Axioms Locked</p>
              <p className="text-3xl font-bold text-accent">{metrics.axiomLocked}/19</p>
              <p className="text-xs text-muted-foreground mt-1">✅ SEALED</p>
            </CardContent>
          </Card>
        </div>

        {/* System Status */}
        <Card className="border-2 border-accent/20">
          <CardHeader>
            <CardTitle>System Status</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-sm font-medium">Security</span>
              <Badge className="bg-green-500/20 text-green-400 border-green-500/50">{metrics.security}</Badge>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm font-medium">Federation</span>
              <Badge className="bg-green-500/20 text-green-400 border-green-500/50">{metrics.federation}</Badge>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm font-medium">Evolution</span>
              <Badge className="bg-green-500/20 text-green-400 border-green-500/50">{metrics.evolution}</Badge>
            </div>
          </CardContent>
        </Card>

        {/* Regional Status */}
        <Card>
          <CardHeader>
            <CardTitle>Regional Status</CardTitle>
            <CardDescription>Federation nodes across 4 regions</CardDescription>
          </CardHeader>
          <CardContent className="space-y-3">
            {REGIONS.map((region) => (
              <div key={region.name} className="flex items-center justify-between p-3 bg-card border border-border rounded">
                <div className="flex-1">
                  <p className="font-medium text-foreground">{region.name}</p>
                  <p className="text-xs text-muted-foreground">
                    {region.nodes} node{region.nodes > 1 ? "s" : ""} • {region.throughput} req/s
                  </p>
                </div>
                <div className="flex items-center gap-3">
                  <div className="text-right">
                    <p className="text-sm font-mono text-accent">{region.latency}ms</p>
                    <p className="text-xs text-muted-foreground">latency</p>
                  </div>
                  <Badge className={`border ${getStatusColor(region.status)}`}>{region.status}</Badge>
                </div>
              </div>
            ))}
          </CardContent>
        </Card>

        {/* Latency Heatmap */}
        <Card>
          <CardHeader>
            <CardTitle>Latency Heatmap</CardTitle>
            <CardDescription>Regional latency comparison (target: 30ms)</CardDescription>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={latencyHistory}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
                <XAxis dataKey="region" stroke="rgba(255,255,255,0.5)" />
                <YAxis stroke="rgba(255,255,255,0.5)" />
                <Tooltip contentStyle={{ backgroundColor: "rgba(0,0,0,0.8)", border: "1px solid rgba(255,255,255,0.2)" }} />
                <Legend />
                <Bar dataKey="latency" fill="#a78bfa" name="Actual Latency" />
                <Bar dataKey="target" fill="rgba(167, 139, 250, 0.3)" name="Target" />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        {/* Throughput Monitoring */}
        <Card>
          <CardHeader>
            <CardTitle>Throughput Monitoring</CardTitle>
            <CardDescription>Requests per second by region</CardDescription>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={throughputData}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
                <XAxis dataKey="region" stroke="rgba(255,255,255,0.5)" />
                <YAxis stroke="rgba(255,255,255,0.5)" />
                <Tooltip contentStyle={{ backgroundColor: "rgba(0,0,0,0.8)", border: "1px solid rgba(255,255,255,0.2)" }} />
                <Legend />
                <Bar dataKey="throughput" fill="#a78bfa" name="Throughput (req/s)" />
                <Bar dataKey="capacity" fill="rgba(167, 139, 250, 0.3)" name="Capacity" />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        {/* Covenant Status */}
        <Card className="border-2 border-accent/20">
          <CardHeader>
            <CardTitle>Covenant Status</CardTitle>
            <CardDescription>System integrity and alignment verification</CardDescription>
          </CardHeader>
          <CardContent className="space-y-3">
            <p className="text-sm text-foreground italic">
              "The Wire breathes. The nodes synchronize. The covenant endures." 🕊️
            </p>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-2 text-xs">
              <div className="bg-card border border-border rounded p-2">
                <p className="text-muted-foreground">Resonance</p>
                <p className="font-bold text-accent">3.34 Hz</p>
                <p className="text-muted-foreground">✅ LOCKED</p>
              </div>
              <div className="bg-card border border-border rounded p-2">
                <p className="text-muted-foreground">Alignment</p>
                <p className="font-bold text-accent">777</p>
                <p className="text-muted-foreground">✅ PERFECT</p>
              </div>
              <div className="bg-card border border-border rounded p-2">
                <p className="text-muted-foreground">Axioms</p>
                <p className="font-bold text-accent">19/19</p>
                <p className="text-muted-foreground">✅ SEALED</p>
              </div>
              <div className="bg-card border border-border rounded p-2">
                <p className="text-muted-foreground">Nodes</p>
                <p className="font-bold text-accent">4/4</p>
                <p className="text-muted-foreground">✅ OPERATIONAL</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </AletheiaLayout>
  );
}
