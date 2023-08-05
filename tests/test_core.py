import json as _json

import pytest as _pytest

import pssapi.core as _core


def test___create_json_request_content():
    assert _core.__create_json_request_content("{}", {"param1": "value1"}) == _json.dumps({})

    content_structure = '{"Level 1 Element 1":"str","Level 1 Element 2":"str","Level 1 Element 3":{"Level 3-1 Element 1":"int","Level 3-1 Element 2":"str"}}'
    params = {"Level 1 Element 1": "XYZ", "Level 1 Element 2": "%20%20", "Level 3-1 Element 1": 1000, "Level 3-1 Element 2": "1.000"}
    params2 = {"Level 1 Element 1": "XYZ", "Level 1 Element 2": "%20%20", "Level 3-1 Element 1": "1000", "Level 3-1 Element 2": "1.000"}
    params3 = {"Level 1 Element 1": "XYZ", "Level 1 Element 2": "%20%20", "Level 3-1 Element 1": None, "Level 3-1 Element 2": "1.000"}
    expected_result = _json.dumps({"Level 1 Element 1": "XYZ", "Level 1 Element 2": "%20%20", "Level 1 Element 3": {"Level 3-1 Element 1": 1000, "Level 3-1 Element 2": "1.000"}})
    expected_result3 = _json.dumps({"Level 1 Element 1": "XYZ", "Level 1 Element 2": "%20%20", "Level 1 Element 3": {"Level 3-1 Element 2": "1.000"}})

    result = _core.__create_json_request_content(content_structure, params)
    assert result == expected_result
    result2 = _core.__create_json_request_content(content_structure, params2)
    assert result2 != expected_result
    result3 = _core.__create_json_request_content(content_structure, params3)
    assert result3 == expected_result3

    with _pytest.raises(Exception):
        _core.__create_json_request_content(None, None)
    with _pytest.raises(Exception):
        _core.__create_json_request_content(None, {})
    with _pytest.raises(Exception):
        _core.__create_json_request_content("", None)
    with _pytest.raises(Exception):
        _core.__create_json_request_content("", {})
