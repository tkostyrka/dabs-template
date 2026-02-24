The Databricks Asset Bundle projects form the core of this repository. They are stored in the bundles subfolder, where each project has its own dedicated directory.

Within each project, you will find, among other components:
- **Notebook** definitions – containing the source code and logic executed within Databricks.
- **Databricks Workflows** definitions – describing job orchestration, task dependencies, scheduling, and execution settings.
- **Targets** – used to configure the destination environments (e.g., development, staging, production) where the project will be deployed and installed.
- **Variables** (`variables.yml`) – enabling project parameterization, allowing environment-specific values and configuration to be managed in a flexible and reusable way.

This structure ensures clear separation between projects, promotes maintainability, and supports consistent deployment across multiple environments.
