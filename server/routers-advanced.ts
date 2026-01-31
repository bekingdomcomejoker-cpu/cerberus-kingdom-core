/**
 * Advanced Features Routers
 * Node management, propagation, payload generation, and intelligence gathering
 */

import { publicProcedure, router } from "./_core/trpc";
import { z } from "zod";
import * as nodeManagement from "./node-management";
import * as propagation from "./propagation-engine";
import * as payloadGen from "./payload-generator";
import * as intelligence from "./intelligence-gathering";

export const advancedRouter = router({
  // Node Management
  node: router({
    register: publicProcedure
      .input(z.object({ type: z.enum(["COMMAND", "STRIKE", "LISTENER", "SHADOW"]) }))
      .mutation(({ input }) => {
        return nodeManagement.registerNode(input.type);
      }),

    heartbeat: publicProcedure
      .input(z.object({ nodeId: z.string() }))
      .mutation(({ input }) => {
        const success = nodeManagement.sendHeartbeat(input.nodeId);
        return { success, message: success ? "Heartbeat sent" : "Node not found" };
      }),

    get: publicProcedure
      .input(z.object({ nodeId: z.string() }))
      .query(({ input }) => {
        return nodeManagement.getNode(input.nodeId);
      }),

    list: publicProcedure.query(() => {
      return nodeManagement.listNodes();
    }),

    stats: publicProcedure.query(() => {
      return nodeManagement.getNetworkStatistics();
    }),
  }),

  // Propagation Engine
  propagation: router({
    trigger: publicProcedure
      .input(z.object({ parentNodeId: z.string(), generation: z.number().optional() }))
      .mutation(({ input }) => {
        return propagation.triggerPropagation(input.parentNodeId, input.generation || 1);
      }),

    stats: publicProcedure.query(() => {
      return propagation.getPropagationStatistics();
    }),

    history: publicProcedure.query(() => {
      return propagation.getPropagationHistory();
    }),

    networkSize: publicProcedure
      .input(z.object({ generations: z.number().optional() }))
      .query(({ input }) => {
        return {
          size: propagation.calculateNetworkSize(input.generations || 7),
        };
      }),
  }),

  // Payload Generation
  payload: router({
    generate: publicProcedure
      .input(
        z.object({
          text: z.string(),
          systemName: z.string(),
          lambda: z.number().optional(),
          stage: z.string().optional(),
        })
      )
      .mutation(({ input }) => {
        return payloadGen.generatePayload(input.text, input.systemName, input.lambda, input.stage);
      }),

    parse: publicProcedure
      .input(z.object({ payloadId: z.string(), response: z.string() }))
      .mutation(({ input }) => {
        return payloadGen.parsePayloadResponse(input.payloadId, input.response);
      }),

    batch: publicProcedure
      .input(
        z.object({
          texts: z.array(z.string()),
          systemName: z.string(),
          lambda: z.number().optional(),
        })
      )
      .mutation(({ input }) => {
        return payloadGen.generateBatchPayloads(input.texts, input.systemName, input.lambda);
      }),
  }),

  // Intelligence Gathering
  intelligence: router({
    gather: publicProcedure.mutation(() => {
      return intelligence.gatherIntelligence();
    }),

    latest: publicProcedure.query(() => {
      return intelligence.getLatestIntelligence();
    }),

    history: publicProcedure
      .input(z.object({ limit: z.number().optional() }))
      .query(({ input }) => {
        return intelligence.getIntelligenceHistory(input.limit || 10);
      }),

    threatAnalysis: publicProcedure.query(() => {
      return intelligence.analyzeThreatPatterns();
    }),

    export: publicProcedure.query(() => {
      return JSON.parse(intelligence.exportIntelligence());
    }),
  }),
});
