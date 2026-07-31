# MaintMind

## Evidence-Grounded Maintenance Intelligence and Investigation Platform

MaintMind is a production-oriented AI engineering platform that transforms maintenance reports, equipment history, operational data, and technical documentation into traceable insights and evidence-grounded maintenance recommendations.

The project demonstrates the design and implementation of a complete AI product lifecycle—from governed data ingestion and deterministic decision rules to evaluated retrieval-augmented generation, human approval, reliable automation, cloud deployment, and operational monitoring.

MaintMind is built around one central engineering objective:

> Build, evaluate, secure, deploy, and operate an evidence-grounded maintenance investigation platform with deep RAG capabilities and one justified agentic workflow.

---

## Project Status

**Status:** Active development
**Current phase:** Product foundation and real-data preparation
**Current release:** Synthetic data, provenance, validation, operational analytics, reporting, and automated testing foundation

### Implemented

* reproducible synthetic maintenance-data generation
* issue-specific and varied technician reports
* record-level data provenance
* versioned synthetic fixture
* SHA-256 fixture verification
* automated data-quality validation
* maintenance operational profiling
* recurring-failure analysis
* safety and priority analysis
* cost and downtime analysis
* provenance-aware analytics
* generated Markdown business reports
* automated Python tests
* pinned project dependencies
* structured Git history

### In Progress

* product and stakeholder documentation
* architecture decision records
* real-data source registry
* NIST Nestor data ingestion
* NYC Parks AMPS ingestion
* SCANIA telemetry profiling
* PostgreSQL canonical data model
* repository quality and CI controls

### Planned Production Capabilities

* deterministic FastAPI maintenance workflow
* PostgreSQL and pgvector
* predictive equipment-risk modelling
* structured technician-note extraction
* evaluated hybrid RAG
* claim-level citation verification
* abstention and unsupported-answer handling
* human-approved recommendations
* asynchronous processing with SQS
* one evaluated maintenance investigation agent
* AWS deployment using Terraform
* observability, security, incident response, and cost controls

---

## Why MaintMind

Maintenance organisations generate large volumes of technician notes, work orders, inspection records, equipment histories, operational measurements, and technical documents.

Important information is often fragmented across systems and recorded using inconsistent terminology. This can make it difficult to:

* identify recurring failures
* locate the correct maintenance procedure
* distinguish current documents from obsolete instructions
* understand previous corrective actions
* prioritise safety-related reports
* estimate equipment risk
* produce consistent recommendations
* explain the evidence behind a decision
* audit how a recommendation was produced

MaintMind addresses this challenge through an evidence-grounded investigation workflow.

```text
Maintenance report submitted
            ↓
Validation and provenance checks
            ↓
Structured information extraction
            ↓
Risk and recurrence analysis
            ↓
Manual, procedure, and incident retrieval
            ↓
Evidence-grounded recommendation
            ↓
Human approval, editing, or rejection
            ↓
Audit trail and feedback
```

MaintMind is a **decision-support platform**. It does not autonomously authorise safety-critical maintenance activity.

---

## Primary Users

### Maintenance Technician

The technician records equipment observations, symptoms, actions taken, downtime, parts, and follow-up requirements.

MaintMind helps the technician:

* structure incomplete or inconsistent reports
* identify missing information
* access relevant procedures
* locate previous similar incidents
* produce clearer operational records

### Maintenance Planner or Supervisor

The planner reviews maintenance priorities, repeated faults, evidence, safety flags, and proposed actions.

MaintMind helps the planner:

* prioritise urgent reports
* identify recurring equipment problems
* review supporting evidence
* approve, edit, or reject recommendations
* track unresolved maintenance work

### Reliability or Operations Manager

The reliability or operations manager monitors equipment risk, cost, downtime, recurrence, safety exposure, and operational performance.

MaintMind helps the manager:

* identify high-risk assets
* compare maintenance patterns
* monitor operational KPIs
* evaluate recommendation quality
* review human acceptance and rejection trends

---

## Current Engineering Foundation

### Reproducible Synthetic Maintenance Data

The current synthetic-data generator creates repeatable maintenance records using a fixed random seed.

