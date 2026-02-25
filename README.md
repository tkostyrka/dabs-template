# dabs-template
A template repository for building production-ready Databricks projects.

It provides a recommended project structure, preconfigured support tools, and opinionated best practices for development, testing, CI/CD, and deployment across environments.

This repository is intended to accelerate project setup and enforce consistency across teams.

# Table of Contents

- [Overview](#overview)
- [Core Components](#core-components)
- [Tooling](#tooling)
- [Development & Deployment Lifecycle](#development--deployment-lifecycle)
- [Getting Started](#getting-started)
- [Configuration](#configuration)

# Overview
This repository serves as a standardized starting point for Databricks-based data projects. It reduces setup time and enforces engineering best practices from day one.

- [Engineering Principles](#engineering-principles)
- [Scope](#scope)
- [Target Use Cases](#target-use-cases)
- [Non-Goals](#non-goals)

## Engineering Principles
This repository is built around a set of core engineering principles that guide development, testing, deployment, and overall project structure. These principles are designed to ensure consistency, reproducibility, and high-quality delivery across all environments.

- **Developer Experience:** Development workflows are standardized and reproducible, with automated validation, testing, and quality checks to maintain consistency and reduce errors.
- **Automation-First:** All deployments are fully automated, with no manual edits to workspaces. Infrastructure and jobs are defined as code to ensure reproducibility.
- **Documentation:** Project documentation is generated and versioned alongside the code, ensuring accuracy and eliminating reliance on external sources.
- **Version-Driven Releases:** Releases are semantic versioned, promoted via tags, and deployed as immutable artifacts to guarantee traceability.

## Promoted Concepts
In addition to the core engineering principles, this repository actively promotes architectural and organizational concepts that improve scalability, maintainability, and long-term platform maturity.

### Code as Packages
Our template promotes an approach in which, instead of implementing multiple layers of logic across sequentially invoked notebooks, more advanced logic is cleanly wrapped into Python packages.

This approach is much closer to established software engineering best practices. By encapsulating complex logic inside well-structured Python modules rather than chaining notebooks together, we achieve better separation of concerns and clearer architecture.

It also significantly improves:
- **Testability** – Python packages can be easily unit tested outside of Databricks.
- **Code quality and linting** – standard tooling (e.g., linters, formatters, static analysis) can be applied consistently.
- **Portability and reusability** – packages can be reused across multiple projects without copying notebook code.
- **Maintainability** – structured codebases are easier to extend, refactor, and debug over time.

### Analytics Engineering
xxx

## Scope
The template includes:
- Databricks Asset Bundles configuration for job and resource deployment
- Optional dbt project structure and configuration for analytics engineering workflows
- Opinionated project structure based on Python packages (not notebook-centric development)
- Environment promotion model aligned with CI/CD pipelines

Additionally, the repository comes with preconfigured tools that help standardize the solution development process.
- `uv` for dependency management and reproducible environments
- `just` command runner for standardized developer workflows
- `pytest` configuration for unit and integration testing
- `mypy` for static type checking
- `ruff` for linting and formatting
- `sqlfluff` for SQL linting (including dbt models)
- `pre-commit` hooks to enforce code quality locally
- `mkdocs` for project documentation
- Conventional Commits specification for structured commit messages
- `release-please` for automated versioning and release management
- GitHub Workflows for CI/CD automation

## Target Use Cases
- **Greenfield** Databricks data projects (new data workloads built on an existing platform)
- **Migration** from ad-hoc notebooks to structured repositories
- Building **dbt-based projects** (analytics engineering workflows on Databricks)
- **Wrapping up existing Databricks Asset Bundles** (DAB)-based projects and enhancing them with testing, CI/CD, code quality checks, and structured repository standards
- **Standardizing** projects across the organization through adoption of an approved, reusable template

## Non-Goals
This template intentionally does **not** include:

- Business-specific transformation logic
- Predefined data models
- Organization-specific naming conventions (unless customized)
- Platform engineering setup (e.g., workspace provisioning, networking, private endpoints, VNet injection)
- Foundational cloud infrastructure (e.g., storage accounts, key vaults, managed identities, service principals)

> This template assumes that the underlying data platform is already provisioned and operational.
> Workspace(s), Unity Catalog (if used), networking, identity configuration, and base infrastructure must be in place before using this repository.

# Core Components
- [Databricks Asset Bundles (DABs)](#databricks-asset-bundles-dabs)
- [dbt](#dbt)
- [uv](#uv)

## Databricks Asset Bundles (DABs)
*Databricks Asset Bundles are a tool to facilitate the adoption of software engineering best practices, including source control, code review, testing, and continuous integration and delivery (CI/CD), for your data and AI projects. Bundles provide a way to include metadata alongside your project's source files and make it possible to describe Databricks resources such as jobs and pipelines as source files. Ultimately a bundle is an end-to-end definition of a project, including how the project should be structured, tested, and deployed. This makes it easier to collaborate on projects during active development.*

- **Official Documentation:** [link](https://docs.databricks.com/aws/en/dev-tools/bundles/)
- **DAB projects:** [link](bundles/README.md)
- **DAB configuration (targets):** [link](.bundles/README.md)

## dbt
A framework for analytics engineering and transformation workflows. dbt allows you to define transformations as modular SQL models, test data quality, and manage dependencies between models. It integrates with Databricks to orchestrate transformations and maintain a clean, versioned data pipeline.

- **Official Documentation:** [link](https://github.com/dbt-labs/dbt-core)
- **dbt projects:** [link](dbt/README.md)
- **dbt configuration (profiles):** [link](.dbt/README.md)

## uv
A modern Python package, project, and environment manager written in Rust. UV combines dependency management, virtual environment creation, and tool execution in a single fast CLI. It uses a universal lockfile to ensure reproducible installs across machines and environments.

- **Official Documentation:** [link](https://docs.astral.sh/uv/)

# Auxiliary Tooling
This template comes preconfigured with a set of tools to ensure code quality, reproducibility, and best practices for Databricks projects.

- [Code Quality & Linting](#code-quality--linting)
- [Documentation & Automation](#documentation--automation)
- [Testing](#testing)

## Code Quality & Linting
### pre-commit
pre-commit is a framework for managing and maintaining Git hooks in a consistent, repeatable way across a team. It automatically runs checks before code is committed, helping you catch issues early - before they reach CI/CD or production. Instead of relying only on pipelines to validate code quality, pre-commit shifts feedback left, giving developers instant validation directly in their local environment.

- **Official Documentation:** [link](https://pre-commit.com/)

**What is pre-commit responsible for?**

`pre-commit` runs automated checks before a commit is created. These checks can include:

- Code formatting such as Black
- Linting such as Ruff or Flake8
- Type checking such as mypy
- Security scanning
- Removing trailing whitespace
- Validating YAML or JSON
- Preventing large files from being committed
- Running custom scripts

If any hook fails:
- The commit is blocked
- You receive a clear error message
- You fix the issue and try again

This ensures:
- Consistent code style across the project
- Fewer CI failures
- Cleaner Git history
- Better collaboration in teams

**How pre-commit works**

1. Hooks are defined in a `.pre-commit-config.yaml` file.
2. `pre-commit` installs Git hooks locally.
3. On every `git commit`, the configured hooks run automatically.
4. If checks pass, the commit succeeds.
5. If checks fail, the commit is rejected.

**Installation**

Since `pre-commit` is already added to the project via `uv`, you only need to initialize it in your local repository.

To install Git hooks locally run:
```bash
uv run pre-commit install
```

This installs the Git hook into `.git/hooks/`. From this point on, pre-commit will automatically run on every git commit.

To make sure everything works correctly, run all configured hooks against the entire repository:
```bash
uv run pre-commit run --all-files
```

### ruff
**Ruff** is an extremely fast Python linter and code checker. It scans Python files for style violations, code smells, import issues, and common errors with minimal overhead. It provides a significant speed advantage compared to traditional linters such as flake8. Ruff can replace multiple tools at once, including flake8, isort, pydocstyle, pycodestyle, and pyflakes. Because of its performance and broad rule support, it is well suited for large repositories and CI environments.

- **Official Documentation:** [link](https://docs.astral.sh/ruff/)

**What is Ruff responsible for?**

Ruff helps ensure:

- Consistent code style
- Correct import ordering
- Detection of unused variables and imports
- Identification of common Python errors
- Docstring validation
- Enforcement of selected linting standards

It can also automatically fix many issues when run with the `--fix` flag.

**Configuration in `pyproject.toml`**

Ruff is configured in the `pyproject.toml` file under the `[tool.ruff]` section.

Example configuration:

```toml
[tool.ruff]
# Set maximum allowed line length to 100 characters
line-length = 100

[tool.ruff.lint]
# Enable rule groups:
# E = pycodestyle errors
# F = pyflakes checks
# I = import sorting rules
# D = docstring validation rules
select = ["E", "F", "I", "D"]

# Ignore specific rule:
# D104 = Missing docstring in public package
ignore = ["D104"]

[tool.ruff.lint.pydocstyle]
# Enforce Google-style docstring convention
convention = "google"
```

**Running Ruff manually**

Check all files:
```bash
uv run ruff check .
```

Automatically fix issues where possible:
```bash
uv run ruff check . --fix
```

Check a specific file:
```bash
uv run ruff check src/module.py
```

**Using Ruff with pre-commit**

If integrated with pre-commit, Ruff runs automatically before each commit.
A typical hook configuration looks like:

```yaml
- repo: https://github.com/astral-sh/ruff-pre-commit
  rev: v0.5.0
  hooks:
    - id: ruff
      args: [--fix]
```

### mypy
**mypy** is a static type checker for Python. It analyzes your code for type consistency and helps catch type related bugs before runtime, improving maintainability and developer confidence in large codebases. mypy verifies that function arguments, return types, class attributes, and variables match their declared type hints. This is especially valuable in larger projects where implicit assumptions about types can easily introduce subtle bugs.

**What is mypy responsible for?**

mypy helps ensure:

- Functions return the expected types
- Arguments passed to functions match declared types
- Variables are used consistently with their type annotations
- Untyped or partially typed code is detected
- Type safety is preserved across modules

By enforcing type hints at development time, mypy reduces runtime surprises and improves refactoring safety.

**Configuration in `pyproject.toml`**

mypy is configured in the `pyproject.toml` file under the `[tool.mypy]` section.

Example configuration:

```toml
[tool.mypy]

# Only check files inside the packages directory
files = ["packages/"]

# Type check function bodies even if they do not have type annotations
check_untyped_defs = true

# Require all functions to have explicit type annotations
disallow_untyped_defs = true

# Treat top level packages as explicit package bases
explicit_package_bases = true

# Add additional paths where mypy should look for modules
mypy_path = [
    "packages/datagen/src"
]
```

**Running mypy manually**

Check configured files:
```bash
uv run mypy
```

Check a specific directory:
```bash
uv run mypy packages/
```

Check a specific file:
```bash
uv run mypy packages/datagen/src/module.py
```

**Using mypy with pre-commit**

If integrated with pre-commit, mypy runs automatically before each commit, preventing type errors from entering the repository.

Example configuration:

```yaml
- repo: https://github.com/pre-commit/mirrors-mypy
  rev: v1.10.0
  hooks:
    - id: mypy
```

This ensures type safety is validated before code is committed.

### sqlfluff
A SQL linter and formatter designed for consistent style and readability. It supports multiple SQL dialects, can automatically fix some style violations, and integrates into CI pipelines to enforce SQL best practices.

```bash
uv run sqlfluff lint dbt/sample_project
```
```bash
uv run sqlfluff fix dbt/sample_project
```

## Documentation & Automation
### mkdocs
A static site generator specifically for project documentation written in Markdown. MkDocs allows you to create searchable, versioned, and visually appealing documentation websites for your Databricks projects.

### justfile
A command runner for automating repetitive tasks. It defines project-specific tasks in a simple file format, allowing developers to run commands like building, testing, or deploying with a single `just` command.

## Testing
### pytest
A Python testing framework that supports unit, functional, and integration tests. Pytest provides a simple syntax for writing tests, powerful fixtures for setup/teardown, and extensive plugins for coverage, reporting, and mocking.

# Development & Deployment Lifecycle

- [Development Workflow](#development-workflow)
- [Versioning & Release Management](#versioning--release-management)
- [CI/CD & Environment Promotion](#cicd--environment-promotion)
- [Release Governance Principles](#release-governance-principles)

## Development Workflow
### Branching Strategy
### Local Development Workflow
How engineers work locally: Environment setup (uv), Running lint/tests, Validating bundles, Working with dbt (if enabled)
### Pull Request & Code Review Process
Required checks, CI validation steps, Approval requirements, Merge policy

## Versioning & Release Management
### Commit & Versioning Strategy
- https://semver.org/
- https://www.conventionalcommits.org/en/v1.0.0/
- https://github.com/googleapis/release-please

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

### Automated Releases
How release-please works, Release PR generation, Changelog generation, Git tagging

## CI/CD & Environment Promotion
### Pipeline Overview
### Environment Promotion Model
Dev → Test → Prod flow, Version-based promotion, Tag-driven deployments, Manual approval gates (Prod)
```
feature branch → main → release PR → git tag (vX.Y.Z) → Test → Production
```
### Environment Deployments
####  Dev
When it happens, What gets deployed, Purpose of the environment
####  Test
Trigger conditions, Validation scope, Release candidate verification
####  Production
Approval model, Version immutability, Auditability
###  Rollback Strategy
How to redeploy previous tag, Handling hotfixes, Emergency procedures
## Release Governance Principles
- No manual workspace edits
- Everything version-controlled
- Immutable artifacts

# Getting Started
```
choco install just
```

# Configuration

# How-To's
- add a new package > configure it in uv, reference it in bundle

# Links
https://medium.com/the-data-movement/day-16-dbt-pre-commit-hooks-linting-enforcing-sql-quality-with-sqlfluff-dbt-pre-commit-7a5d0639312e

https://docs.databricks.com/aws/en/repos/get-access-tokens-from-git-provider
https://docs.databricks.com/aws/en/dev-tools/auth/oauth-federation-policy#configure-workload
https://docs.databricks.com/aws/en/dev-tools/ci-cd/github
https://docs.databricks.com/aws/en/dev-tools/auth/provider-github
https://github.com/databricks/setup-cli

https://www.youtube.com/watch?v=XumUXF1e6RI

https://docs.astral.sh/uv/guides/integration/github/#publishing-to-pypi
https://packaging.python.org/en/latest/guides/section-build-and-publish/
