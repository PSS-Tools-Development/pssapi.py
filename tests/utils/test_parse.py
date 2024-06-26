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
    assert _parse.pss_bool(False) is False
    assert _parse.pss_bool(True) is True

    with _pytest.raises(Exception):
        _parse.pss_bool(2)  # value is not str
    with _pytest.raises(Exception):
        _parse.pss_bool("kek")  # value has wrong format


def test_pss_color():
    assert _parse.pss_color(None) is None
    assert _parse.pss_color("") is None
    assert _parse.pss_color("  ") is None

    color_1 = _parse.pss_color("64,128,255")
    assert color_1.red == 64
    assert color_1.green == 128
    assert color_1.blue == 255

    color_2 = _parse.pss_color("#4080FF")
    assert color_2.red == 64
    assert color_2.green == 128
    assert color_2.blue == 255


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
    assert _parse.pss_int_enum(None, _enums.CrewRarity) is None
    assert _parse.pss_int_enum("", _enums.CrewRarity) is None
    assert _parse.pss_int_enum("3", _enums.CrewRarity) == _enums.CrewRarity.EPIC
    assert _parse.pss_int_enum(3, _enums.CrewRarity) == _enums.CrewRarity.EPIC
    assert _parse.pss_int_enum("0", _enums.CrewRarity) == _enums.CrewRarity.COMMON
    assert _parse.pss_int_enum(0, _enums.CrewRarity) == _enums.CrewRarity.COMMON

    # If a value doesn't exist, return None
    assert _parse.pss_int_enum("10", _enums.CrewRarity) is None
    with _pytest.raises(ValueError):  # If the value is not an int, throw an error
        _parse.pss_int_enum("f", _enums.CrewRarity)


def test_pss_int_flag():
    assert _parse.pss_int_flag(None, _enums.SituationDesignFlag) is None
    assert _parse.pss_int_flag(1, _enums.SituationDesignFlag) == _enums.SituationDesignFlag.AFFECT_ATTACKING_SHIP
    assert _parse.pss_int_flag("1", _enums.SituationDesignFlag) == _enums.SituationDesignFlag.AFFECT_ATTACKING_SHIP
    assert _parse.pss_int_flag(3, _enums.SituationDesignFlag) == _enums.SituationDesignFlag.AFFECT_ATTACKING_SHIP | _enums.SituationDesignFlag.AFFECT_DEFENDING_SHIP
    assert _parse.pss_int_flag("3", _enums.SituationDesignFlag) == _enums.SituationDesignFlag.AFFECT_ATTACKING_SHIP | _enums.SituationDesignFlag.AFFECT_DEFENDING_SHIP

    # If '0' shall be parsed for an IntFlag enum without a matching value, return None
    assert _parse.pss_int_flag("0", _enums.SaleItemMask) is None
    assert _parse.pss_int_flag(0, _enums.SaleItemMask) is None

    # If '0' shall be parsed for an IntFlag enum with a matching value, return None, too
    assert _parse.pss_int_flag("0", _enums.SituationDesignFlag) is None
    assert _parse.pss_int_flag(0, _enums.SituationDesignFlag) is None

    # If value exceeds the max value of the enum, ignore it
    assert _parse.pss_int_flag(1024, _enums.SituationDesignFlag) is None
    assert _parse.pss_int_flag(1025, _enums.SituationDesignFlag) == _enums.SituationDesignFlag.AFFECT_ATTACKING_SHIP

    # If the value is not an int, throw an error
    with _pytest.raises(ValueError):
        _parse.pss_int_flag("bruh", _enums.SituationDesignFlag)


def test_pss_str_enum():
    assert _parse.pss_str_enum(None, _enums.DeviceType) is None
    assert _parse.pss_str_enum("DeviceTypeAndroid", _enums.DeviceType) == _enums.DeviceType.ANDROID

    # If a value doesn't exist, return None
    assert _parse.pss_str_enum("DeviceType", _enums.DeviceType) is None
    assert _parse.pss_str_enum("3", _enums.DeviceType) is None


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
    assert _parse.pss_int("") is None
    assert _parse.pss_int("", 1) == 1
    assert _parse.pss_int("", "A") == "A"

    result = _parse.pss_int("0")
    assert isinstance(result, int)
    assert result == 0

    result = _parse.pss_int("1")
    assert isinstance(result, int)
    assert result == 1

    result = _parse.pss_int("50000")
    assert isinstance(result, int)
    assert result == 50000

    assert _parse.pss_int(0) == 0
    assert _parse.pss_int(0, 1) == 0
    assert _parse.pss_int(8) == 8

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
