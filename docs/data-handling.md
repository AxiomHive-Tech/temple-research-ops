# Data handling

This guidance is a baseline and must be reviewed by the accountable project owner before real records are ingested.

## Repository boundary

Git may contain application code, documentation, schema migrations, and small synthetic or approved public fixtures. Git must not contain credentials, personal information, confidential client/employee/customer records, temple operational records, or production exports. Do not put secrets in source files, logs, test snapshots, container images, or issue text.

## Before real data is used

Document the data owner, purpose, classification, access roles, authorized storage location, retention period, backup and restore method, and incident contact. Minimize collected fields. Use de-identified or synthetic data for development and CI. Keep original inputs immutable where policy permits, and record source identifiers, timestamps, checksums, and transformation versions without duplicating sensitive payloads unnecessarily.

## If data is exposed

Stop further exposure, restrict access, notify the designated owner, preserve necessary evidence safely, and follow the organization's incident and notification procedures. Rotate exposed credentials. Do not attempt to conceal or overwrite the incident history.
