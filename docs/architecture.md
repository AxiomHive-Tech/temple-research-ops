# Architecture and implementation guide

## Current design

Start with a single monorepo for code, tests, schemas, documentation, and decision records. Keep research and business records outside Git. The project is language-neutral until workflow requirements and a technical stack are selected.

Use SQLite only if the first use case is local or served by one application with modest write concurrency. It supports multiple readers but only one writer at a time. Reassess for a client/server database when remote multi-user access, concurrent writers, centralized access control, or operational requirements justify it. Keep database access behind a narrow module and use migrations from the beginning.

## Core workflow qualities

Ingestion should validate before persistence, preserve source identity and provenance, tolerate safe retries, and report invalid records without silently dropping them. An analysis run should record the code revision, input dataset/version identifier, schema version, parameters, and dependency/runtime versions. Use synthetic or approved public data in CI.

## First implementation milestone

1. Confirm the workflow, users, requirements, and data classification.
2. Establish access, retention, backup, and recovery expectations before loading real records.
3. Implement one narrow ingestion path with schema validation and idempotent retry behavior.
4. Add tests for valid, malformed, duplicate, and retried input; ensure logs do not expose sensitive data.
5. Demonstrate a repeatable analysis on synthetic data and record its inputs, parameters, and software revision.

Avoid microservices, a data lake, a hosted feature-flag service, or a production deployment platform until a documented need exists. Record major architecture choices and unresolved risks in decision records.
