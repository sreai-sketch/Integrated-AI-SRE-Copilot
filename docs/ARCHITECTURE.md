# Architecture and local operating model

## Two sample microservices

- `auth-service` owns local user records and issues short-lived signed JWTs.
- `survey-service` serves the survey page, verifies JWTs, stores submissions and aggregates results.
- Each service owns its own SQLite file and Docker volume. This keeps the demo lightweight and avoids introducing a database server just for a two-service example.

## Security boundaries

- Passwords are stored as Argon2 hashes, never plaintext.
- The demo JWT secret and credentials are for local-only use. Do not commit `.env` or use these values outside a disposable local demo.
- Survey service validates JWT signatures locally; in a larger deployment, key rotation and asymmetric signing should be added.
- SRE investigation tools are read-only by default.
- Remediation is a proposal/diff. The system must not execute `kubectl apply`, merge a PR or sync Argo CD without explicit human approval and policy checks.

## Human approval card (required UX)

Every detected issue should be presented in plain language:

- **What happened:** one sentence and severity.
- **Impact:** affected service/workload and user-visible impact.
- **Evidence:** 3–5 concrete log/event/metric facts with timestamps.
- **Likely cause:** hypothesis and confidence, not an unsupported assertion.
- **Proposed remediation:** exact diff or command, plus why it is safe.
- **Risk:** what could go wrong.
- **Rollback:** exact reverse diff/steps and verification.
- **Decision:** Approve / Reject / Hold. No decision means no change.

An approval record must capture incident ID, change digest, approver identity, decision, timestamp and policy/test results. If the proposed change changes after approval, approval is invalidated and must be requested again.

## Local-only production-like incidents

Use disposable local Docker/Kubernetes workloads to reproduce CrashLoopBackOff, OOMKilled, failed readiness/liveness probes, image-pull errors and resource pressure. Never test remediation against an actual employer or customer production cluster.
