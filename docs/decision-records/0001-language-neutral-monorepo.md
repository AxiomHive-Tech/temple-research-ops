# ADR 0001: Start with a language-neutral monorepo scaffold

- **Status:** Accepted for initial scaffold
- **Date:** 2026-10-24
- **Decision owner:** To be assigned

## Context

The project needs a repository structure that can support research, ingestion, analysis, documentation, and operational governance. The application language, database workload, and deployment environment are not yet established.

## Decision

Create one repository with separate areas for source, tests, documentation, migrations, configuration defaults, and synthetic/public fixtures. Keep sensitive operational and research data outside Git. Do not choose an application framework or production database before requirements and data-handling needs are documented.

## Alternatives considered

- Select a full application stack immediately: deferred because the first workflow and operational constraints are not yet defined.
- Split research data and software into separate repositories: unnecessary for the scaffold; reconsider if ownership or access-control boundaries require it.

## Risks and follow-up

A language-neutral scaffold does not yet build an application. The project owner must select the first workflow, assign data stewardship and technical ownership, and decide on a runtime before implementation. Revisit the decision when these requirements are known.
