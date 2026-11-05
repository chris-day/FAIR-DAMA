# 11. Data Integration & Interoperability

Worksheet name: **DataIntegrationInteroperability**. This section adds the DMBOK2 knowledge area to the earlier ten-segment structure; the section number is a document continuation, not a DMBOK knowledge-area number.

## Definition

Working summary: Plan, design, develop and operate the movement and transformation of data between sources and consumers so it is available where, when and in the form required.

## Goals

1. Make data available from disparate sources in the format and timeframe needed.
2. Lower cost and complexity by developing shared models and interfaces.
3. Identify meaningful events and automatically trigger alerts and actions.
4. Support business intelligence, analytics, master data management and operational efficiency.

## FAIR Alignment

The supplied table proposes direct alignment with rich discovery and reuse descriptions (F2, R1), searchable registration (F4), protected access procedures (A1.2), and provenance (R1.2). Indirect alignment covers identifier-based retrieval (A1), open retrieval protocols (A1.1), authentication and authorization (A1.2), metadata persistence (A2), shared representations (I1), qualified references (I3), reuse descriptions (R1), provenance (R1.2), and community standards (R1.3). Each mapping remains conditional on the implementation and evidence described in its row.

| DAMA Segments overview name | FAIR Direct IDs | FAIR Indirect IDs |
|---|---|---|
| 11. Data Integration & Interoperability | F2, F4, A1.2, R1, R1.2 | A1, A1.1, A1.2, A2, I1, I3, R1, R1.2, R1.3 |

## Business Drivers

### Activities

The activity table below contains 15 subactivities, grouped under Plan & Analyze, Design DII Solutions, Develop DII Solutions, and Implement and Monitor. Activity names use the agreed prefix_suffix convention.

Role lists below reproduce the supplier, participant and consumer names supplied for this area in the conversation; activity-level responsibility and approval assignments remain proposed.

## Knowledge Area Roles

### Suppliers

- Data Producers
- IT Steering Committee
- Executives and Managers
- Subject Matter Experts

### Participants

- Data Architects
- Business and Data Analysts
- Data Modelers
- Data Stewards
- ETL, Service, Interface Developers
- Project and Program Managers

### Consumers

- Information Consumers
- Knowledge Workers
- Managers and Executives

## Technical Drivers

### Techniques

- Loosely coupled applications
- Minimize the number of interfaces
- Create standard canonical interfaces
- Service Orchestration

Source: the **Data Integration & Interoperability** row in Appendix — Activity Technical Drivers.

## Worksheet Detail

Source: user-supplied Data Integration Interoperability table, provided on 31 October 2026. The duplicate header has been removed; all 15 activity rows and 12 columns are retained, including blanks. Role assignments and deliverable associations are proposed. P = Planning; D = Development; O = Operational. The O code is retained despite the existing column heading. The diagram's activity labels and grouping are retained, including Examine Business Rule Compliance and Maintain DII Metadata under Implement and Monitor.

