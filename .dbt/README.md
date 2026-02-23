# dbt Profiles
This folder contains the **dbt profiles** used by the dbt projects located in this repository.

## Why is `profiles.yml` not committed?
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
The local `profiles.yml` is **only required for local development**.   Settings needed in higher environments with automated deployments reuse the content of Databricks Asset Bundle targets.
Configuration in those environments is propagated via variables, so developers do **not** need to manage these settings manually.

## How to Use
1. Copy the sample file:

   ```bash
   cp profiles.yml.sample profiles.yml
   ```

2. Update profiles.yml with your local authentication details.
3. Make sure not to commit profiles.yml.

## Important
Developers must never commit their local `profiles.yml` file to the repository.
This approach ensures that authentication methods based on passwords, secrets, or PAT tokens are not accidentally exposed in version control.
