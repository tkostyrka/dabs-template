[📖 Back to main README](/README.md)

# dbt Profiles
This folder contains the **dbt profiles** used by all dbt projects located in this repository.

## `profiles.yml`
dbt requires the profile configuration file to be named exactly `profiles.yml`.

However, this file may contain sensitive authentication details such as:

- Passwords
- Secrets
- Personal Access Tokens (PAT)
- Other credentials

To prevent accidental exposure of sensitive information:

- `profiles.yml` is added to `.gitignore`
- A template file named `profiles.yml.sample` is committed to the repository instead

## Scope
The local `profiles.yml` is **only required for local development**. Settings needed in higher environments with automated deployments reuse the content of Databricks Asset Bundle targets.
Configuration in those environments is propagated via variables, so developers do **not** need to manage these settings manually.

## How to Use
1. Copy the sample file:

   ```bash
   cp profiles.yml.sample profiles.yml
   ```

2. Update profiles.yml with your local authentication details. By default its set to oauth.
3. Add one block for each dbt project-target pair (replace `sample_project`)

```yaml
sample_project:
   target: dev
   outputs:
     dev:
       type: databricks
       method: http
       catalog: <your_catalog>
       schema: <your_schema>
       http_path: /sql/1.0/warehouses/<your_http_path>
       host: https://adb-<your_workspace>.azuredatabricks.net/
       auth_type: oauth
```

## Important
Developers must never commit their local `profiles.yml` file to the repository.
This approach ensures that authentication methods based on passwords, secrets, or PAT tokens are not accidentally exposed in version control.

# Running dbt Commands
The structure of this repository requires running dbt in a specific way.

**From the repository root:**
```bash
uv run dbt run --project-dir dbt/sample_project --profiles-dir .dbt
```

```bash
uv run dbt docs serve --project-dir dbt/sample_project --profiles-dir .dbt
```

**From inside a project folder:**
```bash
uv run dbt run --profiles-dir ../../.dbt
```

You can also use the shortcut defined in just:
```bash
# Generic command template
dbt command project:
    uv run dbt {{command}} \
      --project-dir dbt/{{project}} \
      --profiles-dir .dbt
```

Then invoke it like this:
```bash
just dbt run sample_project
```
