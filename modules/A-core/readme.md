============================================================
             AI SRE COPILOT - MODULE A
============================================================

1. WHAT ARE WE BUILDING?
------------------------

We will build THREE applications:

APPLICATION 1: AUTH SERVICE
- User registration.
- User login.
- User authentication.

APPLICATION 2: SURVEY SERVICE
- Display survey questions.
- Accept user responses.
- Display combined survey results.

APPLICATION 3: AI SRE COPILOT
- Monitor Auth and Survey services.
- Detect application failures.
- Investigate incidents.
- Use AI to identify possible causes.
- Recommend remediation.
- Ask a human for approval.
- Deploy approved changes.
- Verify application health.

Think of Auth and Survey as our sample applications.
AI SRE Copilot is the main project we are building.

IMPORTANT:
AI will NOT independently modify production systems.
It must explain the problem, show the proposed fix and
rollback plan, and wait for human approval.

============================================================
2. WHAT ARE API AND API CALLS?
============================================================

API = A way for two applications to communicate.

API CALL = A request one application sends to another.

Example:

AI SRE Copilot asks Kubernetes:
"Tell me why my Survey Service Pod failed."

Kubernetes replies:
"The Pod was OOMKilled."

The request and response are an API interaction.

In our project, Python is the main programming language
used to build the AI SRE Copilot application.

It will communicate with these systems:

1. Kubernetes API
   Gets Pod status, events, logs and deployment details.

2. Monitoring API
   Gets CPU, memory, alerts and health information.

3. OpenAI API
   Analyzes incident evidence and recommends solutions.

4. Slack API
   Sends incident notifications and receives human decisions.

5. GitHub API
   Creates branches, updates YAML and creates Pull Requests.

6. Argo CD API
   Checks deployment status and synchronizes approved changes.

============================================================
3. COMPLETE PROJECT FLOW
============================================================

                         USER
                           |
                           v
                  +------------------+
                  |  SURVEY WEBSITE  |
                  +------------------+
                           |
               +-----------+-----------+
               |                       |
               v                       v
        +--------------+       +----------------+
        | AUTH SERVICE |       | SURVEY SERVICE |
        |              |       |                |
        | Registration |       | Questions      |
        | Login        |       | Submissions     |
        | Authentication|      | Results        |
        +--------------+       +----------------+
               ^                       |
               |                       |
               +-----------------------+
                 API communication:
                 Survey verifies users
                 through Auth Service.


============================================================
           APPLICATION 3: AI SRE COPILOT
============================================================

                  +----------------------+
                  |    AI SRE COPILOT    |
                  |    Python Application|
                  +----------------------+
                             |
                     Incident detected
                             |
              +--------------+--------------+
              |                             |
              v                             v
       +--------------+              +--------------+
       | KUBERNETES   |              | MONITORING    |
       | API           |              | API           |
       |              |              |              |
       | Pod status   |              | CPU metrics   |
       | Pod events   |              | Memory metrics|
       | Pod logs     |              | Alerts        |
       | Restarts     |              | Health        |
       +--------------+              +--------------+
              |                             |
              +--------------+--------------+
                             |
                             v
                  +----------------------+
                  |    AI SRE COPILOT    |
                  | Collects evidence    |
                  +----------------------+
                             |
                             v
                      +-------------+
                      |  OPENAI API |
                      |             |
                      | AI analysis |
                      | Root cause  |
                      | Suggestions |
                      +-------------+
                             |
                             v
                  +----------------------+
                  |    AI SRE COPILOT    |
                  | Prepares YAML change |
                  | Explains risks       |
                  | Prepares rollback    |
                  +----------------------+
                             |
                             v
                  +----------------------+
                  |   HUMAN APPROVAL     |
                  |                      |
                  | APPROVE / REJECT     |
                  | HOLD                 |
                  +----------------------+
                             |
                             v
                       +-----------+
                       | SLACK API |
                       |           |
                       | Sends     |
                       | incident  |
                       | Receives  |
                       | decision  |
                       +-----------+
                             |
                      If APPROVED
                             |
                             v
                       +-----------+
                       | GITHUB API|
                       |           |
                       | New branch|
                       | YAML update|
                       | Pull Request|
                       +-----------+
                             |
                             v
                       +-----------+
                       | CI CHECKS |
                       |           |
                       | YAML      |
                       | Security  |
                       | Tests     |
                       +-----------+
                             |
                       If checks pass
                             |
                             v
                       +-----------+
                       | ARGO CD   |
                       | API       |
                       |           |
                       | Sync      |
                       | approved  |
                       | changes   |
                       +-----------+
                             |
                             v
                       +-----------+
                       | KUBERNETES|
                       |           |
                       | Deploy    |
                       | changes   |
                       +-----------+
                             |
                             v
                  +----------------------+
                  |    AI SRE COPILOT    |
                  | Checks Pod health    |
                  | Checks app health    |
                  | Checks metrics       |
                  | Records result       |
                  +----------------------+
                             |
                             v
                      INCIDENT RESOLVED
                             |
                             v
                      FINAL REPORT


