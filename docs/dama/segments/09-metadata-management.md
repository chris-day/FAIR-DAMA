# 9. Meta-data Management

## Definition

Planning, implementation, and control activities to enable easy access to high quality, integrated meta-data.

## Goals

1. Provide organizational understanding of terms, and usage.
2. Integrate meta-data from diverse source.
3. Provide easy, integrated access to meta-data.
4. Ensure meta-data quality and security.

## FAIR Alignment

Direct alignment spans rich discovery and reuse descriptions (F2, R1), searchable registration (F4), standardized retrieval (A1), formal shared representations (I1), qualified references (I3), provenance (R1.2) and community standards (R1.3). Indirect alignment concerns explicitly including the described data identifier in metadata (F3) and keeping metadata accessible when data is no longer available (A2).

| DAMA Segments overview name | FAIR Direct IDs | FAIR Indirect IDs |
|---|---|---|
| 9. Meta-data Management | F2, F4, A1, I1, I3, R1, R1.2, R1.3 | F3, A2 |

## Business Drivers

### Inputs

- Meta-data Requirements
- Meta-data Issues
- Data Architecture
- Business Meta-data
- Technical Meta-data
- Process Meta-data
- Operational Meta-data
- Data Stewardship Meta-data

### Activities

1. Understand Meta-data Requirements (P)
2. Define the Meta-data Architecture (P)
3. Develop and Maintain Meta-data Standards (P)
4. Implement a Managed Meta-data Environment (D)
5. Create and Maintain Meta-data (O)
6. Integrate Meta-data (C)
7. Manage Meta-data Repositories (C)
8. Distribute and Deliver Meta-data (C)
9. Query, Report, and Analyze Meta-data (O)

### Primary Deliverables

- Meta-data Repositories
- Quality Meta-data
- Meta-data Models and Architecture
- Meta-data Management Operational Analysis
- Meta-data Analysis
- Data Lineage
- Change Impact Analysis
- Meta-data Control Procedures

## Knowledge Area Roles

### Suppliers

- Data Stewards
- Data Architects
- Data Modelers
- Database Administrators
- Other Data Professionals
- Data Brokers
- Government and Industry Regulators

### Participants

- Meta-data Specialist
- Data Integration Architects
- Data Stewards
- Data Architects and Modelers
- Database Administrators
- Other DM Professionals
- Other IT Professionals
- DM Executive
- Business Users

### Consumers

- Data Stewards
- Data Professionals
- Other IT Professionals
- Knowledge Workers
- Managers and Executives
- Customers and Collaborators
- Business Users

## Technical Drivers

### Techniques

- Data Lineage and Impact Analysis
- Metadata for Big Data Ingest

Source: the **Metadata Management** row in Appendix — Activity Technical Drivers.

### Tools

- Meta-data Repositories
- Data Modeling Tools
- Database Management Systems
- Data Integration Tools
- Business Intelligence Tools
- System Management Tools
- Object Modeling Tools
- Process Modeling Tools
- Report Generating Tools
- Data Quality Tools
- Data Development and Administration Tools
- Reference and Master Data Management Tools

### Metrics

- Meta Data Quality
- Master Data Service Data Compliance
- Meta-data Repository Contribution
- Meta-data Documentation Quality
- Steward Representation / Coverage
- Meta-data Usage / Reference
- Meta-data Management Maturity
- Meta-data Repository Availability

## Worksheet Detail

Source: DAMA-PDOC_FAIR-MASTER_2026-10-13.xlsx, worksheet **MetadataManagement**. All populated table rows and all 12 columns are reproduced below. Blank cells remain blank; items previously separated by line breaks within cells are separated by semicolons.