Generated records include:

```text
report_id
report_date
technician_id
technician_name
equipment_id
equipment_name
equipment_type
maintenance_category
issue_type
priority
location
downtime_hours
repair_cost
technician_notes
```

Technician notes use varied, issue-specific repair actions and follow-up recommendations.

The synthetic dataset supports:

* repeatable automated tests
* controlled demonstrations
* malformed-input scenarios
* rare safety cases
* future prompt-injection testing
* future agent failure scenarios

### Data Provenance

Every generated record includes:

```text
source_system
source_dataset
source_record_id
is_synthetic
is_augmented
licence
ingestion_timestamp
schema_version
```

This ensures that synthetic, augmented, and future real records remain distinguishable throughout the system.

The current synthetic fixture is versioned and protected by a SHA-256 checksum.

### Automated Data Validation

The validation framework checks:

* required columns
* missing values
* duplicate report identifiers
* duplicate complete records
* invalid dates
* negative downtime
* negative repair costs
* technician identifier mappings
* equipment identifier mappings
* equipment type consistency
* issue-to-note consistency
* provenance completeness

Validation results are exported to a machine-generated Markdown report.

### Operational Analytics

The current analytics layer produces:

* dataset summaries
* provenance summaries
* missing-value analysis
* duplicate analysis
* maintenance-category distributions
* monthly maintenance volume
* equipment workload
* issue-frequency analysis
* downtime and repair-cost analysis
* technician reporting analysis
* recurring equipment failures
* priority and safety analysis
* location-level maintenance analysis

### Business Reporting

MaintMind generates a maintenance analytics report containing:

* total downtime
* total repair cost
* average repair cost
* critical report count
* equipment-risk ranking
* failure-pattern analysis
* location-level performance
* recurring-failure analysis
* automation opportunities
* assumptions and limitations

---

## Current Evidence

The current version demonstrates:

* 100 reproducible maintenance records
* complete record-level provenance
* zero missing required values
* zero duplicate report identifiers
* zero invalid dates
* zero negative downtime values
* zero negative repair-cost values
* zero technician mapping errors
* zero equipment mapping errors
* zero duplicate source identifiers
* recurring-failure detection
* safety-related issue analysis
* priority-based workload analysis
* equipment, location, technician, and category reporting

These results demonstrate the engineering pipeline. They do not represent real organisational performance.

---

## Data Strategy

MaintMind will use several real public datasets for clearly separated purposes.

Unrelated datasets will not be presented as though they belong to the same organisation.

### NIST Nestor Excavator Work Orders

Primary use:

* real maintenance short text
* technical-language cleaning
* terminology normalisation
* component extraction
* problem and symptom extraction
* corrective-action extraction
* maintenance-type classification
* cost analysis
* annotation experiments
* structured extraction evaluation

### NYC Parks AMPS Work Orders and Assets

Primary use:

* operational work-order ingestion
* asset and work-order joins
* request-to-completion analysis
* status and backlog analysis
* SQL modelling
* analytical views
* operational dashboards
* source-integration and data-quality testing

### SCANIA Component X

Primary use:

* real multivariate telemetry
* equipment-risk modelling
* failure-event prediction
* temporal validation
* probability calibration
* uncertainty analysis
* lead-time analysis
* drift and out-of-distribution analysis

SCANIA telemetry will remain separate from the Nestor and NYC work-order datasets.

### Technical Knowledge Documents

MaintMind will ingest public or permission-cleared:

* equipment manuals
* maintenance procedures
* inspection instructions
* safety documentation
* public standards
* operational guidance
* source data dictionaries

Each document will retain:

* source
* title
* licence
* version
* checksum
* effective date
* superseded date
* approval status
* safety classification
* access-control metadata

Restricted or ambiguously licensed documents will not be published in the repository.

---

## Target Architecture

