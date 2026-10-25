# Temple Research Operations

Axiom Hive Technology project for supporting reliable business development and client, employee, and customer relationships through research-led, accountable technology.

## Principles

- AI supports; humans lead, decide, authorize, and own actions and outcomes. AI does not control the organization or independently take authority.
- Research and requirements come before technology selection.
- Material claims and decisions are traceable to evidence, rationale, alternatives, and risks.
- Findings distinguish fact, estimate, interpretation, and hypothesis.
- Disagreement and impact are examined rather than hidden or forced into consensus.
- Affected people can raise concerns, seek human review, and receive corrective action.
- Work should support responsible, goal-oriented innovation and continuous improvement while prioritizing human safety and societal well-being.

The operational review checklist is in [`docs/responsible-ai-checklist.md`](docs/responsible-ai-checklist.md). The human-oversight compliance audit checklist is in [`docs/human-oversight-compliance-audit-checklist.md`](docs/human-oversight-compliance-audit-checklist.md). The architecture overview is in [`docs/architecture.md`](docs/architecture.md), with supporting research in [`docs/research-architecture-recommendations.md`](docs/research-architecture-recommendations.md).

## Human Oversight, Research, and Stewardship Guidelines

### Human authority and accountability

AI may support research, analysis, drafting, and review within an explicitly human-defined purpose and scope. It must not set or override human objectives, grant itself authority, accept or approve its own output, authorize a release, or independently take actions that require human authority. Human operators make and own consequential decisions and remain accountable for actions and outcomes; accountability cannot be transferred to an AI system.

For each workflow, contributors should identify the responsible human owner, decision rights, approval boundaries, escalation contact, and the people authorized to pause, reject, override, or stop work. A field, checklist, or model-generated statement saying “approved” is not proof that an authorized human actually approved the exact material.

### Research before design

Define the problem, intended outcomes, affected people, and requirements before selecting a technical solution. Use appropriate guidance and engineering practices; avoid harmful malpractice, under-informed engineering, and unsupported claims. Prefer constructive, evidence-led work directed toward clearly stated goals.

For each material claim, preserve source provenance, date or version, relevance, method, limitations, and the evidence that supports the claim. Record major choices, rationale, alternatives, assumptions, and risks. A source link that resolves is traceability, not proof that the source is reliable or supports the claim.

Label claims as **Fact**, **Estimate**, **Interpretation**, or **Hypothesis** where useful. Record uncertainty and credible disagreement. Do not silently combine conflicting statements, force consensus, or present an unsupported claim as established fact. Consider both intended purpose and effects on affected people.

### Review before acceptance

Before new information or content is accepted into an authoritative record, dataset, prompt, codebase, policy, workflow, or release artifact, use a dual-support review: AI may screen, summarize, check, or flag concerns against the stated principles, and an authorized human operator must independently review the material and its underlying evidence. The human records the acceptance decision; AI review is advisory and cannot replace that decision or authorize acceptance.

Record the human disposition—**accepted**, **accepted with conditions**, **rejected**, or **deferred**—with the reviewer’s role, rationale, date, evidence considered, and the version reviewed. Re-review material changes that could affect the decision. Track corrections and identify downstream claims or decisions that may need reassessment.

### Safety, bias, feedback, and impact

Assess relevant privacy, security, safety, accessibility, bias, and stakeholder-impact risks before deployment and after material changes. Seek evidence before attributing negative motives to people when intent is ambiguous. Consider alternative explanations, conflicting accounts, and differences between intent and impact.

Invite specific, respectful feedback so concerns can be addressed constructively. Document escalation and correction routes. Do not treat a completed checklist, a passing structural validation, or a favorable AI-generated review as proof that a system is safe, fair, or appropriate.

### Discussion records and chronology

When organizing multi-turn project discussions, preserve the order in which topics and updates are introduced. Organize material dynamically as the conversation develops rather than imposing a predetermined endpoint or forced conclusion. Preserve the intent of inputs, keep conflicts visible, and do not add unsupported claims.

Apply the project’s relational tags consistently to captured discussion units:

- **a — Initial topic**
- **b — Related topic**
- **c — Continuation**
- **d — Reference**
- **e — Consolidation**
- **f — Resolution**

Use professional, technically precise language and avoid ambiguous phrasing.

### Approval, release, and evidence of implementation

Human approval must apply to the exact version and scope being accepted or released. Material edits require renewed review where they could change the decision. Release paths should fail closed when required human approval or safety, privacy, rights, or evidence reviews remain unresolved.

Distinguish a **principle**, **planned design**, **implemented control**, **tested control**, and **observed operating result**. Documentation and framework mappings describe intent; they do not establish implementation or compliance. Comparative claims such as “more advanced” or “safer than other systems” require a defined comparator, method, and supporting evidence.

This repository is a language-neutral scaffold, not a deployed AI control system. `tests/test_workflow.py` currently depends on companion validator, schema, and example files that are not yet in the repository. The current `scaffold-check` verifies repository structure and required-file presence; it does not execute that unit-test suite. Do not represent those tests or the described workflow as operationally validated until the missing implementation is supplied and tested.

## Repository layout

- `src/` — application and analysis modules (currently a scaffold)
- `tests/` — automated and reference tests; some require implementation modules before they can run
- `docs/` — operating guidance, evidence practices, and decision records
- `docs/decision-records/` — significant architecture and governance decisions
- `migrations/` — database schema migrations
- `fixtures/` — synthetic or approved public test fixtures only
- `configs/` — non-secret defaults; never store credentials here

## Data safety

Do not commit personal information, confidential temple or business records, credentials, production exports, or raw research datasets. Use synthetic data in tests. Store approved operational data only in access-controlled systems with documented retention, backup, and access-review practices. See [Data handling](docs/data-handling.md).

## Development status

This repository begins as a language-neutral scaffold. No production application, database backend, or deployment target has been selected. Add those only after workflow requirements and data classification are documented.

## Contributing

Use a short-lived branch and pull request. Keep changes small and connect each change to a research or operational need. Before merging, pass the repository checks and document material changes to data handling, security, or system behavior. For substantive work, identify the human reviewer and the evidence reviewed. `main` requires the `scaffold-check` CI status, disallows force-pushes and deletion, and requires conversation resolution.

New code files must include the requested project ownership/stewardship attribution, with authorship and AI assistance identified separately where applicable. Do not infer authorship from ownership or imply human approval that has not occurred.

## Attribution

- **Project ownership and stewardship (as requested):** Nicholas M. Grossi and Caden H. McCullen.
- **Existing source-material authorship wording:** Caden McCullen.
- **Existing technology-leadership and engineering-founder wording:** Nicholas Michael Grossi and Alexis M. Adam’s.
- **AI-assisted preparation:** disclose where applicable; human review and approval are separate roles.

These role and name forms are recorded separately as supplied. Do not infer individual authorship from project ownership or assume name variants identify the same person without human confirmation.
