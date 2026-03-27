from src.generators import create_checkbox_input, create_date_input, create_text_input


def test_checkbox_input_checked():
    spec = {"type": "checkbox", "value": True, "selector": "#checkbox"}

    partial = create_checkbox_input("example", spec)

    assert partial == "document.querySelector('#checkbox').checked = true;"


def test_checkbox_input_unchecked():
    spec = {"type": "checkbox", "value": False, "selector": "#checkbox"}

    partial = create_checkbox_input("example", spec)

    assert partial == "document.querySelector('#checkbox').checked = false;"


def test_date_input():
    spec = {"type": "date", "value": "2027-05-25", "selector": "#date"}

    partial = create_date_input("example", spec)

    assert partial == "document.querySelector('#date').value = '2027-05-25';"


def test_textual_input():
    spec = {"type": "text", "value": "Jane Doe", "selector": "#name"}

    partial = create_date_input("example", spec)

    assert partial == "document.querySelector('#name').value = 'Jane Doe';"


def test_numeric_input():
    spec = {"type": "text", "value": 27.5, "selector": "#price"}

    partial = create_date_input("example", spec)

    assert partial == "document.querySelector('#price').value = '27.5';"
