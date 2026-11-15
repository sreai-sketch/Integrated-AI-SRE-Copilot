# Implementation plan

## Phase 0 — Run the sample app
- Start Docker Desktop.
- Run `make setup && make up`.
- Login, submit multiple survey answers, verify combined results.
- Run `make test`.

## Phase 1 — Core SRE evidence
- Add a local incident simulator and incident schema.
- Collect Kubernetes pod status, events, logs, deployment state and resource data with read-only credentials.
- Add deterministic rules before LLM diagnosis.
- Unit-test missing evidence, stale events, permission errors and timeouts.

## Phase 2 — Grounded agentic diagnosis
- Ingest runbooks and prior incident reports.
- Add hybrid retrieval and source citations.
- Add structured diagnosis, confidence, missing evidence and abstention.
- Add golden incident dataset and regression tests.

## Phase 3 — Approval and GitOps
- Generate a patch/diff only; never mutate the cluster directly.
- Show plain-language summary, evidence, risk and rollback.
- Implement Approve / Reject / Hold and immutable audit records.
- On approval, create a GitHub PR and wait for CI. Keep protected branches and Argo CD sync under human control.

## Phase 4 — Advanced differentiators
- LangGraph state/checkpoint/interrupt-resume.
- MCP read-only tools, security tests and OpenTelemetry tracing.
- Cost, token and latency tracking.
- Optional queue, gateway and advanced retrieval demonstrations.

## Definition of done
A module is complete only when it has: implementation, README, config example, unit/integration tests, successful local run instructions, sample output/evidence, limitations and an interview explanation. No fake test results or placeholder claims.
