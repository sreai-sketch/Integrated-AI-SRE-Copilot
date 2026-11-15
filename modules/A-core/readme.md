============================================================
          AI SRE COPILOT - MODULE A EXPLAINED
============================================================

FIRST: WHAT ARE WE BUILDING?

Imagine you are working as an SRE in a company. The company has an application running on Kubernetes. The application has two microservices:

1. AUTH SERVICE - Handles user registration and login.

2. SURVEY SERVICE - Allows users to submit surveys and view combined results.

Now imagine the Survey Service suddenly stops working. Normally, an SRE engineer has to:

- Check alerts.
- Check application logs.
- Check Kubernetes events.
- Investigate the failure.
- Find the root cause.
- Decide how to fix it.
- Prepare a configuration change.
- Get approval.
- Deploy the fix.
- Verify application health.

Our AI SRE Copilot will help automate this investigation and remediation workflow.

IMPORTANT: The AI will NOT independently modify production systems. It will investigate, explain the problem, recommend a fix, show the YAML changes and rollback plan, and ask a human
for approval before proceeding.

============================================================
MODULE A - 8 CORE CAPABILITIES
============================================================

Think of Module A as the ENGINE of our complete project. Each folder will contain actual Python code, configuration, tests, sample data and its own README.

------------------------------------------------------------
A1 - PYTHON FOR GENERATIVE AI
------------------------------------------------------------

WHAT WILL IT DO?

This is the foundation of our entire AI application. We will use Python to build the application logic.
Example:

- Receive an incident.
- Read JSON data.
- Call external APIs.
- Process Kubernetes information.
- Communicate with AI models.
- Handle errors.
- Return structured results.

What is an API?

API stands for Application Programming Interface. Imagine you have a restaurant. There are three people involved:

1. You (Customer)
2. Waiter
3. Kitchen (Chef)

You cannot enter the kitchen and prepare the food yourself. You tell the waiter what you want. The waiter communicates your order to the kitchen and brings the food back.

       YOU
        |
        | Request: I want a pizza
        |
        v
      WAITER
        |
        | Communicates your order
        |
        v
      KITCHEN
        |
        | Prepares the pizza
        |
        v
      WAITER
        |
        | Returns your order
        |
        v
       YOU

An API works in exactly the same way. API means Application Programming Interface. An API allows two different software applications to communicate with each other.

For example:
* Our Python application wants information from Kubernetes.
* Our Python application wants an AI model to analyze an incident.
* Our Survey Service wants to communicate with our Auth Service.

What is the role of APIs in our AI SRE Copilot?

This is the most important part. Our project will use APIs to connect different components. Let’s take a real production-like incident.
"Scenario: Survey Service is failing"

Our AI SRE Copilot needs information from different systems to investigate the problem.


WHAT IS AN AI API CALL?

An API call is simply a request sent from one application to another through an API. For example, imagine our Survey Service needs to check whether a user is logged in.
An API call means asking another application for information or requesting it to perform an action.

For example: Our AI SRE Copilot asks Kubernetes: “Tell me the status of my Survey Service Pods.”

Kubernetes replies: “One Pod is OOMKilled.”

That request and response are an API call.


================================================================
                    OUR COMPLETE PROJECT
================================================================

                         USER
                           |
                           v
                 +-------------------+
                 |   SURVEY WEBSITE  |
                 +-------------------+
                           |
               +-----------+-----------+
               |                       |
               v                       v
     +------------------+    +----------------------+
     | APPLICATION 1    |    | APPLICATION 2        |
     | AUTH SERVICE     |    | SURVEY SERVICE       |
     |                  |    |                      |
     | User Registration|    | Display Questions   |
     | User Login       |    | Submit Responses     |
     | Authentication   |    | Combined Results     |
     +------------------+    +----------------------+
               ^                       |
               |                       |
               +-----------------------+
                  API COMMUNICATION
                  Survey Service asks
                  Auth Service to verify
                  the logged-in user.


================================================================
                 APPLICATION 3: AI SRE COPILOT
