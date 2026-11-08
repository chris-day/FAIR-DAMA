# Implementation-oriented alignment for all 15 FAIR principles

This proposed implementation-oriented alignment uses the **11 DMBOK2 knowledge areas**, which differ from the ten areas in the earlier DAMA images—for example, Data Integration & Interoperability is a separate area. These are proposed responsibilities and deliverables that extend beyond what was explicitly identified in the spreadsheet. They are not an official DAMA–FAIR crosswalk. [DAMA-DMBOK framework](https://www.damadmbok.org/dmbok-framework)

In the tables, **Direct** means the proposed deliverable can implement or demonstrate the principle. **Enabling** means the knowledge area supplies policy, architecture or oversight.

**A1.1 concerns the communications protocol**, not whether the software or data is free. Keeping metadata accessible after data deletion belongs to **A2**. Schema.org is a vocabulary rather than a harvesting protocol, and REST alone does not establish A1.1. [GO FAIR’s A1.1 interpretation](https://www.gofair.foundation/a1-1)

The principle descriptions below are abbreviated from the [FAIR Guiding Principles](https://www.gofair.foundation/fair-principles). The knowledge-area assignments and deliverables are proposed expert mappings.

## F1 — Globally unique, persistent identification

| DAMA-DMBOK Knowledge Area | Core Alignment with F1 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Metadata Management | **Direct:** Assign and maintain identifiers for data and metadata resources. | Identifier register; separate data and metadata identifiers; version identification rules. |
| Reference & Master Data Management | **Direct:** Maintain stable entity identifiers and mappings between identifier systems. | Governed namespaces; identifier crosswalks; non-reassignment rules. Internal keys alone do not establish global uniqueness or persistence. |
| Data Storage & Operations | **Direct:** Sustain identifier services through migrations and retirement. | Maintain resolver services; redirect records; monitor persistence. |
| Data Governance | **Enabling:** Establish ownership and long-term commitments for identification. | Identifier policy; accountable custodians; funded persistence arrangements. |

## F2 — Rich metadata describing data

| DAMA-DMBOK Knowledge Area | Core Alignment with F2 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Metadata Management | **Direct:** Capture sufficient description to discover and understand a resource. | Metadata profiles covering subject, creator, scope, coverage, format and access conditions. |
| Data Modeling & Design | **Direct:** Structure metadata fields and relationships for consistent interpretation. | Implemented metadata schemas; field definitions; cardinalities; validation rules. |
| Data Quality Management | **Direct:** Assess completeness and usefulness of discovery metadata. | Required-field checks; description-quality rules; remediation reports. |
| Document & Content Management | **Direct:** Apply descriptive metadata to documents and other content. | Populated content metadata; document classifications; searchable descriptions. |

## F3 — Metadata explicitly identifies the data described

| DAMA-DMBOK Knowledge Area | Core Alignment with F3 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Metadata Management | **Direct:** Record the data identifier explicitly in its metadata. | Mandatory resource-identifier field; distinction between metadata-record ID and data ID. |
| Data Modeling & Design | **Direct:** Model an unambiguous relationship between metadata and the described resource. | Explicit “describes” relationship; version-specific resource references. |
| Data Integration & Interoperability | **Direct:** Preserve identifiers through metadata harvesting and exchange. | Identifier-preserving mappings; round-trip exchange tests. |
| Data Quality Management | **Direct:** Verify identifier presence and correct resource association. | Missing-identifier checks; mismatched-reference detection; identifier consistency tests. |

## F4 — Registration or indexing in a searchable resource

| DAMA-DMBOK Knowledge Area | Core Alignment with F4 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Metadata Management | **Direct:** Register resources in searchable catalogs. | Catalog records; discovery indexes; searchable metadata interfaces. |
| Data Integration & Interoperability | **Direct:** Feed and synchronize metadata with discovery services. | Harvesting connectors; indexing pipelines; update and deletion synchronization. |
| Document & Content Management | **Direct:** Make managed content discoverable through indexed descriptions. | Content indexes; document search; metadata-based filtering. |
| Data Warehousing & Business Intelligence | **Direct:** Register published analytical resources for discovery. | Searchable inventories of datasets, reports and semantic models with stable resource references. |

## A1 — Retrieval by identifier through a standardized protocol

| DAMA-DMBOK Knowledge Area | Core Alignment with A1 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Data Integration & Interoperability | **Direct:** Connect identifiers to standardized retrieval interfaces. | Identifier-based retrieval APIs; documented protocol bindings; retrieval tests. |
| Data Storage & Operations | **Direct:** Operate the services that return identified resources. | Retrieval endpoints; resolver-to-resource routing; availability monitoring. |
| Metadata Management | **Direct:** Support retrieval of metadata and describe data access routes. | Retrievable metadata records; distribution and access-service descriptions. |
| Data Architecture | **Enabling:** Define how identifiers, resolvers and retrieval services work together. | Access architecture; endpoint conventions; service contracts. |

## A1.1 — Open, free and universally implementable retrieval protocol

| DAMA-DMBOK Knowledge Area | Core Alignment with A1.1 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Data Integration & Interoperability | **Direct:** Implement retrieval through protocols that independent clients can implement freely. | HTTP/HTTPS interfaces; documented protocol behavior; independent-client interoperability tests. |
| Metadata Management | **Direct:** Expose metadata through qualifying protocols. | Metadata retrieval over HTTPS; harvesting interfaces using open protocol specifications. |
| Data Architecture | **Enabling:** Select protocols without proprietary implementation dependencies. | Approved protocol catalog; protocol-selection criteria; interoperability architecture. |
| Data Governance | **Enabling:** Require protocol openness in procurement and service approval. | Checks for freely available specifications and unrestricted implementation; exception review. |

## A1.2 — Authentication and authorization where needed

| DAMA-DMBOK Knowledge Area | Core Alignment with A1.2 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Data Security | **Direct:** Provide identity verification and access decisions within the retrieval process. | Authentication services; authorization policies; access-control tests. |
| Data Integration & Interoperability | **Direct:** Integrate protected access into data and metadata interfaces. | Supported authentication flows; token validation; documented access responses. |
| Metadata Management | **Direct:** Describe access conditions and the procedure for obtaining access. | Machine-readable access requirements; authorization-service references. |
| Data Governance | **Enabling:** Assign decision rights for access approval and review. | Access policies; approval responsibilities; periodic entitlement reviews. |

## A2 — Metadata remains accessible after data becomes unavailable

| DAMA-DMBOK Knowledge Area | Core Alignment with A2 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Metadata Management | **Direct:** Retain an accessible description of withdrawn or unavailable data. | Persistent metadata records; withdrawal status; tombstone records. |
| Data Storage & Operations | **Direct:** Preserve metadata services independently of data retention. | Separate metadata retention; service continuity; post-deletion retrieval tests. |
| Document & Content Management | **Direct:** Retain descriptive records when content is disposed of. | Disposition records linked to retained metadata; archival descriptions. |
| Data Governance | **Enabling:** Define metadata survival obligations and ownership. | Metadata retention policy; decommissioning criteria; preservation responsibilities. |

## I1 — Formal, shared language for knowledge representation

| DAMA-DMBOK Knowledge Area | Core Alignment with I1 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Data Modeling & Design | **Direct:** Express meaning and relationships using an appropriate formal representation. | Implemented semantic models; RDF/OWL where appropriate; explicit relation definitions. |
| Metadata Management | **Direct:** Publish metadata in a shared, machine-interpretable representation. | Semantic metadata profiles; documented representation specifications. |
| Data Integration & Interoperability | **Direct:** Preserve meaning when exchanging representations. | Semantic mappings; transformation tests; independently parseable outputs. |
| Data Architecture | **Enabling:** Establish enterprise conventions for knowledge representation. | Approved representation languages; semantic architecture; interoperability patterns. |

A file format or schema alone does not demonstrate that the representation conveys shared meaning.

## I2 — Use of vocabularies that are themselves FAIR

| DAMA-DMBOK Knowledge Area | Core Alignment with I2 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Reference & Master Data Management | **Direct:** Manage and publish reusable vocabularies and code lists as FAIR resources. | Persistent term identifiers; accessible vocabulary versions; licences and provenance. |
| Metadata Management | **Direct:** Reference identified vocabulary terms in metadata. | Vocabulary bindings; vocabulary registry; recorded term and scheme versions. |
| Data Quality Management | **Direct:** Check actual vocabulary use and the FAIR properties of referenced vocabularies. | Term-validity checks; vocabulary assessment; deprecated-term detection. |
| Data Governance | **Enabling:** Assign vocabulary stewardship and approval responsibilities. | Vocabulary lifecycle policy; approved sources; replacement and retirement procedures. |

A controlled vocabulary does not satisfy I2 merely because its terms are standardized internally.

## I3 — Qualified references to other data or metadata

| DAMA-DMBOK Knowledge Area | Core Alignment with I3 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Data Modeling & Design | **Direct:** Specify the meaning of relationships between identified resources. | Typed relationships such as “derived from,” “is version of” and “is part of.” |
| Metadata Management | **Direct:** Record explicit, meaningful links to related resources. | Related-resource metadata; relation types; contextual qualifiers. |
| Data Integration & Interoperability | **Direct:** Preserve and exchange qualified links across systems. | Relationship mappings; linked-resource interfaces; reference-preservation tests. |
| Reference & Master Data Management | **Direct:** Express governed identity and hierarchical relationships. | Qualified entity links; crosswalk semantics; hierarchy and affiliation records. |

## R1 — Accurate, relevant descriptions sufficient for reuse

| DAMA-DMBOK Knowledge Area | Core Alignment with R1 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Metadata Management | **Direct:** Capture the context a consumer needs to assess reuse. | Descriptions of meaning, methods, units, scope, limitations and intended use. |
| Data Quality Management | **Direct:** Validate descriptive attributes and communicate relevant quality limitations. | Metadata accuracy checks; quality statements; documented limitations. |
| Data Modeling & Design | **Direct:** Make interpretation requirements explicit. | Data dictionaries; unit definitions; constraints; missing-value conventions. |
| Data Warehousing & Business Intelligence | **Direct:** Explain how analytical outputs should be interpreted and reused. | Metric definitions; calculation logic; dimensional context; refresh and coverage statements. |

## R1.1 — Clear, accessible data usage licence

| DAMA-DMBOK Knowledge Area | Core Alignment with R1.1 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Metadata Management | **Direct:** Associate each resource with an accessible licence. | Licence identifier or URI; machine-readable licence field; explicit applicability to data and metadata. |
| Document & Content Management | **Direct:** Publish and retain the applicable licence text and version. | Accessible licence documents; resource-to-licence links; retained licence versions. |
| Data Integration & Interoperability | **Direct:** Carry licence information with published and exchanged resources. | Licence fields in distribution metadata; licence-preservation checks. |
| Data Governance | **Enabling:** Establish authority and processes for approving usage terms. | Rights assessment; licence-selection policy; approval and exception records. |

Data Security can enforce access restrictions, but access permission does not itself supply a data usage licence.

## R1.2 — Detailed provenance

| DAMA-DMBOK Knowledge Area | Core Alignment with R1.2 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Metadata Management | **Direct:** Associate resources with their origins and processing history. | Provenance records identifying sources, agents, activities, dates and versions. |
| Data Integration & Interoperability | **Direct:** Capture transformations and movement between resources. | Source-to-target lineage; transformation versions; execution identifiers. |
| Data Warehousing & Business Intelligence | **Direct:** Explain derivation of analytical datasets and measures. | Dataset and column lineage; calculation history; source snapshots. |
| Data Storage & Operations | **Direct:** Preserve operational evidence linked to resource versions. | Ingestion records; version history; retained provenance logs and links. |

## R1.3 — Conformance to relevant community standards

| DAMA-DMBOK Knowledge Area | Core Alignment with R1.3 | Key Technical Deliverables / Targets |
| --- | --- | --- |
| Data Governance | **Enabling:** Identify applicable domain standards and assign responsibility for adoption. | Standards register; adoption policy; documented exceptions and versions. |
| Data Modeling & Design | **Direct:** Implement community information models and constraints. | Conformant schemas; domain model mappings; standard units and representations. |
| Metadata Management | **Direct:** Apply the relevant community metadata requirements. | Community metadata profiles; required descriptive elements; conformance declarations. |
| Data Integration & Interoperability | **Direct:** Exchange resources according to domain standards. | Standard exchange interfaces; implementation guides; interoperability tests. |
| Data Quality Management | **Direct:** Validate actual resources against those standards. | Conformance rules; validation reports; remediation records. |

This broader mapping gives **all 15 principles a proposed implementation home**. It does not change the earlier workbook finding: that assessment identified support in the supplied activities, while this proposal identifies what the knowledge areas **could explicitly implement**, including the previously missing A1.1 alignment.
