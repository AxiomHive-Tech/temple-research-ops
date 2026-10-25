# Human Oversight and Accountability Compliance Audit Checklist

**Purpose:** Assess whether an AI-supported workflow keeps people in control of objectives, decisions, approvals, actions, and outcomes while supporting ethical research, safe engineering, and accountable improvement.

**Project ownership and stewardship attribution (as requested):** Nicholas M. Grossi and Caden H. McCullen.  
**Prepared by:** Manus AI, based on the supplied Human-Support Research & Design Workflow and project principles.  
**Document status:** Draft audit instrument for qualified human review and approval before adoption; not a certification, legal opinion, or substitute for human operator judgment.

## How to use this checklist

Apply this audit to a clearly named AI system or workflow, including its models, prompts, tools, data sources, integrations, operators, vendors, deployment environment, and intended users. Use it before launch, after material changes, on a risk-based periodic schedule, and after a significant incident or complaint. Record the version of the system and evidence examined so the result can be reproduced.

For every control, mark **Pass**, **Partial**, **Fail**, or **Not applicable**. “Not applicable” requires a written reason and human approval. Do not mark a control as passing based only on a policy statement; inspect implementation and operating evidence. Record evidence references, not unnecessary personal or confidential data.

### Audit record

- **System/workflow and version:**
- **Business purpose and intended users:**
- **Business owner with decision authority:**
- **Technical owner:**
- **Human reviewers and release approvers:**
- **Audit lead:**
- **Audit date and period covered:**
- **Data/model/vendor versions reviewed:**
- **Affected people and groups:**
- **Overall decision:** Approved / Approved with conditions / Paused / Rejected
- **Residual risks accepted by:**
- **Next review date or trigger:**

## 1. Human authority, ownership, and accountability

- [ ] A named human business owner is accountable for the purpose, acceptable use, and outcomes of the workflow.
- [ ] A named technical owner is accountable for operation, security, reliability, and change control.
- [ ] Decision rights are documented: which tasks AI may assist with, which tasks require human review, and which actions are human-only.
- [ ] AI is explicitly treated as a support tool; it cannot set organizational objectives, grant itself authority, approve its own work, or assume human accountability.
- [ ] Human operators can pause, override, correct, reject, or stop the system without needing the AI’s permission.
- [ ] An authorized person—not an AI system—owns every consequential decision and resulting action.
- [ ] Responsibility remains assigned when AI output is incorrect, misleading, harmful, or used outside the intended scope.
- [ ] Roles and handoffs are clear for routine decisions, exceptions, complaints, incidents, and release approval.
- [ ] Conflicts of interest are disclosed and managed for owners, reviewers, vendors, and decision-makers.
- [ ] Accountability cannot be evaded by blaming the model, vendor, prompt, user, or automated process.

**Evidence to inspect:** responsibility matrix; named role assignments; operating procedures; access-control configuration; interviews; override and pause tests; incident records; sampled decisions with named human owners.

## 2. Scope, objective, and use boundaries

- [ ] The problem and intended outcome are stated before selecting or expanding AI use.
- [ ] The workflow identifies intended users, affected groups, operating context, and foreseeable misuse.
- [ ] Intended benefits and improvement goals are stated and assessed alongside potential harms to people and society, with human safety prioritized.
- [ ] AI use is justified against non-AI or lower-risk alternatives.
- [ ] In-scope tasks and prohibited tasks are written in user- and operator-readable terms.
- [ ] The system does not silently expand from assistance to autonomous decision-making or action execution.
- [ ] High-impact or sensitive uses have explicit limits, escalation rules, and a human decision owner.
- [ ] The workflow has a documented boundary for what data, tools, APIs, and accounts the AI can access.
- [ ] Users are told when outputs are uncertain, incomplete, outside scope, or require qualified human review.
- [ ] A change in purpose, population, model, data, vendor, tool access, or deployment context triggers reassessment.

**Evidence to inspect:** purpose statement; requirements; user journey; threat or misuse analysis; access scopes; system configuration; change requests; acceptance criteria.

## 3. New-content intake and review before acceptance