================================================================

                 +---------------------------+
                 |      AI SRE COPILOT       |
                 |      Python Application  |
                 +---------------------------+
                              ^
                              |
                 Application failure detected
                              |
                              |
              +---------------+---------------+
              |                               |
              |                               |
              v                               v
     +-------------------+          +-------------------+
     | KUBERNETES API    |          | MONITORING API    |
     |                   |          |                   |
     | Pod status        |          | CPU metrics       |
     | Pod events        |          | Memory metrics    |
     | Pod logs          |          | Alerts             |
     | Restart count     |          | Application health |
     +-------------------+          +-------------------+
              |                               |
              +---------------+---------------+
                              |
                              v
                 +---------------------------+
                 |      AI SRE COPILOT       |
                 |                           |
                 | Collects incident data   |
                 | Correlates evidence      |
                 +---------------------------+
                              |
                              v
                    +-------------------+
                    |    OPENAI API     |
                    |                   |
                    | AI Analysis       |
                    | Root Cause        |
                    | Recommendations   |
                    +-------------------+
                              |
                              v
                 +---------------------------+
                 |      AI SRE COPILOT       |
                 |                           |
                 | Prepares remediation     |
                 | Shows YAML changes       |
                 | Explains risks           |
                 | Prepares rollback plan   |
                 +---------------------------+
                              |
                              v
                 +---------------------------+
                 |       HUMAN APPROVAL      |
                 |                           |
                 | APPROVE / REJECT / HOLD   |
                 +---------------------------+
                              |
                              v
                    +-------------------+
                    |     SLACK API     |
                    |                   |
                    | Sends incident    |
                    | Receives decision |
                    +-------------------+
                              |
                       If APPROVED
                              |
                              v
                    +-------------------+
                    |    GITHUB API     |
                    |                   |
                    | Create branch     |
                    | Update YAML       |
                    | Create Pull Request|
                    +-------------------+
                              |
                              v
                    +-------------------+
                    |   CI VALIDATION   |
                    |                   |
                    | YAML validation   |
                    | Security checks   |
                    | Automated tests   |
                    +-------------------+
                              |
                       If checks pass
                              |
                              v
                    +-------------------+
                    |    ARGO CD API    |
                    |                   |
                    | Sync approved     |
                    | configuration     |
                    +-------------------+
                              |
                              v
                    +-------------------+
                    |   KUBERNETES      |
                    |                   |
                    | Deploy changes    |
                    +-------------------+
                              |
                              v
                 +---------------------------+
                 |      AI SRE COPILOT       |
                 |                           |
                 | Checks Pod health        |
                 | Checks application health|
                 | Checks monitoring metrics|
                 | Records incident result  |
                 +---------------------------+
                              |
                              v
                     INCIDENT RESOLVED
                              |
                              v
                    HUMAN GETS FINAL REPORT
      

1.Kubernetes API - Collects Pod, Deployment, Events and Logs information.

2.Monitoring API - Collects metrics, alerts and application health information.

3.OpenAI API - Analyzes collected evidence and recommends remediation.

4.GitHub API - Creates branches, updates YAML files and creates Pull Requests.

5.Slack API - Sends incident notifications and receives human approval.

6.Argo CD API - Checks deployment status and manages approved synchronisation.  

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

FILES WE WILL CREATE:

A1-python-genai/
|
|-- README.md
|-- requirements.txt
|-- config.py
|-- main.py
|-- api_client.py
|-- json_handler.py
|-- exceptions.py
|-- models.py
|-- tests/
|   |-- test_api_client.py
|   |-- test_json_handler.py
|   |-- test_models.py
|-- examples/
    |-- sample_incident.json

WHAT EACH FILE DOES:

config.py - Stores application configuration.

main.py - Starts the Python application.

api_client.py - Communicates with external APIs, including AI providers.

json_handler.py - Reads and processes JSON information.

exceptions.py - Handles application errors.

models.py - Defines the structure of incoming and outgoing data.

requirements.txt - Lists Python packages required by this module.

tests/ - Checks whether the code works correctly.

examples/ - Contains sample incident information.

RESULT: We will have a working Python foundation that can communicate with APIs and AI models.


