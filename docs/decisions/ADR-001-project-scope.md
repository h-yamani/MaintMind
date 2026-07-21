# ADR-001 — MaintMind Project Scope

* **Status:** Accepted
* **Date:** 2026-07-21
* **Decision owners:** Hoda Yamani
* **Related phase:** Phase 0

## Context

MaintMind could expand into many areas, including predictive maintenance, dashboards, document search, workflow automation, generative AI, autonomous agents, cloud infrastructure, and equipment monitoring.

Without a controlled scope, the project could become a collection of disconnected technologies rather than a coherent production AI system.

MaintMind must also provide credible portfolio evidence for senior AI engineering roles. This requires demonstrating architecture, data governance, evaluation, safety, deployment, observability, and technical decision-making through one integrated product story.

## Decision

MaintMind will be developed as:

> An evidence-grounded maintenance intelligence and investigation platform that transforms governed maintenance data and approved technical documents into traceable operational insights and human-approved recommendations.

The primary end-to-end workflow is:

```text
Maintenance report submitted
            ↓
Validation and provenance checks
            ↓
Structured information extraction
            ↓
Risk and recurrence analysis
            ↓
Document and incident retrieval
            ↓
Evidence-grounded recommendation
            ↓
Human approval, editing, or rejection
            ↓
Audit and feedback
```

The project will focus on:

* real-data ingestion and provenance
* reproducible data-quality pipelines
* PostgreSQL modelling and analytical SQL
* deterministic maintenance workflows
* predictive-maintenance modelling
* structured maintenance-text extraction
* evaluated retrieval-augmented generation
* claim-level evidence and citations
* abstention and escalation
* human approval
* reliable asynchronous processing
* one justified maintenance investigation agent
* security and AI governance
* AWS deployment using Terraform
* observability and incident response

## Product Boundaries

MaintMind is a decision-support platform.

It will not autonomously:

* authorise safety-critical maintenance
* execute maintenance recommendations
* close consequential work orders
* return equipment to service
* change risk or safety policy
* alter equipment history
* schedule safety-critical work
* override an authorised human decision

## Data Boundaries

MaintMind will use multiple public datasets for separate technical purposes.

The project will not claim that unrelated datasets represent the same:

* organisation
* equipment
* work order
* technician
* vehicle
* maintenance event

Synthetic data will remain clearly identified and will be used for testing, controlled demonstrations, rare cases, and failure scenarios.

## AI Boundaries

MaintMind will use deterministic processing where deterministic methods are sufficient.

LLMs will be used only where they provide appropriate value, such as:

* structured extraction from ambiguous text
* grounded answer generation
* evidence synthesis
* complex multi-tool investigation

The project will include only one agentic workflow. The agent must demonstrate measurable value over fixed and routed deterministic baselines.

## Alternatives Considered

### Broad AI maintenance platform

This option would include many loosely related capabilities.

**Rejected because:**

* it would increase scope without strengthening the primary product story
* completion would become difficult to define
* evaluation evidence would become fragmented

### Automation prototype using spreadsheets and n8n

This option would prioritise rapid workflow demonstration.

**Rejected as the primary architecture because:**

* it does not demonstrate sufficient backend, data, evaluation, reliability, or cloud engineering depth
* it limits control over auditability and production behaviour
* it does not support the intended senior engineering portfolio positioning

It may remain an optional integration demonstration after the core platform is complete.

### Fully autonomous maintenance agent

This option would allow an agent to plan or execute maintenance actions.

**Rejected because:**

* maintenance decisions may be safety-critical
* autonomous execution would create unacceptable risk
* the project lacks valid organisational authority and live operational integration
* human accountability must remain explicit

## Consequences

### Positive

* the repository communicates one coherent engineering story
* implementation phases have clear dependencies
* evaluation can be tied to product outcomes
* human approval and safety remain central
* optional technologies can be postponed
* portfolio evidence remains credible and auditable

### Negative

* some potentially interesting features will not be implemented
* the complete roadmap requires substantial engineering work
* advanced features cannot begin until foundational gates pass
* the project must maintain strong documentation and evaluation discipline

## Risks

* scope may still expand during RAG or agent development
* planned features may be described as completed before evidence exists
* dashboard or model experiments may distract from the core workflow
* public datasets may be incorrectly interpreted as one operational system

## Risk Controls

* maintain `ROADMAP_STATUS.md`
* complete one phase at a time
* use phase completion gates
* document major decisions through ADRs
* separate implemented and planned capabilities
* preserve source provenance
* evaluate agents against deterministic baselines
* require human approval for consequential actions