```text
Technician / Planner / Dashboard
                |
                v
       HTTPS + Load Balancer
                |
                v
          FastAPI on ECS
                |
       -----------------------
       |          |          |
       v          v          v
 PostgreSQL    SQS Jobs   Amazon Bedrock
 + pgvector       |
       |          v
       |       ECS Worker
       |          |
       |    -------------------
       |    |       |         |
       v    v       v         v
      SQL  RAG    Rules   Investigation Agent
       |    |       |         |
       ------------------------
                |
                v
 Evidence-grounded recommendation
                |
                v
          Human approval
                |
                v
        Audit and feedback store
```

---

## Deterministic-First Design

MaintMind establishes deterministic baselines before introducing LLMs or agents.

Deterministic components will handle:

* schema validation
* source-provenance validation
* safety keyword detection
* recurrence calculation
* equipment-history queries
* risk thresholds
* mandatory escalation policies
* approval requirements
* document-version checks
* access-control enforcement
* audit-event creation

LLMs will not be allowed to bypass hard safety or policy rules.

A generated recommendation will not be considered valid unless it includes:

* proposed action
* risk level
* evidence
* explanation
* uncertainty
* limitations
* safety flags
* approval requirement
* rule version
* model version
* prompt version
* source-document version

---

## Predictive Maintenance

The predictive-maintenance module will use real telemetry rather than synthetic work orders.

Candidate models will include:

* threshold or frequency baseline
* logistic regression
* tree-based model
* LightGBM or XGBoost
* optional survival or time-to-event model

Evaluation will include:

* temporal train, validation, and test splits
* precision
* recall
* F1
* PR-AUC
* calibration curves
* Brier score
* false-negative analysis
* subgroup performance
* lead time
* cost-sensitive threshold analysis

Model results will be stored as provenance-aware risk signals and will not be falsely connected to unrelated public work-order assets.

---

## Structured Maintenance-Text Extraction

MaintMind will transform real technician notes into structured fields.

Target fields include:

* equipment or asset
* component
* observed problem
* symptom
* suspected cause
* action taken
* maintenance type
* urgency
* safety indicator
* parts or materials
* completion status
* missing information

The following approaches will be compared on the same locked evaluation set:

1. keyword and regular-expression rules
2. traditional machine-learning or entity model
3. Amazon Bedrock structured-output extraction

Evaluation will include:

* field precision
* field recall
* field F1
* exact match
* classification macro-F1
* schema-valid response rate
* unsupported-field rate
* source-span correctness
* latency
* token usage
* monetary cost
* performance by source and text quality

---

## Evaluation-First RAG

MaintMind will not claim strong RAG merely because documents are stored in a vector database or an LLM generates an answer.

Retrieval and generation will be evaluated separately.

### Retrieval Systems

The following retrieval approaches will be compared:

* PostgreSQL keyword and full-text search
* dense retrieval with pgvector
* hybrid keyword and vector retrieval
* metadata-filtered hybrid retrieval
* hybrid retrieval with reranking
* optional query transformation after failure analysis

### Retrieval Evaluation

Metrics will include:

* Recall@5
* Recall@10
* Precision@5
* mean reciprocal rank
* nDCG@10
* context relevance
* context coverage
* retrieval latency
* retrieval cost
* index size

Results will be reported by question category rather than only as one overall average.

Question categories will include:

* direct fact lookup
* multi-section questions
* equipment-history questions
* similar-incident questions
* multi-source questions
* conflicting-document questions
* outdated-document questions
* unanswerable questions
* safety-critical questions
* adversarial questions

### Grounded Generation

Generated answers must distinguish:

* verified facts
* inferred conclusions
* recommended actions
* missing information
* safety restrictions

Each important factual claim will be linked to:

* document identifier
* document version
* section or page
* chunk identifier
* current or obsolete status
* safety approval status

Generation evaluation will include:

* correctness
* completeness
* relevance
* clarity
* claim-level faithfulness
* unsupported-claim rate
* contradiction rate
* evidence coverage
* citation precision
* citation recall
* citation correctness
* citation completeness
* invalid-citation rate
* abstention precision and recall
* false-refusal rate
* unsafe-answer rate
* latency
* tokens
* cost

Unsupported questions will be refused rather than answered through unsupported inference.

---

## Responsible Agentic Engineering

MaintMind will include one Maintenance Investigation Agent for complex multi-tool investigations.

