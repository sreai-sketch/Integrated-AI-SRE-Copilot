#!/usr/bin/env bash
set -euo pipefail
if ! command -v docker >/dev/null 2>&1; then
  echo 'Docker CLI not found. Install Docker Desktop for Mac, start it, then rerun: make setup' >&2
  exit 1
fi
if ! docker info >/dev/null 2>&1; then
  echo 'Docker is installed but the Docker engine is not running. Start Docker Desktop, then rerun: make setup' >&2
  exit 1
fi
if ! command -v git >/dev/null 2>&1; then
  echo 'Git is required. Install the Xcode Command Line Tools: xcode-select --install' >&2
  exit 1
fi
[ -f .env ] || cp .env.example .env
printf '\nSetup complete. Run: make up\n'
