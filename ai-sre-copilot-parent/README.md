# AI SRE Copilot — Parent Repository

A local-first, modular learning and capstone repository. The goal is to build one credible, demonstrable **AI SRE Copilot** while keeping curriculum modules isolated instead of mixing everything into one application.

## Project rules

1. **Local-first:** development and demos run on a Mac using Docker Compose. No Azure/GCP/AWS account is required for the default path.
2. **Human approval before action:** the copilot may investigate and propose a remediation, but must never apply a production change automatically. It explains the incident briefly, shows evidence, risk, proposed fix and rollback, then waits for Approve / Reject / Hold.
3. **Production-like, not real production:** incidents are reproduced in a local demo environment. Do not connect this starter to a real production cluster.
4. **Modular:** curriculum content is grouped into A (8 core), B (7 advanced), and C (4 specialized) modules. Each module has its own README and should be implemented/tested independently.
5. **No hidden setup:** use the root `Makefile`, `requirements-dev.txt`, Dockerfiles and Compose file. The only manual prerequisite is installing Docker Desktop (and Git) on the Mac; a repository cannot install or run its own container engine without that host prerequisite.

## Repository layout

```text
apps/
  auth-service/       # Login and JWT issuing microservice
  survey-service/    # Survey UI, submissions and combined results microservice
modules/
  A-core/             # 8 core capabilities
  B-advanced/         # 7 advanced capabilities
  C-specialized/      # 4 specialist capabilities
infra/                # Docker Compose and local demo infrastructure
docs/                 # Architecture, security and implementation guide
scripts/              # One-command setup, test and teardown
 tests/               # Cross-service smoke tests
```

## Quick start (Mac)

Prerequisites: macOS, Git, and Docker Desktop running. No Python installation is needed for the default Docker path.

```bash
git clone <your-parent-repo-url>
cd ai-sre-copilot-parent
make setup
make up
```

Open:
- Survey page: http://localhost:8081
- Auth API docs: http://localhost:8080/docs
- Survey API docs: http://localhost:8081/docs

Demo login is created only for local development: `demo@example.com` / `ChangeMe123!`. Change it before sharing or deploying anything. The app is a learning scaffold, not an internet-facing production identity system.

Useful commands:

```bash
make status
make logs
make test
make down
make clean       # removes local persisted demo data
```

## The 3-part module plan

See [docs/MODULE-MAP.md](docs/MODULE-MAP.md) for the exact mapping of all 19 original curriculum modules into A/B/C and which parts are full implementations, practical demonstrations or conceptual labs.

## Application behaviour

- Auth service registers/logs in users and issues signed JWTs.
- Survey service serves a small random survey page, accepts authenticated submissions and returns aggregate results across all participants.
- Survey records are persisted in a local SQLite database volume.
- These two services are the sample application that the SRE Copilot will monitor and investigate. They are deliberately lightweight.

## AI SRE Copilot target workflow

```text
Simulated alert / fault
  -> Incident classification
  -> Read-only Kubernetes / application evidence collection
  -> Runbook retrieval (RAG + hybrid search)
  -> Agent diagnosis with cited evidence and confidence
  -> Human-readable incident summary
  -> Proposed YAML/code remediation + risk + rollback plan
  -> Human decision: APPROVE / REJECT / HOLD
  -> If approved: create GitHub PR (never push directly to protected main)
  -> CI tests / policy checks
  -> Human-controlled GitOps sync
  -> Health verification and incident closure
```

**Approval is mandatory at the remediation boundary.** Reject and Hold must be supported. Approval authorizes a reviewed PR workflow, not an unrestricted direct cluster mutation. The default local scaffold does not yet implement the AI workflow; that is built module-by-module under `modules/A-core` and `modules/B-advanced`.

## Development approach

Implement in this order:
1. Make the two-service demo run and pass tests.
2. Add read-only incident/evidence collection and deterministic diagnosis.
3. Add RAG and evaluation before adding multi-agent complexity.
4. Add approval workflow and GitHub PR creation behind explicit permissions.
5. Add tracing, security controls and cost tracking.
6. Add specialist demos only when they strengthen a specific interview story.

Never claim a module is production-ready just because its README or demo exists. Update each module's status and attach test evidence.
