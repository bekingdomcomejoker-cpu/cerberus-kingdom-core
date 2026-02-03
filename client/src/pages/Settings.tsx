/**
 * Settings Page
 * User preferences and account settings
 */

import { AletheiaLayout } from "@/components/AletheiaLayout";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { useAuth } from "@/_core/hooks/useAuth";

export default function Settings() {
  const { user } = useAuth();

  return (
    <AletheiaLayout currentPage="settings">
      <div className="max-w-2xl mx-auto space-y-6">
        {/* Header */}
        <div>
          <h2 className="text-2xl font-bold text-foreground">Settings</h2>
          <p className="text-sm text-muted-foreground mt-1">Manage your account and preferences</p>
        </div>

        {/* Account Information */}
        <Card className="border-2 border-accent/20">
          <CardHeader>
            <CardTitle>Account Information</CardTitle>
            <CardDescription>Your profile details</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div>
              <p className="text-xs font-medium text-muted-foreground mb-1">Name</p>
              <p className="text-foreground">{user?.name || "Not set"}</p>
            </div>
            <div>
              <p className="text-xs font-medium text-muted-foreground mb-1">Email</p>
              <p className="text-foreground">{user?.email || "Not set"}</p>
            </div>
            <div>
              <p className="text-xs font-medium text-muted-foreground mb-1">Role</p>
              <Badge className="bg-accent/20 text-accent border-accent/50">
                {user?.role === "admin" ? "Administrator" : "User"}
              </Badge>
            </div>
            <div>
              <p className="text-xs font-medium text-muted-foreground mb-1">User ID</p>
              <p className="text-xs font-mono text-muted-foreground">{user?.id}</p>
            </div>
          </CardContent>
        </Card>

        {/* Analysis Preferences */}
        <Card>
          <CardHeader>
            <CardTitle>Analysis Preferences</CardTitle>
            <CardDescription>Configure how analyses are performed</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <p className="text-sm font-medium text-foreground">Default Analysis Type</p>
              <p className="text-sm text-muted-foreground">Comprehensive analysis with all components</p>
            </div>
            <div className="space-y-2">
              <p className="text-sm font-medium text-foreground">Auto-save Analyses</p>
              <p className="text-sm text-muted-foreground">All analyses are automatically saved to your history</p>
            </div>
          </CardContent>
        </Card>

        {/* Display Preferences */}
        <Card>
          <CardHeader>
            <CardTitle>Display Preferences</CardTitle>
            <CardDescription>Customize your experience</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <p className="text-sm font-medium text-foreground">Theme</p>
              <p className="text-sm text-muted-foreground">Dark theme (optimized for extended analysis sessions)</p>
            </div>
            <div className="space-y-2">
              <p className="text-sm font-medium text-foreground">Color Scheme</p>
              <p className="text-sm text-muted-foreground">Purple and violet accents for Aletheia brand identity</p>
            </div>
          </CardContent>
        </Card>

        {/* About */}
        <Card>
          <CardHeader>
            <CardTitle>About Aletheia</CardTitle>
            <CardDescription>Information about this application</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div>
              <p className="text-sm font-medium text-foreground mb-2">Aletheia Engine v2.0</p>
              <p className="text-sm text-muted-foreground">
                A comprehensive truth analysis and discernment system featuring multi-dimensional scoring,
                advanced pattern recognition, temporal coherence tracking, and professional reporting.
              </p>
            </div>
            <div className="pt-4 border-t border-border">
              <p className="text-xs text-muted-foreground">
                Aletheia - The Un-concealment of Truth
              </p>
              <p className="text-xs text-muted-foreground mt-1">
                Chicka chicka orange. 🍊
              </p>
            </div>
          </CardContent>
        </Card>

        {/* Data & Privacy */}
        <Card>
          <CardHeader>
            <CardTitle>Data & Privacy</CardTitle>
            <CardDescription>Your data is secure and private</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <p className="text-sm font-medium text-foreground">Data Storage</p>
              <p className="text-sm text-muted-foreground">
                All your analyses and reports are stored securely and only accessible to you.
              </p>
            </div>
            <div className="space-y-2">
              <p className="text-sm font-medium text-foreground">Export Your Data</p>
              <Button variant="outline" size="sm" disabled>
                Export Data (Coming Soon)
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </AletheiaLayout>
  );
}