| Activities | Deliverables | Responsible Roles | Approving Roles | Contributing Roles | Plan,Develop,Organise,Control | Relevant deliverables | FAIR principles supported | How they can support FAIR | Indirect support | What would demonstrate the supported FAIR requirement | FAIR principles indirectly supported |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Plan & Analyze_Define data integration and lifecycle requirements | DII Architecture; Data Exchange Specifications; Data Access Agreements | Business and Data Analysts; Data Stewards; Data Architects | Executives and Managers | Data Producers; Subject Matter Experts; Project and Program Managers | P | Business and technical metadata; integration, access and retention requirements | F2; R1 | Requirements analysis creates descriptive metadata that can explain resource meaning, structure, context and intended use. | Access and retention requirements can commission protected retrieval and metadata preservation when explicitly included. | Inspect populated metadata associated with identified resources for accurate discovery and reuse descriptions. For indirect support, inspect explicit authentication requirements and independent metadata-retention requirements. | A1.2; A2 |
| Plan & Analyze_Perform Data Discovery | DII Architecture; Data Exchange Specifications | Business and Data Analysts; Data Architects | | Data Producers; Subject Matter Experts; Data Stewards | P | Organizational data inventory maintained in a metadata repository | F2; F4 | Discovery can enrich resource descriptions and register resources in a searchable inventory. F4 depends on the inventory being searchable. | Source suitability findings can improve descriptions of scope, limitations and fitness for reuse. | Inspect inventory entries linked to identified datasets; test search retrieval; verify descriptions against actual sources. For R1, verify that reuse-relevant findings are incorporated into metadata. | R1 |
| Plan & Analyze_Document Data Lineage | Data Exchange Specifications; DII Architecture | Business and Data Analysts; Data Architects | | ETL, Service, Interface Developers; Data Producers; Subject Matter Experts; Data Stewards | P | Source, movement, transformation and usage lineage | R1.2 | Lineage can describe resource origins, transformations, processing rules and change frequency. | Lineage relationships can support qualified references when identifiable resources and explicit relationship types are recorded. | Inspect provenance linked to resource versions, including sources, transformations, agents and times. For I3, inspect typed references to identifiable related resources. | I3 |
| Plan & Analyze_Profile Data | Data Exchange Specifications | Business and Data Analysts | | ETL, Service, Interface Developers; Data Stewards; Data Producers; Subject Matter Experts | P | Profiling results recorded in a metadata repository; corrected structural and descriptive metadata | F2; R1 | Recorded profiling results can improve metadata accuracy and describe formats, population, valid values, relationships and limitations relevant to reuse. | Profiling can identify candidate relationships and vocabulary inconsistencies for later modeling. | Inspect resource-linked metadata containing verified profiling findings and limitations. General cleansing or quality scores alone do not demonstrate F2 or R1. | |
| Plan & Analyze_Examine Business Rule Compliance | Data Exchange Specifications | Business and Data Analysts; Data Stewards | Executives and Managers | Subject Matter Experts; Data Producers; ETL, Service, Interface Developers | P | Harvested business terms, constraints, derivations and rule-compliance findings | R1 | Documented rules can explain the meaning, constraints and derivation of data for reuse. | Rules can support community-standard validation when explicitly derived from applicable domain standards. Internal rules alone do not establish R1.3. | Inspect published or accessible resource descriptions containing applicable rules and interpretation constraints. For R1.3, trace validation rules to named community standards and versions. | R1.3 |
| Design DII Solutions_Design DII Architecture | DII Architecture; Data Exchange Specifications; Data Access Agreements | Data Architects | IT Steering Committee | Business and Data Analysts; Data Modelers; Data Stewards; ETL, Service, Interface Developers; Project and Program Managers | P | Integration architecture; interaction models; exchange patterns; security and lifecycle designs | | Architecture can specify FAIR-capable services, but an architectural design alone does not establish implemented resource properties. | Commission identifier-based retrieval, open protocols, authentication and metadata persistence. The text does not mandate these specific mechanisms. | Inspect explicit protocol, identifier, authentication and metadata-survival requirements; verify the resulting services and retained metadata independently. | A1; A1.1; A1.2; A2 |
| Design DII Solutions_Model Data Hubs, Interfaces, Messages, and Data Services | DII Architecture; Data Exchange Specifications | Data Modelers; Data Architects | Data Architects; Data Stewards | Business and Data Analysts; ETL, Service, Interface Developers; Subject Matter Experts | P | Persistent and transient data models; canonical message models; interface and service models | | Models can support formal representations and explicit resource relationships when these are deliberately designed. Structural models alone are insufficient. | Provide a basis for shared knowledge representation and qualified links. | Inspect implemented representations using an accessible, shared formal language; verify semantic definitions and explicitly typed references to identifiable resources. | I1; I3 |
| Design DII Solutions_Map Sources to Targets | Data Exchange Specifications | Business and Data Analysts; Data Modelers | Data Architects; Data Stewards | ETL, Service, Interface Developers; Data Producers; Subject Matter Experts | P | Attribute-level source-to-target mappings; transformation and derivation specifications | R1.2 | Mapping specifications can document how target attributes originate and are transformed, providing design-time provenance. | Mappings can preserve resource references and vocabulary identifiers when explicitly specified. | Trace identified target attributes and versions to sources and transformation rules. For I3, verify that qualified resource references survive transformation; mappings alone are not qualified references. | I3 |
| Design DII Solutions_Design Data Orchestration | DII Architecture; Data Exchange Specifications | Data Architects; ETL, Service, Interface Developers | Data Architects | Business and Data Analysts; Project and Program Managers | P | Data-flow designs; processing dependencies; schedules and event triggers | R1.2 | Documented processing steps and dependencies can describe the planned derivation of resources. | Provide a basis for capturing execution-level provenance. | Inspect resource-linked workflow definitions and transformation dependencies; associate actual runs, inputs and outputs with these definitions to establish execution provenance. | |
| Develop DII Solutions_Develop Data Services | Data Services; Data Exchange Specifications | ETL, Service, Interface Developers | Data Architects | Business and Data Analysts; Data Modelers; Data Stewards; Project and Program Managers | D | Implemented access, transformation and delivery services | | Services can implement FAIR retrieval, but the text does not establish identifier-based retrieval or an open protocol. | Enable retrieval by identifier through standardized, open protocols and authentication where required. Vendor tooling does not automatically satisfy these requirements. | Retrieve identified data and metadata through documented standardized protocols; verify protocol specifications are open and freely implementable; test required authentication and authorization flows. | A1; A1.1; A1.2 |
| Develop DII Solutions_Develop Data Flow | Data Services | ETL, Service, Interface Developers | Data Architects | Business and Data Analysts; Data Modelers; Data Producers; Project and Program Managers | D | Implemented ETL flows; schedules; mappings; coordination points | | Data movement alone does not demonstrate a FAIR requirement. | Flows can capture provenance and preserve qualified references if those capabilities are explicitly implemented. | Inspect run-linked provenance identifying source and target versions, transformations and execution times; test preservation of explicitly typed resource references. | R1.2; I3 |
| Develop DII Solutions_Develop Data Migration Approach | Data Exchange Specifications; Data Services | ETL, Service, Interface Developers; Business and Data Analysts | Project and Program Managers; Data Architects | Data Producers; Data Modelers; Data Stewards; Subject Matter Experts | D | Migration specifications; transformation rules; test and reconciliation results | | Migration can maintain FAIR properties, but moving data between applications does not establish those properties. | Preserve provenance and explicit resource relationships through migration. | Trace migrated resources to source versions and transformation records; verify preservation of qualified references and document any changes in resource identity. | R1.2; I3 |
| Develop DII Solutions_Develop a Publication Approach | Data Services; Data Exchange Specifications; Data Access Agreements | Data Architects; ETL, Service, Interface Developers | Data Stewards; Executives and Managers | Data Producers; Business and Data Analysts; Data Modelers; Project and Program Managers | D | Publication and subscription mechanisms; canonical messages; access-authority rules | A1.2 | The text explicitly restricts subscription to consumers with appropriate access authority. Implemented protocol-level authentication and authorization can support A1.2. | Publication interfaces can support identifier-based standardized retrieval and formal shared representations, but publication and canonical messages alone do not establish them. | Test permitted and denied subscription/access requests and the authentication/authorization procedure. For A1 and I1, inspect identifier-based retrieval and the actual shared knowledge-representation language. | A1; I1 |
| Develop DII Solutions_Develop Complex Event Processing Flows | Complex Event Processing Thresholds and Alerts; Data Services | ETL, Service, Interface Developers | Executives and Managers | Business and Data Analysts; Subject Matter Experts; Data Producers; Data Architects | D | Predictive-model inputs; event-processing rules; thresholds; alerts and triggered actions | | Event detection and automated responses have no inherent FAIR alignment. | Recording historical inputs, model versions, events and triggered actions can provide provenance for derived outputs. | Inspect provenance linking identified outputs to input versions, predictive-model versions, processing rules and execution events. Alerts alone do not demonstrate provenance. | R1.2 |
| Implement and Monitor_Maintain DII Metadata | DII Architecture; Data Exchange Specifications; Data Services | Data Stewards; Business and Data Analysts; ETL, Service, Interface Developers | Data Stewards; Data Architects | Data Modelers; Data Producers; Subject Matter Experts | O | Maintained business and technical definitions; transformation metadata; operational lineage; service registry | F2; F4; R1; R1.2 | Maintained definitions and transformation records support rich discovery and reuse descriptions and provenance. A searchable service registry can support F4 where its entries identify the data or metadata resources accessible through services. | Review and approval can sustain metadata quality and consistency over time. | Inspect current resource-linked descriptions and provenance; search registry entries for identified resources; trace metadata changes to business and technical approvals. Service names alone are insufficient for F4. | |
