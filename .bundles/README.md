# Targets Configuration
This folder contains configuration files that define the target environments (`targets`) to which solutions created using **Databricks Asset Bundles** are deployed.
Each target represents a separate deployment environment (for example: development, test, or production).

## Defining Multiple Environments
You can define any number of environments. The only requirement is that each environment must have a **unique name**. This flexibility allows you to manage multiple stages of your deployment process, such as:

- `dev`
- `test`
- `uat`
- `prod`

Each environment can have its own:
- workspace configuration
- permissions
- variables
- deployment mode
- tagging strategy

## Example Target Definition
Below is an example configuration for a `dev` environment:

```yaml
targets:
  dev:
    mode: development
    default: true
    presets:
      tags:
        environment: ${bundle.target}
    workspace:
      host: https://dbc-11111111-1111.cloud.databricks.com/
    permissions:
      - user_name: ${workspace.current_user.userName}
        level: CAN_MANAGE
    variables:
      var_source_catalog: sample
      var_catalog: second
      var_schema: ${workspace.current_user.short_name}
      var_warehouse_id: 1111111111111111
```

## Configuration Breakdown

### `mode`
Specifies the deployment mode of the target environment.
- `development`
- `production`

### `default`
Indicates whether this target is used by default when no explicit target is provided during deployment.
Only one target should have `default: true`.

### `presets.tags`
Defines tags that are automatically attached to deployed resources.

In the example:

```yaml
presets:
  tags:
    environment: ${bundle.target}
```

The environment tag dynamically resolves to the current bundle target name (e.g., `dev`, `prod`).

### `workspace.host`
Specifies the Databricks workspace URL where bundle resources will be deployed. Each target environment should point to its dedicated workspace (for example: separate workspaces for `dev`, `test`, and `prod`). This ensures proper isolation between environments.

Example:

```yaml
workspace:
  host: https://dbc-11111111-1111.cloud.databricks.com/
```

### `permissions`
Defines access control rules applied after deployment.

Example:

```yaml
permissions:
  - user_name: user@example.com
    level: CAN_MANAGE
```

Common permission levels include:
- `CAN_VIEW`
- `CAN_RUN`
- `CAN_MANAGE`

Follow the principle of least privilege, especially in production environments.

### `variables`
Defines environment-specific variables that can be referenced across bundle resources. Variables are commonly used to parameterize:
- catalog names
- schema names
- SQL warehouse identifiers
- other environment-dependent configuration values

Using variables improves reusability and allows the same bundle definition to be deployed safely across multiple environments.

Example:

```yaml
variables:
  var_source_catalog: sample
  var_catalog: dev_catalog
  var_schema: dev_schema
  var_warehouse_id: 1111111111111111
```
