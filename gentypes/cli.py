import argparse
import sys
from pathlib import Path
from typing import Optional, Sequence, Text, Tuple

import black
import docformatter
import isort
import jsonschema_gentypes
from jsonschema_gentypes.cli import _AddType

from gentypes.api import API

HEADER_TEXT = "# This is an auto-generated file. Do not modify by hand.\n"


class PythonModule:
    def __init__(self, path: Path):
        self.path = path
        self.sub_modules = set()

    def add_submodule(self, name: str) -> Path:
        file_path = self.path.joinpath(name)
        self.sub_modules.add(name)

        return file_path

    def write_init(self) -> Path:
        init_path = self.path / "__init__.py"
        sub_modules = sorted(self.sub_modules)
        with open(init_path, "w") as f:
            f.writelines([
                HEADER_TEXT,
                "\n",
                *(f"from . import {name}\n" for name in sub_modules),
                "\n",
                "__all__ = [\n",
                *(f'    "{name}",\n' for name in sub_modules),
                "]\n"
            ])

        return init_path


def python_version_type(val: str) -> Tuple[int, ...]:
    return tuple(int(x) for x in val.split("."))


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to cumulus directory", type=Path)
    parser.add_argument("--force", help="Overwrite files if they exist", action="store_true")
    parser.add_argument(
        "--python-version",
        help="The minimal Python version that will support the generate type stubs.",
        default="3.8",
        type=python_version_type
    )
    parser.add_argument("--line-length", help="Max line length", type=int, default=88)

    return parser


def main(args: Optional[Sequence[Text]] = None):
    parser = get_parser()
    ns = parser.parse_args(args)

    tasks_path = ns.path / "tasks"
    tasks_module = PythonModule(Path("cumulus_types/tasks/"))

    for task_path in tasks_path.iterdir():
        task_name = task_path.name.replace("-", "_")
        schema_path = task_path / "schemas"

        if not schema_path.exists() or not schema_path.is_dir():
            continue

        print(f"Processing task {task_name}")

        python_dir = tasks_module.add_submodule(task_name)
        if not python_dir.exists():
            python_dir.mkdir(parents=True)

        module = PythonModule(python_dir)

        for schema_path in schema_path.iterdir():
            if not schema_path.suffix == ".json":
                continue

            python_path = module.add_submodule(schema_path.stem).with_suffix(".py")
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
                line_length=ns.line_length,
                root_name=schema_path.stem.title()
            )
            cleanup_file(python_path, ns.line_length, ns.python_version)

        init_path = module.write_init()
        cleanup_file(init_path, ns.line_length, ns.python_version)

    init_path = tasks_module.path / "__init__.py"
    with open(init_path, "w") as f:
        f.write(HEADER_TEXT)

    cleanup_file(init_path, ns.line_length, ns.python_version)


def generate_types(
    src: Path,
    dst: Path,
    python_version: Tuple[int, ...],
    line_length: int,
    root_name: Optional[str] = None
) -> None:
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
        python_version
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

    with open(dst, "w", encoding="utf-8") as f:
        f.write(HEADER_TEXT)
        f.write("\n")
        f.write("\n".join(lines))
        f.write("\n")


def cleanup_file(path: Path, line_length: int, python_version: Tuple[int, ...]):
    # Code cleanup
    black.format_file_in_place(
        src=path,
        fast=False,
        mode=black.Mode(
            target_versions=set([
                black.TargetVersion[f"PY{''.join(str(x) for x in python_version[:2])}"]
            ]),
            line_length=line_length,
        ),
        write_back=black.WriteBack.YES,
    )

    isort.file(path)

    configurator = docformatter.Configurater([
        "--quite",
        "--wrap-summaries", str(line_length),
        "--in-place",
        str(path)
    ])
    configurator.do_parse_arguments()
    formator = docformatter.Formatter(
        configurator.args,
        stderror=sys.stderr,
        stdin=sys.stdin,
        stdout=sys.stdout,
    )

    formator.do_format_files()