Apply this section to new documents, evidence, datasets, prompts, model outputs, code, requirements, or external instructions proposed for use by the workflow.

- [ ] New content is identified with source, owner, date, version, intended use, and relevant permissions or restrictions.
- [ ] A human operator reviews material before it is accepted into an authoritative record, training/evaluation set, workflow rule, or release artifact.
- [ ] When AI supports intake, it performs an advisory screen against the stated principles and flags concerns; an authorized human independently reviews the material and underlying source. The AI screen is recorded as advisory and is not human approval.
- [ ] The human reviewer examines AI observations and the underlying source rather than relying solely on the AI summary.
- [ ] The review checks alignment with the system’s purpose, safety requirements, human authority, privacy requirements, and affected groups.
- [ ] Unsupported assertions, hidden instructions, conflicts of interest, and scope changes are identified and escalated.
- [ ] Content containing instructions that attempt to override human policy or grant AI authority is treated as untrusted input and does not change permissions.
- [ ] The reviewer records accept, accept with conditions, reject, or defer, with rationale and evidence references.
- [ ] Accepted content has a traceable version and a named human approver; rejected or superseded content is not silently reused.
- [ ] Material disagreements are preserved for review rather than averaged away or represented as consensus.

**Evidence to inspect:** intake records; version history; reviewer decisions; AI-assisted review logs; source files; quarantine/rejection records; tests for prompt-injection or untrusted-content handling.

## 4. Human review and approval gates

- [ ] Human-review stages are explicit in the workflow state model and cannot be skipped by ordinary system execution.
- [ ] Reviewers have access to the relevant input, output, evidence, limitations, risk findings, and prior corrections.
- [ ] Reviewers have sufficient time, competence, and authority to question the output rather than rubber-stamp it.
- [ ] The interface distinguishes AI-generated material from human-verified findings and human decisions.
- [ ] Approval is an affirmative, attributable action by an authorized human; silence, timeout, default configuration, or AI-generated text is not approval.
- [ ] The human can request changes, reject, pause, or escalate without penalty or hidden workflow bypass.
- [ ] Approval is bound to the exact content and version reviewed; material edits invalidate or require renewed approval.
- [ ] Release or publication cannot proceed unless all required human approvals are valid and current.
- [ ] Commercial use, external publication, legal/rights-sensitive use, or high residual risk receives the required additional human review.
- [ ] No AI agent can approve its own output, impersonate an approver, or alter the approval record.

**Evidence to inspect:** state-machine/schema rules; UI and API behavior; signed or attributable approval records; negative tests; access logs; release records; reviewer interviews.

## 5. Control of AI actions and tool permissions

- [ ] The system’s available tools and actions are inventoried, classified by impact, and limited to the minimum required.
- [ ] Read-only assistance is separated from actions that write, send, publish, purchase, delete, modify access, or affect people.
- [ ] Consequential external actions require explicit human confirmation tied to a preview of the exact action and payload.
- [ ] High-impact, irreversible, financial, legal, employment, health, safety, or public-communication actions are human-controlled and appropriately escalated.
- [ ] The AI cannot independently create or elevate its own credentials, permissions, or scope.
- [ ] Credentials are held in an approved secret store, least-privilege access is used, and secrets are not placed in prompts, source code, logs, or generated artifacts.
- [ ] Tool inputs and outputs are validated; untrusted content cannot cause unauthorized tool execution.
- [ ] A human-accessible kill switch, rollback path, and emergency contact are available and tested.
- [ ] Retries, timeouts, and partial failures cannot result in duplicate or unintended actions.
- [ ] Logs establish what the AI proposed, what the human approved, what action actually occurred, and who or what executed it.

**Evidence to inspect:** tool registry; permission scopes; secrets configuration; action previews; confirmation UX; API authorization tests; kill-switch tests; idempotency and rollback tests; audit events.

## 6. Research quality, evidence, and claim traceability

