from cerberus import Validator

from src.schema import schema, input_schema


def test_overall_schema():
    spec = {
        "inputs": {"name": {"type": "text", "value": "Jane Doe", "selector": "#name"}}
    }

    v = Validator()
    assert v.validate(spec, schema) is True


def test_overall_schema_fail():
    spec = {
        "fields": {"name": {"type": "text", "value": "Jane Doe", "selector": "#name"}}
    }

    v = Validator()
    assert v.validate(spec, schema) is False


def test_input_schema():
    spec = {"type": "text", "value": "Jane Doe", "selector": "#name"}

    v = Validator()

    assert v.validate(spec, input_schema) is True


def test_input_schema_missing_value():
    spec = {"type": "text", "selector": "#name"}

    v = Validator()

    assert v.validate(spec, input_schema) is False
    assert v.errors == {"value": ["required field"]}
