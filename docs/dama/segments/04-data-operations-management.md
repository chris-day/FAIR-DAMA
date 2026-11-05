# 4. Data Operations Management

## Definition

Planning, control, and support for structured data assets across the data lifecycle, from creation and acquisition through archival and purge.

## Goals

1. Protect and ensure the integrity of structured data assets.
2. Manage availability of data throughout its lifecycle.
3. Optimize performance of database transactions.

## FAIR Alignment

No direct principle IDs are identified. Operations provides indirect alignment with keeping metadata accessible after data is no longer available (A2), clear data usage licensing (R1.1), and provenance (R1.2). Retention, technology licensing and operational records require explicit resource-level requirements to support these FAIR outcomes; they do not establish them by themselves.

| DAMA Segments overview name | FAIR Direct IDs | FAIR Indirect IDs |
|---|---|---|
| 4. Data Operations Management | None identified | A2, R1.1, R1.2 |

## Business Drivers

### Inputs

- Data Requirements
- Data Architecture
- Data Models
- Legacy Data
- Service Level Agreements

### Activities

1. **Database Support**
   1. Implement and Control Database Environments (C)
   2. Obtain Externally Sourced Data (O)
   3. Plan for Data Recovery (P)
   4. Backup and Recover Data (O)
   5. Set Database Performance Service Levels (P)
   6. Monitor and Tune Database Performance (C)
   7. Plan for Data Retention (P)
   8. Archive, Retain, and Purge Data (O)
   9. Support Specialized Databases (O)
2. **Data Technology Management**
   1. Understand Data Technology Requirements (P)
   2. Define the Data Technology Architecture (P)
   3. Evaluate Data Technology (P)
   4. Install and Administer Data Technology (C)
   5. Inventory and Track Data Technology Licenses (C)
   6. Support Data Technology Usage and Issues (O)

### Primary Deliverables

- DBMS Technical Environments
- Dev/Test, QA, DR, and Production Databases
- Externally Sourced Data
- Database Performance
- Data Recovery Plans
- Business Continuity
- Data Retention Plan
- Archived and Purged Data

## Knowledge Area Roles

### Suppliers

- Executives
- IT Steering Committee
- Data Governance Council
- Data Stewards
- Data Architects and Modelers
- Software Developers

### Participants

- Database Administrators
- Software Developers
- Project Managers
- Data Stewards
- Data Architects and Analysts
- DM Executives and Other IT Management
- IT Operators

### Consumers

- Data Creators
- Information Consumers
- Enterprise Customers
- Data Professionals
- Other IT Professionals

## Technical Drivers

### Techniques

- Test in Lower Environments
- Physical Naming Standards
- Script Usage for All Changes

Source: the **Data Storage & Operations** row in Appendix — Activity Technical Drivers.

### Tools

- Database Management Systems
- Data Development Tools
- Database Administration Tools
- Office Productivity Tools

### Metrics

- Availability
- Performance

## Worksheet Detail

Source: DAMA-PDOC_FAIR-MASTER_2026-10-13.xlsx, worksheet **DataOperationsManagement**. All populated table rows and all 12 columns are reproduced below. Blank cells remain blank; items previously separated by line breaks within cells are separated by semicolons.

