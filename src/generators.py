from typing import TypedDict


class SpecInput(TypedDict):
    """A form input specification.

    type: type of input field (currently supported: input|checkbox)
    value: value to fill in
    selector: a CSS selector to be used to select the input
    """

    type: str
    value: str | bool
    selector: str


def create_text_input(name: str, text_input: SpecInput) -> str:
    """Creates a line of Javascript code that inputs value into
    an input found with a given CSS selector"""
    selector = text_input.get("selector")
    value = text_input.get("value", "")

    if not selector:
        raise AttributeError(
            f"No valid selector provided for {text_input} (for input {name})"
        )

    return f"""document.querySelector('{selector}').value = '{value}';"""


def create_checkbox_input(name: str, checkbox_input: SpecInput) -> str:
    """Creates a line of Javascript code that checks or unchecks a
    checkbox found with a given CSS selector"""
    selector = checkbox_input.get("selector")
    value = checkbox_input.get("value", "")

    if not selector:
        raise AttributeError(
            f"No valid selector provided for {checkbox_input} (for input {name})"
        )

    js_bool = "true" if value else "false"

    return f"""document.querySelector('{selector}').checked = {js_bool};"""


def create_date_input(name: str, date_input: SpecInput) -> str:
    """Creates a line of Javascript code that inputs a date into
    an input found with a given CSS selector"""
    selector = date_input.get("selector")
    value = date_input.get("value", "")

    if not selector:
        raise AttributeError(
            f"No valid selector provided for {date_input} (for input {name})"
        )

    return f"""document.querySelector('{selector}').value = '{value}';"""