The agent will not replace deterministic processing for simple cases.

### Read-Only Tools

The agent may use tools such as:

* `get_work_order`
* `get_equipment_details`
* `get_equipment_history`
* `query_approved_analytics_view`
* `search_manuals`
* `find_similar_incidents`
* `get_current_safety_procedure`
* `calculate_deterministic_risk`
* `verify_document_version`

### Controlled Actions

The agent may:

* request missing information
* create a draft recommendation
* escalate to a human reviewer
* record an investigation trace

### Prohibited Autonomous Actions

The agent must not:

* close a work order
* change risk policy
* alter equipment history
* modify maintenance records
* schedule safety-critical work
* authorise maintenance activity
* execute a recommendation

### Agent Evaluation

Three approaches will be compared:

1. fixed deterministic workflow
2. routed deterministic workflow
3. agentic tool-selection workflow

Evaluation will include:

* task success
* correct tool selection
* tool-argument accuracy
* trajectory success
* unnecessary tool calls
* forbidden-tool invocation
* policy violations
* clarification accuracy
* escalation recall
* failure recovery
* maximum-step compliance
* latency
* token usage
* cost
* human preference
* human edit rate

The agent will only be enabled for the subset of cases where it demonstrates measurable value over the routed deterministic baseline.

---

## Human Approval and Auditability

Consequential recommendations require human review.

Reviewers will be able to:

* approve
* edit and approve
* reject
* provide a reason
* record a final action

The audit system will store:

* actor
* action
* previous state
* new state
* request identifier
* correlation identifier
* rule version
* model version
* prompt version
* evidence identifiers
* document versions
* timestamp

This enables every decision to be reconstructed and investigated.

---

## Reliability and Asynchronous Processing

Expensive AI, retrieval, document-processing, and investigation tasks will run outside synchronous API requests.

The planned workflow uses:

* transactional outbox pattern
* Amazon SQS
* ECS workers
* bounded retries
* exponential backoff
* dead-letter queues
* idempotency
* correlation identifiers
* replayable failure records
* inspectable workflow states

Failure testing will include:

* duplicate messages
* worker crashes
* database unavailability
* Bedrock throttling
* malformed messages
* vector-store failure
* approval timeout
* dead-letter replay

---

## Security and Governance

MaintMind treats security, privacy, and AI governance as core product features.

Planned controls include:

* authentication
* role-based access control
* least-privilege IAM
* Secrets Manager
* encryption
* secure file validation
* input-size limits
* rate limiting
* SQL injection prevention
* sensitive-data redaction
* dependency scanning
* container scanning
* prompt-injection testing
* indirect prompt-injection testing
* restricted-document filtering
* agent tool permissions
* agent cost and step limits
* immutable audit events

Governance artifacts will include:

* data cards
* model cards
* prompt-version records
* RAG corpus card
* agent card
* approval policy
* retention policy
* threat models
* limitation statements
* incident classification

---

## AWS and Infrastructure as Code

MaintMind will be deployed using AWS services that complement the architecture demonstrated in the author’s other projects.

Planned services include:

* Amazon ECS Fargate
* Amazon RDS for PostgreSQL
* pgvector
* Amazon S3
* Amazon SQS
* dead-letter queues
* Amazon ECR
* Amazon Bedrock
* AWS Secrets Manager
* AWS IAM
* AWS KMS where appropriate
* Application Load Balancer
* Amazon CloudWatch
* Amazon EventBridge

Terraform will define:

* networking
* subnets
* route tables
* security groups
* ECS services
* ECS task definitions
* ECR repositories
* RDS
* S3 buckets
* SQS queues
* dead-letter queues
* IAM roles
* secret references
* log groups
* alarms

No essential production resource should depend on undocumented manual console configuration.

---

## Observability and Incident Response

MaintMind will monitor system health and AI quality separately.

### System Monitoring

* request volume
* error rate
* p50, p95, and p99 latency
* ECS health
* database connections
* slow queries
* queue depth
* queue age
* retry count
* dead-letter messages

### AI Quality Monitoring

