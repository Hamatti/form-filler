"""Defines a top level schema and schema for individual inputs"""

schema = {
    "inputs": {
        "type": "dict",
    }
}

input_schema = {
    "type": {"type": "string"},
    "value": {"type": ["string", "boolean", "number"], "required": True},
    "selector": {"type": "string"},
}
