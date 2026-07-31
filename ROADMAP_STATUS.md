# MaintMind Roadmap Status

## Progress Dashboard

| Phase | Status | Progress |
|---|---|---:|
| Phase 0 — Project foundation | Complete | 100% |
| Phase 1 — Real-data acquisition, licensing, and provenance | Active | 0% |
| Phase 2 — PostgreSQL canonical data model | Not started | 0% |

## Current Phase

Phase 1 — Real-data acquisition, licensing, and provenance

## Phase 0 Completed

- Product problem statement
- Users, workflows, and human-approval boundaries
- Non-goals
- Data, AI, system, and business success metrics
- Four initial architecture decision records
- Product context diagram
- Container diagram
- Versioned synthetic dataset and SHA-256 verification
- Ruff linting and formatting
- GitHub Actions continuous integration
- Automated tests passing

## Current Evidence

- `docs/product/`
- `docs/decisions/`
- `docs/architecture/`
- `data/synthetic/v1/`
- `pyproject.toml`
- `requirements-dev.txt`
- `.github/workflows/ci.yml`
- `tests/`

## Phase 1 Objective

Acquire approved real public maintenance datasets while recording licensing,
source identity, retrieval details, checksums, versions, intended uses, and
source-separation rules.

## Selected Sources

1. NIST Nestor excavator maintenance work orders
2. NYC Parks AMPS work orders and asset data
3. SCANIA Component X telemetry
4. Permission-cleared technical maintenance documents

## Phase 1 Completion Gate

- [ ] Create the real-data directory structure
- [ ] Create a machine-readable source registry
- [ ] Document source URLs, owners, licences, and intended uses
- [ ] Record access and redistribution restrictions
- [ ] Create an ingestion manifest schema
- [ ] Download or formally register each selected source
- [ ] Generate and verify SHA-256 checksums
- [ ] Preserve dataset versions and retrieval dates
- [ ] Document source-separation and prohibited joins
- [ ] Add provenance validation tests
- [ ] Add a Phase 1 data acquisition report
- [ ] Run linting and automated tests
- [ ] Update this dashboard and activate Phase 2

## Next Exact Task

Create the Phase 1 real-data directory structure and source registry.
