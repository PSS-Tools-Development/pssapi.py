import datetime as _datetime

PSS_DATETIME_FORMAT_ISO: str = "%Y-%m-%dT%H:%M:%S"
PSS_DATETIME_FORMAT_ISO_DETAILED: str = "%Y-%m-%dT%H:%M:%S.%f"
PSS_DATETIME_FORMAT_CUSTOM: str = "%d.%m.%y %H:%M"


def convert_to_pss_timestamp(dt: _datetime.datetime) -> str:
    if dt is None:
        return None
    result = dt.strftime(PSS_DATETIME_FORMAT_ISO)
    return result


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


def get_utc_now() -> _datetime.datetime:
    return _datetime.datetime.now(_datetime.timezone.utc)
