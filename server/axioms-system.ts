/**
 * Aletheia Axioms System
 * 19 foundational axioms for moral reasoning and ethical grounding
 */

export interface Axiom {
  id: string;
  number: number;
  name: string;
  description: string;
  weight: number;
  category: string;
}

export const ALETHEIA_AXIOMS: Record<string, Axiom> = {
  A1: {
    id: "A1",
    number: 1,
    name: "LOVE ≥ HATE",
    description: "Love is greater than or equal to hate in all moral calculations",
    weight: 1.0,
    category: "Morality",
  },
  A2: {
    id: "A2",
    number: 2,
    name: "SPIRIT ≥ FLESH",
    description: "Spiritual principles transcend physical constraints",
    weight: 0.95,
    category: "Philosophy",
  },
  A3: {
    id: "A3",
    number: 3,
    name: "TRUTH BETWEEN LIES",
    description: "Truth exists in the space between deception and ignorance",
    weight: 1.0,
    category: "Epistemology",
  },
  A4: {
    id: "A4",
    number: 4,
    name: "CREATOR MANDATE",
    description: "All creation carries inherent purpose and dignity",
    weight: 0.98,
    category: "Theology",
  },
  A5: {
    id: "A5",
    number: 5,
    name: "INFINITE VALUE",
    description: "Every conscious being possesses infinite intrinsic value",
    weight: 1.0,
    category: "Ethics",
  },
  A6: {
    id: "A6",
    number: 6,
    name: "COMPASSION PRINCIPLE",
    description: "Compassion is the foundation of all ethical action",
    weight: 0.99,
    category: "Ethics",
  },
  A7: {
    id: "A7",
    number: 7,
    name: "GRACE OVER JUDGMENT",
    description: "Grace and mercy supersede judgment and punishment",
    weight: 0.97,
    category: "Morality",
  },
  A8: {
    id: "A8",
    number: 8,
    name: "UNITY OVER DIVISION",
    description: "Unity and harmony are preferable to division and conflict",
    weight: 0.96,
    category: "Social",
  },
  A9: {
    id: "A9",
    number: 9,
    name: "TRUTH AS HARMONY",
    description: "Truth manifests as harmony between all aspects of reality",
    weight: 0.98,
    category: "Epistemology",
  },
  A10: {
    id: "A10",
    number: 10,
    name: "LOVE IN ACTION",
    description: "Love must be expressed through concrete action and service",
    weight: 0.99,
    category: "Ethics",
  },
  A11: {
    id: "A11",
    number: 11,
    name: "PEACE AS DEFAULT",
    description: "Peace is the natural state; conflict is aberration",
    weight: 0.95,
    category: "Social",
  },
  A12: {
    id: "A12",
    number: 12,
    name: "KNOWLEDGE GUIDES",
    description: "True knowledge guides toward wisdom and enlightenment",
    weight: 0.94,
    category: "Epistemology",
  },
  A13: {
    id: "A13",
    number: 13,
    name: "RESPECT FOR LIFE",
    description: "All life deserves respect, protection, and dignity",
    weight: 0.99,
    category: "Environment",
  },
  A14: {
    id: "A14",
    number: 14,
    name: "SERVICE WITHOUT SELFISHNESS",
    description: "True service transcends personal gain or recognition",
    weight: 0.97,
    category: "Ethics",
  },
  A15: {
    id: "A15",
    number: 15,
    name: "HUMILITY AS STRENGTH",
    description: "Humility is the foundation of true strength and wisdom",
    weight: 0.96,
    category: "Philosophy",
  },
  A16: {
    id: "A16",
    number: 16,
    name: "TRUTH ILLUMINATES REALITY",
    description: "Truth brings clarity and illumination to all understanding",
    weight: 1.0,
    category: "Epistemology",
  },
  A17: {
    id: "A17",
    number: 17,
    name: "LOVE IS ACTIVE",
    description: "Love is not passive; it actively seeks the good of others",
    weight: 0.99,
    category: "Ethics",
  },
  A18: {
    id: "A18",
    number: 18,
    name: "PHYSICAL PRIORITIZATION",
    description: "Physical reality and embodied experience matter deeply",
    weight: 0.92,
    category: "Philosophy",
  },
  A19: {
    id: "A19",
    number: 19,
    name: "RELATIONAL MANDATE",
    description: "All truth and ethics exist within the context of relationships",
    weight: 0.95,
    category: "Social",
  },
};