IMPORTANT:
- Human approval is mandatory.
- Failed CI checks stop deployment.
- No automatic production changes.
- Rollback information is prepared before approval.

============================================================
4. MODULE A - 8 CORE CAPABILITIES
============================================================

A1. PYTHON FOR GENERATIVE AI
----------------------------
Purpose:
Build the Python foundation of our AI application.

We will learn and implement:
- Python fundamentals and OOP.
- Functions and exception handling.
- JSON and file handling.
- API communication.
- AI model API calls.
- Structured data handling.

Files:

A1-python-genai/
|-- README.md
|-- requirements.txt
|-- config.py          # Application configuration
|-- main.py            # Application entry point
|-- api_client.py      # Communicates with APIs
|-- json_handler.py    # Processes JSON data
|-- exceptions.py      # Handles errors
|-- models.py          # Defines data structures
|-- tests/
|   |-- test_api_client.py
|   |-- test_json_handler.py
|   |-- test_models.py
|-- examples/
    |-- sample_incident.json

Result:
A working Python foundation for API and AI communication.


A2. AGENT FOUNDATIONS
---------------------
Purpose:
Build an AI agent that can investigate incidents.

An AI agent can receive a task, collect information,
analyze it and use tools to complete the task.

Example:
Task: Investigate why Survey Service is failing.

The agent:
1. Understands the task.
2. Identifies required information.
3. Calls investigation tools.
4. Analyzes the results.
5. Produces a diagnosis.

Reflex Agent:
IF Pod is OOMKilled, classify it as a possible
memory-related incident.

ReAct:
THINK -> ACT -> OBSERVE -> THINK AGAIN.

Files:

A2-agent-foundations/
|-- README.md
|-- requirements.txt
|-- agent.py             # Main agent logic
|-- agent_state.py       # Stores task status
|-- prompts.py           # AI instructions
|-- tool_registry.py     # Registers available tools
|-- reflex_rules.py      # Predefined incident rules
|-- react_agent.py       # ReAct workflow
|-- memory.py            # Stores relevant information
|-- tests/
    |-- test_agent.py
    |-- test_reflex_rules.py
    |-- test_tool_registry.py

Result:
An AI agent capable of investigating incidents.


A3. RAG KNOWLEDGE AGENT
-----------------------
Purpose:
Allow AI to search our own technical documents.

RAG = Retrieval-Augmented Generation.

Example:
AI detects an OOMKilled incident.
It searches our Kubernetes runbooks and previous incidents
before recommending a solution.

How it works:
1. Import documents.
2. Split documents into smaller pieces.
3. Convert text into embeddings.
4. Store embeddings in a searchable database.
5. Retrieve relevant information.
6. Send information to the AI model.
7. Generate an evidence-based answer.

Embedding:
A numerical representation of text meaning.

Files:

A3-rag-knowledge-agent/
|-- README.md
|-- requirements.txt
|-- ingestion.py         # Imports documents
|-- document_parser.py   # Extracts document text
|-- chunker.py           # Splits documents
|-- embeddings.py        # Creates embeddings
|-- vector_store.py      # Stores embeddings
|-- retriever.py         # Searches documents
|-- context_builder.py   # Prepares AI context
|-- rag_pipeline.py      # Connects RAG steps
|-- evaluator.py         # Evaluates results
|-- knowledge_base/
|   |-- kubernetes_runbook.md
|   |-- oom_troubleshooting.md
|   |-- application_incidents.md
|-- tests/
    |-- test_chunker.py
    |-- test_retriever.py
    |-- test_rag_pipeline.py

Result:
AI can use our own technical knowledge while investigating.


A4. MULTI-AGENT SYSTEM
----------------------
Purpose:
Use multiple specialized AI agents instead of one agent
doing everything.

Our agents:

1. Investigation Agent
   Collects incident information.

2. Knowledge Agent
   Searches technical documents.

3. RCA Agent
   Identifies possible root causes.

4. Remediation Agent
   Suggests configuration changes.

5. Verification Agent
   Checks application health.

Files:

A4-multi-agent/
|-- README.md
|-- requirements.txt
|-- orchestrator.py          # Coordinates agents
|-- investigation_agent.py   # Investigates incidents
|-- knowledge_agent.py       # Searches knowledge
|-- rca_agent.py             # Root cause analysis
|-- remediation_agent.py     # Suggests fixes
|-- verification_agent.py    # Checks recovery
|-- shared_state.py          # Shared information
|-- agent_messages.py        # Agent communication
|-- tests/
    |-- test_orchestrator.py
    |-- test_agent_messages.py

