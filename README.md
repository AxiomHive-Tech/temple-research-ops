# Temple Research Operations

Axiom Hive Technology project for supporting reliable business development and client, employee, and customer relationships through research-led, accountable technology.

## Principles

- Responsibility remains with named people; AI does not absorb accountability.
- Research and requirements come before technology selection.
- Material claims and decisions are traceable to evidence, rationale, alternatives, and risks.
- Findings distinguish fact, estimate, interpretation, and hypothesis.
- Disagreement and impact are examined rather than hidden or forced into consensus.
- Affected people can raise concerns, seek human review, and receive corrective action.

The operational review checklist is in [`docs/responsible-ai-checklist.md`](docs/responsible-ai-checklist.md). The architecture recommendations are in [`docs/architecture.md`](docs/architecture.md).

## Repository layout

- `src/` — application and analysis modules (currently a scaffold)
- `tests/` — automated tests
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

Use a short-lived branch and pull request. Keep changes small and connect each change to a research or operational need. Before merging, pass the repository checks and document material changes to data handling, security, or system behavior. The initial CI check is active. GitHub rejected branch protection because the current plan does not enable it for private repositories; enable it if the plan changes, or only make the repository public after an explicit decision.

## Attribution

The responsible AI and relationship reliability principles in this repository are based on material provided by Axiom Hive Technology. Authored by Caden McCullen. Technology leadership and engineering founders: Nicholas Michael Grossi and Alexis M. Adam’s.
