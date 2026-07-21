# Contributing to MaintMind

## Development Principle

MaintMind is developed one roadmap phase at a time.

Do not begin work from a later phase until the current phase completion gate has passed, unless the dependency is explicitly documented.

---

## Before Starting Work

1. Read `README.md`.
2. Read `ROADMAP_STATUS.md`.
3. Confirm the current phase and next exact task.
4. Review the relevant Architecture Decision Records.
5. Create or select a GitHub issue for the work.
6. Confirm that the feature supports the flagship maintenance investigation workflow.

---

## Branch and Commit Practice

Use focused branches where practical:

```text
feature/<short-description>
fix/<short-description>
docs/<short-description>
test/<short-description>
```

Keep commits small and meaningful.

Recommended commit prefixes:

```text
feat:
fix:
test:
docs:
refactor:
chore:
data:
ci:
security:
```

Examples:

```text
feat(ingestion): add idempotent Nestor download
test(ingestion): cover checksum mismatch
docs(data): document Nestor licence limitations
fix(validation): reject duplicate source identifiers
```

Generated files should be committed separately from the code that generates them when this improves traceability.

---

## Code Standards

Reusable production logic belongs under `src/`.

Notebooks are permitted for exploration but must not become the only implementation of reusable logic.

Code should include:

* type hints
* clear names
* focused functions
* structured logging
* explicit error handling
* documented assumptions
* configurable paths
* deterministic behaviour where possible

Avoid:

* hidden global state
* silent exception handling
* hard-coded credentials
* silent file overwrites
* unversioned prompts
* undocumented model choices
* unnecessary abstractions
* technology additions without product value

---

## Testing Requirements

Tests must be added with each feature.

Relevant test categories include:

* unit tests
* ingestion tests
* contract tests
* database tests
* API tests
* integration tests
* evaluation regression tests
* security tests
* failure-injection tests

Before committing, run:

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -v
```

As tooling is introduced, also run:

```bash
ruff check .
black --check .
mypy src
```

A feature is not complete because it works once manually.

---

## Data Requirements

Every ingested or generated record must preserve provenance.

Required provenance fields are:

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

Do not:

* commit restricted datasets
* commit large raw files without justification
* remove original source identifiers
* falsely join unrelated datasets
* describe synthetic data as real operational data
* overwrite frozen versioned fixtures

Use a new version when a frozen fixture changes.

---

## AI and RAG Requirements

LLM and RAG features require measurable baselines and evaluation.

Do not claim RAG quality without:

* a versioned golden question set
* keyword, dense, and hybrid comparisons
* retrieval metrics
* generation evaluation
* citation verification
* abstention testing
* adversarial testing
* latency and cost reporting

Prompt, model, corpus, chunker, and retriever versions must be recorded.

---

## Agent Requirements

Do not use an agent for work that is better handled deterministically.

Agent work requires:

* fixed deterministic baseline
* routed deterministic baseline
* versioned scenario set
* typed tools
* permission checks
* step and cost limits
* forbidden-action tests
* trajectory evaluation
* failure-recovery evaluation
* human approval for consequential actions

The agent is retained only where measured evidence demonstrates value.

---

## Security Requirements

Never commit:

* passwords
* API keys
* AWS access keys
* private tokens
* confidential documents
* personal operational data without permission

Security-sensitive changes must include appropriate tests.

Consequential tools must use:

* least privilege
* typed inputs
* typed outputs
* permission checks
* timeouts
* structured errors
* audit events

---

## Documentation Requirements

Update documentation when a change affects:

* architecture
* data contracts
* source provenance
* user workflow
* security boundaries
* model behaviour
* prompts
* deployment
* operational procedures
* limitations

Record important technical choices in `docs/decisions/`.

Each Architecture Decision Record should include:

* context
* decision
* alternatives
* consequences
* risks
* status

---

## Completion Requirements

Before closing an issue:

* implementation is complete
* tests pass
* documentation is updated
* relevant evidence is saved
* limitations are recorded
* generated outputs are refreshed where required
* `ROADMAP_STATUS.md` is updated
* the phase completion gate remains valid

A phase is not complete until all mandatory gate conditions pass.

