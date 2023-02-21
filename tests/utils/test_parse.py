import datetime as _datetime
import pytest as _pytest
import pytz as _pytz

import pssapi.utils.parse as _parse
import pssapi.enums as _enums


def test_pss_bool():
    assert _parse.pss_bool(None) is None
    assert _parse.pss_bool('true') == True
    assert _parse.pss_bool('false') == False
    assert _parse.pss_bool(None, 1) == 1

    with _pytest.raises(Exception):
        _parse.pss_bool(2)
    with _pytest.raises(Exception):
        _parse.pss_bool('kek')
    with _pytest.raises(Exception):
        _parse.pss_bool(True)


def test_pss_datetime():
    assert _parse.pss_datetime(None) is None
    assert _parse.pss_datetime('2023-05-01T23:55:43') == _pytz.utc.localize(_datetime.datetime(2023, 5, 1, 23, 55, 43))
    assert _parse.pss_datetime('2023-05-01T23:55:43.367') == _pytz.utc.localize(_datetime.datetime(2023, 5, 1, 23, 55, 43, 367000))

    with _pytest.raises(Exception):
        _parse.pss_datetime('ABC')
    with _pytest.raises(Exception):
        _parse.pss_datetime(2)
    with _pytest.raises(Exception):
        _parse.pss_datetime(True)


def test_pss_enum():
    assert _parse.pss_enum(None, _enums.AchievementType) is None
    assert _parse.pss_enum('DeviceTypeAndroid', _enums.DeviceType) == _enums.DeviceType.DEVICE_TYPE_ANDROID
    assert _parse.pss_enum(3, _enums.VisibilityFlags) == _enums.VisibilityFlags.ALWAYSSHOW

    with _pytest.raises(TypeError): # The enum doesn't have such a value
        _parse.pss_enum('DeviceType', _enums.DeviceType)
    with _pytest.raises(TypeError): # The enum doesn't have such a value
        _parse.pss_enum('3', _enums.VisibilityFlags) == _enums.VisibilityFlags.ALWAYSSHOW


def test_pss_float():
    assert _parse.pss_float(None) is None
    assert _parse.pss_float(None, 1) == 1

    result = _parse.pss_float('1.2')
    assert isinstance(result, float)
    assert result == 1.2

    result = _parse.pss_float('5')
    assert isinstance(result, float)
    assert result == 5.0

    with _pytest.raises(Exception):
        _parse.pss_float('X')
    with _pytest.raises(Exception):
        _parse.pss_float('2023-05-01T23:55:43')


def test_pss_int():
    assert _parse.pss_int(None) is None
    assert _parse.pss_int(None, 1) == 1
    assert _parse.pss_int(None, 'A') == 'A'

    result = _parse.pss_int('1')
    assert isinstance(result, int)
    assert result == 1

    result = _parse.pss_int('50000')
    assert isinstance(result, int)
    assert result == 50000

    with _pytest.raises(Exception):
        _parse.pss_int('1.2')
    with _pytest.raises(Exception):
        _parse.pss_int('X')
    with _pytest.raises(Exception):
        _parse.pss_int('2023-05-01T23:55:43')


def test_pss_str():
    assert _parse.pss_str(None) is None
    assert _parse.pss_str('') is None
    assert _parse.pss_str(None, 1) == 1
    assert _parse.pss_str(None, 'A') == 'A'

    assert _parse.pss_str('A') == 'A'
    assert _parse.pss_str('kek') == 'kek'
    assert _parse.pss_str('0') is None
    assert _parse.pss_str('none') is None
    assert _parse.pss_str('NONE') is None
    assert _parse.pss_str('None') is None