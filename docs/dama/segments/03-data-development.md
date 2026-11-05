# 3. Data Development

## Definition

Designing, implementing, and maintaining solutions to meet the data needs of the enterprise.

## Goals

1. Identify and define data requirements.
2. Design data structures and other solutions to these requirements.
3. Implement and maintain solution components that meet these requirements.
4. Ensure solution conformance to data architecture and standards as appropriate.
5. Ensure the integrity, security, usability, and maintainability of structured data assets.

## FAIR Alignment

Direct alignment concerns retrieval through a standardized communications protocol (A1), formal shared representations (I1), qualified references (I3) and provenance (R1.2). Development activities and deliverables can implement these resource and service properties. No additional indirect principle IDs are identified.

| DAMA Segments overview name | FAIR Direct IDs | FAIR Indirect IDs |
|---|---|---|
| 3. Data Development | A1, I1, I3, R1.2 | None identified |

## Business Drivers

### Inputs

- Business Goals and Strategies
- Data Needs and Strategies
- Data Standards
- Data Architecture
- Process Architecture
- Application Architecture
- Technical Architecture

### Activities

1. **Data Modeling, Analysis and Solution Design (D)**
   1. Analyze Information Requirements
   2. Develop and Maintain Conceptual Data Models
   3. Develop and Maintain Logical Data Models
   4. Develop and Maintain Physical Data Models
2. **Detailed Data Design (D)**
   1. Design Physical Databases
   2. Design Information Products
   3. Design Data Access Services
   4. Design Data Integration Services
3. **Data Model and Design Quality Management**
   1. Develop Data Modeling and Design Standards (P)
   2. Review Data Model and Database Design Quality (C)
   3. Manage Data Model Versioning and Integration (C)
4. **Data Implementation (D)**
   1. Implement Development / Test Database Changes
   2. Create and Maintain Test Data
   3. Migrate and Convert Data
   4. Build and Test Information Products
   5. Build and Test Data Access Services
   6. Validate Information Requirements
   7. Prepare for Data Deployment

### Primary Deliverables

- Data Requirements and Business Rules
- Conceptual Data Models
- Logical Data Models and Specifications
- Physical Data Models and Specifications
- Meta-data (Business and Technical)
- Data Modeling and DB Design Standards
- Data Model and DB Design Reviews
- Version Controlled Data Models
- Test Data
- Development and Test Databases
- Information Products
- Data Access Services
- Data Integration Services
- Migrated and Converted Data

## Knowledge Area Roles

### Suppliers

- Data Stewards
- Subject Matter Experts
- IT Steering Committee
- Data Governance Council
- Data Architects and Analysts
- Software Developers
- Data Producers
- Information Consumers

### Participants

- Data Stewards and SMEs
- Data Architects and Analysts
- Database Administrators
- Data Model Administrators
- Software Developers
- Project Managers
- DM Executives and Other IT Management

### Consumers

- Data Producers
- Knowledge Workers
- Managers and Executives
- Customers
- Data Professionals
- Other IT Professionals

## Technical Drivers

### Techniques

These techniques correspond to Data Modeling & Design and apply to the modeling and design activities within this legacy Data Development section.

- Naming conventions
- Forward/reverse engineering
- Approach determination

Source: the **Data Modeling & Design** row in Appendix — Activity Technical Drivers.

### Tools

- Data Modeling Tools
- Database Management Systems
- Software Development Tools
- Testing Tools
- Data Profiling Tools
- Model Management Tools
- Configuration Management Tools
- Office Productivity Tools

### Metrics

Not shown in source.

## Worksheet Detail

Source: DAMA-PDOC_FAIR-MASTER_2026-10-13.xlsx, worksheet **DataDevelopment**. All populated table rows and all 12 columns are reproduced below. Blank cells remain blank; items previously separated by line breaks within cells are separated by semicolons.

