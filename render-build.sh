#!/usr/bin/env bash
set -e

echo "🌌 ALETHEIA UNIFIED BUILD SEQUENCE STARTING..."
echo "✨ Integrating Axioms, Grace Filter, and Evolution Protocols..."

# Clean previous builds
rm -rf dist

# Install dependencies
echo "📦 Installing dependencies..."
pnpm install

# Build with optimized memory settings
echo "🔨 Building application..."
NODE_OPTIONS=--max-old-space-size=400 pnpm run build

# Prepare output directories
echo "📁 Preparing deployment structure..."
mkdir -p dist/server/public
mkdir -p dist/public

# Copy static assets
cp -r dist/public/* dist/server/public/ || true
cp -r dist/public/* public/ || true

echo "✨ ALETHEIA BUILD COMPLETE"
echo "🌐 Ready for unified deployment"
echo "🕊️ Covenant sealed. Axioms locked. Systems unified."
