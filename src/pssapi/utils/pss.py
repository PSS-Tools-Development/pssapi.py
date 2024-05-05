import datetime as _datetime

from . import datetime as _utils_datetime


def is_tournament_time(now: _datetime.datetime) -> bool:
    if now is None:
        raise ValueError("Parameter 'dt' must not be None!")

    if now.day < 22:
        return False  # Tournament starts earliest on 22nd of a month (February in non-leap years)

    first_of_next_month = _utils_datetime.get_first_of_next_month(now)
    tournament_start = first_of_next_month - _datetime.timedelta(days=7)

    result = now < first_of_next_month and now >= tournament_start
    return result
