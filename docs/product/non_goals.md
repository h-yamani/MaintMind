# MaintMind Non-Goals

## Purpose

MaintMind has a deliberately controlled scope. These non-goals prevent the project from becoming an unfocused collection of technologies or overstating the capabilities of an AI decision-support system.

---

## 1. No Autonomous Safety-Critical Decisions

MaintMind will not autonomously:

* authorise safety-critical maintenance
* approve return-to-service decisions
* execute maintenance actions
* close consequential work orders
* schedule safety-critical work
* override mandatory escalation rules

All consequential actions require an authorised human decision.

---

## 2. No Unsupported Maintenance Instructions

MaintMind will not present maintenance instructions as verified when sufficient approved evidence is unavailable.

The system must refuse, request more information, or escalate when:

* supporting evidence is missing
* available sources conflict
* required safety information is incomplete
* the relevant document is obsolete
* the necessary source is restricted
* the recommendation would require unsupported inference

---

## 3. No False Integration of Unrelated Datasets

MaintMind will not claim that unrelated public datasets describe the same organisation, assets, vehicles, technicians, or maintenance events.

In particular:

* NIST Nestor work orders remain a separate source
* NYC Parks AMPS records remain a separate source
* SCANIA telemetry remains a separate source
* synthetic MaintMind records remain clearly labelled

Cross-source comparisons may be performed, but false record-level joins are prohibited.

---

## 4. No Synthetic-Only Product Claims

Synthetic data supports:

* repeatable testing
* controlled demonstrations
* rare safety scenarios
* malformed-input testing
* agent failure scenarios
* prompt-injection examples

Synthetic results will not be presented as evidence of real organisational performance.

---

## 5. No Agents for Simple Deterministic Operations

MaintMind will not use an agent when a deterministic workflow is:

* more reliable
* easier to test
* easier to audit
* less expensive
* faster
* safer

The investigation agent will only be retained for complex cases where measured evaluation shows value over fixed and routed deterministic baselines.

---

## 6. No Uncontrolled Agent Actions

The agent will not be allowed to:

* edit equipment history
* modify work-order facts
* change access permissions
* change risk rules
* approve recommendations
* execute recommendations
* call unrestricted external tools
* continue beyond configured step or cost limits

Agent tools will be typed, permission-controlled, observable, and tested.

---

## 7. No Foundation-Model Training From Scratch

MaintMind will not train a general-purpose foundation model.

The project focuses on:

* structured model use
* retrieval
* evaluation
* deterministic policies
* workflow engineering
* safety controls
* deployment
* observability

Fine-tuning is optional and only justified by measured failure analysis after the core system is complete.

---

## 8. No Technology Accumulation Without Evidence

Technologies will not be added merely to expand the technology list.

Every major component must have:

* a defined product requirement
* a simpler baseline
* measurable acceptance criteria
* documented trade-offs
* tests
* operational ownership

Optional technologies remain postponed until all core phases are complete.

---

## 9. No Unverified RAG Claims

MaintMind will not claim strong retrieval-augmented generation merely because it uses embeddings or a vector database.

RAG claims require evidence including:

* keyword, dense, and hybrid comparisons
* retrieval metrics
* chunking experiments
* metadata filtering
* document-version handling
* reranking evaluation
* claim-level citation checks
* unsupported-answer detection
* latency and cost measurement
* locked evaluation datasets

---

## 10. No Unverified Agent Claims

MaintMind will not claim agentic value without:

* a versioned scenario dataset
* fixed and routed deterministic baselines
* tool-selection evaluation
* tool-argument evaluation
* trajectory evaluation
* forbidden-action testing
* failure-recovery testing
* cost and latency comparison
* measured value on complex cases

---

## 11. No Publication of Restricted Data

MaintMind will not publish:

* restricted technical manuals
* confidential maintenance records
* private operational information
* personal information without permission
* ambiguously licensed source files
* credentials, secrets, or access tokens

Only public, permission-cleared, or appropriately summarised material will be committed.

---

## 12. No Replacement of Professional Engineering Judgement

MaintMind supports investigation and decision-making. It does not replace:

* qualified maintenance technicians
* reliability engineers
* safety officers
* authorised supervisors
* organisational maintenance policies
* regulatory obligations
* manufacturer-approved instructions

The final responsibility for consequential maintenance decisions remains with authorised professionals.
