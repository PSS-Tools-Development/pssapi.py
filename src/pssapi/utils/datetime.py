from datetime import datetime as _datetime
from datetime import timezone as _timezone

PSS_DATETIME_FORMAT_ISO: str = "%Y-%m-%dT%H:%M:%S"
PSS_DATETIME_FORMAT_ISO_DETAILED: str = "%Y-%m-%dT%H:%M:%S.%f"
PSS_DATETIME_FORMAT_CUSTOM: str = "%d.%m.%y %H:%M"


def get_utc_now() -> _datetime:
    return _datetime.now(_timezone.utc)


def convert_to_pss_timestamp(dt: _datetime) -> str:
    result = dt.strftime(PSS_DATETIME_FORMAT_ISO)
    return result
