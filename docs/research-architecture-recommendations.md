# Research operations architecture: design review

## Current status

The current work is a research and design recommendation, not an implemented repository. The workspace has no project scaffold or linked GitHub repository. GitHub is signed out in the available browser session, so repository creation and configuration have not occurred.

The original proposal is directionally sound: one repository, short-lived branches, automated checks, containers, modular ingestion, and tests. Its main quality risk is that it names tools and phases without specifying the data lifecycle, reproducibility contract, access controls, and conditions for changing the design. The improvements below make those decisions explicit without requiring a large platform up front.

## Improve the design before implementation

### Define the data boundary first

Separate three categories: application code and documentation; small, synthetic or public test fixtures; and operational/research data. Only the first two belong in Git. Keep sensitive or identifying records in access-controlled storage with a documented retention and backup policy. Record dataset IDs, checksums, collection/protocol metadata, access classification, and transformation history in the system so an analysis can be traced without copying raw data into the repository.

Before any real temple records are loaded, document who may access them, what is considered sensitive, where copies and backups may exist, and how deletion or correction requests are handled. Use de-identified or synthetic data in development and CI. This is a design gate, not a feature to defer until after ingestion.

### Make results reproducible

For each analysis run, preserve the code revision, input dataset/version identifier, parameter values, schema version, and runtime/dependency versions. Pin dependencies with a lockfile and provide a single documented command to run tests and a representative analysis. Keep transformations deterministic where possible; record random seeds and external data sources when they affect results. These records make it possible to explain why two runs differ.

### Choose storage by workload, not by label

SQLite is suitable for a local prototype or a single application with modest write concurrency. It supports multiple readers but only one writer at a time, and the SQLite project recommends a client/server database for many computers directly sharing a database or for high concurrent-write needs [3]. Keep storage access behind a narrow module and write migrations from the start. Move to PostgreSQL or another server database only when remote multi-user access, concurrent writers, centralized permissions, or backup/operations needs justify it. Avoid a generic "schema-less" approach for core operational records: flexible raw payloads can be retained, but normalize identifiers, timestamps, provenance, and state needed for validation and queries.

### Make ingestion safe to rerun

Design ingestion as a sequence of stages: receive, validate, normalize, persist, and report. Require stable source IDs or content hashes, schema/version checks, duplicate handling, clear quarantine for invalid records, and structured error logs. A retry should not silently create duplicate records or overwrite source data. Keep original inputs immutable where policy allows, and version derived outputs separately.

### Keep the repository intentionally small

Use one monorepo while the application, schema, analysis modules, tests, and documentation change together. A practical layout is `src/`, `tests/`, `docs/`, `migrations/`, and `fixtures/` (synthetic/public data only). Add `configs/` only for non-secret, environment-independent defaults. Avoid adopting a data lake, microservices, orchestration platform, or separate repositories until actual scale or access-control boundaries require them.

Use GitHub Issues and pull requests to tie implementation work to research needs. Issues should identify the question or workflow, acceptance criteria, data classification, and any approval constraints. Keep pull requests small and short-lived; DORA describes frequent small integrations and fast automated feedback as central to trunk-based development and CI [1] [2]. Protect `main` with passing checks and require review for changes to sensitive workflows, schemas, or access controls.

### Build quality gates around risk

Run formatting/linting, unit tests, migration validation, dependency checks, and a small integration suite on pull requests and commits to `main`. Test ingestion with malformed input, duplicate input, interrupted/retried runs, and empty or unusually large batches. Test that sensitive data is not printed in logs or included in artifacts. Keep fast checks under a few minutes and run longer end-to-end or representative-data checks on a separate cadence. Every test should use synthetic or explicitly approved data.

Use Docker for consistent development and CI, not as a substitute for pinning dependencies or managing secrets. Pin base images and dependency versions. If building or publishing images with GitHub Actions, Docker provides maintained Actions for Buildx builds and image scanning [4]. Restrict workflow token permissions, protect secrets, and pin third-party Actions to verified full commit SHAs or use a dependency lockfile [5]. Do not make pull-request workflows that execute untrusted code with privileged secrets.

### Simplify feature-flag policy

Do not add a feature-flag service in the first milestone unless there is a concrete staged-rollout or configuration need. For a small project, a typed configuration setting may be enough. If flags are later introduced, give each one an owner, purpose, safe default, and removal date; test both enabled and disabled behavior. OpenFeature supplies a vendor-neutral evaluation API and provider model if portability becomes useful [6]. Flags must not replace authentication, authorization, or consent.

### Add operational readiness proportionately

Document how to run locally, back up and restore the database, apply or roll back migrations, and recover from a failed ingestion. Log operational events with correlation/run IDs but exclude sensitive payloads. Add health checks and basic monitoring when there is a deployed service. Define an owner for incidents and access reviews before the system becomes relied on for important temple operations.

## Recommended first implementation milestone

1. Create a private repository with a README, `.gitignore`, dependency lockfile, `src/`, `tests/`, `docs/`, `migrations/`, and synthetic fixtures.
2. Write a short data-classification and handling policy before importing real records.
3. Implement one narrow ingestion workflow with schema validation, idempotent retries, provenance metadata, and structured errors.
4. Add automated tests for valid, invalid, duplicate, and retried inputs; verify logs do not expose sensitive values.
5. Add Docker-based local setup and GitHub Actions for fast checks. Protect `main` and use least-privilege workflow permissions.
6. Demonstrate a repeatable analysis from a versioned synthetic dataset and capture code revision, input version, parameters, and dependency versions.

Do not build more infrastructure until usage reveals concrete limits. Revisit the database choice when concurrency or remote access grows. Revisit repository boundaries when components need different owners, release cycles, or data access controls.

## References

[1]: https://dora.dev/capabilities/trunk-based-development/ "DORA capability: Trunk-based development"
[2]: https://dora.dev/capabilities/continuous-integration/ "DORA capability: Continuous integration"
[3]: https://www.sqlite.org/whentouse.html "Appropriate Uses For SQLite"
[4]: https://docs.docker.com/build/ci/github-actions/ "Docker Build GitHub Actions"
[5]: https://docs.github.com/en/actions/reference/security/secure-use "GitHub Actions secure use reference"
[6]: https://openfeature.dev/specification/ "OpenFeature Specification"