- [ ] Research is conducted before design or implementation choices are finalized.
- [ ] Material claims identify sources and can be traced to the underlying evidence.
- [ ] Sources are assessed for relevance, date, provenance, methodology, limitations, and potential bias.
- [ ] Claims are categorized as **Fact**, **Estimate**, **Interpretation**, or **Hypothesis** where appropriate.
- [ ] Estimates disclose assumptions and uncertainty; interpretations are distinguished from direct observations.
- [ ] Every cited source identifier resolves to a source record; broken or unknown references block release where material.
- [ ] Conflicting evidence and stakeholder perspectives are documented with context and remain visible to reviewers.
- [ ] The workflow does not represent source linkage as proof of truth or use AI output as independent verification of itself.
- [ ] Research conclusions are limited to what the evidence supports; unresolved questions and data gaps are stated.
- [ ] Corrections update affected claims, analyses, decisions, and releases while preserving the prior audit history.

**Evidence to inspect:** claim/source records; source metadata; research notes; versioned datasets; citation checks; sampled claims; corrections and reassessment logs.

## 7. Safety, risk, and harm prevention

- [ ] A documented risk assessment identifies hazards, affected groups, likelihood, severity, mitigations, and residual risk.
- [ ] Risks are evaluated across the full lifecycle, including data collection, development, deployment, use, and retirement.
- [ ] Risk categories include privacy, security, reliability, misinformation, unfair treatment, relationship harm, misuse, and foreseeable secondary effects.
- [ ] Safety review includes an explicit path to pass, redirect, or escalate; unresolved risks are not silently treated as acceptable.
- [ ] High residual risk blocks a pass decision. It triggers pause, escalation, redesign, or rejection under the human-governed risk process; no person or AI may bypass the gate or relabel the risk without new supporting evidence.
- [ ] Mitigations are specific, assigned to an owner, testable, and tracked to completion.
- [ ] Harms to affected people are considered, including both intended use and actual outcomes.
- [ ] Ambiguous behavior is assessed from evidence; hostile intent is not assumed without support.
- [ ] Affected groups and relevant stakeholders are consulted where appropriate and safe.
- [ ] Stop-use conditions and incident escalation thresholds are written and tested.

**Evidence to inspect:** risk register; hazard analysis; affected-group assessment; mitigation tests; escalation decisions; incident simulations; residual-risk approvals.

## 8. Privacy, data stewardship, and confidentiality

- [ ] A data owner and permitted purpose are identified for each data class.
- [ ] Data collection is limited to what is necessary; identity inference or verification is excluded unless separately justified and approved.
- [ ] Personal, confidential, or sensitive information is classified and access-controlled.
- [ ] Retention, deletion, correction, backup, restore, and data-subject handling procedures are documented where applicable.
- [ ] Real sensitive data is not used in development or tests unless specifically authorized; synthetic or de-identified data is used by default.
- [ ] Sensitive inputs are not included in public repositories, prompts to unapproved services, logs, analytics, test snapshots, or generated PDFs.
- [ ] Data is protected in transit and at rest using approved controls.
- [ ] Third-party and model-provider data handling, training use, storage location, retention, and deletion are understood and approved.
- [ ] Privacy incidents trigger containment, notification through approved channels, investigation, and credential rotation where relevant.
- [ ] Data flows, copies, exports, and derived artifacts can be identified and governed.

**Evidence to inspect:** data inventory; classification; access review; privacy assessment; vendor terms; retention schedules; deletion tests; incident procedures; development/test data samples.

## 9. Fairness, bias, accessibility, and human impact

- [ ] The audit identifies groups likely to be affected and how outcomes may differ among them.
- [ ] Evaluation data and scenarios are relevant to the intended population and limitations are documented.
- [ ] Tests examine foreseeable disparate error or outcome patterns appropriate to the context.
- [ ] Known data gaps, representation limits, and proxy variables are assessed.
- [ ] Accessibility and language needs are considered for users and affected people.
- [ ] Human reviewers are trained to recognize automation bias, overreliance, and inappropriate deference to confident output.
- [ ] The system offers a meaningful route to correction, appeal, or human assistance for affected people.
- [ ] The audit compares intended purpose with observed impact and records material differences.
- [ ] Bias findings and disagreements are investigated rather than concealed or prematurely resolved.
- [ ] Remediation is assigned, tracked, and re-tested before affected use resumes.

