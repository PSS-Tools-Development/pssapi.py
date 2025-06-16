import datetime as _datetime

import pytest as _pytest

import pssapi.utils.datetime as _utils_datetime


def test_convert_to_pss_timestamp():
    assert _utils_datetime.convert_to_pss_timestamp(_datetime.datetime(2022, 5, 6, 12, 4, 2)) == "2022-05-06T12:04:02"
    assert _utils_datetime.convert_to_pss_timestamp(_datetime.datetime(1900, 1, 1, 0, 0, 0)) == "1900-01-01T00:00:00"
    assert _utils_datetime.convert_to_pss_timestamp(None) is None


def test_get_first_of_next_month():
    with _pytest.raises(ValueError):
        _utils_datetime.get_first_of_next_month(None)

    test_cases = [
        (_datetime.datetime(2024, 1, 2, tzinfo=_datetime.timezone.utc), _datetime.datetime(2024, 2, 1, tzinfo=_datetime.timezone.utc)),
        (_datetime.datetime(2024, 12, 24, tzinfo=_datetime.timezone.utc), _datetime.datetime(2025, 1, 1, tzinfo=_datetime.timezone.utc)),
    ]

    for now, result in test_cases:
        assert _utils_datetime.get_first_of_next_month(now) == result