------------------------------------------------------------
A2 - AGENT FOUNDATIONS
------------------------------------------------------------

WHAT IS AN AI AGENT?

A normal AI chatbot answers questions. An AI agent can receive a task, analyze information, choose an action and use tools to complete the task.

Example: Task: Investigate why the Survey Service is failing.

The agent will:
1. Understand the task.
2. Identify which information is required.
3. Call the appropriate tools.
4. Analyze the collected information.
5. Produce a diagnosis.

WHAT IS A REFLEX AGENT - Imagine a simple rule: IF a Kubernetes pod is OOMKilled, THEN classify the incident as a memory-related issue. This is a basic reflex.

WHAT IS ReAct - ReAct means Reasoning + Acting. The agent follows a cycle: THINK -> ACT -> OBSERVE -> THINK AGAIN. Example:

Think: I need to investigate the failed pod.
Act: Call the Kubernetes investigation tool.
Observe: The pod was terminated with exit code 137.
Think again: I should inspect its memory limit and previous logs.

FILES WE WILL CREATE:

A2-agent-foundations/
|
|-- README.md
|-- requirements.txt
|-- agent.py
|-- agent_state.py
|-- prompts.py
|-- tool_registry.py
|-- reflex_rules.py
|-- react_agent.py
|-- memory.py
|-- tests/
    |-- test_agent.py
    |-- test_reflex_rules.py
    |-- test_tool_registry.py

WHAT EACH FILE DOES:

agent.py
Main agent logic.

agent_state.py
Stores the current task and investigation status.

prompts.py
Contains instructions given to the AI.

tool_registry.py
Registers tools the agent can use.

reflex_rules.py
Contains predefined rules for common incidents.

react_agent.py
Implements the Think, Act and Observe cycle.

memory.py
Stores relevant information from previous steps.

RESULT:

We will have an agent capable of investigating
an incident using predefined tools.


------------------------------------------------------------
A3 - RAG KNOWLEDGE AGENT
------------------------------------------------------------

WHAT IS RAG?

RAG means Retrieval-Augmented Generation.

Imagine the AI detects an OOMKilled incident.

Instead of relying only on its general knowledge,
we want it to search our own technical documentation.

For example:

- Kubernetes troubleshooting guide.
- Company runbooks.
- Previous incident reports.
- Memory troubleshooting documentation.

HOW DOES IT WORK?

Step 1:
Upload technical documents.

Step 2:
Break documents into smaller pieces.

Step 3:
Convert these pieces into numerical representations
called embeddings.

Step 4:
Store embeddings in a searchable database.

Step 5:
When an incident occurs, search for relevant information.

Step 6:
Send the relevant information to the AI model.

Step 7:
AI generates an answer using the retrieved information.

WHAT IS AN EMBEDDING?

An embedding converts text into a list of numbers.

These numbers represent the meaning of the text.

This allows the application to search for similar meanings,
not just identical words.

FILES WE WILL CREATE:

A3-rag-knowledge-agent/
|
|-- README.md
|-- requirements.txt
|-- ingestion.py
|-- document_parser.py
|-- chunker.py
|-- embeddings.py
|-- vector_store.py
|-- retriever.py
|-- context_builder.py
|-- rag_pipeline.py
|-- evaluator.py
|-- knowledge_base/
|   |-- kubernetes_runbook.md
|   |-- oom_troubleshooting.md
|   |-- application_incidents.md
|-- tests/
    |-- test_chunker.py
    |-- test_retriever.py
    |-- test_rag_pipeline.py

WHAT EACH FILE DOES:

ingestion.py
Imports documents into our knowledge system.

document_parser.py
Extracts text from documents.

chunker.py
Breaks documents into smaller pieces.

embeddings.py
Converts text into numerical embeddings.

vector_store.py
Stores and searches embeddings.

retriever.py
Finds relevant information.

context_builder.py
Prepares retrieved information for the AI model.

rag_pipeline.py
Connects all RAG steps.

evaluator.py
Checks whether retrieval and answers are useful.

knowledge_base/
Contains our sample technical documentation.

