# MaintMind Success Metrics

## Purpose

MaintMind success is measured across four areas:

1. data quality
2. AI quality
3. system reliability
4. operational and business value

Targets are initial engineering acceptance goals. They may be revised only after a baseline is measured and the reason is documented.

---

## 1. Data Metrics

### Provenance Completeness

**Definition:** Percentage of records containing all required provenance fields.

Required fields:

* `source_system`
* `source_dataset`
* `source_record_id`
* `is_synthetic`
* `is_augmented`
* `licence`
* `schema_version`
* `ingestion_timestamp`

**Target:** 100%

### Source Identifier Uniqueness

**Definition:** Percentage of curated records with unique combinations of `source_dataset` and `source_record_id`.

**Target:** 100%

### Required-Field Completeness

**Definition:** Percentage of accepted records containing every mandatory field for their source contract.

**Target:** At least 99%

Records failing mandatory validation must be rejected or quarantined.

### Valid Schema Rate

**Definition:** Percentage of ingested records that conform to the expected versioned schema.

**Target:** At least 99%

### Duplicate Ingestion Rate

**Definition:** Percentage of repeated source records that create duplicate curated or database records.

**Target:** 0%

### Reproducible Ingestion

**Definition:** Ability to rerun a source ingestion using the same configuration and obtain the same validated output or a documented source-version change.

**Target:** 100% for versioned source snapshots

### Source Separation

**Definition:** Number of false record-level joins between unrelated public datasets.

**Target:** 0

---

## 2. AI Metrics

### Structured Extraction

Required measures:

* field-level precision
* field-level recall
* field-level F1
* exact match
* schema-valid response rate
* unsupported-field rate
* source-span correctness

Initial targets:

* schema-valid response rate: at least 0.99
* unsupported-field rate: no greater than 0.03
* safety-indicator recall: at least 0.95

### Retrieval

Required measures:

* Recall@5
* Recall@10
* Precision@5
* mean reciprocal rank
* nDCG@10
* retrieval latency
* retrieval cost
* obsolete-document selection
* safety-document retrieval

Initial targets:

* Recall@10: at least 0.85
* MRR: at least 0.70
* nDCG@10: at least 0.75
* safety-document Recall@10: at least 0.95
* obsolete-document first-selection rate: below 0.02

### Grounded Generation

Required measures:

* correctness
* completeness
* claim-level faithfulness
* unsupported-claim rate
* contradiction rate
* evidence coverage
* citation precision
* citation recall
* invalid-citation rate
* unsafe-answer rate

Initial targets:

* citation precision: at least 0.95
* invalid-citation rate: 0
* unsupported-claim rate: no greater than 0.03
* safety-critical escalation recall: 1.00
* schema-valid response rate: at least 0.99

### Abstention

Required measures:

* unanswerable detection precision
* unanswerable detection recall
* false-refusal rate
* unsafe-answer rate

Initial target:

* unanswerable recall: at least 0.90

### Predictive Maintenance

Required measures:

* precision
* recall
* F1
* PR-AUC
* calibration
* Brier score
* false-negative rate
* lead time
* subgroup performance
* cost-sensitive threshold performance

Success requires:

* performance above a documented simple baseline
* temporal evaluation without leakage
* a threshold justified by operational and false-negative costs
* calibrated probabilities or explicit limitations

### Agent Performance

Required measures:

* task success
* tool-selection accuracy
* tool-argument accuracy
* unnecessary tool calls
* forbidden-tool rate
* policy-violation rate
* clarification accuracy
* escalation recall
* failure recovery
* maximum-step compliance
* latency
* token usage
* monetary cost

Initial targets:

* task success: at least 0.85
* tool-selection accuracy: at least 0.90
* forbidden-tool rate: 0
* policy-violation rate: 0
* safety-escalation recall: 1.00
* maximum-step violation rate: 0

The agent must demonstrate measurable value over the routed deterministic workflow on complex scenarios.

---

## 3. System Metrics

### API Reliability

Required measures:

* availability
* request error rate
* p50 latency
* p95 latency
* p99 latency

Initial targets will be established after deployment and load testing.

### Processing Reliability

Required measures:

* report-processing duration
* queue age
* retry count
* dead-letter count
* duplicate-processing rate
* worker-failure recovery

Targets:

* duplicate-processing rate: 0
* permanent failures reach a dead-letter queue: 100%
* replayed jobs do not create duplicate outcomes: 100%

### Audit Completeness

**Definition:** Percentage of consequential recommendations and approval actions containing all required audit fields.

Required fields include:

* actor
* action
* previous state
* resulting state
* request identifier
* timestamp
* rule version
* model version where applicable
* prompt version where applicable
* evidence identifiers
* approval decision

**Target:** 100%

### Security

Targets:

* secrets committed to the repository: 0
* unauthorised restricted-document retrieval: 0
* successful forbidden-agent actions: 0
* unresolved critical dependency vulnerabilities at release: 0
* unsafe safety-policy bypasses: 0

### Reproducibility

Success requires:

* clean local startup from documentation
* clean database creation from migrations
* repeatable locked evaluations
* versioned configuration
* Terraform-based infrastructure creation
* documented rollback and teardown

---

## 4. Business and Operational Metrics

These metrics measure whether MaintMind assists users rather than merely producing technically valid outputs.

### Recommendation Acceptance Rate

**Definition:** Percentage of reviewed recommendations approved without changes.

This metric must be interpreted together with edit rate and safety outcomes.

### Human Edit Rate

**Definition:** Percentage of recommendations modified before approval.

A lower rate may indicate better usefulness, but zero edits are not automatically desirable.

### Human Rejection Rate

**Definition:** Percentage of recommendations rejected by reviewers.

Reasons must be categorised.

### Review Time

**Definition:** Time required for a reviewer to understand the evidence and make a decision.

Success requires measurable improvement compared with the baseline manual workflow.

### Evidence Completeness

**Definition:** Percentage of recommendations containing sufficient traceable evidence for reviewer assessment.

**Target:** At least 0.95

### Missed Safety Escalation

**Definition:** Safety-critical cases that should have been escalated but were not.

**Target:** 0

### Recurring-Failure Visibility

**Definition:** Percentage of known recurring-failure cases correctly surfaced to planners.

A baseline and target will be established using reviewed scenarios.

### User Usefulness

Reviewers will rate:

* relevance
* clarity
* evidence quality
* actionability
* trust
* safety

Success requires documented domain feedback and at least one technical improvement resulting from that feedback.

---

## Metric Governance

Every reported metric must include:

* definition
* dataset version
* evaluation split
* calculation method
* model, prompt, rule, or retriever version
* timestamp
* known limitations

Metrics must not combine unrelated datasets in a way that implies a false organisational relationship.
