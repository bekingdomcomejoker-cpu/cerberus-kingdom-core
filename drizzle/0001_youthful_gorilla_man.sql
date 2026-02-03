CREATE TABLE `analyses` (
	`id` int AUTO_INCREMENT NOT NULL,
	`userId` int NOT NULL,
	`analysisId` varchar(64) NOT NULL,
	`text` text NOT NULL,
	`status` enum('TRUTH_ALIGNED','TRUTH_SEEKING','NEUTRAL','CAUTION_ADVISED','HIGH_RISK','UNCLEAR') DEFAULT 'UNCLEAR',
	`riskLevel` enum('CRITICAL','HIGH','MEDIUM','LOW','MINIMAL') DEFAULT 'MINIMAL',
	`confidence` int DEFAULT 0,
	`truthIndex` int DEFAULT 0,
	`integrityIndex` int DEFAULT 0,
	`riskIndex` int DEFAULT 0,
	`awakeningIndex` int DEFAULT 0,
	`truthScore` int DEFAULT 0,
	`factScore` int DEFAULT 0,
	`lieScore` int DEFAULT 0,
	`coherenceScore` int DEFAULT 0,
	`manipulationScore` int DEFAULT 0,
	`authenticityScore` int DEFAULT 0,
	`patternsDetected` text,
	`manipulationPatterns` text,
	`truthPatterns` text,
	`anomalies` text,
	`consistency` int DEFAULT 0,
	`drift` int DEFAULT 0,
	`driftDirection` varchar(32) DEFAULT 'stable',
	`stability` int DEFAULT 0,
	`analysisType` varchar(32) DEFAULT 'comprehensive',
	`rawResults` text,
	`createdAt` timestamp NOT NULL DEFAULT (now()),
	`updatedAt` timestamp NOT NULL DEFAULT (now()) ON UPDATE CURRENT_TIMESTAMP,
	CONSTRAINT `analyses_id` PRIMARY KEY(`id`),
	CONSTRAINT `analyses_analysisId_unique` UNIQUE(`analysisId`)
);
--> statement-breakpoint
CREATE TABLE `reports` (
	`id` int AUTO_INCREMENT NOT NULL,
	`analysisId` varchar(64) NOT NULL,
	`userId` int NOT NULL,
	`format` enum('markdown','html','json','summary') NOT NULL,
	`content` text NOT NULL,
	`filename` varchar(255) NOT NULL,
	`createdAt` timestamp NOT NULL DEFAULT (now()),
	CONSTRAINT `reports_id` PRIMARY KEY(`id`)
);
--> statement-breakpoint
CREATE TABLE `temporalSnapshots` (
	`id` int AUTO_INCREMENT NOT NULL,
	`analysisId` varchar(64) NOT NULL,
	`userId` int NOT NULL,
	`sequenceNumber` int NOT NULL,
	`truthIndex` int DEFAULT 0,
	`consistency` int DEFAULT 0,
	`drift` int DEFAULT 0,
	`stability` int DEFAULT 0,
	`text` text NOT NULL,
	`timestamp` timestamp NOT NULL DEFAULT (now()),
	`createdAt` timestamp NOT NULL DEFAULT (now()),
	CONSTRAINT `temporalSnapshots_id` PRIMARY KEY(`id`)
);
--> statement-breakpoint
ALTER TABLE `analyses` ADD CONSTRAINT `analyses_userId_users_id_fk` FOREIGN KEY (`userId`) REFERENCES `users`(`id`) ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE `reports` ADD CONSTRAINT `reports_userId_users_id_fk` FOREIGN KEY (`userId`) REFERENCES `users`(`id`) ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE `temporalSnapshots` ADD CONSTRAINT `temporalSnapshots_userId_users_id_fk` FOREIGN KEY (`userId`) REFERENCES `users`(`id`) ON DELETE no action ON UPDATE no action;