| Activities | Deliverables | Responsible Roles | Approving Roles | Contributing Roles | Plan,Develop,Organise,Control | Relevant deliverables | FAIR principles supported | How they can support FAIR | Indirect support | What would demonstrate the supported FAIR requirement | FAIR principles indirectly supported |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Implement and Control Database Environments (O,C) | Production database environment maintenance, managed changes to production databases, releases | DBAs  | DM Executive | System programmers, data stewards, data analysts, software developers, project managers | O,C |  | No clear FAIR support identified. | Implement and Control Database Environments (O,C) \[source: DataOperationsManagement!A2:F2\] — Deliverable: Production database environment maintenance, managed changes to production databases, releases.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Acquire Externally Sourced Data (O) | Externally sourced data | DBAs, data analysts, data stewards  | Data Governance Council | Data stewards, data analysts  | O |  | No clear FAIR support identified. | Acquire Externally Sourced Data (O) \[source: DataOperationsManagement!A3:F3\] — Deliverable: Externally sourced data.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. Acquisition procedures can capture origin (R1.2) and establish release rights (R1.1), but neither is specified by the externally sourced data deliverable. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | R1.1; R1.2 |
| Plan for Data Recovery (P) | Data availability SLAs, data recovery plans  | DBAs | DM Executive, Data Governance Council |  | P |  | No clear FAIR support identified. | Plan for Data Recovery (P) \[source: DataOperationsManagement!A4:F4\] — Deliverable: Data availability SLAs, data recovery plans.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. Recovery, retention or archives can support availability. A2 additionally requires accessible metadata after the associated data cease to be available; this is not specified. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | A2 |
| Backup and Recover Data (O) | Database backups and logs,restored databases,business continuity | DBAs | DM Executive |  | O |  | No clear FAIR support identified. | Backup and Recover Data (O) \[source: DataOperationsManagement!A5:F5\] — Deliverable: Database backups and logs,restored databases,business continuity.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. Recovery, retention or archives can support availability. A2 additionally requires accessible metadata after the associated data cease to be available; this is not specified. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | A2 |
| Set Database Performance Service Levels (P) | Database performance SLAs | DBAs | DM Executive, Data Governance Council |  | P |  | No clear FAIR support identified. | Set Database Performance Service Levels (P) \[source: DataOperationsManagement!A6:F6\] — Deliverable: Database performance SLAs.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Monitor and Tune Database Performance (O) | Database performance reporting, Database performance | DBAs |  |  | O |  | No clear FAIR support identified. | Monitor and Tune Database Performance (O) \[source: DataOperationsManagement!A7:F7\] — Deliverable: Database performance reporting, Database performance.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Plan for Data Retention (P) | Data retention plan, storage management procedures | DBAs | DM Executive | Storage management specialists | P | Data retention plan, storage management procedures | No clear FAIR support identified. | Plan for Data Retention (P) \[source: DataOperationsManagement!A8:F8\] — Deliverable: Data retention plan, storage management procedures.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. Recovery, retention or archives can support availability. A2 additionally requires accessible metadata after the associated data cease to be available; this is not specified. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. For an A2 extension, withdraw a sample data resource and verify that its retained metadata remain retrievable. | A2 |
| Archive, Retrieve and Purge Data (O) | Archived data, retrieved data, purged data | DBAs | DM Executive |  | O | Archived data, retrieved data, purged data | No clear FAIR support identified. | Archive, Retrieve and Purge Data (O) \[source: DataOperationsManagement!A9:F9\] — Deliverable: Archived data, retrieved data, purged data.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. Recovery, retention or archives can support availability. A2 additionally requires accessible metadata after the associated data cease to be available; this is not specified. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. For an A2 extension, withdraw a sample data resource and verify that its retained metadata remain retrievable. | A2 |
| Manage Specialized Databases (O) | Geospatial databases, CAD / CAM databases, XML databases, object databases | DBAs | DM Executive | Data stewards, Subject matter experts  | O | Geospatial databases, CAD / CAM databases, XML databases, object databases | No clear FAIR support identified. | Manage Specialized Databases (O) \[source: DataOperationsManagement!A10:F10\] — Deliverable: Geospatial databases, CAD / CAM databases, XML databases, object databases.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Understand Data Technology Requirements (P) | Data technology requirements | Data architect, DBAs | DM Executive | Data stewards, other IT professionals | P |  | No clear FAIR support identified. | Understand Data Technology Requirements (P) \[source: DataOperationsManagement!A11:F11\] — Deliverable: Data technology requirements.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Define the Database Architecture (P)  | Data technology architecture | Data architect | DM Executive, Data Governance Council | DBAs, data analysts, data stewards | P | Data technology architecture | No clear FAIR support identified. | Define the Database Architecture (P)  \[source: DataOperationsManagement!A12:F12\] — Deliverable: Data technology architecture.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Evaluate Data Technology (P)  | Tool evaluation findings, tool selection decisions | Data analysts, DBAs | DM Executive, Data Governance Council | Data stewards, other IT professionals | P |  | No clear FAIR support identified. | Evaluate Data Technology (P)  \[source: DataOperationsManagement!A13:F13\] — Deliverable: Tool evaluation findings, tool selection decisions.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Install and Administer Data Technology (O) | Installed technology | DBAs | DM Executive | Data analysts, other data professionals | O |  | No clear FAIR support identified. | Install and Administer Data Technology (O) \[source: DataOperationsManagement!A14:F14\] — Deliverable: Installed technology.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
| Inventory and Track Data Technology Licenses (C) | License inventory | DBAs | DM Executive | Other data professionals | C |  | No clear FAIR support identified. | Inventory and Track Data Technology Licenses (C) \[source: DataOperationsManagement!A15:F15\] — Deliverable: License inventory.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. Technology licences concern software use; they do not establish R1.1 data usage licensing. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. Inspect data usage licences attached to released data/metadata separately from the software licence inventory. | R1.1 |
| Support Data Technology Usage and Issues (O)  | Identified and resolved technology issues | DBAs | DM Executive | Other data professionals | O |  | No clear FAIR support identified. | Support Data Technology Usage and Issues (O)  \[source: DataOperationsManagement!A16:F16\] — Deliverable: Identified and resolved technology issues.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Operations, availability and change management can sustain FAIR infrastructure where the relevant services are commissioned. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | None identified |