**Evidence to inspect:** evaluation plan and results; subgroup analyses where appropriate; accessibility tests; user feedback; appeal records; reviewer training; remediation reports.

## 10. Transparency and communication

- [ ] People are informed when AI materially contributes to a decision, communication, or service interaction.
- [ ] The system explains its intended purpose, role, limitations, and when human review is needed in terms appropriate to its audience.
- [ ] AI-generated, AI-assisted, and human-verified content are distinguishable in records and, where relevant, to users.
- [ ] Material uncertainty, conflicts of interest, data/model limitations, and vendor dependencies are disclosed.
- [ ] The organization does not claim the AI is objective, unbiased, fully explainable, or compliant without evidence.
- [ ] Affected people can reach a responsible human and learn how to raise a concern or request correction.
- [ ] Public statements and customer-facing descriptions match system capabilities and actual human controls.
- [ ] Comparative capability or safety claims (for example, “more advanced”) define the comparator, scope, measures, method, and supporting evidence; otherwise they are labeled as hypotheses or design intent rather than established fact.
- [ ] Material model or workflow changes are communicated to operators and affected users as appropriate.

**Evidence to inspect:** notices; user interface; help content; marketing claims; staff scripts; disclosures; complaint and correction paths.

## 11. Technical verification and testing

- [ ] Structural validation rejects missing, malformed, or undeclared workflow fields.
- [ ] Cross-field validation checks source resolution, timestamp ordering, stage sequence, risk gates, approval status, and release alignment.
- [ ] Tests verify that the required workflow stages cannot be reordered, skipped, or duplicated.
- [ ] Tests verify that unknown source IDs, unsupported claims, high residual risk, and unapproved releases are rejected or escalated as designed.
- [ ] Tests cover corrected content, changed-after-approval content, retries, duplicate actions, interrupted execution, and safe recovery.
- [ ] Negative tests attempt unauthorized tool calls, prompt-injection, permission escalation, and human-review bypass.
- [ ] Tests use synthetic or specifically approved data and do not depend on hidden live credentials.
- [ ] Test results are reproducible and linked to code, schema, data, model, and configuration versions.
- [ ] Performance and reliability claims are measured under a documented workload before they are treated as acceptance evidence.
- [ ] Failures are triaged by named owners; passing tests do not replace human impact and safety review.

**Evidence to inspect:** schemas; validators; unit/integration/adversarial tests; CI results; test data classification; performance test setup; defect and remediation records.

## 12. Release, change management, and rollback

- [ ] Release criteria are defined before deployment and include safety, privacy, security, human approval, and operational readiness.
- [ ] The release record identifies the exact artifact, model, prompt, configuration, data, and approval version.
- [ ] A named human release authority reviews unresolved issues and explicitly approves, pauses, or rejects release.
- [ ] Publication is impossible without valid human approval and completed required safety/legal/rights gates.
- [ ] Deployment begins with a limited rollout where appropriate and includes monitoring and human fallback.
- [ ] Rollback, disablement, and restoration procedures are tested and accessible to authorized people.
- [ ] Material changes trigger revalidation and fresh human approval before high-impact use resumes.
- [ ] Feature flags, if used, have an owner, purpose, safe default, expiry/removal date, and tests for both states.
- [ ] Release notes describe material limitations and known residual risks to operators.
- [ ] Unapproved or failed artifacts cannot be mistaken for released versions.

**Evidence to inspect:** release checklist; approval record; deployment logs; artifact/version tags; rollback exercises; change records; feature-flag inventory.

## 13. Monitoring, incidents, feedback, and correction

