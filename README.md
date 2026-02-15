# dabs-template

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
