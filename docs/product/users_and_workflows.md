# MaintMind Users and Workflows

## Purpose

MaintMind supports maintenance investigation and decision-making while keeping consequential actions under human control.

The platform has three primary users:

1. maintenance technician
2. maintenance planner or supervisor
3. reliability or operations manager

---

## 1. Maintenance Technician

### Goals

* record maintenance observations accurately
* describe symptoms, faults, and completed actions
* identify equipment requiring follow-up
* access relevant maintenance procedures
* reduce repetitive reporting effort
* ensure important safety information is visible

### Input Data

* technician notes
* equipment identifier
* component or subsystem
* observed symptoms
* maintenance actions performed
* parts or materials used
* downtime
* completion status
* photos or attachments where permitted
* recommended follow-up

### Decisions Made

The technician may decide:

* what observations to record
* whether the report is complete
* whether more inspection information is needed
* whether the equipment should be escalated for review
* whether the proposed structured extraction reflects the original report

### Risks

* incomplete or ambiguous descriptions
* inconsistent terminology
* incorrect equipment identification
* omitted safety information
* unsupported assumptions
* accidental disclosure of restricted information

### Expected Outputs

* validated maintenance report
* extracted equipment, component, symptom, and action fields
* highlighted missing information
* relevant approved procedures
* recurrence indicators
* safety warnings
* draft follow-up actions

### Actions Requiring Approval

The technician cannot use MaintMind to autonomously:

* authorise safety-critical work
* return equipment to service
* close consequential work orders
* change maintenance policy
* modify historical records
* execute generated recommendations

---

## 2. Maintenance Planner or Supervisor

### Goals

* prioritise maintenance work
* identify recurring failures
* review evidence supporting recommendations
* confirm that current procedures are being used
* manage unresolved and high-risk reports
* approve appropriate maintenance actions
* maintain an auditable decision history

### Input Data

* validated work orders
* technician reports
* extracted maintenance fields
* recurrence history
* downtime and repair-cost information
* asset criticality
* deterministic risk results
* relevant procedures and manuals
* similar historical incidents
* predictive risk signals where valid

### Decisions Made

The planner or supervisor may decide:

* work-order priority
* whether further information is required
* whether a recommendation is sufficiently supported
* whether escalation is necessary
* whether to approve, edit, or reject a recommendation
* which follow-up action should be assigned

### Risks

* approving recommendations with insufficient evidence
* relying on obsolete documentation
* overlooking conflicting information
* incorrect prioritisation
* excessive trust in AI-generated content
* failure to escalate a safety-critical issue

### Expected Outputs

* prioritised maintenance investigation
* recurrence and historical context
* deterministic risk level
* relevant current procedures
* traceable supporting evidence
* proposed recommendation
* uncertainty and missing-information summary
* approval requirement
* complete audit record

### Actions Requiring Approval

Only authorised reviewers may:

* approve recommendations
* edit and approve recommendations
* reject recommendations
* assign consequential follow-up work
* confirm safety escalation
* approve return-to-service decisions outside MaintMind

MaintMind records these decisions but does not make them autonomously.

---

## 3. Reliability or Operations Manager

### Goals

* understand equipment reliability trends
* reduce repeated failures
* monitor downtime and maintenance cost
* identify high-risk assets
* assess maintenance process quality
* review recommendation acceptance and rejection
* evaluate whether AI-supported workflows provide operational value

### Input Data

* maintenance work orders
* equipment histories
* recurrence metrics
* cost and downtime measures
* predictive risk signals
* approval outcomes
* human edits and rejections
* safety escalations
* system and AI-quality metrics

### Decisions Made

The reliability or operations manager may decide:

* which assets require investigation
* which recurring problems require systemic action
* whether maintenance policies should be reviewed
* which operational risks require management attention
* whether AI-supported recommendations are sufficiently useful
* whether a model, prompt, rule, or workflow should remain active

### Risks

* misinterpreting data from unrelated sources
* using synthetic results as real business evidence
* relying on poorly calibrated risk scores
* overlooking source limitations
* applying conclusions outside the valid data scope
* optimising operational metrics at the expense of safety

### Expected Outputs

* reliability and recurrence trends
* cost and downtime summaries
* high-risk asset indicators
* source-separated operational analysis
* recommendation acceptance and edit rates
* safety escalation statistics
* model and workflow performance
* documented limitations

### Actions Requiring Approval

Management approval is required for:

* risk-policy changes
* production model activation
* major workflow changes
* access-control changes
* document approval policies
* operational use of new predictive signals
* changes affecting safety-critical processes

---

## Flagship Workflow

```text
Maintenance report submitted
            ↓
Validation and provenance checks
            ↓
Structured information extraction
            ↓
Missing-information detection
            ↓
Risk and recurrence analysis
            ↓
Document and incident retrieval
            ↓
Evidence-grounded recommendation proposal
            ↓
Human approval, editing, or rejection
            ↓
Audit record and feedback
```

---

## Human Approval Boundary

MaintMind may:

* validate data
* extract structured information
* calculate deterministic indicators
* retrieve approved evidence
* identify conflicts
* identify missing information
* generate draft recommendations
* request clarification
* escalate cases for review

MaintMind must not autonomously:

* authorise safety-critical maintenance
* execute a recommendation
* close a work order
* return equipment to service
* change risk policy
* modify equipment history
* schedule consequential maintenance
* override an authorised human decision

---

## Traceability Requirement

Every recommendation and approval must retain:

* source record identifiers
* evidence identifiers
* document versions
* rule version
* model version
* prompt version
* actor
* action
* timestamp
* previous state
* resulting state
* approval or rejection reason
