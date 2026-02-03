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
