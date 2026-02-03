import { eq, desc, asc } from "drizzle-orm";
import { drizzle } from "drizzle-orm/mysql2";
import { InsertUser, users, analyses, InsertAnalysis, temporalSnapshots, InsertTemporalSnapshot, reports, InsertReport } from "../drizzle/schema";
import { ENV } from './_core/env';

let _db: ReturnType<typeof drizzle> | null = null;

// Lazily create the drizzle instance so local tooling can run without a DB.
export async function getDb() {
  if (!_db && process.env.DATABASE_URL) {
    try {
      _db = drizzle(process.env.DATABASE_URL);
    } catch (error) {
      console.warn("[Database] Failed to connect:", error);
      _db = null;
    }
  }
  return _db;
}

export async function upsertUser(user: InsertUser): Promise<void> {
  if (!user.openId) {
    throw new Error("User openId is required for upsert");
  }

  const db = await getDb();
  if (!db) {
    console.warn("[Database] Cannot upsert user: database not available");
    return;
  }

  try {
    const values: InsertUser = {
      openId: user.openId,
    };
    const updateSet: Record<string, unknown> = {};

    const textFields = ["name", "email", "loginMethod"] as const;
    type TextField = (typeof textFields)[number];

    const assignNullable = (field: TextField) => {
      const value = user[field];
      if (value === undefined) return;
      const normalized = value ?? null;
      values[field] = normalized;
      updateSet[field] = normalized;
    };

    textFields.forEach(assignNullable);

    if (user.lastSignedIn !== undefined) {
      values.lastSignedIn = user.lastSignedIn;
      updateSet.lastSignedIn = user.lastSignedIn;
    }
    if (user.role !== undefined) {
      values.role = user.role;
      updateSet.role = user.role;
    } else if (user.openId === ENV.ownerOpenId) {
      values.role = 'admin';
      updateSet.role = 'admin';
    }

    if (!values.lastSignedIn) {
      values.lastSignedIn = new Date();
    }

    if (Object.keys(updateSet).length === 0) {
      updateSet.lastSignedIn = new Date();
    }

    await db.insert(users).values(values).onDuplicateKeyUpdate({
      set: updateSet,
    });
  } catch (error) {
    console.error("[Database] Failed to upsert user:", error);
    throw error;
  }
}

export async function getUserByOpenId(openId: string) {
  const db = await getDb();
  if (!db) {
    console.warn("[Database] Cannot get user: database not available");
    return undefined;
  }

  const result = await db.select().from(users).where(eq(users.openId, openId)).limit(1);

  return result.length > 0 ? result[0] : undefined;
}

// Analysis Queries
export async function createAnalysis(data: InsertAnalysis) {
  const db = await getDb();
  if (!db) throw new Error("Database not available");
  
  return await db.insert(analyses).values(data);
}

export async function getAnalysisByAnalysisId(analysisId: string) {
  const db = await getDb();
  if (!db) return undefined;
  
  const result = await db
    .select()
    .from(analyses)
    .where(eq(analyses.analysisId, analysisId))
    .limit(1);
  
  return result.length > 0 ? result[0] : undefined;
}

export async function getUserAnalyses(userId: number, limit = 50) {
  const db = await getDb();
  if (!db) return [];
  
  const result = await db
    .select()
    .from(analyses)
    .where(eq(analyses.userId, userId))
    .orderBy(desc(analyses.createdAt))
    .limit(limit);
  
  return result;
}

export async function getAnalysisById(id: number) {
  const db = await getDb();
  if (!db) return undefined;
  
  const result = await db
    .select()
    .from(analyses)
    .where(eq(analyses.id, id))
    .limit(1);
  
  return result.length > 0 ? result[0] : undefined;
}

// Temporal Snapshot Queries
export async function createTemporalSnapshot(data: InsertTemporalSnapshot) {
  const db = await getDb();
  if (!db) throw new Error("Database not available");
  
  return await db.insert(temporalSnapshots).values(data);
}

export async function getTemporalSnapshots(analysisId: string) {
  const db = await getDb();
  if (!db) return [];
  
  const result = await db
    .select()
    .from(temporalSnapshots)
    .where(eq(temporalSnapshots.analysisId, analysisId))
    .orderBy(asc(temporalSnapshots.sequenceNumber));
  
  return result;
}

// Report Queries
export async function createReport(data: InsertReport) {
  const db = await getDb();
  if (!db) throw new Error("Database not available");
  
  return await db.insert(reports).values(data);
}

export async function getReportsByAnalysisId(analysisId: string) {
  const db = await getDb();
  if (!db) return [];
  
  const result = await db
    .select()
    .from(reports)
    .where(eq(reports.analysisId, analysisId))
    .orderBy(desc(reports.createdAt));
  
  return result;
}

export async function getUserReports(userId: number, limit = 50) {
  const db = await getDb();
  if (!db) return [];
  
  const result = await db
    .select()
    .from(reports)
    .where(eq(reports.userId, userId))
    .orderBy(desc(reports.createdAt))
    .limit(limit);
  
  return result;
}