RESULT:

The AI will be able to refer to our own runbooks
while investigating incidents.


------------------------------------------------------------
A4 - MULTI-AGENT SYSTEM
------------------------------------------------------------

WHAT IS A MULTI-AGENT SYSTEM?

Instead of asking one AI agent to do everything,
we create multiple specialized agents.

Think of a company with different departments.

Each department has a specific responsibility.

Our project will have:

1. INVESTIGATION AGENT
   Collects incident information.

2. KNOWLEDGE AGENT
   Searches technical documentation.

3. RCA AGENT
   Analyzes evidence and identifies possible root causes.

4. REMEDIATION AGENT
   Suggests configuration changes.

5. VERIFICATION AGENT
   Checks whether the application recovered.

HOW DO THEY COMMUNICATE?

The agents exchange structured information.

Example:

Investigation Agent:
Pod terminated with exit code 137.

Knowledge Agent:
Found a runbook explaining memory-related failures.

RCA Agent:
Memory limit may be insufficient.

Remediation Agent:
Proposes increasing the memory limit.

Verification Agent:
Will check application health after deployment.

FILES WE WILL CREATE:

A4-multi-agent/
|
|-- README.md
|-- requirements.txt
|-- orchestrator.py
|-- investigation_agent.py
|-- knowledge_agent.py
|-- rca_agent.py
|-- remediation_agent.py
|-- verification_agent.py
|-- shared_state.py
|-- agent_messages.py
|-- tests/
    |-- test_orchestrator.py
    |-- test_agent_messages.py

WHAT EACH FILE DOES:

orchestrator.py
Coordinates all agents.

investigation_agent.py
Investigates incidents.

knowledge_agent.py
Retrieves technical knowledge.

rca_agent.py
Performs root cause analysis.

remediation_agent.py
Creates remediation proposals.

verification_agent.py
Checks application health.

shared_state.py
Stores information shared between agents.

agent_messages.py
Defines how agents exchange information.

RESULT:

Multiple specialized agents will work together
to investigate and resolve an incident.


------------------------------------------------------------
A5 - HYBRID SEARCH
------------------------------------------------------------

WHAT IS HYBRID SEARCH?

Imagine we are searching for an incident involving:

"Payment pod OOMKilled with exit code 137"

There are two ways to search.

1. KEYWORD SEARCH

Finds exact words such as:

OOMKilled
exit code 137
memory limit

2. SEMANTIC SEARCH

Finds documents with similar meaning,
even when the exact words are different.

HYBRID SEARCH combines both approaches.

We will also use:

BM25:
A keyword-based search ranking technique.

RRF:
Reciprocal Rank Fusion combines results from
different search methods.

FILES WE WILL CREATE:

A5-hybrid-search/
|
|-- README.md
|-- requirements.txt
|-- keyword_search.py
|-- semantic_search.py
|-- bm25_search.py
|-- hybrid_retriever.py
|-- rrf.py
|-- reranker.py
|-- search_evaluator.py
|-- tests/
    |-- test_keyword_search.py
    |-- test_hybrid_retriever.py
    |-- test_rrf.py

RESULT:

The knowledge agent will find more relevant
troubleshooting information.


------------------------------------------------------------
A6 - SAFE, EVALUATED AND COST-OPTIMIZED AI
------------------------------------------------------------

WHY DO WE NEED THIS?

AI can produce incorrect answers.

AI can also misunderstand an incident.

We cannot blindly trust its recommendations.

We will introduce safety checks.

EXAMPLE:

AI proposes:

Increase memory limit from 32Mi to 4Gi.

Our system checks:

- Is the proposed YAML valid?
- Is the resource change reasonable?
- Is there supporting evidence?
- Is the rollback available?
- Is human approval available?

We will also evaluate AI quality.

WHAT IS A GOLDEN DATASET?

A collection of known test cases with expected results.

Example:

Input:
Pod OOMKilled with exit code 137.

Expected:
The AI should identify a possible memory-related issue.

We compare the AI response with the expected result.

WHAT IS LLM-AS-A-JUDGE?

