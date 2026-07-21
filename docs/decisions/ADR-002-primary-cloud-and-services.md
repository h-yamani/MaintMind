# ADR-002 — Primary Cloud and Service Architecture

* **Status:** Accepted
* **Date:** 2026-07-21
* **Decision owners:** Hoda Yamani
* **Related phases:** Phase 0 and Phase 15

## Context

MaintMind requires a production-oriented architecture that supports:

* synchronous APIs
* relational and vector data
* long-running AI tasks
* asynchronous processing
* document storage
* foundation-model inference
* auditability
* access control
* infrastructure automation
* monitoring
* cost control

The architecture must remain understandable and suitable for a portfolio project while demonstrating credible production engineering.

## Decision

Amazon Web Services will be the primary cloud platform for MaintMind.

The target architecture will use:

* **Amazon ECS Fargate** for the FastAPI application
* **Amazon ECS Fargate workers** for asynchronous processing
* **Amazon RDS for PostgreSQL** as the primary database
* **pgvector** for approved document and incident embeddings
* **Amazon S3** for documents, source artifacts, and evaluation outputs
* **Amazon SQS** for asynchronous jobs
* **SQS dead-letter queues** for permanent failures
* **Amazon ECR** for container images
* **Amazon Bedrock** for embeddings and foundation-model inference
* **AWS Secrets Manager** for credentials and secrets
* **AWS IAM** for role-based service permissions
* **AWS KMS** where additional encryption control is justified
* **Application Load Balancer** for HTTPS application traffic
* **Amazon CloudWatch** for logs, metrics, alarms, and operational dashboards
* **Amazon EventBridge** for scheduled evaluation and maintenance tasks
* **Terraform** for infrastructure provisioning

## Primary Architecture

```text
Technician / Planner / Dashboard
                |
                v
       Application Load Balancer
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

## Service Responsibilities

### FastAPI on ECS

Responsible for:

* authentication and authorisation
* request validation
* report submission
* recommendation retrieval
* approval actions
* audit queries
* job-status queries
* health checks

Long-running AI processing will not block synchronous API requests.

### PostgreSQL and pgvector

Responsible for:

* source registry
* canonical maintenance records
* equipment and work-order data
* recommendations and approvals
* audit events
* document metadata
* document chunks
* vector embeddings
* retrieval events
* model and prompt versions
* agent trajectories

Raw source data will remain logically separated from curated and application schemas.

### SQS and Workers

Responsible for:

* structured extraction jobs
* document ingestion jobs
* retrieval and investigation jobs
* evaluation jobs
* notifications
* retry and failure handling

Workers must support:

* idempotency
* bounded retries
* correlation identifiers
* structured errors
* dead-letter handling
* safe replay

### Amazon Bedrock

Responsible for:

* text embeddings
* structured LLM extraction
* grounded generation
* controlled agent reasoning where justified

Bedrock output will remain subject to:

* deterministic safety rules
* schema validation
* evidence checks
* citation validation
* cost and step limits
* human approval

### S3

Responsible for:

* approved source documents
* source snapshots where licensing permits
* checksums and manifests
* evaluation artifacts
* generated reports
* model and experiment artifacts

S3 object versioning and lifecycle policies will be used where appropriate.

### CloudWatch

Responsible for:

* structured application logs
* worker logs
* request latency
* error rate
* queue depth and age
* retry and dead-letter metrics
* Bedrock failures
* AI-quality monitoring outputs
* cost-related alarms

## Infrastructure as Code

Terraform will define all essential cloud resources.

Manual console configuration will not be considered a valid production deployment process unless the exception is explicitly documented.

The Terraform structure will separate reusable modules and environments:

```text
infra/terraform/
├── modules/
└── environments/
    ├── dev/
    └── demo/
```

## Identity and Secrets

* application code will not contain long-lived credentials
* GitHub Actions will use AWS identity federation where practical
* API and worker services will have separate IAM roles
* Bedrock permissions will be limited to required models and actions
* secrets will be retrieved from Secrets Manager
* database access will be restricted through networking and security groups

## Alternatives Considered

### Serverless-first architecture using Lambda

**Not selected as the primary architecture because:**

* some extraction, ingestion, and agent workflows may exceed comfortable Lambda execution patterns
* container parity between local and cloud environments is valuable
* ECS provides a clearer deployment model for the API and workers

Lambda may still be used for small, bounded tasks where justified.

### Kubernetes

**Rejected for the core project because:**

* it adds significant operational complexity
* the project does not require Kubernetes-specific capabilities
* ECS Fargate sufficiently demonstrates container deployment and service operation
* Kubernetes would distract from the primary AI engineering goals

### Managed Bedrock Knowledge Bases only

**Rejected as the only RAG architecture because:**

* MaintMind must demonstrate retrieval design and evaluation
* custom PostgreSQL and pgvector retrieval enables transparent benchmarking
* keyword, dense, hybrid, metadata-filtered, and reranked retrieval must be compared

Bedrock Knowledge Bases may be included as an optional managed comparison.

### Google Sheets and n8n as the main platform

**Rejected as the production architecture because:**

* relational integrity and source provenance require stronger database controls
* reliable retries, idempotency, access control, and auditability require deeper backend ownership
* it does not provide sufficient production engineering evidence

n8n may remain an optional external integration.

## Consequences

### Positive

* one cloud platform supports application, data, AI, messaging, monitoring, and security
* containers provide consistency between local and cloud execution
* PostgreSQL supports both relational data and vector retrieval
* asynchronous processing separates expensive AI work from API requests
* Terraform makes infrastructure reproducible
* AWS services align with the intended production architecture

### Negative

* AWS deployment introduces ongoing cost
* RDS and ECS require careful teardown and budget controls
* Bedrock availability and model behaviour are external dependencies
* infrastructure implementation will require substantial testing
* local development must provide substitutes for managed services

## Cost Controls

The project will include:

* resource tagging
* AWS budgets and alerts
* small development and demonstration resources
* limited log retention
* Bedrock request budgets
* agent step and token limits
* controlled document-ingestion limits
* documented teardown procedures
* automatic scaling only when justified

## Risks

* excessive infrastructure cost
* over-permissioned IAM roles
* accidental public exposure
* unmanaged secrets
* Bedrock throttling or model changes
* database migration failure
* deployment drift
* manual infrastructure dependencies

## Risk Controls

* Terraform validation and plans
* least-privilege IAM
* private database networking
* Secrets Manager
* deployment smoke tests
* migration and rollback policies
* CloudWatch alarms
* cost budgets
* documented teardown
* failure-injection testing
