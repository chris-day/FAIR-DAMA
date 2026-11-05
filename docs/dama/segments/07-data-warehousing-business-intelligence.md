# 7. Data Warehousing & Business Intelligence Management

## Definition

Planning, implementation, and control processes to provide decision support data and support knowledge workers engaged in reporting, query and analysis.

## Goals

1. To support and enable effective business analysis and decision making by knowledge workers.
2. To build and maintain the environment / infrastructure to support business intelligence activity, specifically leveraging all the other data management functions to cost effectively deliver consistent integrated data for all BI activity.

## FAIR Alignment

Direct alignment concerns registration or indexing in a searchable resource (F4) and retrieval by identifier through a standardized communications protocol (A1). Warehouse discovery and access services can support these requirements when explicitly implemented. No indirect principle IDs are identified.

| DAMA Segments overview name | FAIR Direct IDs | FAIR Indirect IDs |
|---|---|---|
| 7. Data Warehousing & Business Intelligence Management | F4, A1 | None identified |

## Business Drivers

### Inputs

- Business Drivers
- BI Data and Access Requirements
- Data Quality Requirements
- Data Security Requirements
- Data Architecture
- Technical Architecture
- Data Modeling Standards and Guidelines
- Transactional Data
- Master and Reference Data
- Industry and External Data

### Activities

1. Understand Business Intelligence Information Needs (P)
2. Define and Maintain the DW / BI Architecture (P)
3. Implement Data Warehouses and Data Marts (D)
4. Implement BI Tools and User Interfaces (D)
5. Process Data for Business Intelligence (O)
6. Monitor and Tune Data Warehousing Processes (C)
7. Monitor and Tune BI Activity and Performance (C)

### Primary Deliverables

- DW/BI Architecture
- Data Warehouses
- Data Marts and OLAP Cubes
- Dashboards and Scorecards
- Analytic Applications
- File Extracts (for Data Mining / Stat. Tools)
- BI Tools and User Environments
- Data Quality Feedback Mechanism/Loop

## Knowledge Area Roles

### Suppliers

- Executives and Managers
- Subject Matter Experts
- Data Governance Council
- Information Consumers (Internal and External)
- Data Producers
- Data Architects and Analysts

### Participants

- Business Executives and Managers
- DM Execs and Other IT Mgmt
- BI Program Manager
- SMEs and Other Info Consumers
- Data Stewards
- Project Managers
- Data Architects and Analysts
- Data Integration (ETL) Specialists
- BI Specialists
- Database Administrators
- Data Security Administrators
- Data Quality Analysts

### Consumers

- Knowledge Workers
- Managers and Executives
- External Customers and Systems
- Internal Customers and Systems
- Data Professionals
- Other IT Professionals

## Technical Drivers

### Techniques

- Prototypes to Drive Requirements
- Self Service BI
- Queryable Audit Data

Source: the **Data Warehouse & Business Intelligence** row in Appendix — Activity Technical Drivers.

### Tools

- Database Management Systems
- Data Profiling Tools
- Data Integration Tools
- Data Cleansing Tools
- Business Intelligence Tools
- Analytic Applications
- Data Modeling Tools
- Performance Management Tools
- Meta-data Repository
- Data Quality Tools
- Data Security Tools

### Metrics

- Usage Metrics
- Customer/User Satisfaction
- Subject Area Coverage %s
- Response/Performance Metrics

## Worksheet Detail

Source: DAMA-PDOC_FAIR-MASTER_2026-10-13.xlsx, worksheet **DWandBIActivities**. All populated table rows and all 12 columns are reproduced below. Blank cells remain blank; items previously separated by line breaks within cells are separated by semicolons.

