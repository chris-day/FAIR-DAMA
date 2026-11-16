# FAIR Alignment Gaps

**Version 1.9.0 addition:** DMMaturityAssessment provides an assessment and improvement process but adds no specific FAIR principle IDs. Combined coverage remains ten principles with potential direct alignment and five with indirect alignment only.

**Updated position (version 1.8.0):** Adding the user-supplied DataIntegrationInteroperability analysis brings combined potential coverage to all 15 FAIR principles: ten have direct alignment, and five have indirect alignment only ([F1](fair-principles.md#f1-globally-unique-persistent-identification), [F3](fair-principles.md#f3-metadata-explicitly-identifies-the-data-described), [A1.1](fair-principles.md#a11-open-free-and-universally-implementable-retrieval-protocol), [A2](fair-principles.md#a2-metadata-remains-accessible-after-data-becomes-unavailable), [R1.1](fair-principles.md#r11-clear-accessible-data-usage-licence)). [A1.1](fair-principles.md#a11-open-free-and-universally-implementable-retrieval-protocol) now has proposed indirect support from integration architecture and data services; it still has no direct mapping. The original ten-segment findings and workbook references below are retained as the historical baseline and exclude the new table.

Across all ten DAMA segments, **10 of the 15 FAIR principles have direct alignment, four have indirect alignment only, and one has no identified alignment**. These counts describe the combined mappings, not the coverage of each segment.

| Gap category | FAIR principle ID | Requirement | Alignment found |
| --- | --- | --- | --- |
| No alignment identified | **[A1.1](fair-principles.md#a11-open-free-and-universally-implementable-retrieval-protocol)** | The retrieval protocol is open, free and universally implementable. | Neither direct nor indirect |
| Indirect only | **[F1](fair-principles.md#f1-globally-unique-persistent-identification)** | Data and metadata receive globally unique, persistent identifiers. | Data Architecture Management |
| Indirect only | **[F3](fair-principles.md#f3-metadata-explicitly-identifies-the-data-described)** | Metadata explicitly includes the identifier of the data it describes | Meta-data Management |
| Indirect only | **[A2](fair-principles.md#a2-metadata-remains-accessible-after-data-becomes-unavailable)** | Metadata remains accessible when the data is no longer available. | Meta-data Management; Document & Content Management; Data Operations Management |
| Indirect only | **[R1.1](fair-principles.md#r11-clear-accessible-data-usage-licence)** | Data and metadata are released with a clear, accessible data usage licence. | Data Operations Management |

The remaining principles have **potential direct alignment** somewhere in the mappings:

**[F2](fair-principles.md#f2-rich-metadata-describing-data), [F4](fair-principles.md#f4-registration-or-indexing-in-a-searchable-resource), [A1](fair-principles.md#a1-retrieval-by-identifier-through-a-standardized-protocol), [A1.2](fair-principles.md#a12-authentication-and-authorization-where-needed), [I1](fair-principles.md#i1-formal-shared-language-for-knowledge-representation), [I2](fair-principles.md#i2-use-of-vocabularies-that-are-themselves-fair), [I3](fair-principles.md#i3-qualified-references-to-other-data-or-metadata), [R1](fair-principles.md#r1-accurate-relevant-descriptions-sufficient-for-reuse), [R1.2](fair-principles.md#r12-detailed-provenance), [R1.3](fair-principles.md#r13-conformance-to-relevant-community-standards).**

These IDs appear explicitly in column H, **FAIR principles supported**, in the workbook cells listed below. The table identifies every segment in that column that contains each ID. “Potential” reflects the workbook’s assessment of activity and deliverable descriptions; these mappings do not establish implementation or compliance.

| FAIR principle ID | DAMA segment with potential direct alignment | Workbook evidence (column H) |
| --- | --- | --- |
| [F2](fair-principles.md#f2-rich-metadata-describing-data) | Meta-data Management | MetadataManagement!H2, H6 |
| [F2](fair-principles.md#f2-rich-metadata-describing-data) | Document & Content Management | DocumentContentManagement!H8 |
| [F4](fair-principles.md#f4-registration-or-indexing-in-a-searchable-resource) | Meta-data Management | MetadataManagement!H8, H10 |
| [F4](fair-principles.md#f4-registration-or-indexing-in-a-searchable-resource) | Data Warehousing & Business Intelligence Management | DWandBIActivities!H5 |
| [F4](fair-principles.md#f4-registration-or-indexing-in-a-searchable-resource) | Document & Content Management | DocumentContentManagement!H8 |
| [A1](fair-principles.md#a1-retrieval-by-identifier-through-a-standardized-protocol) | Meta-data Management | MetadataManagement!H9 |
| [A1](fair-principles.md#a1-retrieval-by-identifier-through-a-standardized-protocol) | Data Warehousing & Business Intelligence Management | DWandBIActivities!H6 |
| [A1](fair-principles.md#a1-retrieval-by-identifier-through-a-standardized-protocol) | Document & Content Management | DocumentContentManagement!H3, H9 |
| [A1](fair-principles.md#a1-retrieval-by-identifier-through-a-standardized-protocol) | Data Development | DataDevelopment!H8, H17 |
| [A1.2](fair-principles.md#a12-authentication-and-authorization-where-needed) | Data Security Management | DataSecurityManagement!H5, H6, H7, H8 |
| [A1.2](fair-principles.md#a12-authentication-and-authorization-where-needed) | Document & Content Management | DocumentContentManagement!H3 |
| [I1](fair-principles.md#i1-formal-shared-language-for-knowledge-representation) | Meta-data Management | MetadataManagement!H3, H7 |
| [I1](fair-principles.md#i1-formal-shared-language-for-knowledge-representation) | Data Development | DataDevelopment!H6 |
| [I1](fair-principles.md#i1-formal-shared-language-for-knowledge-representation) | Data Architecture Management | DataArchitectureManagement!H3, H8, H9 |
| [I2](fair-principles.md#i2-use-of-vocabularies-that-are-themselves-fair) | Document & Content Management | DocumentContentManagement!H7 |
| [I2](fair-principles.md#i2-use-of-vocabularies-that-are-themselves-fair) | Data Architecture Management | DataArchitectureManagement!H3, H8 |
| [I3](fair-principles.md#i3-qualified-references-to-other-data-or-metadata) | Meta-data Management | MetadataManagement!H7 |
| [I3](fair-principles.md#i3-qualified-references-to-other-data-or-metadata) | Reference & Master Data Management | ReferenceMasterDataManagement!H7, H8 |
| [I3](fair-principles.md#i3-qualified-references-to-other-data-or-metadata) | Data Development | DataDevelopment!H9 |
| [I3](fair-principles.md#i3-qualified-references-to-other-data-or-metadata) | Data Architecture Management | DataArchitectureManagement!H3, H6 |
| [R1](fair-principles.md#r1-accurate-relevant-descriptions-sufficient-for-reuse) | Meta-data Management | MetadataManagement!H2, H6, H10 |
| [R1.2](fair-principles.md#r12-detailed-provenance) | Meta-data Management | MetadataManagement!H10 |
| [R1.2](fair-principles.md#r12-detailed-provenance) | Reference & Master Data Management | ReferenceMasterDataManagement!H3, H7 |
| [R1.2](fair-principles.md#r12-detailed-provenance) | Data Development | DataDevelopment!H9, H12 |
| [R1.2](fair-principles.md#r12-detailed-provenance) | Data Architecture Management | DataArchitectureManagement!H6 |
| [R1.3](fair-principles.md#r13-conformance-to-relevant-community-standards) | Meta-data Management | MetadataManagement!H4 |
| [R1.3](fair-principles.md#r13-conformance-to-relevant-community-standards) | Data Architecture Management | DataArchitectureManagement!H8 |

Two distinctions matter when interpreting these gaps:

- **Parent principles do not establish their subprinciples.** Alignment with [A1](fair-principles.md#a1-retrieval-by-identifier-through-a-standardized-protocol) does not establish [A1.1](fair-principles.md#a11-open-free-and-universally-implementable-retrieval-protocol), and alignment with [R1](fair-principles.md#r1-accurate-relevant-descriptions-sufficient-for-reuse) does not establish [R1.1](fair-principles.md#r11-clear-accessible-data-usage-licence).
- **Mapped alignment is not evidence of implementation.** Even the ten directly aligned principles still need evidence of implementation and validation. The workbook identifies potential support from activities and deliverables.

The main additions needed are therefore explicit requirements for **persistent identifiers, identifiers within metadata, open retrieval protocols, metadata persistence, and data usage licensing**. In particular, software or technology licensing in operations does not by itself establish a FAIR data usage licence.

Source: [DAMA-PDOC_FAIR-MASTER_2026-10-13.xlsx](../assets/downloads/DAMA-PDOC_FAIR-MASTER_2026-10-13.xlsx), columns H (direct support) and L (indirect support), across the ten segment worksheets from DataGovernance through DataArchitectureManagement.

Added in version 1.2.0.

Version 1.3.0 adds the principle-to-segment table and exact workbook cell references for potential direct alignment.
