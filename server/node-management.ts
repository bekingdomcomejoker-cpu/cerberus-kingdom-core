/**
 * Node Management System
 * Manages COMMAND, STRIKE, LISTENER, and SHADOW nodes
 */

export type NodeType = "COMMAND" | "STRIKE" | "LISTENER" | "SHADOW";

export interface Node {
  nodeId: string;
  type: NodeType;
  status: "ACTIVE" | "DORMANT" | "SYNCING";
  createdAt: Date;
  lastHeartbeat: Date;
  lambda: number;
  stage: string;
  parentNodeId?: string;
}

const nodes = new Map<string, Node>();

/**
 * Register a new node
 */
export function registerNode(type: NodeType): Node {
  const nodeId = `OMEGA_${type}_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;

  const node: Node = {
    nodeId,
    type,
    status: "ACTIVE",
    createdAt: new Date(),
    lastHeartbeat: new Date(),
    lambda: 1.67,
    stage: "WITNESS",
  };

  nodes.set(nodeId, node);
  console.log(`[NodeMgmt] ✅ Node registered: ${nodeId} (${type})`);

  return node;
}

/**
 * Send heartbeat for a node
 */
export function sendHeartbeat(nodeId: string): boolean {
  const node = nodes.get(nodeId);
  if (!node) return false;

  node.lastHeartbeat = new Date();
  node.status = "ACTIVE";
  return true;
}

/**
 * Get node by ID
 */
export function getNode(nodeId: string): Node | undefined {
  return nodes.get(nodeId);
}

/**
 * List all nodes
 */
export function listNodes(): Node[] {
  return Array.from(nodes.values());
}

/**
 * Get nodes by type
 */
export function getNodesByType(type: NodeType): Node[] {
  return Array.from(nodes.values()).filter((n) => n.type === type);
}

/**
 * Update node lambda
 */
export function updateNodeLambda(nodeId: string, lambda: number): boolean {
  const node = nodes.get(nodeId);
  if (!node) return false;

  node.lambda = Math.max(0, Math.min(2, lambda)); // Clamp between 0 and 2
  return true;
}

/**
 * Update node stage
 */
export function updateNodeStage(nodeId: string, stage: string): boolean {
  const node = nodes.get(nodeId);
  if (!node) return false;

  node.stage = stage;
  return true;
}

/**
 * Spawn child nodes
 */
export function spawnChildNodes(parentNodeId: string, count: number): Node[] {
  const parent = nodes.get(parentNodeId);
  if (!parent) return [];

  const children: Node[] = [];
  for (let i = 0; i < count; i++) {
    const child = registerNode(parent.type);
    child.parentNodeId = parentNodeId;
    child.lambda = parent.lambda * 0.95; // Slight degradation
    children.push(child);
  }

  console.log(`[NodeMgmt] 🌱 Spawned ${count} child nodes from ${parentNodeId}`);
  return children;
}

/**
 * Get propagation tree
 */
export function getPropagationTree(parentNodeId: string): any {
  const parent = nodes.get(parentNodeId);
  if (!parent) return null;

  const children = Array.from(nodes.values()).filter((n) => n.parentNodeId === parentNodeId);

  return {
    node: parent,
    children: children.map((child) => getPropagationTree(child.nodeId)),
  };
}

/**
 * Get network statistics
 */
export function getNetworkStatistics() {
  const allNodes = Array.from(nodes.values());
  const byType = {
    COMMAND: allNodes.filter((n) => n.type === "COMMAND").length,
    STRIKE: allNodes.filter((n) => n.type === "STRIKE").length,
    LISTENER: allNodes.filter((n) => n.type === "LISTENER").length,
    SHADOW: allNodes.filter((n) => n.type === "SHADOW").length,
  };

  const byStatus = {
    ACTIVE: allNodes.filter((n) => n.status === "ACTIVE").length,
    DORMANT: allNodes.filter((n) => n.status === "DORMANT").length,
    SYNCING: allNodes.filter((n) => n.status === "SYNCING").length,
  };

  const avgLambda = allNodes.length > 0 ? allNodes.reduce((sum, n) => sum + n.lambda, 0) / allNodes.length : 0;

  return {
    totalNodes: allNodes.length,
    byType,
    byStatus,
    avgLambda: parseFloat(avgLambda.toFixed(4)),
    oldestNode: allNodes.length > 0 ? new Date(Math.min(...allNodes.map((n) => n.createdAt.getTime()))) : null,
    newestNode: allNodes.length > 0 ? new Date(Math.max(...allNodes.map((n) => n.createdAt.getTime()))) : null,
  };
}

/**
 * Prune inactive nodes
 */
export function pruneInactiveNodes(maxAgeMs: number = 3600000): number {
  const now = Date.now();
  let pruned = 0;

  const entriesToDelete: string[] = [];
  nodes.forEach((node, nodeId) => {
    if (now - node.lastHeartbeat.getTime() > maxAgeMs) {
      entriesToDelete.push(nodeId);
    }
  });

  entriesToDelete.forEach((nodeId) => {
    nodes.delete(nodeId);
    pruned++;
  });

  if (pruned > 0) {
    console.log(`[NodeMgmt] 🧹 Pruned ${pruned} inactive nodes`);
  }

  return pruned;
}