| Activities | Deliverables | Responsible Roles | Approving Roles | Contributing Roles | Plan,Develop,Organise,Control | Relevant deliverables | FAIR principles supported | How they can support FAIR | Indirect support | What would demonstrate the supported FAIR requirement | FAIR principles indirectly supported |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Understand Business Intelligence Information Needs (P) | DW-BIM Project Requirements | Data / BI Analyst,BI Program Manager,SME | Data Steward,Business Executives and Managers | Metadata Specialist,Business Process Lead | P |  | No clear FAIR support identified. | Understand Business Intelligence Information Needs (P) \[source: DWandBIActivities!A2:F2\] — Deliverable: DW-BIM Project Requirements.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Warehouse delivery and performance control can sustain consumer-facing datasets and supporting metadata services. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Define the Data Warehouse / BI Architecture (P)  | Data Warehouse / Business Intelligence Architecture | Data Warehouse Architect,Business Intelligence Architect;  | Enterprise Data Architect, DM Executive, CDO,Data Architecture Steering Committee, Data Governance Council;  | Business Intelligence Specialists,Data Integration Specialists, DBAs, Other Data Mgmt. Professionals,IT Architects;  | P | Data Warehouse / Business Intelligence Architecture | No clear FAIR support identified. | Define the Data Warehouse / BI Architecture (P)  \[source: DWandBIActivities!A3:F3\] — Deliverable: Data Warehouse / Business Intelligence Architecture.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Warehouse delivery and performance control can sustain consumer-facing datasets and supporting metadata services. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Implement Data Warehouses and Data Marts (D)  | Data Warehouses, Data Marts, OLAP Cubes | Business Intelligence Specialists | Data Warehouse Architect, Data Stewardship Teams | Data Integration Specialists, DBAs, Other Data Mgmt. Professionals, Other IT Professionals | D |  | No clear FAIR support identified. | Implement Data Warehouses and Data Marts (D)  \[source: DWandBIActivities!A4:F4\] — Deliverable: Data Warehouses, Data Marts, OLAP Cubes.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Warehouse delivery and performance control can sustain consumer-facing datasets and supporting metadata services. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Implement Business Intelligence Tools and User Interfaces (D)  | BI Tools and User Environments, Query and Reporting, Dashboards, Scorecards, Analytic Applications, etc. | Business Intelligence Specialists | Data Warehouse Architect, Data Stewardship Committee, Data Governance Council, Business Executives and Managers | Data Warehouse Architect, Other Data Mgmt. Professionals,, Other IT Professionals | D |  | F4 — registration/indexing in a searchable resource | Implement Business Intelligence Tools and User Interfaces (D)  \[source: DWandBIActivities!A5:F5\] — Deliverable: BI Tools and User Environments, Query and Reporting, Dashboards, Scorecards, Analytic Applications, etc..; Inferred support: query/reporting interfaces can provide searchable registration for datasets or metadata if those resources are indexed. Querying business facts, dashboards or scorecards alone does not establish F4. No implementation evidence is supplied. | Indirect support: Warehouse delivery and performance control can sustain consumer-facing datasets and supporting metadata services. | F4: Search the deployed index/catalogue using several attributes and confirm representative data/metadata records are registered and returned. Database tuning indexes and a repository without search do not establish F4.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | None identified |
| Process Data for Business Intelligence (O) | Accessible Integrated Data, Data Quality Feedback Details | Data Integration Specialists | Data Stewards | Other Data Mgmt. Professionals,Other IT Professionals | O | Accessible Integrated Data, Data Quality Feedback Details | A1 — retrieval by identifier via a standard communications protocol | Process Data for Business Intelligence (O) \[source: DWandBIActivities!A6:F6\] — Deliverable: Accessible Integrated Data, Data Quality Feedback Details.; Inferred support: Accessible Integrated Data can be exposed for retrieval if identified resources are served through a standard protocol; the deliverable does not specify this mechanism. No implementation evidence is supplied. | Indirect support: Warehouse delivery and performance control can sustain consumer-facing datasets and supporting metadata services. | A1: Starting with an identifier, retrieve representative data and metadata through a documented standard communications protocol; test each separately, including permitted restricted access. A portal, distribution process or accessible database alone is insufficient.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | None identified |
| Monitor and Tune Data Warehousing Processes (C)  | DW Performance Reports | DBAs,Data Integration Specialists |  | IT Operators | C |  | No clear FAIR support identified. | Monitor and Tune Data Warehousing Processes (C)  \[source: DWandBIActivities!A7:F7\] — Deliverable: DW Performance Reports.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Warehouse delivery and performance control can sustain consumer-facing datasets and supporting metadata services. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
|  Monitor and Tune BI Activity and Performance (C)  | BI Performance Reports, New Indexes, New Aggregations | Business Intelligence Specialists, DBAs,Business Intelligence Analysts |  | Other Data Mgmt. Professionals,IT Operators,IT Auditors | C |  | No clear FAIR support identified. | Monitor and Tune BI Activity and Performance (C)  \[source: DWandBIActivities!A8:F8\] — Deliverable: BI Performance Reports, New Indexes, New Aggregations.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Warehouse delivery and performance control can sustain consumer-facing datasets and supporting metadata services. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