| Activities | Deliverables | Responsible Roles | Approving Roles | Contributing Roles | Plan,Develop,Organise,Control | Relevant deliverables | FAIR principles supported | How they can support FAIR | Indirect support | What would demonstrate the supported FAIR requirement | FAIR principles indirectly supported |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Analyze Information Requirements (D)  | Information Requirement Specification Statements | Data Architects, Data Analysts | Data Stewards | Data Stewards, Other SMEs | D |  | No clear FAIR support identified. | Analyze Information Requirements (D)  \[source: DataDevelopment!A2:F2\] — Deliverable: Information Requirement Specification Statements.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Develop and Maintain Conceptual Data Models (D) | Conceptual Data Model Diagrams and Reports | Data Architects, Data Analysts | Data Stewards, Data Architects | Data Stewards, Other SMEs | D | Conceptual Data Model Diagrams and Reports | No clear FAIR support identified. | Develop and Maintain Conceptual Data Models (D) \[source: DataDevelopment!A3:F3\] — Deliverable: Conceptual Data Model Diagrams and Reports.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Develop and Maintain Logical Data Models (D) | Logical Data Model Diagrams and Reports | Data Architects, Data Analysts, Data Modelers | Data Stewards, Data Architects | Data Stewards, Other SMEs | D | Logical Data Model Diagrams and Reports | No clear FAIR support identified. | Develop and Maintain Logical Data Models (D) \[source: DataDevelopment!A4:F4\] — Deliverable: Logical Data Model Diagrams and Reports.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Develop and Maintain Physical Data Models (D) | Physical Data Model Diagrams and Reports | Data Architects, Data Modelers, DBAs | DBAs, Data Architects | Software Developers | D |  | No clear FAIR support identified. | Develop and Maintain Physical Data Models (D) \[source: DataDevelopment!A5:F5\] — Deliverable: Physical Data Model Diagrams and Reports.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Design Physical Databases (D) | DDL Specifications, OLAP Cube Specs, XML schemas | DBAs, Application Architects, Software Developers | Data Architects, DBAs, Application Architects | Data Analysts, Data Modelers, Software Developers | D | DDL Specifications, OLAP Cube Specs, XML schemas | I1 — formal, accessible, shared knowledge representation | Design Physical Databases (D) \[source: DataDevelopment!A6:F6\] — Deliverable: DDL Specifications, OLAP Cube Specs, XML schemas.; Inferred support: XML schemas can support formal machine-readable representation if the implemented language is shared, accessible and broadly applicable. DDL or OLAP specifications alone are not sufficient knowledge representation. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | I1: Inspect the implemented language, shared specification and sample data/metadata representations. Parse them independently and verify that the language is formal, accessible, shared and broadly applicable; schema syntax or diagrams alone are insufficient.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | None identified |
| Design Information Products (D) | Application Screens, Reports | Software Developers | Application Architects | Data Analysts, DBAs | D |  | No clear FAIR support identified. | Design Information Products (D) \[source: DataDevelopment!A7:F7\] — Deliverable: Application Screens, Reports.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Design Data Access Services (D) | Data Access Service Design Specifications | Software Developers, DBAs | Application Architects, Data Architects | Data Analysts, DBAs | D | Data Access Service Design Specifications | A1 — retrieval by identifier via a standard communications protocol | Design Data Access Services (D) \[source: DataDevelopment!A8:F8\] — Deliverable: Data Access Service Design Specifications.; Inferred support: access-service design can specify identifier-based retrieval through a standard protocol; neither identifiers nor protocols are named in the source. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | A1: Starting with an identifier, retrieve representative data and metadata through a documented standard communications protocol; test each separately, including permitted restricted access. A portal, distribution process or accessible database alone is insufficient.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | None identified |
| Design Data Integration Services (D)  | Source-to-Target Maps, ETL Design Specs, Conversion Designs | Data Integration Specialists, DBAs, Data Analysts | DBAs, Data Architects, Application Architects | Data Analysts, Data Stewards, DBAs | D | Source-to-Target Maps, ETL Design Specs, Conversion Designs | I3 — qualified references to other data or metadata; R1.2 — detailed provenance associated with data and metadata | Design Data Integration Services (D)  \[source: DataDevelopment!A9:F9\] — Deliverable: Source-to-Target Maps, ETL Design Specs, Conversion Designs.; Explicit partial support for R1.2: source-to-target maps and ETL/conversion designs record transformation context. Inferred support for I3: those mappings can be expressed as typed references to identifiable source/target resources; design documents alone do not prove implementation. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | I3: Inspect sample data/metadata for references to identifiable related resources with explicit relation types and context; check targets and meanings. Matching keys or diagrammed entity relationships alone are insufficient.; R1.2: Trace representative data and metadata to identified sources, contributors/agents, transformations, dates and versions. Inspect associated provenance records; an unlinked source assessment, ETL design or change log documents only part of the requirement.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | None identified |
| Develop Data Modeling and Database Design Standards (P) | Data Modeling Standards Documents, Database Design Standards Documents | Data Architects, Data Analysts, Data Modelers, DBAs | DM Executive, Data Governance Council | Data Stewards, Application Architects, Software Developers | P | Data Modeling Standards Documents, Database Design Standards Documents | No clear FAIR support identified. | Develop Data Modeling and Database Design Standards (P) \[source: DataDevelopment!A10:F10\] — Deliverable: Data Modeling Standards Documents, Database Design Standards Documents.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Review Data Model and Database Design Quality (C) | Design Review Findings | Data Architects, Data Analysts, Data Modelers, DBAs | DM Executive, Project Manager | Application Architects, Software Developers | C |  | No clear FAIR support identified. | Review Data Model and Database Design Quality (C) \[source: DataDevelopment!A11:F11\] — Deliverable: Design Review Findings.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Manage Data Model Versioning and Integration (C)  | Model Management Libraries and Contents | Data Model Administrators, Data Modelers | Data Architects, DM Executive | Data Analysts, DBAs | C | Model Management Libraries and Contents | R1.2 — detailed provenance associated with data and metadata | Manage Data Model Versioning and Integration (C)  \[source: DataDevelopment!A12:F12\] — Deliverable: Model Management Libraries and Contents.; Explicit partial support: model management libraries and versioning can record the provenance of model artefacts if these are in the FAIR scope. Version records must be associated with released model data/metadata; versioning alone is incomplete provenance. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | R1.2: Trace representative data and metadata to identified sources, contributors/agents, transformations, dates and versions. Inspect associated provenance records; an unlinked source assessment, ETL design or change log documents only part of the requirement.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | None identified |
| Implement Development and Test Database Changes (D) | Dev and Test DB Environments, Database Tables, Other DB Objects | DBAs | DM Executive | Data Architects, Data Analysts, Software Developers | D |  | No clear FAIR support identified. | Implement Development and Test Database Changes (D) \[source: DataDevelopment!A13:F13\] — Deliverable: Dev and Test DB Environments, Database Tables, Other DB Objects.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Create and Maintain Test Data (D) | Test Databases, Test Data | DBAs, Data Analysts, Software Developers, Test Analysts | Data Architects, Application Architects, Data Stewards | Data Stewards, Software Developers, Data Analysts | D |  | No clear FAIR support identified. | Create and Maintain Test Data (D) \[source: DataDevelopment!A14:F14\] — Deliverable: Test Databases, Test Data.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Migrate and Convert Data (D) | Migrated and Converted Data | DBAs, Software Developers | Data Stewards, Data Architects | Data Analysts | D |  | No clear FAIR support identified. | Migrate and Convert Data (D) \[source: DataDevelopment!A15:F15\] — Deliverable: Migrated and Converted Data.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Build and Test Information Products (D) | Information Products: Screens, Reports | Software Developers | Data Stewards, Application Architects, Data Architects | DBAs,Data Analysts | D |  | No clear FAIR support identified. | Build and Test Information Products (D) \[source: DataDevelopment!A16:F16\] — Deliverable: Information Products: Screens, Reports.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Build and Test Data Access Services (D) | Data Access Services,(interfaces) | Software Developers | Data Architects, Application Architects | DBAs | D | Data Access Services,(interfaces) | A1 — retrieval by identifier via a standard communications protocol | Build and Test Data Access Services (D) \[source: DataDevelopment!A17:F17\] — Deliverable: Data Access Services,(interfaces).; Inferred support: built and tested data access services can implement retrieval by identifier using a standard protocol; interface existence and generic service tests are insufficient. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | A1: Starting with an identifier, retrieve representative data and metadata through a documented standard communications protocol; test each separately, including permitted restricted access. A portal, distribution process or accessible database alone is insufficient.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | None identified |
| Build and Test Data Integration Services (D) | Data Integration Services (ETL, etc.) | Data Integration Specialists | Data Stewards, Data Architects | DBAs,Data Analysts | D | Data Integration Services (ETL, etc.) | No clear FAIR support identified. | Build and Test Data Integration Services (D) \[source: DataDevelopment!A18:F18\] — Deliverable: Data Integration Services (ETL, etc.).; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Validate Information Requirements (D) | Validated Requirements, User Acceptance Signoff | Data Stewards, Testing Specialists | Data Stewards | Data Analysts, Data Architects, DBAs | D |  | No clear FAIR support identified. | Validate Information Requirements (D) \[source: DataDevelopment!A19:F19\] — Deliverable: Validated Requirements, User Acceptance Signoff.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Prepare for Data Deployment (D) | User Training, User Documentation | Data Stewards, Business SMEs, Training Specialists, Data Analysts | Data Stewards, Data Architects | Data Stewards, Data Architects, DBAs | D |  | No clear FAIR support identified. | Prepare for Data Deployment (D) \[source: DataDevelopment!A20:F20\] — Deliverable: User Training, User Documentation.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Development standards, design review and testing can incorporate explicit FAIR requirements into released data services and metadata. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
