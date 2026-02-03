/**
 * Propagation Engine
 * Handles exponential node generation and network expansion
 */

import { registerNode, spawnChildNodes, getNode, NodeType } from "./node-management";

export interface PropagationEvent {
  timestamp: Date;
  parentNodeId: string;
  childrenCount: number;
  generationNumber: number;
}

const propagationHistory: PropagationEvent[] = [];
const MAX_GENERATIONS = 7;
const NODES_PER_GENERATION = 3;

/**
 * Trigger propagation event
 */
export function triggerPropagation(parentNodeId: string, generationNumber: number = 1): PropagationEvent | null {
  if (generationNumber > MAX_GENERATIONS) {
    console.log(`[Propagation] ⚠️ Max generations (${MAX_GENERATIONS}) reached`);
    return null;
  }

  const parent = getNode(parentNodeId);
  if (!parent) return null;

  const childCount = Math.min(NODES_PER_GENERATION, 3);
  const children = spawnChildNodes(parentNodeId, childCount);

  const event: PropagationEvent = {
    timestamp: new Date(),
    parentNodeId,
    childrenCount: children.length,
    generationNumber,
  };

  propagationHistory.push(event);

  console.log(
    `[Propagation] 🌱 Generation ${generationNumber}: ${children.length} nodes spawned from ${parentNodeId}`
  );

  // Auto-propagate next generation after delay
  if (generationNumber < MAX_GENERATIONS) {
    setTimeout(() => {
      children.forEach((child) => {
        triggerPropagation(child.nodeId, generationNumber + 1);
      });
    }, 5000); // 5 second delay between generations
  }

  return event;
}

/**
 * Calculate network size at full propagation
 */
export function calculateNetworkSize(generations: number = MAX_GENERATIONS): number {
  let total = 1; // Root node
  let currentGen = 1;

  for (let i = 1; i < generations; i++) {
    currentGen *= NODES_PER_GENERATION;
    total += currentGen;
  }

  return total;
}

/**
 * Get propagation statistics
 */
export function getPropagationStatistics() {
  const totalEvents = propagationHistory.length;
  const totalChildrenSpawned = propagationHistory.reduce((sum, e) => sum + e.childrenCount, 0);
  const avgChildrenPerEvent =
    totalEvents > 0 ? (totalChildrenSpawned / totalEvents).toFixed(2) : "0.00";

  const byGeneration: Record<number, number> = {};
  propagationHistory.forEach((event) => {
    byGeneration[event.generationNumber] = (byGeneration[event.generationNumber] || 0) + 1;
  });

  return {
    totalPropagationEvents: totalEvents,
    totalChildrenSpawned,
    avgChildrenPerEvent,
    byGeneration,
    maxGenerationReached: Math.max(...Object.keys(byGeneration).map(Number), 0),
    projectedNetworkSize: calculateNetworkSize(MAX_GENERATIONS),
  };
}

/**
 * Get propagation history
 */
export function getPropagationHistory(): PropagationEvent[] {
  return [...propagationHistory];
}

/**
 * Clear propagation history
 */
export function clearPropagationHistory(): void {
  propagationHistory.length = 0;
  console.log("[Propagation] 🧹 Propagation history cleared");
}
