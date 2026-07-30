# MaintMind Container Diagram

## Purpose

This diagram shows the main deployable containers inside MaintMind, the users
and external systems that interact with them, and the primary data flows between
the platform components.

## Container Diagram

```mermaid
flowchart TB
    subgraph Users["Users"]
        Manager["Maintenance Manager"]
        Planner["Maintenance Planner"]
        Technician["Maintenance Technician"]
        Analyst["Reliability / Operations Analyst"]
    end

    subgraph External["External Data and Services"]
        CMMS["CMMS / EAM Systems"]
        Telemetry["Equipment Telemetry"]
        Documents["Technical Documents and Manuals"]
        ModelProvider["Approved AI Model Provider"]
    end

    subgraph MaintMind["MaintMind Platform"]
        Web["Web Dashboard"]
        API["Application API<br/>FastAPI"]
        Ingestion["Ingestion and Validation Service<br/>Python"]
        Analytics["Analytics and Risk Service<br/>Python / ML"]
        Investigation["Investigation and Recommendation Service<br/>RAG and Controlled Agents"]
        Worker["Background Jobs and Scheduled Pipelines"]
        Database[("Operational Database<br/>PostgreSQL")]
        Evidence[("Evidence Index<br/>pgvector")]
        ObjectStore[("Document and Dataset Store<br/>S3-compatible")]
        Audit["Audit, Monitoring and Logs"]
    end

    Manager --> Web
    Planner --> Web
    Technician --> Web
    Analyst --> Web

    Web --> API

    CMMS --> Ingestion
    Telemetry --> Ingestion
    Documents --> Ingestion

    Ingestion --> Database
    Ingestion --> Evidence
    Ingestion --> ObjectStore
    Ingestion --> Audit

    API --> Analytics
    API --> Investigation
    API --> Database
    API --> Audit

    Analytics --> Database
    Analytics --> Audit

    Investigation --> Database
    Investigation --> Evidence
    Investigation --> ObjectStore
    Investigation --> ModelProvider
    Investigation --> Audit

    Worker --> Ingestion
    Worker --> Analytics
    Worker --> Investigation
    Worker --> Audit

    API --> Web
```

## Container Responsibilities

- **Web Dashboard:** Presents asset risk, recurring failures, evidence, reports,
  and human-review workflows.
- **Application API:** Provides authenticated access to platform capabilities
  and coordinates requests between the interface and internal services.
- **Ingestion and Validation Service:** Imports source data, validates schemas,
  records provenance, and transforms records into the canonical model.
- **Analytics and Risk Service:** Produces deterministic metrics, recurring
  failure analysis, equipment-risk rankings, and predictive outputs.
- **Investigation and Recommendation Service:** Retrieves supporting evidence
  and creates traceable recommendations subject to human approval.
- **Background Jobs and Scheduled Pipelines:** Runs recurring ingestion,
  validation, analytics, indexing, and monitoring tasks.
- **Data Stores:** Separate operational records, vector evidence, and source
  documents while preserving provenance and audit history.

## Architectural Boundaries

MaintMind does not directly control equipment or automatically approve or
execute maintenance actions. High-impact recommendations must remain
evidence-linked, auditable, and subject to authorised human review.
