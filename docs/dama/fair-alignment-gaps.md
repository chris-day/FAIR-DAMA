# FAIR Alignment Gaps

**Version 1.9.0 addition:** DMMaturityAssessment provides an assessment and improvement process but adds no specific FAIR principle IDs. Combined coverage remains ten principles with potential direct alignment and five with indirect alignment only.

**Updated position (version 1.8.0):** Adding the user-supplied DataIntegrationInteroperability analysis brings combined potential coverage to all 15 FAIR principles: ten have direct alignment, and five have indirect alignment only (F1, F3, A1.1, A2, R1.1). A1.1 now has proposed indirect support from integration architecture and data services; it still has no direct mapping. The original ten-segment findings and workbook references below are retained as the historical baseline and exclude the new table.

Across all ten DAMA segments, **10 of the 15 FAIR principles have direct alignment, four have indirect alignment only, and one has no identified alignment**. These counts describe the combined mappings, not the coverage of each segment.

| Gap category | FAIR principle ID | Requirement | Alignment found |
| --- | --- | --- | --- |
| No alignment identified | **A1.1** | The retrieval protocol is open, free and universally implementable. | Neither direct nor indirect |
| Indirect only | **F1** | Data and metadata receive globally unique, persistent identifiers. | Data Architecture Management |
| Indirect only | **F3** | Metadata explicitly includes the identifier of the data it describes | Meta-data Management |
| Indirect only | **A2** | Metadata remains accessible when the data is no longer available. | Meta-data Management; Document & Content Management; Data Operations Management |
| Indirect only | **R1.1** | Data and metadata are released with a clear, accessible data usage licence. | Data Operations Management |

The remaining principles have **potential direct alignment** somewhere in the mappings:

**F2, F4, A1, A1.2, I1, I2, I3, R1, R1.2, R1.3.**

These IDs appear explicitly in column H, **FAIR principles supported**, in the workbook cells listed below. The table identifies every segment in that column that contains each ID. “Potential” reflects the workbook’s assessment of activity and deliverable descriptions; these mappings do not establish implementation or compliance.

| FAIR principle ID | DAMA segment with potential direct alignment | Workbook evidence (column H) |
| --- | --- | --- |
| F2 | 9. Meta-data Management | MetadataManagement!H2, H6 |
| F2 | 8. Document & Content Management | DocumentContentManagement!H8 |
| F4 | 9. Meta-data Management | MetadataManagement!H8, H10 |
| F4 | 7. Data Warehousing & Business Intelligence Management | DWandBIActivities!H5 |
| F4 | 8. Document & Content Management | DocumentContentManagement!H8 |
| A1 | 9. Meta-data Management | MetadataManagement!H9 |
| A1 | 7. Data Warehousing & Business Intelligence Management | DWandBIActivities!H6 |
| A1 | 8. Document & Content Management | DocumentContentManagement!H3, H9 |
| A1 | 3. Data Development | DataDevelopment!H8, H17 |
| A1.2 | 5. Data Security Management | DataSecurityManagement!H5, H6, H7, H8 |
| A1.2 | 8. Document & Content Management | DocumentContentManagement!H3 |
| I1 | 9. Meta-data Management | MetadataManagement!H3, H7 |
| I1 | 3. Data Development | DataDevelopment!H6 |
| I1 | 2. Data Architecture Management | DataArchitectureManagement!H3, H8, H9 |
| I2 | 8. Document & Content Management | DocumentContentManagement!H7 |
| I2 | 2. Data Architecture Management | DataArchitectureManagement!H3, H8 |
| I3 | 9. Meta-data Management | MetadataManagement!H7 |
| I3 | 6. Reference & Master Data Management | ReferenceMasterDataManagement!H7, H8 |
| I3 | 3. Data Development | DataDevelopment!H9 |
| I3 | 2. Data Architecture Management | DataArchitectureManagement!H3, H6 |
| R1 | 9. Meta-data Management | MetadataManagement!H2, H6, H10 |
| R1.2 | 9. Meta-data Management | MetadataManagement!H10 |
| R1.2 | 6. Reference & Master Data Management | ReferenceMasterDataManagement!H3, H7 |
| R1.2 | 3. Data Development | DataDevelopment!H9, H12 |
| R1.2 | 2. Data Architecture Management | DataArchitectureManagement!H6 |
| R1.3 | 9. Meta-data Management | MetadataManagement!H4 |
| R1.3 | 2. Data Architecture Management | DataArchitectureManagement!H8 |

Two distinctions matter when interpreting these gaps:

- **Parent principles do not establish their subprinciples.** Alignment with A1 does not establish A1.1, and alignment with R1 does not establish R1.1.
- **Mapped alignment is not evidence of implementation.** Even the ten directly aligned principles still need implementation evidence and validation. The workbook identifies potential support from activities and deliverables.

The main additions needed are therefore explicit requirements for **persistent identifiers, identifiers within metadata, open retrieval protocols, metadata persistence, and data usage licensing**. In particular, software or technology licensing in operations does not by itself establish a FAIR data usage licence.

Source: [DAMA-PDOC_FAIR-MASTER_2026-10-13.xlsx](../assets/downloads/DAMA-PDOC_FAIR-MASTER_2026-10-13.xlsx), columns H (direct support) and L (indirect support), across the ten segment worksheets from DataGovernance through DataArchitectureManagement.

Added in version 1.2.0.

Version 1.3.0 adds the principle-to-segment table and exact workbook cell references for potential direct alignment.
