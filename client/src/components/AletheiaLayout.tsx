/**
 * Aletheia Dashboard Layout
 * Main layout with sidebar navigation and dark theme
 */

import { useAuth } from "@/_core/hooks/useAuth";
import { Button } from "@/components/ui/button";
import { Sidebar, SidebarContent, SidebarHeader, SidebarMenu, SidebarMenuButton, SidebarMenuItem, SidebarTrigger } from "@/components/ui/sidebar";
import { Activity, BarChart3, BookOpen, LogOut, Settings, Zap, Command } from "lucide-react";
import { ReactNode } from "react";
import { Link } from "wouter";

interface AletheiaLayoutProps {
  children: ReactNode;
  currentPage?: "analyze" | "history" | "reports" | "settings" | "wallboard" | "admin" | "koan";
}

export function AletheiaLayout({ children, currentPage }: AletheiaLayoutProps) {
  const { user, logout } = useAuth();

  const handleLogout = async () => {
    await logout();
  };

  return (
    <div className="flex h-screen bg-background text-foreground">
      {/* Sidebar */}
      <div className="w-64 bg-card border-r border-border flex flex-col">
        {/* Header */}
        <div className="p-6 border-b border-border">
          <h1 className="text-2xl font-bold text-accent">Aletheia</h1>
          <p className="text-xs text-muted-foreground mt-1">Truth Analysis Engine</p>
        </div>

        {/* Navigation Menu */}
        <nav className="flex-1 overflow-y-auto p-4">
          <div className="space-y-2">
            <Link href="/">
              <Button
                variant={currentPage === "analyze" ? "default" : "ghost"}
                className="w-full justify-start"
                asChild
              >
                <span>
                  <Activity className="mr-2 h-4 w-4" />
                  New Analysis
                </span>
              </Button>
            </Link>

            <Link href="/history">
              <Button
                variant={currentPage === "history" ? "default" : "ghost"}
                className="w-full justify-start"
                asChild
              >
                <span>
                  <BookOpen className="mr-2 h-4 w-4" />
                  History
                </span>
              </Button>
            </Link>

            <Link href="/reports">
              <Button
                variant={currentPage === "reports" ? "default" : "ghost"}
                className="w-full justify-start"
                asChild
              >
                <span>
                  <BarChart3 className="mr-2 h-4 w-4" />
                  Reports
                </span>
              </Button>
            </Link>

            <Link href="/settings">
              <Button
                variant={currentPage === "settings" ? "default" : "ghost"}
                className="w-full justify-start"
                asChild
              >
                <span>
                  <Settings className="mr-2 h-4 w-4" />
                  Settings
                </span>
              </Button>
            </Link>

            <Link href="/global-wallboard">
              <Button
                variant={currentPage === "wallboard" ? "default" : "ghost"}
                className="w-full justify-start"
                asChild
              >
                <span>
                  <BarChart3 className="mr-2 h-4 w-4" />
                  Global Wallboard
                </span>
              </Button>
            </Link>

            <Link href="/admin">
              <Button
                variant={currentPage === "admin" ? "default" : "ghost"}
                className="w-full justify-start"
                asChild
              >
                <span>
                  <Zap className="mr-2 h-4 w-4" />
                  Admin Dashboard
                </span>
              </Button>
            </Link>

            <Link href="/koan">
              <Button
                variant={currentPage === "koan" ? "default" : "ghost"}
                className="w-full justify-start"
                asChild
              >
                <span>
                  <Command className="mr-2 h-4 w-4" />
                  Koan Interface
                </span>
              </Button>
            </Link>
          </div>
        </nav>

        {/* User Section */}
        <div className="p-4 border-t border-border space-y-3">
          {user && (
            <div className="text-sm">
              <p className="text-muted-foreground">Logged in as</p>
              <p className="font-medium text-accent truncate">{user.name || user.email}</p>
            </div>
          )}
          <Button
            variant="outline"
            className="w-full justify-start"
            onClick={handleLogout}
          >
            <LogOut className="mr-2 h-4 w-4" />
            Logout
          </Button>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Top Bar */}
        <div className="h-16 bg-card border-b border-border flex items-center px-6">
          <h2 className="text-lg font-semibold text-foreground">
            {currentPage === "analyze" && "New Analysis"}
            {currentPage === "history" && "Analysis History"}
            {currentPage === "reports" && "Generated Reports"}
            {currentPage === "settings" && "Settings"}
            {currentPage === "wallboard" && "Global Wallboard"}
            {currentPage === "admin" && "Admin Dashboard"}
            {currentPage === "koan" && "Koan Interface"}
          </h2>
        </div>

        {/* Content Area */}
        <div className="flex-1 overflow-y-auto bg-background">
          <div className="p-6">
            {children}
          </div>
        </div>
      </div>
    </div>
  );
}