Another AI model evaluates the quality of an AI response.

It can assess:

- Accuracy.
- Relevance.
- Evidence.
- Completeness.

We will also monitor token usage and AI API costs.

FILES WE WILL CREATE:

A6-safe-evaluated-cost/
|
|-- README.md
|-- requirements.txt
|-- guardrails.py
|-- input_validator.py
|-- output_validator.py
|-- yaml_validator.py
|-- policy_engine.py
|-- golden_dataset.json
|-- evaluation.py
|-- hallucination_checks.py
|-- token_tracker.py
|-- cost_calculator.py
|-- tests/
    |-- test_guardrails.py
    |-- test_yaml_validator.py
    |-- test_evaluation.py

RESULT:

AI recommendations will be validated and evaluated
before they reach a human for approval.


------------------------------------------------------------
A7 - LANGGRAPH ORCHESTRATION
------------------------------------------------------------

WHAT IS LANGGRAPH?

LangGraph is a framework used to build AI workflows
as connected steps.

Imagine our complete incident investigation.

The workflow is:

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
  +---- REJECT ----> END
  |
  +---- HOLD ------> WAIT
  |
  +---- APPROVE ---> GitHub PR
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

LangGraph manages the workflow and its state.

WHAT IS HUMAN-IN-THE-LOOP?

It means a human can interrupt the workflow
and make a decision before it continues.

For our project:

The workflow must stop before remediation is applied.

It must wait for APPROVE, REJECT or HOLD.

FILES WE WILL CREATE:

A7-langgraph-orchestration/
|
|-- README.md
|-- requirements.txt
|-- graph.py
|-- state.py
|-- nodes.py
|-- edges.py
|-- routing.py
|-- checkpointing.py
|-- approval.py
|-- recovery.py
|-- tests/
    |-- test_graph.py
    |-- test_routing.py
    |-- test_approval.py

RESULT:

We will have a controlled AI workflow
with approval, retry and recovery capabilities.


------------------------------------------------------------
A8 - ENTERPRISE AI SRE COPILOT
------------------------------------------------------------

THIS IS THE FINAL INTEGRATION MODULE.

All previous modules will work together here.

Imagine a real production-like incident.

SCENARIO:

The Survey Service is experiencing failures.

Our complete workflow:

1. INCIDENT DETECTION

A monitoring alert is received.

2. INVESTIGATION

The system collects:

- Pod status.
- Application logs.
- Kubernetes events.
- Resource information.
- Deployment health.

3. KNOWLEDGE RETRIEVAL

The RAG agent searches relevant runbooks.

4. ROOT CAUSE ANALYSIS

The AI agents analyze the collected evidence.

5. REMEDIATION PROPOSAL

The system prepares:

- Problem summary.
- Root cause hypothesis.
- Supporting evidence.
- Proposed YAML changes.
- Risk assessment.
- Rollback plan.

6. HUMAN APPROVAL

The human receives a short explanation.

Available decisions:

APPROVE
REJECT
HOLD

7. GITHUB INTEGRATION

After approval:

- Create a GitHub branch.
- Generate a YAML change.
- Create a Pull Request.
- Run automated tests.

8. GITOPS DEPLOYMENT

After required checks and deployment approval,
Argo CD synchronizes the reviewed configuration.

9. VERIFICATION

The system checks:

- Pod health.
- Application health.
- Error rate.
- Restart count.
- Incident status.

10. AUDIT

Store:

- Original incident.
- AI diagnosis.
- Evidence.
- Proposed remediation.
- Human decision.
- GitHub PR.
- Deployment result.
- Rollback information.

FILES WE WILL CREATE:

A8-enterprise-ai-sre-copilot/
|
|-- README.md
|-- requirements.txt
|-- main.py
|-- incident_manager.py
|-- alert_receiver.py
|-- kubernetes_collector.py
|-- log_collector.py
|-- diagnosis_engine.py
|-- remediation_manager.py
|-- approval_manager.py
|-- github_client.py
|-- argocd_client.py
|-- health_verifier.py
|-- audit_logger.py
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

RESULT:

One integrated AI SRE Copilot that can investigate
production-like incidents and propose controlled remediation.

============================================================
HOW WILL THE MODULES COMMUNICATE?
============================================================

A1 provides Python application logic.

A2 provides agent intelligence and tool usage.

A3 provides knowledge retrieval.

A4 provides multiple specialized agents.

A5 improves knowledge searching.

A6 adds safety and evaluation.

A7 controls the complete workflow.

A8 integrates everything into the final application.

Think of it this way:

A1 = FOUNDATION
A2 = BRAIN
A3 = KNOWLEDGE
A4 = TEAM OF SPECIALISTS
A5 = BETTER SEARCH
A6 = SAFETY
A7 = WORKFLOW CONTROLLER
A8 = COMPLETE PRODUCT

============================================================
API CALLS AND AI CALLS - IMPORTANT DIFFERENCE
============================================================

There are three main types of communication.

1. INTERNAL API CALLS

Example:

Survey Service calls Auth Service to validate a user.

This is communication between our own applications.

2. EXTERNAL API CALLS

Example:

Our application calls the OpenAI API.

It sends a prompt and incident evidence.

The AI provider returns a response.

This may incur API charges depending on the provider
and usage.

3. KUBERNETES API CALLS

Our Python application communicates with Kubernetes
through the Kubernetes API.

It can retrieve:

- Pods.
- Events.
- Deployments.
- Services.
- Resource information.

Initially, investigation will use read-only permissions.

No production modifications will be allowed automatically.

============================================================
WHERE WILL THE CODE LIVE?
============================================================

The parent repository will contain:

AI-SRE-COPILOT/
|
|-- apps/
|   |-- auth-service/
|   |-- survey-service/
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
|   |-- setup.sh
|
|-- tests/
|
|-- requirements-dev.txt
|-- Makefile
|-- .env.example
|-- README.md

============================================================
HOW WILL WE START THE PROJECT?
============================================================

You asked whether you need to install everything manually.

NO, you will not need to manually install every Python
library, AI framework or application dependency.

Our goal is to automate those installations.

But there are two prerequisites:

1. Git must be available.
2. Docker Desktop must be installed and running.

Once these are ready:

make setup

Checks Docker and Git and creates the local .env file.

make up

Builds the application containers and starts the services.
Docker installs the Python packages listed in each
microservice's requirements.txt during image building.

make test

Runs the tests.

IMPORTANT:
The current Makefile also creates a Python virtual environment
and installs pytest and httpx on your Mac for testing.
So this command currently needs Python 3.

make logs

Displays application logs.

make down

Stops the containers.

These commands are not magic installation commands.
They are shortcuts that execute instructions already
written in our Makefile.

============================================================
CURRENT STATUS - HONEST UPDATE
============================================================

The existing repository contains:

- Parent folder structure.
- Module README files.
- Two microservice implementations.
- Dockerfiles.
- Docker Compose configuration.
- Initial test files.
- Makefile.
- Setup script.
- Architecture documentation.

However:

- A1 to A8 are not implemented yet.
- There is no completed RAG pipeline.
- There is no completed multi-agent system.
- There is no completed LangGraph workflow.
- There is no integrated AI SRE Copilot yet.

We will implement actual code in every module.

A folder with only README.md will never be considered
a completed module.

============================================================
OUR IMPLEMENTATION RULE
============================================================

For every module:

1. Actual working source code.
2. Requirements file.
3. Configuration and environment examples.
4. Unit tests.
5. Integration tests wherever applicable.
6. Sample inputs and outputs.
7. Docker support where needed.
8. Detailed README.
9. API documentation.
10. Interview explanation.

We will not mark a module COMPLETE until its code
runs and its tests pass.

============================================================
FINAL OBJECTIVE
============================================================

One GitHub parent repository.

Two lightweight microservices.

Eight fully implemented core capabilities.

Seven advanced capabilities.

Four specialized capabilities.

One integrated AI SRE Copilot.

Local MacBook development.

Human approval before remediation.

Automated testing and documentation.

No mandatory cloud account.

============================================================
