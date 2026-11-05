# 5. Data Security Management

## Definition

Planning, development, and execution of security policies and procedures to provide proper authentication, authorization, access, and auditing of data and information.

## Goals

1. Enable appropriate, and prevent inappropriate, access and change to data assets.
2. Meet regulatory requirements for privacy and confidentiality.
3. Ensure the privacy and confidentiality needs of all stakeholders are met.

## FAIR Alignment

Both direct and indirect alignment concern protocols that allow authentication and authorization where necessary (A1.2). Specific access controls can address this requirement directly, while security policies and supporting processes can enable it indirectly. The same ID appears in both categories because different activities contribute in different ways.

| DAMA Segments overview name | FAIR Direct IDs | FAIR Indirect IDs |
|---|---|---|
| 5. Data Security Management | A1.2 | A1.2 |

## Business Drivers

### Inputs

- Business Goals
- Business Strategy
- Business Rules
- Business Process
- Data Strategy
- Data Privacy Issues
- Related IT Policies and Standards

### Activities

1. Understand Data Security Needs and Regulatory Requirements (P)
2. Define Data Security Policy (P)
3. Define Data Security Standards (P)
4. Define Data Security Controls and Procedures (D)
5. Manage Users, Passwords, and Group Membership (C)
6. Manage Data Access Views and Permissions (C)
7. Monitor User Authentication and Access Behavior (C)
8. Classify Information Confidentiality (C)
9. Audit Data Security (C)

### Primary Deliverables

- Data Security Policies
- Data Privacy and Confidentiality Standards
- User Profiles, Passwords and Memberships
- Data Security Permissions
- Data Security Controls
- Data Access Views
- Document Classifications
- Authentication and Access History
- Data Security Audits

## Knowledge Area Roles

### Suppliers

- Data Stewards
- IT Steering Committee
- Data Stewardship Council
- Government
- Customers

### Participants

- Data Stewards
- Data Security Administrators
- Database Administrators
- BI Analysts
- Data Architects
- DM Leader
- CIO/CTO
- Help Desk Analysts

### Consumers

- Data Producers
- Knowledge Workers
- Managers
- Executives
- Customers
- Data Professionals

## Technical Drivers

### Techniques

- CRUD Matrix Usage
- Immediate Security Patch Deployment
- Data Security Attributes in Metadata
- Security Needs in Project
- Efficient Search for Encrypted Data
- Document Sanitization

Source: the **Data Security** row in Appendix — Activity Technical Drivers.

### Tools

- Database Management System
- Business Intelligence Tools
- Application Frameworks
- Identity Management Technologies
- Change Control Systems

### Metrics

Not shown in source.

## Worksheet Detail

Source: DAMA-PDOC_FAIR-MASTER_2026-10-13.xlsx, worksheet **DataSecurityManagement**. All populated table rows and all 12 columns are reproduced below. Blank cells remain blank; items previously separated by line breaks within cells are separated by semicolons.