Result:
Multiple agents work together to investigate incidents.


A5. HYBRID SEARCH
-----------------
Purpose:
Improve how our knowledge agent searches documents.

Two search methods:

1. Keyword Search
   Finds exact words such as OOMKilled or exit code 137.

2. Semantic Search
   Finds documents with similar meanings.

Hybrid Search combines both methods.

BM25:
Ranks documents based on keyword relevance.

RRF:
Combines search rankings from different methods.

Files:

A5-hybrid-search/
|-- README.md
|-- requirements.txt
|-- keyword_search.py     # Keyword search
|-- semantic_search.py    # Meaning-based search
|-- bm25_search.py        # BM25 ranking
|-- hybrid_retriever.py   # Combines search results
|-- rrf.py                # Combines rankings
|-- reranker.py           # Reorders results
|-- search_evaluator.py   # Evaluates search quality
|-- tests/
    |-- test_keyword_search.py
    |-- test_hybrid_retriever.py
    |-- test_rrf.py

Result:
The knowledge agent finds more relevant documents.


A6. SAFE, EVALUATED AND COST-OPTIMIZED AI
-----------------------------------------
Purpose:
Make AI recommendations safer and measurable.

Why?
AI can provide incorrect recommendations.
We must validate its output before presenting a fix.

Example:
AI suggests increasing memory from 32Mi to 4Gi.

Our application checks:
- Is the YAML valid?
- Is the change reasonable?
- Is there supporting evidence?
- Is a rollback plan available?
- Is human approval required?

Golden Dataset:
A collection of test cases with expected answers.

LLM-as-a-Judge:
An AI model evaluates another AI response.

We will also track token usage and API costs.

Files:

A6-safe-evaluated-cost/
|-- README.md
|-- requirements.txt
|-- guardrails.py             # Safety rules
|-- input_validator.py        # Validates input
|-- output_validator.py       # Validates AI output
|-- yaml_validator.py         # Checks YAML
|-- policy_engine.py          # Enforces policies
|-- golden_dataset.json       # Known test cases
|-- evaluation.py             # Evaluates AI results
|-- hallucination_checks.py   # Checks unsupported answers
|-- token_tracker.py          # Tracks token usage
|-- cost_calculator.py        # Estimates AI costs
|-- tests/
    |-- test_guardrails.py
    |-- test_yaml_validator.py
    |-- test_evaluation.py

Result:
AI recommendations are checked before human approval.


A7. LANGGRAPH ORCHESTRATION
---------------------------
Purpose:
Control the complete AI workflow using LangGraph.

Workflow:

START
  |
  v
Incident Detection
  |
  v
Kubernetes Investigation
  |
  v
RAG Knowledge Search
  |
  v
Root Cause Analysis
  |
  v
Remediation Proposal
  |
  v
Human Approval
  |
  +-- REJECT --> END
  |
  +-- HOLD ----> WAIT
  |
  +-- APPROVE -> GitHub PR
                    |
                    v
                CI Validation
                    |
                    v
                Deployment
                    |
                    v
                Health Check
                    |
                    v
                   END

LangGraph manages workflow steps and their state.

Human-in-the-Loop:
The workflow pauses and waits for a human decision.

Files:

A7-langgraph-orchestration/
|-- README.md
|-- requirements.txt
|-- graph.py          # Defines workflow
|-- state.py          # Stores workflow state
|-- nodes.py          # Workflow steps
|-- edges.py          # Connects steps
|-- routing.py        # Controls workflow direction
|-- checkpointing.py  # Saves workflow progress
|-- approval.py       # Handles human approval
|-- recovery.py       # Handles retries and recovery
|-- tests/
    |-- test_graph.py
    |-- test_routing.py
    |-- test_approval.py

Result:
A controlled workflow with approval, retry and recovery.


A8. ENTERPRISE AI SRE COPILOT
-----------------------------
Purpose:
Integrate A1 to A7 into one complete application.

Complete workflow:

1. INCIDENT DETECTION
   Receives an alert.

2. INVESTIGATION
   Collects Pod status, logs, events and metrics.

3. KNOWLEDGE RETRIEVAL
   Searches relevant runbooks.

4. ROOT CAUSE ANALYSIS
   Agents analyze the collected evidence.

5. REMEDIATION PROPOSAL
   Prepares diagnosis, YAML changes, risks and rollback.

6. HUMAN APPROVAL
   Human chooses APPROVE, REJECT or HOLD.

7. GITHUB INTEGRATION
   Creates branch, updates YAML and opens a Pull Request.

8. GITOPS DEPLOYMENT
   CI validates changes and Argo CD deploys approved changes.

