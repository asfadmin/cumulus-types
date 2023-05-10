import argparse
import sys
from pathlib import Path
from typing import Optional, Sequence, Text

import black
import docformatter
import isort
import jsonschema_gentypes
from jsonschema_gentypes.cli import _AddType

from gentypes.api import API

HEADER_TEXT = "# This is an auto-generated file. Do not modify by hand.\n"


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to cumulus directory", type=Path)
    parser.add_argument("--force", help="Overwrite files if they exist", action="store_true")
    parser.add_argument(
        "--python-version",
        help="The minimal Python version that will support the generate type stubs.",
        default="3.8"
    )

    return parser


def main(args: Optional[Sequence[Text]] = None):
    parser = get_parser()
    ns = parser.parse_args(args)

    tasks_path = ns.path / "tasks"

    for task_path in tasks_path.iterdir():
        task_name = task_path.name.replace("-", "_")
        schema_path = task_path / "schemas"

        if not schema_path.exists() or not schema_path.is_dir():
            continue

        print(f"Processing task {task_name}")

        python_dir = Path("cumulus_types/tasks/") / task_name
        if not python_dir.exists():
            python_dir.mkdir(parents=True)

        init_path = python_dir / "__init__.py"
        init_path.write_text(HEADER_TEXT)

        for schema_path in schema_path.iterdir():
            if not schema_path.suffix == ".json":
                continue

            python_path = (python_dir / schema_path.name).with_suffix(".py")
            if (
                python_path.exists()
                and not ns.force
                and input(f"{python_path} exists. Overwrite? ").lower() != "y"
            ):
                print("Skipping...")
                continue

            generate_types(
                schema_path,
                python_path,
                python_version=ns.python_version,
                root_name=schema_path.stem.title()
            )


def generate_types(
    src: Path,
    dst: Path,
    python_version: Optional[str] = None,
    line_length: int = 88,
    root_name: Optional[str] = None
) -> None:
    if python_version is not None:
        python_version_tup = tuple(int(x) for x in python_version.split("."))
    else:
        python_version_tup = sys.version_info[:3]

    print(f"Processing {src}")

    resolver = jsonschema_gentypes.resolver.RefResolver(str(src))
    schema = resolver.schema

    openapi = "openapi" in schema
    api = API(resolver)

    types = {}
    imports = {}

    add_type = _AddType(
        api,
        resolver,
        imports,
        types,
        {},
        {
            "lineLength": line_length
        },
        python_version_tup
    )

    if openapi:
        raise RuntimeError("OpenAPI not supported")
    else:
        if root_name:
            schema["title"] = root_name
        add_type(schema, root_name or "Root", force_name=bool(root_name))

    lines = []
    for imp, names in imports.items():
        lines.append(f'from {imp} import {", ".join(names)}')

    for type_2 in sorted(types.values(), key=lambda type_3: type_3.name()):
        # Skip constants for default values
        if isinstance(type_2, jsonschema_gentypes.Constant):
            continue

        lines += type_2.definition(line_length)

    with open(dst, "w", encoding="utf-8") as destination_file:
        destination_file.write(HEADER_TEXT)
        destination_file.write("\n")
        destination_file.write("\n".join(lines))
        destination_file.write("\n")

    # Code cleanup
    black.format_file_in_place(
        src=dst,
        fast=False,
        mode=black.Mode(
            target_versions=set([
                black.TargetVersion[f"PY{python_version_tup[0]}{python_version_tup[1]}"]
            ]),
            line_length=line_length,
        ),
        write_back=black.WriteBack.YES,
    )

    isort.file(dst)

    configurator = docformatter.Configurater([
        "--quite",
        "--wrap-summaries", str(line_length),
        "--in-place",
        str(dst)
    ])
    configurator.do_parse_arguments()
    formator = docformatter.Formatter(
        configurator.args,
        stderror=sys.stderr,
        stdin=sys.stdin,
        stdout=sys.stdout,
    )

    formator.do_format_files()