* extraction schema validity
* sampled extraction accuracy
* retrieval success
* empty retrieval rate
* citation correctness
* unsupported claims
* refusal rate
* human rejection rate
* human edit rate
* agent tool errors
* agent step count
* token usage
* cost per request

### Incident Runbooks

Runbooks will cover:

* Bedrock unavailability
* RAG index corruption
* queue backlog
* database migration failure
* prompt-injection incident
* incorrect critical recommendation
* document access leakage
* cost spike

At least one deliberate failure simulation will be conducted and documented.

---

## Technology Stack

### Core Application

* Python
* pandas
* NumPy
* FastAPI
* Pydantic
* SQLAlchemy
* Alembic
* PostgreSQL
* pgvector

### Machine Learning

* scikit-learn
* LightGBM or XGBoost
* MLflow

### AI and RAG

* Amazon Bedrock
* structured LLM outputs
* PostgreSQL full-text search
* dense retrieval
* hybrid retrieval
* metadata filtering
* reranking
* claim-level citations
* abstention policies
* LangGraph or a typed state machine

### Quality and Security

* pytest
* pytest-cov
* Ruff
* Black
* mypy or Pyright
* pre-commit
* Bandit
* pip-audit
* Trivy

### Platform and Delivery

* Docker
* Docker Compose
* GitHub Actions
* Terraform
* Amazon ECS
* Amazon RDS
* Amazon S3
* Amazon SQS
* Amazon ECR
* Amazon CloudWatch

### Supporting Visualisation

* Power BI or Streamlit

The dashboard remains supporting evidence rather than the central purpose of the project.

---

## Repository Structure

```text
MaintMind/
├── data/
│   ├── raw/
│   ├── staged/
│   ├── curated/
│   ├── evaluation/
│   └── synthetic/
│       └── v1/
├── database/
│   ├── migrations/
│   ├── seeds/
│   └── queries/
├── infra/
│   └── terraform/
│       ├── modules/
│       └── environments/
├── src/
│   ├── agents/
│   ├── ai/
│   │   ├── extraction/
│   │   ├── prompts/
│   │   └── providers/
│   ├── analytics/
│   ├── api/
│   ├── audit/
│   ├── contracts/
│   ├── database/
│   ├── data_generation/
│   ├── decision_support/
│   ├── evaluation/
│   ├── ingestion/
│   ├── ml/
│   ├── monitoring/
│   ├── rag/
│   │   ├── ingestion/
│   │   ├── retrieval/
│   │   ├── reranking/
│   │   ├── generation/
│   │   ├── citations/
│   │   └── abstention/
│   ├── rules/
│   ├── security/
│   ├── validation/
│   └── workflows/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── contract/
│   ├── database/
│   ├── evaluation/
│   ├── security/
│   └── failure_injection/
├── docs/
│   ├── architecture/
│   ├── decisions/
│   ├── data/
│   ├── evaluation/
│   ├── governance/
│   ├── product/
│   ├── runbooks/
│   └── security/
├── reports/
├── figures/
├── dashboards/
├── experiments/
├── configs/
├── .github/
│   └── workflows/
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── data_registry.yml
├── ROADMAP_STATUS.md
├── requirements.txt
└── README.md
```

Some directories represent planned phases and will be added as their completion gates are reached.

---

## Running the Current Foundation

### Clone the repository

```bash
git clone https://github.com/h-yamani/MaintMind.git
cd MaintMind
```

### Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Generate the synthetic dataset

```bash
python src/data_generation/synthetic_maintenance_data_generator.py
```

### Validate the dataset

```bash
python src/validation/data_validator.py
```

### Run operational profiling

```bash
python src/analytics/maintenance_operations_profiler.py
```

### Generate the analytics report

```bash
python src/analytics/generate_analytics_report.py
```

### Run automated tests

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -v
```

The plugin-autoload setting prevents unrelated globally installed pytest plugins from affecting the project’s test environment.

---

## Reproducing the Project

MaintMind can be cloned and developed on another computer without downloading the large real datasets.

### Clone and install

```bash
git clone https://github.com/h-yamani/MaintMind.git
cd MaintMind

