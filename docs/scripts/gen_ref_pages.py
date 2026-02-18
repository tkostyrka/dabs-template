"""Generate the code reference pages and navigation."""

from pathlib import Path
import mkdocs_gen_files

def generate_reference() -> None:
    nav = mkdocs_gen_files.Nav()

    root = Path(__file__).resolve().parents[2]
    packages_dir = root / "packages"

    for package_dir in sorted(packages_dir.iterdir()):
        src_dir = package_dir / "src"

        if not src_dir.exists():
            continue  # skip non-src packages

        package_name = package_dir.name
        print(f"package docs generated: {package_name}")

        for path in sorted(src_dir.rglob("*.py")):
            module_path = path.relative_to(src_dir).with_suffix("")

            # Skip __main__.py
            if module_path.name == "__main__":
                continue

            # Handle __init__.py
            if module_path.name == "__init__":
                module_parts = module_path.parent.parts
                doc_path = Path("reference", package_name, *module_parts, "index.md")
                nav_key = (package_name, *module_parts)
                ident = ".".join(module_parts)
            else:
                module_parts = module_path.parts
                doc_path = Path("reference", package_name, *module_parts).with_suffix(".md")
                nav_key = (package_name, *module_parts)
                ident = ".".join(module_parts)

            nav[nav_key] = doc_path.relative_to("reference").as_posix()

            with mkdocs_gen_files.open(doc_path, "w") as fd:
                fd.write(f"::: {ident}")

            mkdocs_gen_files.set_edit_path(doc_path, path)

    # Write navigation
    with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
        nav_file.writelines(nav.build_literate_nav())

# Execute immediately (also when imported)
generate_reference()
