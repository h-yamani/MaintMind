# ADR-004 — Real and Synthetic Data Policy

* **Status:** Accepted
* **Date:** 2026-07-23
* **Decision owner:** Hoda Yamani
* **Related phases:** 0, 1, 2, 5, 6, 7, and 18

## Context

MaintMind currently uses a synthetic maintenance dataset for repeatable development, validation, analytics, and testing.

A credible maintenance intelligence platform cannot rely only on synthetic data. Real maintenance text, operational work orders, telemetry, and technical documents are required to demonstrate data engineering, machine learning, retrieval, and production AI capability.

The selected public datasets describe different organisations, equipment, and operating environments. Incorrectly joining them would create false relationships and misleading conclusions.

A formal policy is therefore required for provenance, licensing, source separation, synthetic-data use, augmentation, versioning, and publication.

## Decision

MaintMind will use real public or permission-cleared data as the primary basis for product and evaluation evidence.

Synthetic data will remain an explicitly labelled supporting resource for:

* repeatable automated tests
* controlled demonstrations
* malformed-input scenarios
* rare safety cases
* failure-injection tests
* prompt-injection examples
* agent evaluation scenarios
* development without restricted operational data

Synthetic results will not be presented as real organisational performance.

## Approved Data Roles

### NIST Nestor Excavator Work Orders

Used for:

* real maintenance text
* terminology normalisation
* component, problem, and action extraction
* maintenance-type classification
* cost analysis
* annotation and NLP evaluation

### NYC Parks AMPS Work Orders and Assets

Used for:

* operational work-order ingestion
* asset-to-work-order joins
* completion and backlog analysis
* PostgreSQL modelling
* analytical SQL
* operational dashboards
* data-quality and integration testing

### SCANIA Component X

Used separately for:

* multivariate telemetry
* temporal validation
* failure-risk modelling
* time-to-event analysis
* probability calibration
* uncertainty analysis
* predictive-maintenance signals

SCANIA records will not be connected to Nestor or NYC assets or work orders.

### Synthetic MaintMind Data

Used for:

* unit and integration tests
* controlled analytics examples
* invalid-data tests
* safety edge cases
* future RAG adversarial tests
* future agent trajectory tests

## Required Record Provenance

Every generated, staged, or curated record must retain:

```text
source_system
source_dataset
source_record_id
is_synthetic
is_augmented
licence
schema_version
ingestion_timestamp
```

The combination of `source_dataset` and `source_record_id` must uniquely identify a source record within a versioned ingestion.

## Source Separation Policy

MaintMind will not claim that unrelated public datasets describe the same:

* organisation
* equipment
* technician
* vehicle
* work order
* maintenance event
* operational environment

Cross-source comparisons may examine:

* schema quality
* missingness
* text characteristics
* data volume
* ingestion behaviour
* modelling challenges

Cross-source comparisons must not create fictional record-level relationships.

## Synthetic Fixture Versioning

Frozen synthetic fixtures must:

* live in a versioned directory
* use a recorded random seed
* include configuration metadata
* include a SHA-256 checksum
* remain unchanged after release
* be replaced only by creating a new version

Target structure:

```text
data/synthetic/
├── v1/
│   ├── maintenance_reports.csv
│   ├── fixture_metadata.yml
│   └── maintenance_reports.sha256
└── v2/
```

## Augmented Data

Augmented records must remain distinguishable from original source data.

They must include:

```text
is_augmented = true
```

Augmentation metadata must record:

* original source record
* augmentation method
* augmentation purpose
* model or process version
* creation timestamp
* human-review status where applicable

Augmented records will not be included in locked evaluation sets unless the evaluation explicitly requires them.

## Data Layers

MaintMind will use:

```text
data/raw/<source>/
data/staged/<source>/
data/curated/
data/evaluation/
data/synthetic/
```

### Raw

Original source snapshots or lawful small samples, preserved without semantic transformation.

### Staged

Parsed, typed, normalised, and source-specific data that retains original identifiers.

### Curated

Validated canonical records prepared for application, analytics, or modelling use.

### Evaluation

Versioned development, validation, locked test, safety, and adversarial datasets.

### Synthetic

Versioned generated fixtures and controlled test scenarios.

## Knowledge Documents

MaintMind may use public or permission-cleared:

* equipment manuals
* maintenance procedures
* inspection instructions
* safety documentation
* public standards and guidance
* source data dictionaries

Each document must retain:

* source
* title
* document type
* licence
* version
* checksum
* effective date
* superseded date where applicable
* approval status
* access-control level
* safety classification

Restricted or ambiguously licensed documents will not be committed publicly.

## Publication Policy

The repository may contain:

* ingestion code
* source registry metadata
* checksums
* lawful small samples
* generated synthetic fixtures
* derived aggregate reports
* evaluation configurations
* public or permission-cleared documents

The repository must not contain:

* restricted source files
* confidential maintenance records
* personal information without permission
* private operational documents
* credentials or access tokens
* data with unclear publication rights

## Alternatives Considered

### Synthetic-only development

Rejected because it would not provide credible evidence of real-world ingestion, data quality, terminology, modelling, or retrieval challenges.

### Combining public datasets into one fictional organisation

Rejected because it would create unsupported relationships and misleading analysis.

### Removing synthetic data after real ingestion

Rejected because synthetic fixtures remain valuable for repeatable tests, safety cases, adversarial examples, and controlled demonstrations.

## Consequences

### Positive

* source provenance remains visible
* real-data claims remain credible
* synthetic tests stay reproducible
* licensing and publication risks are controlled
* unrelated datasets cannot be accidentally misrepresented
* evaluation datasets can be versioned and audited

### Negative

* ingestion pipelines must remain source-specific
* data integration requires additional modelling effort
* some source files cannot be committed publicly
* provenance fields must survive every transformation
* separate datasets cannot be used as one operational history

## Risks and Controls

| Risk                                   | Control                                                  |
| -------------------------------------- | -------------------------------------------------------- |
| Synthetic data presented as real       | Visible provenance fields and README limitations         |
| False joins between sources            | Source-specific schemas and prohibited cross-source keys |
| Dataset silently changes               | Checksums, versions, and ingestion manifests             |
| Restricted data is committed           | Licence registry and publication review                  |
| Frozen fixtures are modified           | Versioned directories and checksum tests                 |
| Augmented data contaminates evaluation | Explicit flags and locked-set validation                 |
