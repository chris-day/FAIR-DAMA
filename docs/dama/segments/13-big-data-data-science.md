# Big Data & Data Science

Worksheet name: **BigDataDataScience**. This additional DMBOK topic supplements the 11 core knowledge areas. The source identifies this as section 13.

Source: [DAMA activity diagram](../../assets/images/13_BigDataDataScience.webp); activity analysis in the [updated workbook](../../assets/downloads/DAMA-PDOC_FAIR-MASTER_2026-11-16_V3.xlsx). Goals, activity labels, codes, deliverable labels and role lists are transcribed from the diagram. Definitions are working summaries; per-activity deliverable associations, role assignments and FAIR interpretations are proposed.

## Definition

Working summary: Develop and operate data-driven analytical capabilities to investigate business questions, communicate insights and improve analytical models.

## Goals

1. Discover relationships between data and the business.
2. Discover and analyze new factors that might affect the business.
3. Package communications of model outputs for stakeholders and decision-makers.
4. Integrate existing organizational practices with best practices in data management, big data, and data science.

## FAIR Alignment

Conditional potential direct alignment is limited to [R1][fair-r1], through resource-linked hypotheses and method descriptions that can provide accurate, relevant context for reuse. Other activities provide proposed indirect support for metadata descriptions ([F2][fair-f2]), standardized retrieval and access controls ([A1][fair-a1], [A1.1][fair-a1.1], [A1.2][fair-a1.2]), semantic representations and qualified references ([I1][fair-i1], [I3][fair-i3]), reuse descriptions and licences ([R1][fair-r1], [R1.1][fair-r1.1]), provenance ([R1.2][fair-r1.2]), and domain community standards ([R1.3][fair-r1.3]). The named analytics and platform activities alone do not establish those properties.

| DAMA Segments overview name | FAIR Direct IDs | FAIR Indirect IDs |
| --- | --- | --- |
| Big Data & Data Science | [R1][fair-r1] | [F2][fair-f2], [A1][fair-a1], [A1.1][fair-a1.1], [A1.2][fair-a1.2], [I1][fair-i1], [I3][fair-i3], [R1][fair-r1], [R1.1][fair-r1.1], [R1.2][fair-r1.2], [R1.3][fair-r1.3] |

## Business Drivers

### Inputs

- Business Strategy
- Business Case
- Information Requirements
- Information Sources & Metadata
- IT Standards
- Analytical Models
- Data Models

### Activities

1. Define Big Data Strategy & Business Needs (P)
2. Establish Big Data Environments (D)
3. Choose Data Sources (P)
4. Acquire & Ingest Data Sources (D)
5. Develop Hypotheses & Methods (D)
6. Integrate/Align Data For Analysis (D)
7. Explore Data Using Models (D)
8. Communicate Output to Stakeholders (D)
9. Deploy and Monitor (O,C)

### Primary Deliverables

- Big Data Strategy & Standards
- Big Data Landscape
- Data Sourcing Plan
- Acquired Data Sources
- Data Analysis and Hypotheses
- Data Insights and Findings
- Operations Plan
- Model Performance
- Model Enhancement Plan

## Knowledge Area Roles

### Suppliers

- Big Data Platform Architects
- Data Scientists
- Data Producers
- Data Suppliers
- Information Consumers

### Participants

- Data Curators
- Big Data Platform Architects
- Ingestion Architects
- Data SME’s
- Data Scientists
- Analytic Design Lead
- Data Quality and Governance Specialists
- Metadata Specialists

### Consumers

- Business Partners
- Business Executives
- IT Executives
- Intermediaries
- Stakeholders
- Customers

## Technical Drivers

### Techniques

- Analytic Modeling
- Machine Learning Techniques
- Big Data Modeling
- Columnar Compression
- Advanced Supervised Learning

### Tools

- MPP Shared-Nothing Technologies
- Distributed File-based Databases
- In-memory Computing and Databases
- In-database Algorithms
- Big Data Cloud Solutions
- Statistical Computing and Graphical Languages
- Data Visualization Tools

### Metrics

