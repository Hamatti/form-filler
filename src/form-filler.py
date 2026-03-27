"""Python script that turns a yaml specification (see specifications/example.yaml)
into a bookmarklet that fills in a form on a website.

See README.md for specification documentation.
"""

import sys
from typing import TypedDict

import yaml
from cerberus import Validator

from src.generators import (
    create_checkbox_input,
    create_date_input,
    create_text_input,
    SpecInput,
)
from src.schema import schema, input_schema


class Spec(TypedDict):
    """A form specification is a dictionary with one key: inputs and within it,
    any number of inputs with keys that can be any string"""

    inputs: dict[str, SpecInput]


def create_bookmarklet(spec: Spec) -> str:
    """Given a valid spec, create a bookmarklet that fills in a form
    specified by the spec."""
    v = Validator()

    inputs: dict = spec.get("inputs", {})
    bookmarklet = """javascript:(function(){"""
    for name, form_input in inputs.items():
        if not v.validate(form_input, input_schema):
            print(
                f'Specification for "{name}" does not match the schema', file=sys.stderr
            )
            print(v.errors, file=sys.stderr)
            sys.exit(1)
        type = form_input.get("type", "")
        match type:
            case "text":
                bookmarklet += create_text_input(name, form_input)
            case "checkbox":
                bookmarklet += create_checkbox_input(name, form_input)
            case "date":
                bookmarklet += create_date_input(name, form_input)
            case _:
                raise NotImplementedError(
                    f"Type {type} (for input {name} is not supported yet."
                )

    bookmarklet += "})();"

    return bookmarklet


def main(spec_path: str) -> str:
    v = Validator()
    try:
        with open(spec_path, "r") as spec_file:
            spec: Spec = yaml.safe_load(spec_file)
            if not v.validate(spec, schema):
                print("Specification does not match the schema", file=sys.stderr)
                print(v.errors, file=sys.stderr)
                sys.exit(1)
    except FileNotFoundError:
        sys.exit(f"File {spec_path} is not found or is not valid YAML file")

    return create_bookmarklet(spec)


if __name__ == "__main__":
    if "--help" in sys.argv:
        print(
            """form-filler

Generates a bookmarklet from a specification file that when run,
fills in a form based on the values in the spec.

usage: uv run form-filler.py [path_to_specification]              
"""
        )
        sys.exit(0)
    if len(sys.argv) < 2:
        sys.exit("You must provide a path to specification file")

    bookmarklet = main(sys.argv[1])
    print(bookmarklet)
