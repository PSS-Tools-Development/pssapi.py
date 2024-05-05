import datetime as _datetime


def get_first_of_next_month(now: _datetime.datetime) -> _datetime.datetime:
    if now is None:
        raise ValueError("Parameter 'dt' must not be None!")

    year = now.year
    month = now.month + 1
    if month == 13:
        year += 1
        month = 1

    result = _datetime.datetime(year, month, 1, 0, 0, 0, 0, _datetime.timezone.utc)
    return result


def is_tournament_time(now: _datetime.datetime) -> bool:
    if now is None:
        raise ValueError("Parameter 'dt' must not be None!")

    if now.day < 22:
        return False  # Tournament starts earliest on 22nd of a month (February in non-leap years)

    first_of_next_month = get_first_of_next_month(now)
    tournament_start = first_of_next_month - _datetime.timedelta(days=7)

    result = now < first_of_next_month and now >= tournament_start
    return result
