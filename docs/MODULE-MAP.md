# Module Map — 19 original modules grouped into A / B / C

The original curriculum is preserved below and redistributed into three delivery tracks. The split is **8 core + 7 advanced + 4 specialist = 19 modules**. It is not 19 separate applications: modules extend the same parent repository and share the capstone.

## Module A — Core (8 modules): must implement end-to-end

| New ID | Original module | What we will actually build | Evidence for interviews |
|---|---|---|---|
| A1 | 1. Python for Generative AI | Typed Python package, API clients, JSON schemas, async calls, error handling and tests | Explain code structure, async, API contracts and tests |
| A2 | 2. Agentic AI Foundations & Reflex Agents | Incident-triggered reflex rules, ReAct-style investigate/act reasoning, tool calling, structured output and bounded memory | Show how an alert becomes a controlled investigation |
| A3 | 3. RAG-Powered Knowledge Agents | Runbook ingestion, chunking, embeddings, vector retrieval, citations, abstention and RAG evaluation | Demonstrate grounded answers and “insufficient evidence” behaviour |
| A4 | 4. Multi-Agent Systems | Separate investigator, RCA, remediation and verifier roles with explicit state and hand-offs | Explain why each agent exists and how tasks are delegated |
| A5 | 7. Hybrid Search & Retrieval | Keyword + semantic retrieval, metadata filters and ranked fusion; measure retrieval relevance | Compare keyword, vector and hybrid results |
| A6 | 8. Safe, Evaluated & Cost-Optimized Agents | Input/output validation, golden test cases, judge-assisted evaluation, token/cost/latency tracking and guardrails | Show evaluation report and cost/latency metrics |
| A7 | 11. LangGraph & Advanced Agent Orchestration | StateGraph, conditional routes, checkpointing, retry, interrupt/resume and human approval | Trace a workflow and resume after approval |
| A8 | 19. Enterprise AI SRE Copilot | Full incident-to-approved-remediation flow described in section below | End-to-end local demo, tests, PR and rollback evidence |

## Module B — Advanced (7 modules): implement the job-market differentiators

| New ID | Original module | Scope | Implementation level |
|---|---|---|---|
| B1 | 5. Conversational & Multimodal Agents | Conversation/context management, document/image understanding; speech-to-text and text-to-speech adapter interfaces | Image/document demo; voice as optional adapter, not a hard dependency |
| B2 | 6. Agent Communication Protocols | MCP server exposing read-only SRE tools; MCP client; A2A concepts and agent skills | MCP working demo; A2A/ADK protocol comparison and small interoperability lab |
| B3 | 12. LLMOps & AI Observability | OpenTelemetry traces/spans, agent traces, metrics, prompt/model version, token/latency/error dashboards | Working traces and local dashboard; LangSmith optional |
| B4 | 14. Agent Security & AI Governance | Prompt-injection tests, least privilege, secret handling, tool allowlists, audit log, policy gate and approval | Working security tests and audit trail |
| B5 | 15. Advanced RAG & Knowledge Engineering | Parent-child retrieval, query rewriting, reranking, context compression and GraphRAG fundamentals | Implement the most useful retrieval improvements; graph RAG as a small lab |
| B6 | 16. Distributed Agent Execution & Backend Engineering | Async tasks, queue/worker pattern, retries, idempotency, dead-letter handling and fault tolerance | Local Redis/worker demo only if it materially helps; no cloud dependency |
| B7 | 18. GenAI FinOps & Performance Optimization | Token budgets, caching, model routing policy, batch options, latency and quality/cost trade-offs | Working cost report and cache demo |

## Module C — Specialist (4 modules): targeted demonstrations, not expensive infrastructure

| New ID | Original module | Scope | Implementation level |
|---|---|---|---|
| C1 | 9. Fine-Tuning & Domain Adaptation | Dataset preparation, SFT/LoRA/PEFT concepts, evaluation and model-serving options | Small reproducible notebook or documented lab; do not train a costly large model |
| C2 | 10. Enterprise Multi-Agent System | Enterprise reference architecture, tenancy, policy boundaries, memory/state and scaling | Architecture plus one focused prototype; avoid duplicating A4/A8 |
| C3 | 13. AI Gateway & Model Management | LiteLLM gateway, provider abstraction, routing/fallback, budgets and usage tracking | Local gateway demo; provider keys optional and supplied by user |
| C4 | 17. Kubernetes AI Infrastructure & Model Serving | Kubernetes workload patterns, Helm, inference architecture, vLLM/KServe, batching and quantization | Local Kubernetes manifest/lab and architecture; GPU/KServe deployment optional, not required |

## A8 capstone: required functional agents

1. Incident Detection Agent — simulated alert ingestion, classification and reflex trigger.
2. Kubernetes Investigation Agent — read-only pods/events/logs/resource/deployment evidence.
3. RAG Knowledge Agent — runbook and historical incident retrieval with citations.
4. Root Cause Analysis Agent — evidence correlation, hypotheses, confidence and missing evidence.
5. Remediation Agent — proposed YAML diff, risk, validation and rollback plan.
6. Approval Agent — concise human explanation and explicit Approve / Reject / Hold; record actor, time and decision.
7. GitOps Deployment Agent — approved change becomes a GitHub PR; CI checks; protected branch; no direct push to main.
8. Verification Agent — post-change health checks and rollback proposal if checks fail.
9. Observability & Evaluation — traces, cost/latency, golden dataset, groundedness and safety tests.

## What is mandatory vs optional

**Mandatory:** A1–A8; B2–B4; B7; local reproducible demo; tests; security boundaries; human approval; rollback proposal; documentation. These are the strongest differentiators for an AI + DevOps/SRE role.

**Targeted / optional:** B1 voice, B5 GraphRAG, B6 distributed queue, C1 actual fine-tuning, C3 multiple paid model providers, C4 GPU/vLLM/KServe. Cover these with a small lab or architecture explanation unless a target job explicitly requires deeper implementation.

This keeps all 19 curriculum topics represented without pretending every topic is a production-grade feature.
