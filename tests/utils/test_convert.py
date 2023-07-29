import pssapi.utils.convert as _convert


def test_to_pss_bool():
    assert _convert.to_pss_bool(None) == "false"

    assert _convert.to_pss_bool(False) == "false"
    assert _convert.to_pss_bool(True) == "true"

    assert _convert.to_pss_bool(0) == "false"
    assert _convert.to_pss_bool(1) == "true"

    assert _convert.to_pss_bool("") == "false"
    assert _convert.to_pss_bool("a") == "true"