9. VERIFICATION
   Checks Pod health, application health and metrics.

10. AUDIT
    Records incident, evidence, approval and deployment result.

Files:

A8-enterprise-ai-sre-copilot/
|-- README.md
|-- requirements.txt
|-- main.py                 # Starts Copilot application
|-- incident_manager.py     # Manages incidents
|-- alert_receiver.py       # Receives alerts
|-- kubernetes_collector.py # Collects Kubernetes data
|-- log_collector.py        # Collects application logs
|-- diagnosis_engine.py     # Analyzes incidents
|-- remediation_manager.py  # Prepares proposed fixes
|-- approval_manager.py     # Manages approval
|-- github_client.py        # GitHub communication
|-- argocd_client.py        # Argo CD communication
|-- health_verifier.py      # Checks application health
|-- audit_logger.py         # Records activities
|-- api/
|   |-- incidents.py
|   |-- approvals.py
|   |-- remediation.py
|-- integrations/
|   |-- kubernetes.py
|   |-- github.py
|   |-- slack.py
|   |-- argocd.py
|-- tests/
    |-- test_incident_manager.py
    |-- test_approval_manager.py
    |-- test_remediation_manager.py
    |-- test_health_verifier.py

Result:
One integrated AI SRE Copilot for investigating incidents
and proposing controlled remediation.

============================================================
5. HOW WILL THE MODULES WORK TOGETHER?
============================================================

A1 = Python foundation.
A2 = AI agent intelligence.
A3 = Knowledge retrieval.
A4 = Team of specialized agents.
A5 = Better document search.
A6 = AI safety and evaluation.
A7 = Workflow controller.
A8 = Complete AI SRE Copilot.

============================================================
6. WHERE WILL THE CODE LIVE?
============================================================

AI-SRE-COPILOT/
|
|-- apps/
|   |-- auth-service/
|   |-- survey-service/
|
|-- copilot-app/
|   |-- main.py
|   |-- incident_manager.py
|   |-- integrations/
|
|-- modules/
|   |-- A-core/
|   |   |-- A1-python-genai/
|   |   |-- A2-agent-foundations/
|   |   |-- A3-rag-knowledge-agent/
|   |   |-- A4-multi-agent/
|   |   |-- A5-hybrid-search/
|   |   |-- A6-safe-evaluated-cost/
|   |   |-- A7-langgraph-orchestration/
|   |   |-- A8-enterprise-ai-sre-copilot/
|   |
|   |-- B-advanced/
|   |-- C-specialized/
|
|-- infra/
|   |-- compose.yaml
|
|-- docs/
|   |-- ARCHITECTURE.md
|   |-- MODULE-MAP.md
|   |-- IMPLEMENTATION-PLAN.md
|
|-- scripts/
|-- tests/
|-- requirements-dev.txt
|-- Makefile
|-- .env.example
|-- README.md

============================================================
7. HOW WILL WE RUN THE PROJECT?
============================================================

We will automate dependency installation using Docker.

One-time prerequisites:
1. Git installed.
2. Docker Desktop installed and running.

Commands:

make setup
Checks the environment and creates .env.

make up
Builds and starts application containers.
Docker installs the Python dependencies.

make test
Runs automated tests.

make logs
Displays application logs.

make down
Stops the containers.

These commands are shortcuts defined in the Makefile.

Our goal is to avoid manually installing individual
Python packages on your MacBook.

============================================================
8. CURRENT IMPLEMENTATION STATUS
============================================================

Already created:
- Parent repository structure.
- Module README files.
- Two sample microservices.
- Dockerfiles and Docker Compose.
- Initial tests.
- Makefile and setup script.
- Architecture documentation.

Not implemented yet:
- A1 to A8 actual module code.
- Complete RAG pipeline.
- Multi-agent system.
- LangGraph workflow.
- Integrated AI SRE Copilot.

A folder containing only README.md is NOT a completed module.

============================================================
9. OUR IMPLEMENTATION RULE
============================================================

Every module must contain:

1. Working source code.
2. Requirements file.
3. Configuration and .env example.
4. Unit tests.
5. Integration tests where required.
6. Sample inputs and outputs.
7. Docker support where required.
8. Detailed README.
9. API documentation.
10. Interview explanation.

A module is COMPLETE only when its code runs and
its tests pass.

============================================================
10. FINAL OBJECTIVE
============================================================

- One GitHub parent repository.
- Two sample microservices.
- Eight core capabilities (Module A).
- Seven advanced capabilities (Module B).
- Four specialized capabilities (Module C).
- One integrated AI SRE Copilot.
- Local MacBook development.
- Human approval before remediation.
- Automated testing and documentation.
- No mandatory cloud account.

============================================================
