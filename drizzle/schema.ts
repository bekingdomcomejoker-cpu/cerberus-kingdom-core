import { int, mysqlEnum, mysqlTable, text, timestamp, varchar } from "drizzle-orm/mysql-core";

/**
 * Core user table backing auth flow.
 * Extend this file with additional tables as your product grows.
 * Columns use camelCase to match both database fields and generated types.
 */
export const users = mysqlTable("users", {
  /**
   * Surrogate primary key. Auto-incremented numeric value managed by the database.
   * Use this for relations between tables.
   */
  id: int("id").autoincrement().primaryKey(),
  /** Manus OAuth identifier (openId) returned from the OAuth callback. Unique per user. */
  openId: varchar("openId", { length: 64 }).notNull().unique(),
  name: text("name"),
  email: varchar("email", { length: 320 }),
  loginMethod: varchar("loginMethod", { length: 64 }),
  role: mysqlEnum("role", ["user", "admin"]).default("user").notNull(),
  createdAt: timestamp("createdAt").defaultNow().notNull(),
  updatedAt: timestamp("updatedAt").defaultNow().onUpdateNow().notNull(),
  lastSignedIn: timestamp("lastSignedIn").defaultNow().notNull(),
});

export type User = typeof users.$inferSelect;
export type InsertUser = typeof users.$inferInsert;

/**
 * Analysis results table storing comprehensive truth analysis data
 */
export const analyses = mysqlTable("analyses", {
  id: int("id").autoincrement().primaryKey(),
  userId: int("userId").notNull().references(() => users.id),
  analysisId: varchar("analysisId", { length: 64 }).notNull().unique(),
  text: text("text").notNull(),
  status: mysqlEnum("status", ["TRUTH_ALIGNED", "TRUTH_SEEKING", "NEUTRAL", "CAUTION_ADVISED", "HIGH_RISK", "UNCLEAR"]).default("UNCLEAR"),
  riskLevel: mysqlEnum("riskLevel", ["CRITICAL", "HIGH", "MEDIUM", "LOW", "MINIMAL"]).default("MINIMAL"),
  confidence: int("confidence").default(0),
  truthIndex: int("truthIndex").default(0),
  integrityIndex: int("integrityIndex").default(0),
  riskIndex: int("riskIndex").default(0),
  awakeningIndex: int("awakeningIndex").default(0),
  truthScore: int("truthScore").default(0),
  factScore: int("factScore").default(0),
  lieScore: int("lieScore").default(0),
  coherenceScore: int("coherenceScore").default(0),
  manipulationScore: int("manipulationScore").default(0),
  authenticityScore: int("authenticityScore").default(0),
  patternsDetected: text("patternsDetected"),
  manipulationPatterns: text("manipulationPatterns"),
  truthPatterns: text("truthPatterns"),
  anomalies: text("anomalies"),
  consistency: int("consistency").default(0),
  drift: int("drift").default(0),
  driftDirection: varchar("driftDirection", { length: 32 }).default("stable"),
  stability: int("stability").default(0),
  analysisType: varchar("analysisType", { length: 32 }).default("comprehensive"),
  rawResults: text("rawResults"),
  createdAt: timestamp("createdAt").defaultNow().notNull(),
  updatedAt: timestamp("updatedAt").defaultNow().onUpdateNow().notNull(),
});

export type Analysis = typeof analyses.$inferSelect;
export type InsertAnalysis = typeof analyses.$inferInsert;

/**
 * Temporal snapshots for tracking analysis evolution over time
 */
export const temporalSnapshots = mysqlTable("temporalSnapshots", {
  id: int("id").autoincrement().primaryKey(),
  analysisId: varchar("analysisId", { length: 64 }).notNull(),
  userId: int("userId").notNull().references(() => users.id),
  sequenceNumber: int("sequenceNumber").notNull(),
  truthIndex: int("truthIndex").default(0),
  consistency: int("consistency").default(0),
  drift: int("drift").default(0),
  stability: int("stability").default(0),
  text: text("text").notNull(),
  timestamp: timestamp("timestamp").defaultNow().notNull(),
  createdAt: timestamp("createdAt").defaultNow().notNull(),
});

export type TemporalSnapshot = typeof temporalSnapshots.$inferSelect;
export type InsertTemporalSnapshot = typeof temporalSnapshots.$inferInsert;

/**
 * Generated reports for export
 */
export const reports = mysqlTable("reports", {
  id: int("id").autoincrement().primaryKey(),
  analysisId: varchar("analysisId", { length: 64 }).notNull(),
  userId: int("userId").notNull().references(() => users.id),
  format: mysqlEnum("format", ["markdown", "html", "json", "summary"]).notNull(),
  content: text("content").notNull(),
  filename: varchar("filename", { length: 255 }).notNull(),
  createdAt: timestamp("createdAt").defaultNow().notNull(),
});

export type Report = typeof reports.$inferSelect;
export type InsertReport = typeof reports.$inferInsert;