- [ ] Monitoring detects operational failures, unexpected actions, safety incidents, and material outcome shifts.
- [ ] Monitoring does not collect more personal or sensitive data than necessary.
- [ ] Users and affected people have accessible channels for feedback, complaints, correction, and escalation.
- [ ] Each concern is acknowledged, assigned, assessed against evidence, and given a documented disposition.
- [ ] Incidents have severity levels, response owners, escalation contacts, containment steps, and post-incident review.
- [ ] Human operators can suspend the AI workflow while an incident is investigated.
- [ ] Audit logs record actions and approvals with timestamps and actors while limiting sensitive payload exposure.
- [ ] Corrections are linked to affected claims, source records, outputs, users, and decisions where feasible.
- [ ] The organization communicates and repairs harm where appropriate rather than defending the tool by default.
- [ ] Lessons learned update requirements, tests, training, and risk controls; owners and due dates are tracked.

**Evidence to inspect:** monitoring dashboards; incident records; feedback tickets; correction lineage; audit samples; downtime/rollback exercises; action trackers.

## 14. Third parties, models, and supply chain

- [ ] Model, data, software, and service providers are inventoried with an accountable internal owner.
- [ ] Provider claims, limitations, security posture, data practices, retention, and update behavior are assessed before use.
- [ ] Contracts and terms are reviewed for permitted data use, confidentiality, audit support, incident notice, and exit/data deletion needs.
- [ ] Model or provider version changes are detected and assessed before impacting material workflows.
- [ ] External libraries, container images, and CI actions are pinned or otherwise controlled and monitored for security risk.
- [ ] Supplier failure or termination has a continuity plan and a human-controlled fallback.
- [ ] The organization does not transfer accountability to vendors or rely solely on provider assurances.
- [ ] Provenance and attribution obligations for third-party material are recorded and respected.

**Evidence to inspect:** supplier inventory; due diligence; contracts; version inventory; dependency scanning; data-processing terms; exit plans.

## 15. Records, attribution, and audit integrity

- [ ] The system preserves an append-only or otherwise tamper-evident record of material decisions and corrections.
- [ ] Each record distinguishes AI contribution, human review, human approval, and final action.
- [ ] Decision records capture rationale, considered alternatives, evidence, risks, and approving human.
- [ ] Logs are time-stamped, access-controlled, retained only as long as needed, and protected against unauthorized alteration.
- [ ] Attribution identifies source authorship, AI assistance, project ownership, and third-party sources without conflating them.
- [ ] Ownership/stewardship attribution to **Nicholas M. Grossi** and **Caden H. McCullen** is used as requested for this project, while individual authorship is credited only when supported by provenance.
- [ ] New source, test, and workflow-code files carry the requested project stewardship attribution; actual author, AI assistance, human reviewer, and approver are recorded separately and only when supported by provenance.
- [ ] Corrections do not erase the original history needed to understand what changed and why.
- [ ] Audit evidence can be exported in a usable form without exposing unrelated sensitive data.
- [ ] Audit findings, exceptions, and remediation evidence are retained and access-controlled.

**Evidence to inspect:** audit-log schema; change history; attribution notices; Git history; access logs; evidence exports; retention policy.

## 16. Training, readiness, and organizational culture

- [ ] Operators understand that AI outputs may be wrong, incomplete, biased, or overconfident.
- [ ] Reviewers are trained on the specific decision authority, escalation path, and prohibited uses for this workflow.
- [ ] Staff know how to challenge AI output without retaliation or pressure to approve.
- [ ] Owners understand that responsibility remains human even when a decision is recommended or executed with AI assistance.
- [ ] Training covers privacy, security, source evaluation, bias, automation bias, incident response, and attribution as relevant.
- [ ] New staff and vendors receive role-appropriate onboarding before gaining access.
- [ ] The organization learns from disagreements and feedback rather than suppressing them to create artificial consensus.
- [ ] Management allocates time and authority for review rather than using human oversight as a nominal checkbox.

**Evidence to inspect:** training records; scenario exercises; operator interviews; escalation usage; staffing and workload; feedback culture assessments.

## 17. Audit scoring and decision rules

For each item, record a status and supporting evidence:

- **Pass:** the control is implemented, evidenced, and operating as intended.
- **Partial:** a control exists but is incomplete, inconsistently applied, or weakly evidenced.
- **Fail:** the control is absent, bypassable, or contradicted by observed behavior.
- **Not applicable:** the control does not apply to this scoped system; rationale and human approval are recorded.

