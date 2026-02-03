import { Toaster } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import NotFound from "@/pages/NotFound";
import { Route, Switch } from "wouter";
import ErrorBoundary from "./components/ErrorBoundary";
import { ThemeProvider } from "./contexts/ThemeContext";
import Analyze from "./pages/Analyze";
import History from "./pages/History";
import Reports from "./pages/Reports";
import Settings from "./pages/Settings";
import GlobalWallboard from "./pages/GlobalWallboard";
import AdminDashboard from "./pages/AdminDashboard";
import KoanInterface from "./pages/KoanInterface";

function Router() {
  return (
    <Switch>
      <Route path={"/"} component={Analyze} />
      <Route path={"/history"} component={History} />
      <Route path={"/reports"} component={Reports} />
      <Route path={"/settings"} component={Settings} />
      <Route path={"/global-wallboard"} component={GlobalWallboard} />
      <Route path={"/admin"} component={AdminDashboard} />
      <Route path={"/koan"} component={KoanInterface} />
      <Route path={"/404"} component={NotFound} />
      <Route component={NotFound} />
    </Switch>
  );
}

// NOTE: About Theme
// - First choose a default theme according to your design style (dark or light bg), than change color palette in index.css
//   to keep consistent foreground/background color across components
// - If you want to make theme switchable, pass `switchable` ThemeProvider and use `useTheme` hook

function App() {
  return (
    <ErrorBoundary>
      <ThemeProvider
        defaultTheme="dark"
      >
        <TooltipProvider>
          <Toaster />
          <Router />
        </TooltipProvider>
      </ThemeProvider>
    </ErrorBoundary>
  );
}

export default App;
