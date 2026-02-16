# dabs-template
A template repository for building production-ready Databricks projects.
It provides a recommended project structure, preconfigured support tools, and opinionated best practices for development, testing, CI/CD, and deployment across environments.

This repository is intended to accelerate project setup and enforce consistency across teams.

# Table of Contents
- [Overview](#overview)

# Overview
## Purpose
This repository serves as a standardized starting point for Databricks-based data projects. It reduces setup time and enforces engineering best practices from day one.

## Scope
The template includes:
- Opinionated project structure based on Python packages (not notebook-centric development)
- Databricks Asset Bundles configuration for job and resource deployment
- `uv` for dependency management and reproducible environments
- `pytest` configuration for unit and integration testing
- `mypy` for static type checking
- `ruff` for linting and formatting
- `sqlfluff` for SQL linting (including dbt models)
- `pre-commit` hooks to enforce code quality locally
- `just` command runner for standardized developer workflows
- Conventional Commits specification for structured commit messages
- `release-please` for automated versioning and release management
- GitHub Workflows for CI/CD automation
- `mkdocs` for project documentation
- Optional dbt project structure and configuration for analytics engineering workflows
- Environment promotion model aligned with CI/CD pipelines

## Non-Goals
This template intentionally does **not** include:

- Business-specific transformation logic
- Predefined data models
- Organization-specific naming conventions (unless customized)
- Platform engineering setup (e.g., workspace provisioning, networking, private endpoints, VNet injection)
- Foundational cloud infrastructure (e.g., storage accounts, key vaults, managed identities, service principals)

> This template assumes that the underlying data platform is already provisioned and operational.
> Workspace(s), Unity Catalog (if used), networking, identity configuration, and base infrastructure must be in place before using this repository.

## Target Use Cases
- Greenfield Databricks data projects (new data workloads built on an existing platform)
- Migration from ad-hoc notebooks to structured repositories
- Building dbt-based projects (analytics engineering workflows on Databricks)

# WIP
-------------------------------------------------------------------------

https://docs.astral.sh/uv/
https://docs.astral.sh/uv/guides/integration/github/#publishing-to-pypi
https://packaging.python.org/en/latest/guides/section-build-and-publish/

# mkdocs
uv add --dev mkdocs mkdocstrings[python] mkdocs-material
uv add --dev mkdocs-gen-files mkdocs-literate-nav mkdocs-section-index

uv run mkdocs new .

# precommit
uv add --dev pre-commit
uv run pre-commit run --all-files

# ruff
uv add --dev ruff

# mypy
# just
choco install just

# sqlfluff
uv run sqlfluff lint dbt/sample_project
uv run sqlfluff fix dbt/sample_project

# versioning
https://semver.org/
https://www.conventionalcommits.org/en/v1.0.0/
https://github.com/googleapis/release-please

| Type         | When to use                                |
| ------------ | ------------------------------------------ |
| **feat**     | New user-facing functionality              |
| **fix**      | Bug fixes                                  |
| **perf**     | Performance improvements                   |
| **refactor** | Code restructuring without behavior change |
| **build**    | Build system, dependencies, packaging      |
| **ci**       | CI/CD configuration                        |
| **docs**     | Documentation only                         |
| **test**     | Adding or updating tests                   |
| **style**    | Formatting only (no logic changes)         |
| **chore**    | Repo maintenance / cleanup                 |

note:
add validation build to PR that check if commit message is correct (is it possible?)

# ci/cd

## aws
https://docs.databricks.com/aws/en/repos/get-access-tokens-from-git-provider
https://docs.databricks.com/aws/en/dev-tools/auth/oauth-federation-policy#configure-workload
https://docs.databricks.com/aws/en/dev-tools/ci-cd/github
https://docs.databricks.com/aws/en/dev-tools/auth/provider-github
https://github.com/databricks/setup-cli

https://www.youtube.com/watch?v=XumUXF1e6RI


# dbt

from root:
---
uv run dbt run `
  --project-dir dbt/sample_project `
  --profiles-dir .dbt

uv run dbt docs generate `
  --project-dir dbt/sample_project `
  --profiles-dir .dbt

uv run dbt docs serve `
  --project-dir dbt/sample_project `
  --profiles-dir .dbt

from project:
---
uv run dbt run `
  --profiles-dir ../../.dbt



# links
https://medium.com/the-data-movement/day-16-dbt-pre-commit-hooks-linting-enforcing-sql-quality-with-sqlfluff-dbt-pre-commit-7a5d0639312e