| Activities | Deliverables | Responsible Roles | Approving Roles | Contributing Roles | Plan,Develop,Organise,Control | Relevant deliverables | FAIR principles supported | How they can support FAIR | Indirect support | What would demonstrate the supported FAIR requirement | FAIR principles indirectly supported |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Understand Metadata Requirements (P)  | Metadata requirements  | Metadata Specialists,; Data Stewards,; Data Architects and Modelers,; Database Administrators | Enterprise Data Architect,DM Leader,Data Stewardship Committee, DM Leader,Data Stewardship Committee,Data Stewardship Committee,; DM Leader,Data Stewardship Committee,; Data Stewardship Committee | Other IT Professionals, Other DM Professionals, Other DM Professionals | P |  | F2 — rich metadata describing data; R1 — multiple accurate, relevant descriptive attributes | Understand Metadata Requirements (P)  \[source: MetadataManagement!A2:F2\] — Deliverable: Metadata requirements.; Inferred support: metadata requirements can specify rich discovery and reuse descriptions, but required fields and implementation are not supplied. No implementation evidence is supplied. | Indirect support: Metadata ownership, maintenance and standards can sustain resource coverage, descriptive quality and consistent changes. Specify the data identifier explicitly in metadata for F3 and metadata survival for A2; these requirements are absent from the activity labels. | F2: Inspect representative metadata linked to the described data; validate descriptive fields against a discovery profile covering meaning, scope, creator, temporal coverage and intended use as applicable. A requirements document or tool inventory alone is insufficient.; R1: Validate representative descriptions for multiple accurate and relevant attributes needed for reuse, including meaning, scope, creation context and limitations. Compare with authoritative sources; generic business-data quality is not evidence of rich descriptions.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | F3; A2 |
| Define the Metadata Architecture (P) | Metadata architecture | Metadata Architects,Data Integration Architects | Enterprise Data Architect,; DM Leader,; CDO,; Data Stewardship Committee Database Administrators | Metadata Specialists,; Other Data Mgmt. Professionals,; Other IT Professionals | P | Metadata architecture | I1 — formal, accessible, shared knowledge representation | Define the Metadata Architecture (P) \[source: MetadataManagement!A3:F3\] — Deliverable: Metadata architecture.; Inferred support: metadata architecture can define a shared formal representation. No language or serialisation is specified in the source label. No implementation evidence is supplied. | Indirect support: Metadata ownership, maintenance and standards can sustain resource coverage, descriptive quality and consistent changes. Specify the data identifier explicitly in metadata for F3 and metadata survival for A2; these requirements are absent from the activity labels. | I1: Inspect the implemented language, shared specification and sample data/metadata representations. Parse them independently and verify that the language is formal, accessible, shared and broadly applicable; schema syntax or diagrams alone are insufficient.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | F3; A2 |
| Develop and Maintain Metadata Standards (P) | Metadata standards | Metadata and Data Architects, ; Data Stewards,; Database Administrators | Enterprise Data Architect, DM Leader, Data Stewardship Committee | Other IT Professionals,Other DM Professionals | P | Metadata standards | R1.3 — domain-relevant community standards | Develop and Maintain Metadata Standards (P) \[source: MetadataManagement!A4:F4\] — Deliverable: Metadata standards.; Inferred support: metadata standards can implement community conventions if they are domain-relevant and externally adopted; the source does not identify the standards. No implementation evidence is supplied. | Indirect support: Metadata ownership, maintenance and standards can sustain resource coverage, descriptive quality and consistent changes. Specify the data identifier explicitly in metadata for F3 and metadata survival for A2; these requirements are absent from the activity labels. | R1.3: Identify the domain community and relevant standard/version, then validate representative data and metadata against its applicable requirements. Document exceptions; internal enterprise standards and a mention of an industry standard do not prove conformance.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | F3; A2 |
| Implement a Managed Metadata Environment (D) | Metadata metrics | Database Administrators | Enterprise Data Architect,Data Stewardship Committee,DM Leader | Other IT Professionals | D |  | No clear FAIR support identified. | Implement a Managed Metadata Environment (D) \[source: MetadataManagement!A5:F5\] — Deliverable: Metadata metrics.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Metadata ownership, maintenance and standards can sustain resource coverage, descriptive quality and consistent changes. Specify the data identifier explicitly in metadata for F3 and metadata survival for A2; these requirements are absent from the activity labels. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | F3; A2 |
| Create and Maintain Metadata (O) | Data Modelling Tools,; Database Management Systems,; Data Integration Tools,; Business Intelligence Tools,; System Management Tools,Database Management Systems; Object Modeling Tools,; Process Modeling Tools,; Report Generating Tools,; Data Quality Tools ,; Data Development and Administration Tools,; Reference and Master Data Management Tools | Metadata Specialists, Database Administrators,Data Stewards,; Data Architects and Modelers,Data Stewards | Enterprise Data Architect, DM Leader, Data Stewardship Committee | Other IT Professionals | O |  | F2 — rich metadata describing data; R1 — multiple accurate, relevant descriptive attributes | Create and Maintain Metadata (O) \[source: MetadataManagement!A6:F6\] — Deliverable: Data Modelling Tools,; Database Management Systems,; Data Integration Tools,; Business Intelligence Tools,; System Management Tools,Database Management Systems; Object Modeling Tools,; Process Modeling Tools,; Report Generating Tools,; Data Quality Tools ,; Data Development and Administration Tools,; Reference and Master Data Management Tools.; Explicit partial support: creating and maintaining metadata supplies descriptions that can enable discovery and reuse. The deliverable is a tool list, so metadata richness and accuracy require record-level inspection. No implementation evidence is supplied. | Indirect support: Metadata ownership, maintenance and standards can sustain resource coverage, descriptive quality and consistent changes. Specify the data identifier explicitly in metadata for F3 and metadata survival for A2; these requirements are absent from the activity labels. | F2: Inspect representative metadata linked to the described data; validate descriptive fields against a discovery profile covering meaning, scope, creator, temporal coverage and intended use as applicable. A requirements document or tool inventory alone is insufficient.; R1: Validate representative descriptions for multiple accurate and relevant attributes needed for reuse, including meaning, scope, creation context and limitations. Compare with authoritative sources; generic business-data quality is not evidence of rich descriptions.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | F3; A2 |
| Integrate Metadata (C)  | Integrated Metadata repositories  | Integration Data Architects,; Metadata Specialists,; Data Stewards,; Data Architects and Modelers,; Database Administrators | Enterprise Data Architect, ; DM Leader,; Data Stewardship Committee | Other IT Professionals | C | Integrated Metadata repositories | I1 — formal, accessible, shared knowledge representation; I3 — qualified references to other data or metadata | Integrate Metadata (C)  \[source: MetadataManagement!A7:F7\] — Deliverable: Integrated Metadata repositories.; Inferred support: integrated metadata repositories can exchange shared representations and qualified resource links; technical integration alone does not establish either requirement. No implementation evidence is supplied. | Indirect support: Metadata ownership, maintenance and standards can sustain resource coverage, descriptive quality and consistent changes. Specify the data identifier explicitly in metadata for F3 and metadata survival for A2; these requirements are absent from the activity labels. | I1: Inspect the implemented language, shared specification and sample data/metadata representations. Parse them independently and verify that the language is formal, accessible, shared and broadly applicable; schema syntax or diagrams alone are insufficient.; I3: Inspect sample data/metadata for references to identifiable related resources with explicit relation types and context; check targets and meanings. Matching keys or diagrammed entity relationships alone are insufficient.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | F3; A2 |
| Manage Metadata Repositories (C) | Managed Metadata repositories ,; Administration, ; Principles, Practices, Tactics | Metadata Specialists,Metadata Specialists,; Data Stewards,; Data Architects and Modelers,; Database Administrators | Enterprise Data Architect, ; DM Leader,; Data Stewardship Committee | Other IT Professionals | C | Managed Metadata repositories ,; Administration, ; Principles, Practices, Tactics | F4 — registration/indexing in a searchable resource | Manage Metadata Repositories (C) \[source: MetadataManagement!A8:F8\] — Deliverable: Managed Metadata repositories ,; Administration, ; Principles, Practices, Tactics.; Inferred support: managed metadata repositories can register metadata in a searchable resource if indexing and query facilities are implemented; repository administration alone is insufficient. No implementation evidence is supplied. | Indirect support: Metadata ownership, maintenance and standards can sustain resource coverage, descriptive quality and consistent changes. Specify the data identifier explicitly in metadata for F3 and metadata survival for A2; these requirements are absent from the activity labels. | F4: Search the deployed index/catalogue using several attributes and confirm representative data/metadata records are registered and returned. Database tuning indexes and a repository without search do not establish F4.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | F3; A2 |
| Distribute and Deliver Metadata (O) | Distribution of Metadata, Metadata Models and Architecture | Database Administrators | Enterprise Data Architect,; DM Leader,; Data Stewardship Committee | Metadata Architects | O | Distribution of Metadata, Metadata Models and Architecture | A1 — retrieval by identifier via a standard communications protocol | Distribute and Deliver Metadata (O) \[source: MetadataManagement!A9:F9\] — Deliverable: Distribution of Metadata, Metadata Models and Architecture.; Inferred support: metadata distribution can expose retrievable metadata if delivery is by identifier through a standard protocol; the source does not identify either. No implementation evidence is supplied. | Indirect support: Metadata ownership, maintenance and standards can sustain resource coverage, descriptive quality and consistent changes. Specify the data identifier explicitly in metadata for F3 and metadata survival for A2; these requirements are absent from the activity labels. | A1: Starting with an identifier, retrieve representative data and metadata through a documented standard communications protocol; test each separately, including permitted restricted access. A portal, distribution process or accessible database alone is insufficient.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | F3; A2 |
| Query, Report and Analyse Metadata (O)  | Quality Metadata, Metadata Management Operational Analysis, Metadata Analysis,; Data Lineage,; Change Impact Analysis | Data Analysts,Metadata Analysts | Enterprise Data Architect,DM Leader,Data Stewardship Committee | Business Intelligence Specialists, Data Integration Specialists, Database Administrators, Other Data Mgmt. Professionals, Data Integration Specialists, Database Administrators, Other Data Mgmt. Professionals | O | Quality Metadata, Metadata Management Operational Analysis, Metadata Analysis,; Data Lineage,; Change Impact Analysis | F4 — registration/indexing in a searchable resource; R1 — multiple accurate, relevant descriptive attributes; R1.2 — detailed provenance associated with data and metadata | Query, Report and Analyse Metadata (O)  \[source: MetadataManagement!A10:F10\] — Deliverable: Quality Metadata, Metadata Management Operational Analysis, Metadata Analysis,; Data Lineage,; Change Impact Analysis.; Explicit partial support: metadata query/reporting supports discovery, quality metadata supports reuse descriptions, and the named Data Lineage deliverable supports provenance. Search indexing, rich accurate attributes and detailed associated lineage remain to be verified. No implementation evidence is supplied. | Indirect support: Metadata ownership, maintenance and standards can sustain resource coverage, descriptive quality and consistent changes. Specify the data identifier explicitly in metadata for F3 and metadata survival for A2; these requirements are absent from the activity labels. | F4: Search the deployed index/catalogue using several attributes and confirm representative data/metadata records are registered and returned. Database tuning indexes and a repository without search do not establish F4.; R1: Validate representative descriptions for multiple accurate and relevant attributes needed for reuse, including meaning, scope, creation context and limitations. Compare with authoritative sources; generic business-data quality is not evidence of rich descriptions.; R1.2: Trace representative data and metadata to identified sources, contributors/agents, transformations, dates and versions. Inspect associated provenance records; an unlinked source assessment, ETL design or change log documents only part of the requirement.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | F3; A2 |