- Technical Usage Metrics
- Loading and Scanning Metrics
- Learnings and Stories
- Response and Performance Metrics
- Data Loading and Scanning Metrics

## Worksheet Detail

Source: **BigDataDataScience!A1:L10** in the updated workbook. Blank values are preserved. P = Planning; D = Development; O = Operational; C = Control. Role assignments and deliverable associations are proposed, not formal assignments specified by the diagram. The repeated loading/scanning metric in the Big Data diagram is retained as written.

| Activities | Deliverables | Responsible Roles | Approving Roles | Contributing Roles | Plan,Develop,Organise,Control | Relevant deliverables | FAIR principles supported | How they can support FAIR | Indirect support | What would demonstrate the supported FAIR requirement | FAIR principles indirectly supported |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Define Big Data Strategy & Business Needs | Big Data Strategy & Standards | Analytic Design Lead; Big Data Platform Architects | Business Executives; IT Executives | Data Scientists; Information Consumers; Data Quality and Governance Specialists | P | Big Data Strategy & Standards |  | A strategy is an enabling decision record; it does not itself establish FAIR properties of data or metadata. | Standards selection can commission domain-relevant community conformance if named external standards, versions and acceptance tests are explicitly adopted. Internal IT standards alone are insufficient. | Inspect approved standards and their domain relevance, then validate actual data and metadata against the applicable community specifications. Strategy approval alone does not demonstrate conformance. | [R1.3][fair-r1.3] |
| Establish Big Data Environments | Big Data Landscape; Operations Plan | Big Data Platform Architects | IT Executives | Ingestion Architects; Metadata Specialists; Data Quality and Governance Specialists | D | Big Data Landscape; Operations Plan |  | A deployed platform, database or cloud service does not establish identifier-based retrieval or an open protocol. | Platform design can enable standardized retrieval, open protocols and controlled access if these are explicitly commissioned and implemented. | Test retrieval of identified data and metadata through a specified standard protocol; inspect freely implementable protocol specifications; test required authentication and authorization. Platform availability alone is insufficient. | [A1][fair-a1]; [A1.1][fair-a1.1]; [A1.2][fair-a1.2] |
| Choose Data Sources | Data Sourcing Plan | Data Scientists; Data Curators | Analytic Design Lead | Data Suppliers; Data Producers; Data SME’s; Data Quality and Governance Specialists | P | Data Sourcing Plan |  | Selecting sources does not by itself publish resource descriptions, provenance or usage licences. | Source evaluation can record origin, permitted reuse and descriptive context, enabling provenance and licensing requirements when resource-linked records and accessible terms are retained. | Trace selected source versions to providers and acquisition context; inspect accessible usage licences linked to each resource. A commercial purchase or access agreement alone is not a FAIR usage licence. | [R1.1][fair-r1.1]; [R1.2][fair-r1.2] |
| Acquire & Ingest Data Sources | Acquired Data Sources | Ingestion Architects; Data Curators | Big Data Platform Architects | Data Suppliers; Data Producers; Data Scientists; Metadata Specialists | D | Acquired Data Sources |  | Ingesting data is not direct evidence of rich metadata or provenance; the diagram does not explicitly specify their capture. | Ingestion can capture resource descriptions, source versions, acquisition times and transformations if metadata capture is added as an explicit requirement. | Inspect descriptions linked to ingested resources and provenance records identifying sources, versions, agents, acquisition times and transformations. Successful loading and scanning alone are insufficient. | [F2][fair-f2]; [R1.2][fair-r1.2] |
| Develop Hypotheses & Methods | Data Analysis and Hypotheses | Data Scientists | Analytic Design Lead | Data SME’s; Data Curators; Metadata Specialists | D | Data Analysis and Hypotheses | [R1][fair-r1] | Inferred potential direct support: documented hypotheses and methods can supply accurate, relevant methodological context for reusing the associated analytical data. The diagram does not establish that these descriptions are complete or associated with identifiable resources. | Versioned methods and input records can enable provenance when linked to the resulting data and model outputs. | For [R1][fair-r1], inspect resource-linked descriptions of hypotheses, methods, assumptions, units, scope and limitations, and verify their accuracy and relevance for reuse. For [R1.2][fair-r1.2], additionally inspect input versions, methods, agents and execution history. An unexplained model or hypothesis list is insufficient. | [R1.2][fair-r1.2] |
| Integrate/Align Data For Analysis | Data Analysis and Hypotheses | Data Scientists; Ingestion Architects | Analytic Design Lead; Big Data Platform Architects | Data Curators; Data SME’s; Metadata Specialists; Data Quality and Governance Specialists | D | Data Analysis and Hypotheses |  | Joining datasets or aligning statistical features does not by itself establish a shared knowledge-representation language or qualified resource references. | Integration can preserve provenance and implement explicit semantic representations and typed links when these requirements are included in the integration design. | Inspect shared formal representations and identifiable resources with typed relations; trace transformations to source versions. Matching columns, feature vectors and internal keys alone are insufficient. | [I1][fair-i1]; [I3][fair-i3]; [R1.2][fair-r1.2] |
| Explore Data Using Models | Data Insights and Findings | Data Scientists | Analytic Design Lead | Data Curators; Data SME’s; Business Partners | D | Data Insights and Findings |  | Exploratory analysis and model accuracy do not inherently establish FAIR descriptions or provenance. | Exploration can enrich reuse descriptions and provenance if assumptions, limitations, source versions, model versions and analytical steps are recorded with the resulting resources. | Inspect resource-linked descriptions of analytical context and limitations and a traceable execution record linking inputs, model versions and outputs. Performance scores alone are insufficient. | [R1][fair-r1]; [R1.2][fair-r1.2] |
| Communicate Output to Stakeholders | Data Insights and Findings | Data Scientists; Analytic Design Lead | Business Executives | Business Partners; Stakeholders; Metadata Specialists; Intermediaries | D | Data Insights and Findings |  | Communicating a chart, presentation or finding does not automatically create rich resource metadata, a searchable registration or standardized retrieval. | Communications can make discovery and reuse context available if findings are accompanied by accurate descriptions linked to the analytical resources. | Inspect resource-linked discovery and reuse descriptions covering meaning, methods, coverage, assumptions and limitations. A presentation without associated resource descriptions is insufficient. | [F2][fair-f2]; [R1][fair-r1] |
| Deploy and Monitor | Operations Plan; Model Performance; Model Enhancement Plan | Big Data Platform Architects; Data Scientists | IT Executives; Business Executives | Analytic Design Lead; Ingestion Architects; Data Quality and Governance Specialists; Metadata Specialists | O,C | Operations Plan; Model Performance; Model Enhancement Plan |  | Deployment, availability and model performance do not directly establish a FAIR principle. | Operations can sustain identifier-based access and record versioned inputs, model changes and execution history when those controls are explicitly included in the operations plan. | Test standardized retrieval of identified resources and inspect version-linked deployment and execution provenance. Monitoring predictive accuracy or infrastructure utilization alone is insufficient. | [A1][fair-a1]; [R1.2][fair-r1.2] |

[fair-f2]: ../fair-principles.md#f2-rich-metadata-describing-data
[fair-a1]: ../fair-principles.md#a1-retrieval-by-identifier-through-a-standardized-protocol
[fair-a1.1]: ../fair-principles.md#a11-open-free-and-universally-implementable-retrieval-protocol
[fair-a1.2]: ../fair-principles.md#a12-authentication-and-authorization-where-needed
[fair-i1]: ../fair-principles.md#i1-formal-shared-language-for-knowledge-representation
[fair-i3]: ../fair-principles.md#i3-qualified-references-to-other-data-or-metadata
[fair-r1]: ../fair-principles.md#r1-accurate-relevant-descriptions-sufficient-for-reuse
[fair-r1.1]: ../fair-principles.md#r11-clear-accessible-data-usage-licence
[fair-r1.2]: ../fair-principles.md#r12-detailed-provenance
[fair-r1.3]: ../fair-principles.md#r13-conformance-to-relevant-community-standards
