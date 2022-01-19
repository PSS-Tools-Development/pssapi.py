import datetime as _datetime

import pytest as _pytest
import pytz as _pytz

import pssapi.enums as _enums
import pssapi.utils.parse as _parse


def test_pss_bool():
    assert _parse.pss_bool(None) is None
    assert _parse.pss_bool("true")
    assert not _parse.pss_bool("false")
    assert _parse.pss_bool(None, 1) == 1

    with _pytest.raises(Exception):
        _parse.pss_bool(2)  # value is not str
    with _pytest.raises(Exception):
        _parse.pss_bool("kek")  # value has wrong format
    with _pytest.raises(Exception):
        _parse.pss_bool(True)  # value is not str


def test_pss_datetime():
    assert _parse.pss_datetime(None) is None
    assert _parse.pss_datetime("2023-05-01T23:55:43") == _pytz.utc.localize(_datetime.datetime(2023, 5, 1, 23, 55, 43))
    assert _parse.pss_datetime("2023-05-01T23:55:43.367") == _pytz.utc.localize(_datetime.datetime(2023, 5, 1, 23, 55, 43, 367000))

    with _pytest.raises(Exception):
        _parse.pss_datetime("ABC")  # str has wrong format
    with _pytest.raises(Exception):
        _parse.pss_datetime(2)  # value is not str
    with _pytest.raises(Exception):
        _parse.pss_datetime(True)  # value is not str


def test_pss_int_enum():
    assert _parse.pss_int_enum(None, _enums.VisibilityFlags) is None
    assert _parse.pss_int_enum("", _enums.VisibilityFlags) is None
    assert _parse.pss_int_enum("3", _enums.VisibilityFlags) == _enums.VisibilityFlags.ALWAYS_SHOW
    assert _parse.pss_int_enum(3, _enums.VisibilityFlags) == _enums.VisibilityFlags.ALWAYS_SHOW

    with _pytest.raises(ValueError):  # The enum doesn't have such a value
        _parse.pss_int_enum("10", _enums.VisibilityFlags)
    with _pytest.raises(ValueError):  # The enum doesn't have such a value
        _parse.pss_int_enum("f", _enums.VisibilityFlags)


def test_pss_int_flag():
    assert _parse.pss_int_flag(None, _enums.SituationDesignFlag) is None
    assert _parse.pss_int_flag(1, _enums.SituationDesignFlag) == _enums.SituationDesignFlag.AFFECT_ATTACKING_SHIP
    assert _parse.pss_int_flag("1", _enums.SituationDesignFlag) == _enums.SituationDesignFlag.AFFECT_ATTACKING_SHIP
    assert _parse.pss_int_flag(3, _enums.SituationDesignFlag) == _enums.SituationDesignFlag.AFFECT_ATTACKING_SHIP | _enums.SituationDesignFlag.AFFECT_DEFENDING_SHIP
    assert _parse.pss_int_flag("3", _enums.SituationDesignFlag) == _enums.SituationDesignFlag.AFFECT_ATTACKING_SHIP | _enums.SituationDesignFlag.AFFECT_DEFENDING_SHIP

    with _pytest.raises(ValueError):  # The value is out of bounds
        _parse.pss_int_flag(64, _enums.SituationDesignFlag)
    with _pytest.raises(ValueError):  # The value is out of bounds
        _parse.pss_int_flag("64", _enums.SituationDesignFlag)
    with _pytest.raises(ValueError):  # The enum doesn't have such a value
        _parse.pss_int_flag("bruh", _enums.SituationDesignFlag)


def test_pss_str_enum():
    assert _parse.pss_str_enum(None, _enums.DeviceType) is None
    assert _parse.pss_str_enum("DeviceTypeAndroid", _enums.DeviceType) == _enums.DeviceType.ANDROID

    with _pytest.raises(ValueError):  # The enum doesn't have such a value
        _parse.pss_str_enum("DeviceType", _enums.DeviceType)
    with _pytest.raises(ValueError):  # The enum doesn't have such a value
        _parse.pss_str_enum("3", _enums.DeviceType)


def test_pss_float():
    assert _parse.pss_float(None) is None
    assert _parse.pss_float(None, 1) == 1

    result = _parse.pss_float("1.2")
    assert isinstance(result, float)
    assert result == 1.2

    result = _parse.pss_float("5")
    assert isinstance(result, float)
    assert result == 5.0

    assert _parse.pss_float(8) == 8.0
    assert _parse.pss_float(8.2) == 8.2

    with _pytest.raises(Exception):
        _parse.pss_float("X")  # value is wrong format
    with _pytest.raises(Exception):
        _parse.pss_float("2023-05-01T23:55:43")  # value is wrong format


def test_pss_int():
    assert _parse.pss_int(None) is None
    assert _parse.pss_int(None, 1) == 1
    assert _parse.pss_int(None, "A") == "A"

    result = _parse.pss_int("1")
    assert isinstance(result, int)
    assert result == 1

    result = _parse.pss_int("50000")
    assert isinstance(result, int)
    assert result == 50000

    assert _parse.pss_float(8) == 8

    with _pytest.raises(Exception):
        _parse.pss_int("1.2")  # value is wrong format (float)
    with _pytest.raises(Exception):
        _parse.pss_int("X")  # value is wrong format (str)
    with _pytest.raises(Exception):
        _parse.pss_int("2023-05-01T23:55:43")  # value is wrong format (datetime)


def test_pss_str():
    assert _parse.pss_str(None) is None
    assert _parse.pss_str("") is None
    assert _parse.pss_str(None, 1) == 1
    assert _parse.pss_str(None, "A") == "A"

    assert _parse.pss_str("A") == "A"
    assert _parse.pss_str("kek") == "kek"
    assert _parse.pss_str("0") is None
    assert _parse.pss_str("none") is None
    assert _parse.pss_str("NONE") is None
    assert _parse.pss_str("None") is None
