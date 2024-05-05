import datetime as _datetime

import pytest as _pytest

import pssapi.utils.pss as _pss


def test_is_tournament_time():
    with _pytest.raises(ValueError):
        _pss.is_tournament_time(None)

    test_cases = [
        (_datetime.datetime(2024, 1, 1, tzinfo=_datetime.timezone.utc), False),  # now.day < 22
        (_datetime.datetime(2024, 1, 21, tzinfo=_datetime.timezone.utc), False),  # now.day < 22
        # January
        (_datetime.datetime(2024, 1, 24, tzinfo=_datetime.timezone.utc), False),
        (_datetime.datetime(2024, 1, 25, tzinfo=_datetime.timezone.utc), True),
        (_datetime.datetime(2024, 1, 31, tzinfo=_datetime.timezone.utc), True),
        # February
        (_datetime.datetime(2024, 2, 22, tzinfo=_datetime.timezone.utc), False),  # 2024 is a leap year
        (_datetime.datetime(2024, 2, 23, tzinfo=_datetime.timezone.utc), True),
        (_datetime.datetime(2024, 2, 29, tzinfo=_datetime.timezone.utc), True),
        (_datetime.datetime(2023, 2, 21, tzinfo=_datetime.timezone.utc), False),  # 2023 is not a leap year
        (_datetime.datetime(2023, 2, 22, tzinfo=_datetime.timezone.utc), True),
        (_datetime.datetime(2023, 2, 28, tzinfo=_datetime.timezone.utc), True),
        # March
        (_datetime.datetime(2024, 3, 24, tzinfo=_datetime.timezone.utc), False),
        (_datetime.datetime(2024, 3, 25, tzinfo=_datetime.timezone.utc), True),
        (_datetime.datetime(2024, 3, 31, tzinfo=_datetime.timezone.utc), True),
        # April
        (_datetime.datetime(2024, 4, 23, tzinfo=_datetime.timezone.utc), False),
        (_datetime.datetime(2024, 4, 24, tzinfo=_datetime.timezone.utc), True),
        (_datetime.datetime(2024, 4, 30, tzinfo=_datetime.timezone.utc), True),
        # May
        (_datetime.datetime(2024, 5, 24, tzinfo=_datetime.timezone.utc), False),
        (_datetime.datetime(2024, 5, 25, tzinfo=_datetime.timezone.utc), True),
        (_datetime.datetime(2024, 5, 31, tzinfo=_datetime.timezone.utc), True),
        # June
        (_datetime.datetime(2024, 6, 23, tzinfo=_datetime.timezone.utc), False),
        (_datetime.datetime(2024, 6, 24, tzinfo=_datetime.timezone.utc), True),
        (_datetime.datetime(2024, 6, 30, tzinfo=_datetime.timezone.utc), True),
        # July
        (_datetime.datetime(2024, 7, 24, tzinfo=_datetime.timezone.utc), False),
        (_datetime.datetime(2024, 7, 25, tzinfo=_datetime.timezone.utc), True),
        (_datetime.datetime(2024, 7, 31, tzinfo=_datetime.timezone.utc), True),
        # August
        (_datetime.datetime(2024, 8, 24, tzinfo=_datetime.timezone.utc), False),
        (_datetime.datetime(2024, 8, 25, tzinfo=_datetime.timezone.utc), True),
        (_datetime.datetime(2024, 8, 31, tzinfo=_datetime.timezone.utc), True),
        # September
        (_datetime.datetime(2024, 9, 23, tzinfo=_datetime.timezone.utc), False),
        (_datetime.datetime(2024, 9, 24, tzinfo=_datetime.timezone.utc), True),
        (_datetime.datetime(2024, 9, 30, tzinfo=_datetime.timezone.utc), True),
        # October
        (_datetime.datetime(2024, 10, 24, tzinfo=_datetime.timezone.utc), False),
        (_datetime.datetime(2024, 10, 25, tzinfo=_datetime.timezone.utc), True),
        (_datetime.datetime(2024, 10, 31, tzinfo=_datetime.timezone.utc), True),
        # November
        (_datetime.datetime(2024, 11, 23, tzinfo=_datetime.timezone.utc), False),
        (_datetime.datetime(2024, 11, 24, tzinfo=_datetime.timezone.utc), True),
        (_datetime.datetime(2024, 11, 30, tzinfo=_datetime.timezone.utc), True),
        # December
        (_datetime.datetime(2024, 12, 24, tzinfo=_datetime.timezone.utc), False),
        (_datetime.datetime(2024, 12, 25, tzinfo=_datetime.timezone.utc), True),
        (_datetime.datetime(2024, 12, 31, tzinfo=_datetime.timezone.utc), True),
    ]

    for now, result in test_cases:
        assert _pss.is_tournament_time(now) == result


def test_get_first_of_next_month():
    with _pytest.raises(ValueError):
        _pss.get_first_of_next_month(None)

    test_cases = [
        (_datetime.datetime(2024, 1, 2, tzinfo=_datetime.timezone.utc), _datetime.datetime(2024, 2, 1, tzinfo=_datetime.timezone.utc)),
        (_datetime.datetime(2024, 12, 24, tzinfo=_datetime.timezone.utc), _datetime.datetime(2025, 1, 1, tzinfo=_datetime.timezone.utc)),
    ]

    for now, result in test_cases:
        assert _pss.get_first_of_next_month(now) == result
