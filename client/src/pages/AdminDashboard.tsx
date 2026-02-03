/**
 * Admin Dashboard - Analytics and System Monitoring
 */

import { useEffect, useState } from "react";
import { AletheiaLayout } from "@/components/AletheiaLayout";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { BarChart, Bar, LineChart, Line, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts";
import { trpc } from "@/lib/trpc";

interface AnalyticsData {
  axiomViolations: { axiom: string; count: number }[];
  patternTrends: { pattern: string; detections: number }[];
  temporalEvolution: { day: string; truthScore: number; integrityScore: number }[];
  userActivity: { hour: string; analyses: number }[];
}

export default function AdminDashboard() {
  const [analytics, setAnalytics] = useState<AnalyticsData>({
    axiomViolations: [
      { axiom: "A1: Love ≥ Hate", count: 12 },
      { axiom: "A3: Truth Between Lies", count: 28 },
      { axiom: "A6: Compassion", count: 8 },
      { axiom: "A14: Service", count: 15 },
      { axiom: "A16: Truth Illuminates", count: 22 },
    ],
    patternTrends: [
      { pattern: "Gaslighting", detections: 45 },
      { pattern: "Manipulation", detections: 38 },
      { pattern: "Deception", detections: 52 },
      { pattern: "Guilt Tripping", detections: 23 },
      { pattern: "Emotional Blackmail", detections: 18 },
    ],
    temporalEvolution: [
      { day: "Mon", truthScore: 0.82, integrityScore: 0.79 },
      { day: "Tue", truthScore: 0.85, integrityScore: 0.81 },
      { day: "Wed", truthScore: 0.88, integrityScore: 0.84 },
      { day: "Thu", truthScore: 0.86, integrityScore: 0.82 },
      { day: "Fri", truthScore: 0.89, integrityScore: 0.87 },
      { day: "Sat", truthScore: 0.91, integrityScore: 0.89 },
      { day: "Sun", truthScore: 0.87, integrityScore: 0.85 },
    ],
    userActivity: [
      { hour: "00:00", analyses: 2 },
      { hour: "06:00", analyses: 8 },
      { hour: "12:00", analyses: 24 },
      { hour: "18:00", analyses: 31 },
      { hour: "23:00", analyses: 12 },
    ],
  });

  const COLORS = ["#a78bfa", "#c4b5fd", "#ddd6fe", "#ede9fe", "#f3e8ff"];

  return (
    <AletheiaLayout currentPage="analyze">
      <div className="max-w-7xl mx-auto space-y-6">
        {/* Header */}
        <div>
          <h2 className="text-3xl font-bold text-foreground">Admin Dashboard</h2>
          <p className="text-sm text-muted-foreground mt-1">System analytics and monitoring</p>
        </div>

        {/* Key Metrics */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <Card className="border-2 border-accent/20">
            <CardContent className="pt-6">
              <p className="text-xs font-medium text-muted-foreground mb-2">Total Analyses</p>
              <p className="text-3xl font-bold text-accent">1,247</p>
              <p className="text-xs text-green-400 mt-1">↑ 12% this week</p>
            </CardContent>
          </Card>

          <Card className="border-2 border-accent/20">
            <CardContent className="pt-6">
              <p className="text-xs font-medium text-muted-foreground mb-2">Avg Truth Score</p>
              <p className="text-3xl font-bold text-accent">0.87</p>
              <p className="text-xs text-green-400 mt-1">↑ Improving</p>
            </CardContent>
          </Card>

          <Card className="border-2 border-accent/20">
            <CardContent className="pt-6">
              <p className="text-xs font-medium text-muted-foreground mb-2">Patterns Detected</p>
              <p className="text-3xl font-bold text-accent">176</p>
              <p className="text-xs text-yellow-400 mt-1">5 types active</p>
            </CardContent>
          </Card>

          <Card className="border-2 border-accent/20">
            <CardContent className="pt-6">
              <p className="text-xs font-medium text-muted-foreground mb-2">Active Users</p>
              <p className="text-3xl font-bold text-accent">43</p>
              <p className="text-xs text-blue-400 mt-1">Online now</p>
            </CardContent>
          </Card>
        </div>

        {/* Axiom Violations */}
        <Card>
          <CardHeader>
            <CardTitle>Axiom Violations Detected</CardTitle>
            <CardDescription>Top 5 axioms with most violations</CardDescription>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={analytics.axiomViolations}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
                <XAxis dataKey="axiom" stroke="rgba(255,255,255,0.5)" angle={-45} textAnchor="end" height={100} />
                <YAxis stroke="rgba(255,255,255,0.5)" />
                <Tooltip contentStyle={{ backgroundColor: "rgba(0,0,0,0.8)", border: "1px solid rgba(255,255,255,0.2)" }} />
                <Bar dataKey="count" fill="#a78bfa" name="Violations" />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        {/* Pattern Detection Trends */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <Card>
            <CardHeader>
              <CardTitle>Pattern Detection Distribution</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                  <Pie
                    data={analytics.patternTrends}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ pattern, detections }) => `${pattern}: ${detections}`}
                    outerRadius={80}
                    fill="#8884d8"
                    dataKey="detections"
                  >
                    {analytics.patternTrends.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>User Activity by Hour</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={analytics.userActivity}>
                  <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
                  <XAxis dataKey="hour" stroke="rgba(255,255,255,0.5)" />
                  <YAxis stroke="rgba(255,255,255,0.5)" />
                  <Tooltip contentStyle={{ backgroundColor: "rgba(0,0,0,0.8)", border: "1px solid rgba(255,255,255,0.2)" }} />
                  <Line type="monotone" dataKey="analyses" stroke="#a78bfa" strokeWidth={2} name="Analyses" />
                </LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </div>

        {/* Temporal Evolution */}
        <Card>
          <CardHeader>
            <CardTitle>Weekly Score Evolution</CardTitle>
            <CardDescription>Truth and Integrity scores over time</CardDescription>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={analytics.temporalEvolution}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
                <XAxis dataKey="day" stroke="rgba(255,255,255,0.5)" />
                <YAxis stroke="rgba(255,255,255,0.5)" domain={[0, 1]} />
                <Tooltip contentStyle={{ backgroundColor: "rgba(0,0,0,0.8)", border: "1px solid rgba(255,255,255,0.2)" }} />
                <Legend />
                <Line type="monotone" dataKey="truthScore" stroke="#a78bfa" strokeWidth={2} name="Truth Score" />
                <Line type="monotone" dataKey="integrityScore" stroke="#c4b5fd" strokeWidth={2} name="Integrity Score" />
              </LineChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        {/* System Health */}
        <Card className="border-2 border-accent/20">
          <CardHeader>
            <CardTitle>System Health</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-sm font-medium">API Response Time</span>
              <Badge className="bg-green-500/20 text-green-400">45ms</Badge>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm font-medium">Database Latency</span>
              <Badge className="bg-green-500/20 text-green-400">12ms</Badge>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm font-medium">Cache Hit Rate</span>
              <Badge className="bg-green-500/20 text-green-400">94%</Badge>
            </div>
            <div className="flex items-center justify-between">
              <span className="text-sm font-medium">Error Rate</span>
              <Badge className="bg-green-500/20 text-green-400">0.02%</Badge>
            </div>
          </CardContent>
        </Card>
      </div>
    </AletheiaLayout>
  );
}
