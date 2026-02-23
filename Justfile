checkout branch:
    git checkout main
    git pull
    git checkout -b {{branch}}
    git push

commit msg:
    @echo "Committing with message: {{msg}}"
    git pull
    git add .
    git commit -m "{{msg}}"
    git push

validate:
    uv run pre-commit run --all-files
    uv run pytest

dbt command project:
    uv run dbt {{command}} \
      --project-dir dbt/{{project}} \
      --profiles-dir .dbt