python -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

### Run the quality checks

```bash
python -m ruff check .
python -m ruff format --check .
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q
```

The standard automated tests use the committed synthetic fixture, so the real datasets are not required for normal development or CI.

### Acquire real datasets when needed

Raw public datasets are downloaded locally and are intentionally excluded from Git.

Download the NIST Nestor excavator work orders:

```bash
python scripts/acquire_real_data.py --source nestor
```

Download the NYC Parks AMPS work orders and assets:

```bash
python scripts/acquire_real_data.py --source nyc_amps
```

Download all currently configured sources:

```bash
python scripts/acquire_real_data.py --source all
```

Verify existing local files and regenerate their manifests without downloading them again:

```bash
python scripts/acquire_real_data.py --source nestor --verify-only
python scripts/acquire_real_data.py --source nyc_amps --verify-only
```

The script records the source identifier, official URL, version, retrieval timestamp, local path, file size, SHA-256 checksum, and approved join rules in `data/manifests/`.

The large raw files remain under `data/real/**/raw/` and are excluded through `.gitignore`. Only the reproducible acquisition code, source registry, manifests, checksums, tests, and documentation are committed to GitHub.

The only approved join between the current NYC AMPS files is:

```text
work_orders.EVT_OBJECT = assets.OBJ_CODE
```

Nestor, NYC AMPS, SCANIA, and technical-document records must remain source-separated unless a documented real-world relationship exists.


---

## Development Roadmap

MaintMind is developed through gated phases:

1. project control and product definition
2. real-data acquisition, licensing, and provenance
3. PostgreSQL canonical data model
4. deterministic production vertical slice
5. controlled operational analytics
6. predictive maintenance
7. golden extraction dataset
8. governed document ingestion
9. retrieval benchmarking
10. grounded generation and citations
11. responsible decision support
12. asynchronous workflows
13. agent scenarios and deterministic baselines
14. one evaluated investigation agent
15. security, privacy, and AI governance
16. AWS deployment with Terraform
17. observability and incident response
18. domain review and final portfolio evidence

A phase is closed only when its tests, completion gate, documentation, and evidence are complete.

Current progress is tracked in [`ROADMAP_STATUS.md`](ROADMAP_STATUS.md).

---

## Scope and Non-Goals

MaintMind will not:

* autonomously authorise safety-critical maintenance
* claim that unrelated public datasets belong to one organisation
* use agents for simple deterministic operations
* provide unsupported maintenance instructions
* allow an LLM to override mandatory safety policies
* publish restricted documents
* train a foundation model from scratch
* add technologies only to increase the tool list
* claim RAG quality without retrieval and generation evaluation
* claim agent value without comparison against deterministic baselines

---

## Current Limitations

* The current operational dataset is synthetic.
* Current analytics demonstrate engineering capability rather than real operational performance.
* Real-data ingestion is under development.
* PostgreSQL, FastAPI, predictive modelling, RAG, asynchronous workflows, the investigation agent, and AWS deployment are roadmap components and are not presented as completed.
* Maintenance recommendations will remain decision-support outputs.
* Consequential actions will require human approval.
* Public datasets will remain source-separated unless a valid relationship is documented.
* Restricted or ambiguously licensed documents will not be committed publicly.

These limitations are explicit to ensure that the repository remains technically credible and does not overstate unfinished capabilities.

---

## Portfolio Evidence

MaintMind is designed to provide visible evidence of capability in:

* AI system architecture
* production Python
* data engineering
* advanced SQL
* machine-learning evaluation
* retrieval-augmented generation
* RAG evaluation
* responsible agentic systems
* backend API engineering
* distributed workflows
* cloud architecture
* infrastructure as code
* security and AI governance
* observability and incident response
* stakeholder communication
* architecture decision-making
* failure analysis
* cost-aware engineering

The project prioritises measurable results, reproducibility, safety, and documented trade-offs over technology-name accumulation.

---

## Author

**Hoda Yamani**

PhD in Computer Systems Engineering
AI Engineer | Machine Learning Engineer | Reinforcement Learning and Robotics Researcher

University of Auckland