| Activities | Deliverables | Responsible Roles | Approving Roles | Contributing Roles | Plan,Develop,Organise,Control | Relevant deliverables | FAIR principles supported | How they can support FAIR | Indirect support | What would demonstrate the supported FAIR requirement | FAIR principles indirectly supported |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Understand Data Security Needs and Regulatory Requirements (P) | Data Security Requirements and Regulations  | Data Stewards, DM Executive, Security Administrators | Data Governance Council | Data Stewards, Legal Department, IT Security | P |  | No clear FAIR support identified. | Understand Data Security Needs and Regulatory Requirements (P) \[source: DataSecurityManagement!A2:F2\] — Deliverable: Data Security Requirements and Regulations.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Security governance and classification can determine legitimate access conditions and oversee their operation. Security controls must be incorporated into the retrieval protocol to fulfil A1.2; source confidentiality does not imply a FAIR accessibility result. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | A1.2 |
| Define Data Security Policy (P) | Data Security Policy | Data Stewards, DM Executive, Security Administrators | Data Governance Council | Data Stewards, Legal Department, IT Security | P |  | No clear FAIR support identified. | Define Data Security Policy (P) \[source: DataSecurityManagement!A3:F3\] — Deliverable: Data Security Policy.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Security governance and classification can determine legitimate access conditions and oversee their operation. Security controls must be incorporated into the retrieval protocol to fulfil A1.2; source confidentiality does not imply a FAIR accessibility result. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | A1.2 |
| Define Data Security Standards (P)  | Data Security Standards | Data Stewards, DM Executive, Security Administrators | Data Governance Council | Data Stewards, Legal Department, IT Security | P |  | No clear FAIR support identified. | Define Data Security Standards (P)  \[source: DataSecurityManagement!A4:F4\] — Deliverable: Data Security Standards.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Security governance and classification can determine legitimate access conditions and oversee their operation. Security controls must be incorporated into the retrieval protocol to fulfil A1.2; source confidentiality does not imply a FAIR accessibility result. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | A1.2 |
| Define Data Security Controls and Procedures (D) | Data Security Controls and Procedures | Security Administrators | DM Executive | Data Stewards, IT Security | D | Data Security Controls and Procedures | A1.2 — retrieval protocol supports authentication and authorisation | Define Data Security Controls and Procedures (D) \[source: DataSecurityManagement!A5:F5\] — Deliverable: Data Security Controls and Procedures.; Inferred support: Data Security Controls and Procedures can define access checks when applied within a data/metadata retrieval protocol. Generic database security, credential management or access monitoring alone does not establish A1.2. No implementation evidence is supplied. | Indirect support: Security governance and classification can determine legitimate access conditions and oversee their operation. Security controls must be incorporated into the retrieval protocol to fulfil A1.2; source confidentiality does not imply a FAIR accessibility result. | A1.2: Test retrieval of identified data and metadata through the declared protocol with authorised, unauthorised and unauthenticated requests. Verify the documented authentication/authorisation procedure and expected decisions; unrestricted public access is not required.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | A1.2 |
| Manage Users, Passwords and Group Membership (C) | User Accounts, Passwords,Role Groups | Security Administrators, DBAs | Management | Data Producers, Data Consumers, Help Desk | C | User Accounts, Passwords,Role Groups | A1.2 — retrieval protocol supports authentication and authorisation | Manage Users, Passwords and Group Membership (C) \[source: DataSecurityManagement!A6:F6\] — Deliverable: User Accounts, Passwords,Role Groups.; Inferred support: user accounts, passwords and role groups can supply authentication and authorisation when applied within a data/metadata retrieval protocol. Generic database security, credential management or access monitoring alone does not establish A1.2. No implementation evidence is supplied. | Indirect support: Security governance and classification can determine legitimate access conditions and oversee their operation. Security controls must be incorporated into the retrieval protocol to fulfil A1.2; source confidentiality does not imply a FAIR accessibility result. | A1.2: Test retrieval of identified data and metadata through the declared protocol with authorised, unauthorised and unauthenticated requests. Verify the documented authentication/authorisation procedure and expected decisions; unrestricted public access is not required.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | A1.2 |
| Manage Data Access Views and Permissions (C) | Data Access Views Data Resource Permissions | Security Administrators, DBAs | Management | Data Producers, Data Consumers, Software Developers, Management, Help Desk | C | Data Access Views Data Resource Permissions | A1.2 — retrieval protocol supports authentication and authorisation | Manage Data Access Views and Permissions (C) \[source: DataSecurityManagement!A7:F7\] — Deliverable: Data Access Views Data Resource Permissions.; Inferred support: resource permissions and access views can enforce authorisation when applied within a data/metadata retrieval protocol. Generic database security, credential management or access monitoring alone does not establish A1.2. No implementation evidence is supplied. | Indirect support: Security governance and classification can determine legitimate access conditions and oversee their operation. Security controls must be incorporated into the retrieval protocol to fulfil A1.2; source confidentiality does not imply a FAIR accessibility result. | A1.2: Test retrieval of identified data and metadata through the declared protocol with authorised, unauthorised and unauthenticated requests. Verify the documented authentication/authorisation procedure and expected decisions; unrestricted public access is not required.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | A1.2 |
| Monitor User Authentication and Access Behavior (C) | Data Access Logs, Security Notification Alerts, Data Security Reports | Security Administrators, DBAs | DM Executive | Data Stewards, Help Desk | C |  | A1.2 — retrieval protocol supports authentication and authorisation | Monitor User Authentication and Access Behavior (C) \[source: DataSecurityManagement!A8:F8\] — Deliverable: Data Access Logs, Security Notification Alerts, Data Security Reports.; Inferred support: authentication monitoring and access logs can verify access decisions when applied within a data/metadata retrieval protocol. Generic database security, credential management or access monitoring alone does not establish A1.2. No implementation evidence is supplied. | Indirect support: Security governance and classification can determine legitimate access conditions and oversee their operation. Security controls must be incorporated into the retrieval protocol to fulfil A1.2; source confidentiality does not imply a FAIR accessibility result. | A1.2: Test retrieval of identified data and metadata through the declared protocol with authorised, unauthorised and unauthenticated requests. Verify the documented authentication/authorisation procedure and expected decisions; unrestricted public access is not required.; Supporting-process evidence: inspect the named deliverable and its approval/maintenance records separately from the resource tests. | A1.2 |
| Classify Information Confidentiality (C)  | Classified Documents, Classified Databases | Document Authors, Report Designers, Data Stewards | Management | Data Stewards | C |  | No clear FAIR support identified. | Classify Information Confidentiality (C)  \[source: DataSecurityManagement!A9:F9\] — Deliverable: Classified Documents, Classified Databases.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Security governance and classification can determine legitimate access conditions and oversee their operation. Security controls must be incorporated into the retrieval protocol to fulfil A1.2; source confidentiality does not imply a FAIR accessibility result. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | A1.2 |
| Audit Data Security (C)  | Data Security Audit Reports | Data Security Auditors | Data Governance Council, DM Executive | Security Administrators, DBAs, Data Stewards | C |  | No clear FAIR support identified. | Audit Data Security (C)  \[source: DataSecurityManagement!A10:F10\] — Deliverable: Data Security Audit Reports.; No clear FAIR support identified from the supplied activity and deliverable. This item can enable implementation, but it does not specify a defensible resource-level FAIR mechanism. No implementation evidence is supplied. | Indirect support: Security governance and classification can determine legitimate access conditions and oversee their operation. Security controls must be incorporated into the retrieval protocol to fulfil A1.2; source confidentiality does not imply a FAIR accessibility result. | Supporting-process evidence: inspect the named deliverable, responsible/approving roles and dated operating or review records for this activity. No directly supported FAIR requirement is established. To demonstrate FAIR fulfilment, separately test identified data and metadata against the specific requirements commissioned through this process. | A1.2 |