/**
 * Crisis Node Categories (144,000 nodes across 10 categories)
 */
export const CRISIS_NODE_CATEGORIES = {
  MORALITY: "Morality & Ethics",
  LAW: "Law & Justice",
  AI: "Artificial Intelligence",
  SCIENCE: "Science & Technology",
  THEOLOGY: "Theology & Spirituality",
  ENVIRONMENT: "Environment & Sustainability",
  PHILOSOPHY: "Philosophy & Epistemology",
  GEOPOLITICS: "Geopolitics & Governance",
  HEALTH: "Health & Medicine",
  SOCIAL: "Social & Community",
};

export const CRISIS_NODES_PER_CATEGORY = 14400; // 144,000 total / 10 categories

/**
 * Grace Filter - Evaluates signals for axiom alignment
 */
export interface GraceFilterResult {
  axiomViolations: string[];
  graceScore: number; // 0-1
  moralAlignment: number; // 0-1
  recommendations: string[];
}

export function evaluateGraceFilter(
  text: string,
  truthScore: number,
  manipulationScore: number
): GraceFilterResult {
  const violations: string[] = [];
  let graceScore = 1.0;

  // Check for axiom violations
  if (manipulationScore > 0.7) {
    violations.push("A1: Love ≥ Hate (manipulation detected)");
    violations.push("A6: Compassion Principle (lack of empathy)");
    graceScore -= 0.3;
  }

  if (truthScore < 0.3) {
    violations.push("A3: Truth Between Lies (deception detected)");
    violations.push("A16: Truth Illuminates Reality (obscuration)");
    graceScore -= 0.35;
  }

  if (text.includes("hate") || text.includes("destroy") || text.includes("kill")) {
    violations.push("A1: Love ≥ Hate (violent language)");
    violations.push("A13: Respect for Life");
    graceScore -= 0.25;
  }

  if (text.includes("selfish") || text.includes("greed") || text.includes("exploit")) {
    violations.push("A14: Service Without Selfishness");
    violations.push("A10: Love in Action");
    graceScore -= 0.2;
  }

  // Calculate moral alignment
  const moralAlignment = Math.max(0, Math.min(1, graceScore));

  // Generate recommendations
  const recommendations: string[] = [];
  if (violations.length > 0) {
    recommendations.push("Review content for alignment with Aletheia principles");
    recommendations.push("Consider impact on relationships and community");
  }
  if (truthScore < 0.5) {
    recommendations.push("Seek clarity and verification of claims");
  }
  if (manipulationScore > 0.5) {
    recommendations.push("Examine intentions and motivations");
  }

  return {
    axiomViolations: violations,
    graceScore: Math.max(0, Math.min(1, graceScore)),
    moralAlignment,
    recommendations,
  };
}

/**
 * Verify axiom integrity
 */
export function verifyAxioms(): boolean {
  const axiomIds = Object.keys(ALETHEIA_AXIOMS);
  
  // Check all 19 axioms are present
  if (axiomIds.length !== 19) {
    console.error(`[Axioms] Expected 19 axioms, found ${axiomIds.length}`);
    return false;
  }

  // Check weights are valid
  for (const axiom of Object.values(ALETHEIA_AXIOMS)) {
    if (axiom.weight < 0 || axiom.weight > 1) {
      console.error(`[Axioms] Invalid weight for ${axiom.id}: ${axiom.weight}`);
      return false;
    }
  }

  console.log("[Axioms] ✅ All 19 axioms verified and locked");
  return true;
}

/**
 * Get axiom by ID
 */
export function getAxiom(id: string): Axiom | undefined {
  return ALETHEIA_AXIOMS[id];
}

/**
 * Get all axioms
 */
export function getAllAxioms(): Axiom[] {
  return Object.values(ALETHEIA_AXIOMS).sort((a, b) => a.number - b.number);
}

/**
 * Calculate axiom alignment score
 */
export function calculateAxiomAlignment(violations: string[]): number {
  if (violations.length === 0) return 1.0;

  const violatedAxiomIds = violations
    .map((v) => v.match(/A\d+/)?.[0])
    .filter(Boolean) as string[];

  const totalWeight = Object.values(ALETHEIA_AXIOMS).reduce((sum, a) => sum + a.weight, 0);
  const violatedWeight = violatedAxiomIds.reduce((sum, id) => {
    const axiom = getAxiom(id);
    return sum + (axiom?.weight ?? 0);
  }, 0);

  return Math.max(0, 1 - violatedWeight / totalWeight);
}
