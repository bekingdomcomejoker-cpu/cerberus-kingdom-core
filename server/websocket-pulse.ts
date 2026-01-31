/**
 * WebSocket Pulse - 1.67 second heartbeat for real-time federation status
 */

import { Server as HTTPServer } from "http";
import { Server as SocketIOServer, Socket } from "socket.io";
import { getUnifiedFederationStatus, getSimpleStatus } from "./federation-unified";

let io: SocketIOServer | null = null;
const PULSE_INTERVAL = 1670; // 1.67 seconds in milliseconds
let pulseTimer: NodeJS.Timeout | null = null;

/**
 * Initialize WebSocket server
 */
export function initializeWebSocketPulse(httpServer: HTTPServer): SocketIOServer {
  io = new SocketIOServer(httpServer, {
    cors: {
      origin: "*",
      methods: ["GET", "POST"],
    },
  });

  io.on("connection", (socket: Socket) => {
    console.log(`[Pulse] Client connected: ${socket.id}`);

    // Send initial status
    socket.emit("federation:status", getUnifiedFederationStatus());

    // Handle client events
    socket.on("disconnect", () => {
      console.log(`[Pulse] Client disconnected: ${socket.id}`);
    });

    socket.on("pulse:request", () => {
      socket.emit("federation:status", getUnifiedFederationStatus());
    });
  });

  // Start pulse broadcast
  startPulseBroadcast();

  console.log("[Pulse] ✅ WebSocket Pulse initialized - 1.67 Hz heartbeat active");
  return io;
}

/**
 * Start broadcasting pulse to all connected clients
 */
function startPulseBroadcast(): void {
  if (pulseTimer) clearInterval(pulseTimer);

  pulseTimer = setInterval(() => {
    if (io) {
      const status = getUnifiedFederationStatus();
      io.emit("federation:pulse", {
        timestamp: status.timestamp,
        resonance: status.covenant.resonance,
        alignment: status.covenant.alignment,
        unification: status.metrics.unificationScore,
        status: status.metrics.operationalStatus,
      });
    }
  }, PULSE_INTERVAL);
}

/**
 * Stop pulse broadcast
 */
export function stopPulseBroadcast(): void {
  if (pulseTimer) {
    clearInterval(pulseTimer);
    pulseTimer = null;
  }
}

/**
 * Broadcast message to all clients
 */
export function broadcastToClients(event: string, data: any): void {
  if (io) {
    io.emit(event, data);
  }
}

/**
 * Get connected client count
 */
export function getConnectedClientCount(): number {
  return io?.engine.clientsCount || 0;
}
