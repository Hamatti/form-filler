![Form Filler](form-filler-logo.webp)
# Form Filler

Form Filler is a tool that turns a yaml specification into a bookmarklet for filling in forms with demo data.

This is handy for [development of web apps](hamatti.org/posts/automate-filling-form-with-bookmarklet/).

Start by creating a [specification](#specifications) for your form.

## Specifications

To create a new bookmarklet, create a new YAML file in `specifications`.

The data format is as follows:

```yaml
inputs:
    field_1: # This name can be anything that helps you understand
        type: text # see below for available types
        value: example # this varies between types, see below
        selector: "#field" # a CSS selector that identifies your input
    # ... repeat for all the fields
```

### Available types

#### Text

Valid for: 
- `email`
- `hidden`
- `number`
- `password`
- `search`
- `tel`
- `week`

`value` can be pretty much anything, it will be converted to its string representation

#### Checkbox

Valid for:
- `checkbox`

`value` should be either `true` or `false`. Any truthy value will become `true` and any falsy value will become `false`

#### Dates

Valid for:
- `date`

Currently needs to be in `YYYY-MM-DD` format.

## Usage

Install the packages or run with [poetry](https://python-poetry.org/) or [uv](https://docs.astral.sh/uv/) or similar.

```shell
uv sync
uv run src/form-filler.py specifications/example.yaml
```

Copy the output into a new bookmarklet. I usually create a bookmark folder per form and then create a variety of bookmarklets for different scenarios.

### Demo example

In `demo/`, there's an example form that gets filled by a bookmarklet created from `specifications/example.yaml` spec for playing around.

## Dependencies

The project relies on two external dependencies:

- [Cerberus](https://docs.python-cerberus.org/) is used to validate YAML specifications
- [PyYAML](https://pyyaml.org/) is used to parse YAML specifications into Python data structures

## Tests

To run tests, run

```shell
uv run pytest
```