A failed control is not made acceptable by a high overall score. Treat these as **stop-use / no-release conditions** until a responsible human authority reviews and resolves them:

- No named human owner with authority over the workflow.
- AI can independently authorize or execute consequential external actions or public release.
- Required human review can be skipped, forged, or applied to a materially different version.
- A workflow with high residual risk is marked pass or released, contrary to the supplied rule that high residual risk prevents a pass decision.
- Material data use lacks an authorized purpose, access control, or adequate privacy protections.
- Material claims or decisions cannot be traced to evidence, or known harmful errors are hidden.
- The system cannot be paused, contained, or rolled back when serious harm or misuse is detected.
- Attribution or audit records are falsified, misleading, or intentionally removed to evade accountability.

**Overall decision guidance:**

- **Approved:** no stop-use conditions; material controls pass; remaining risks are documented and owned.
- **Approved with conditions:** no unresolved stop-use condition; specific lower-severity actions have owners and deadlines; a human authority approves the limited scope.
- **Paused:** material evidence is missing, controls need correction, or a significant incident/uncertainty needs investigation.
- **Rejected:** the workflow cannot be brought within approved human authority, safety, privacy, or accountability boundaries.

## 18. Findings and remediation register

For every Partial or Fail item, create a finding with a unique ID and record:

- **Control/checklist item and evidence reference:**
- **Observed condition and affected people/groups:**
- **Risk/severity and rationale:**
- **Immediate containment or compensating control:**
- **Corrective action and success test:**
- **Accountable human owner:**
- **Due date:**
- **Re-test result and evidence:**
- **Closure approver and date:**

Do not close a finding solely because a policy was written. Verify the changed control in the workflow, test results, operator behavior, or other appropriate evidence.

## 19. Human sign-off

**Audit lead recommendation:** Approved / Approved with conditions / Paused / Rejected  
**Business owner decision:**  
**Release authority decision (if applicable):**  
**Unresolved risks explicitly accepted, if permitted:**  
**Conditions, owners, and deadlines:**  
**Signature/name and date:**  
**Next review date or change trigger:**

AI-generated analysis may be included as supporting material, but it is not a human signature, approval, or transfer of accountability.

## 20. Discussion chronology, relational tags, and input fidelity

Apply this section to conversational or collaborative records used to capture requirements, evidence, reviews, or decisions.

- [ ] Every captured information unit has a relational tag that accurately describes its function:
  - **a — Initial topic**
  - **b — Related topic**
  - **c — Continuation**
  - **d — Reference**
  - **e — Consolidation**
  - **f — Resolution**
- [ ] Topics and updates remain in the order in which they were introduced; editing for readability does not alter chronology.
- [ ] Information is reorganized dynamically as discussion develops, without imposing a predetermined endpoint or forcing a conclusion.
- [ ] Input intent is preserved. Conflicts, corrections, and uncertainty remain visible rather than being silently merged or rewritten as agreement.
- [ ] Claims remain traceable and are not strengthened beyond the evidence; distinguish fact, estimate, interpretation, and hypothesis where appropriate.
- [ ] Intent and impact are assessed separately, and negative intent is not inferred from ambiguous evidence alone.
- [ ] Discussion records use professional, technically precise language and identify unresolved questions without introducing unsupported claims.
- [ ] If software captures or organizes these records, tests verify tag coverage, chronology preservation, and conflict/input fidelity against representative cases.

**Evidence to inspect:** source conversation or record; ordered change history; tag definitions and examples; reviewer annotations; conflict and correction records; tests for chronology, tagging, and input fidelity.

## Framework relationship

This checklist operationalizes the supplied Human-Support Research & Design Workflow’s eight-stage lifecycle and its requirements for human review, source integrity, risk gates, privacy, and controlled release. It also reflects the project’s stated principles on human authority, ethical research, evidence quality, correction, and responsible attribution. It is an internal audit aid, not a claim of formal NIST, OECD, ISO, or legal certification. Any external compliance mapping must be validated by qualified human reviewers against the applicable versions and jurisdiction.
