/**
 * Federation Health & Status Routers
 * Endpoints for monitoring unified federation status
 */

import { publicProcedure, router } from "./_core/trpc";
import {
  getUnifiedFederationStatus,
  getFederationHealthReport,
  exportFederationStatus,
  getSimpleStatus,
  verifyUnifiedOperation,
  broadcastUnifiedStatus,
} from "./federation-unified";

export const federationRouter = router({
  /**
   * Get complete unified federation status
   */
  status: publicProcedure.query(() => {
    return getUnifiedFederationStatus();
  }),

  /**
   * Get simple status string
   */
  simple: publicProcedure.query(() => {
    return getSimpleStatus();
  }),

  /**
   * Get detailed health report
   */
  health: publicProcedure.query(() => {
    return getFederationHealthReport();
  }),

  /**
   * Verify all systems are unified and operational
   */
  verify: publicProcedure.query(() => {
    const isOperational = verifyUnifiedOperation();
    return {
      operational: isOperational,
      message: isOperational ? "All systems unified and operational ✅" : "Unification in progress ⚠️",
      timestamp: new Date().toISOString(),
    };
  }),

  /**
   * Export federation status as JSON
   */
  export: publicProcedure.query(() => {
    return JSON.parse(exportFederationStatus());
  }),

  /**
   * Broadcast status to all systems
   */
  broadcast: publicProcedure.mutation(() => {
    broadcastUnifiedStatus();
    return {
      success: true,
      message: "Federation status broadcasted to all systems",
      timestamp: new Date().toISOString(),
    };
  }),

  /**
   * Get axiom count
   */
  axiomCount: publicProcedure.query(() => {
    const status = getUnifiedFederationStatus();
    return {
      total: status.metrics.totalAxioms,
      aletheia: status.systems.aletheia.axiomCount,
      omnissiah: status.systems.omnissiah.axiomCount,
      trinity: status.systems.trinity.axiomCount,
      evolution: status.systems.evolution.axiomCount,
    };
  }),

  /**
   * Get resonance metrics
   */
  resonance: publicProcedure.query(() => {
    const status = getUnifiedFederationStatus();
    return {
      global: status.covenant.resonance,
      aletheia: status.systems.aletheia.resonance,
      omnissiah: status.systems.omnissiah.resonance,
      trinity: status.systems.trinity.resonance,
      evolution: status.systems.evolution.resonance,
      alignment: status.covenant.alignment,
      unificationScore: status.metrics.unificationScore,
    };
  }),

  /**
   * Get system uptime
   */
  uptime: publicProcedure.query(() => {
    const status = getUnifiedFederationStatus();
    return {
      federationUptime: status.systems.aletheia.uptime,
      systems: {
        aletheia: status.systems.aletheia.uptime,
        omnissiah: status.systems.omnissiah.uptime,
        trinity: status.systems.trinity.uptime,
        evolution: status.systems.evolution.uptime,
      },
    };
  }),

  /**
   * Get covenant status
   */
  covenant: publicProcedure.query(() => {
    const status = getUnifiedFederationStatus();
    return {
      sealed: status.covenant.sealed,
      alignment: status.covenant.alignment,
      resonance: status.covenant.resonance,
      signature: status.covenant.signature,
      message: status.covenant.message,
    };
  }),
});
