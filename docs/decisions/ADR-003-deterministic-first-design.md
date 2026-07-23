# ADR-003 — Deterministic-First System Design

* **Status:** Accepted
* **Date:** 2026-07-23
* **Decision owner:** Hoda Yamani
* **Related phases:** 0, 3, 6, 9, 10, 12, and 13

## Context

MaintMind will combine conventional software, data pipelines, machine-learning models, retrieval-augmented generation, deterministic policies, and one agentic workflow.

Maintenance investigations may involve incomplete reports, conflicting evidence, obsolete documents, safety-sensitive information, and consequential recommendations. Using an LLM or agent for every operation would reduce predictability, increase cost, complicate testing, and weaken auditability.

The platform therefore requires a clear boundary between deterministic engineering and probabilistic AI.

## Decision

MaintMind will use a deterministic-first architecture.

A capability will remain deterministic when it can be implemented reliably using:

* schema validation
* database constraints
* SQL queries
* explicit rules
* state machines
* reference tables
* threshold calculations
* permission policies
* version checks
* template-based outputs

Machine-learning models, LLMs, retrieval, or agents will be introduced only when they address a documented limitation of the deterministic baseline.

## Deterministic Responsibilities

Deterministic components will control:

* input validation
* required-field checks
* source-provenance validation
* duplicate detection
* idempotency
* database integrity
* access control
* document approval and version policy
* recurrence calculations
* safety escalation rules
* mandatory risk thresholds
* workflow-state transitions
* approval requirements
* audit-event creation
* retry and dead-letter handling
* agent step, cost, and tool limits

These controls cannot be overridden by an LLM or agent.

## Probabilistic Responsibilities

Probabilistic methods may be used for:

* structured extraction from ambiguous technician text
* maintenance-text classification
* equipment-risk estimation
* semantic document retrieval
* retrieval reranking
* grounded evidence synthesis
* draft recommendation generation
* adaptive tool selection for complex investigations

Probabilistic outputs must pass deterministic schema, evidence, permission, and safety checks before they reach a user.

## Baseline Requirement

Every probabilistic capability must be compared against a simpler baseline.

| Capability                 | Deterministic or simple baseline | Advanced approach                     |
| -------------------------- | -------------------------------- | ------------------------------------- |
| Report extraction          | Regex and keyword rules          | Bedrock structured extraction         |
| Maintenance classification | Frequency or linear baseline     | Tree-based or language model          |
| Document retrieval         | PostgreSQL keyword search        | Dense, hybrid, and reranked retrieval |
| Recommendation generation  | Rule-based template              | Grounded LLM generation               |
| Investigation workflow     | Fixed and routed workflow        | One controlled agent                  |
| Predictive risk            | Threshold or logistic model      | LightGBM, XGBoost, or survival model  |

An advanced method will be retained only when evaluation demonstrates meaningful value.

## Recommendation Control Flow

```text
Validated maintenance report
            ↓
Deterministic completeness checks
            ↓
Deterministic safety and escalation rules
            ↓
Structured extraction or model output
            ↓
Schema and evidence validation
            ↓
Retrieval from approved sources
            ↓
Grounded draft recommendation
            ↓
Deterministic policy verification
            ↓
Human approval, editing, or rejection
```

## Mandatory Safety Policies

* An LLM cannot reduce a deterministic critical-risk classification.
* Missing required safety information blocks a final recommendation.
* Obsolete or unapproved documents cannot support safety-critical advice.
* Unsupported claims must be removed, refused, or escalated.
* Consequential recommendations require human approval.
* Agent tools cannot perform prohibited operational actions.
* Model confidence cannot replace evidence requirements.

## Agent Boundary

MaintMind will contain one Maintenance Investigation Agent for complex cases requiring several tools.

Simple and predictable cases will continue through fixed or routed deterministic workflows.

The agent will only be enabled where it demonstrates measurable value over non-agent baselines.

## Alternatives Considered

### LLM-first workflow

Rejected because it would reduce predictability, increase unnecessary model calls, weaken policy enforcement, and make failures harder to diagnose.

### Agent-first workflow

Rejected because many maintenance operations are simple, deterministic, and safer to implement without autonomous tool selection.

### Entirely deterministic system

Rejected because ambiguous technician language, semantic retrieval, predictive risk, and complex investigations may benefit from probabilistic methods.

## Consequences

### Positive

* safety and policy controls remain explicit
* system behaviour is easier to test and audit
* simpler baselines remain visible
* failure causes are easier to isolate
* unnecessary AI latency and cost are reduced
* agent use must be justified by evidence

### Negative

* more foundational engineering is required before AI features
* deterministic rules require versioning and maintenance
* the architecture contains multiple validation layers
* some workflows may be less flexible than fully agentic designs

## Risks and Controls

| Risk                                    | Control                                         |
| --------------------------------------- | ----------------------------------------------- |
| Rules become duplicated or inconsistent | Centralise and version policy logic             |
| AI features bypass baseline evaluation  | Require benchmark evidence before adoption      |
| LLM output is trusted without evidence  | Enforce schema, citation, and policy checks     |
| Agent scope expands                     | Restrict tools, permissions, steps, and costs   |
| Safety rules are bypassed               | Add automated safety and forbidden-action tests |
