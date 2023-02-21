from datetime import datetime as _datetime
from enum import StrEnum as _StrEnum
from typing import Optional as _Optional
from typing import Type as _Type

import pytz as _pytz

import pssapi.constants as _constants


def pss_bool(value: str, default: bool = None) -> _Optional[bool]:
    if not value:
        return default
    return _constants.BOOL_VALUE_LOOKUP[value.lower()]


def pss_datetime(value: str) -> _Optional[_datetime]:
    if not value:
        return None

    try:
        result = _datetime.strptime(value, _constants.DATETIME_FORMAT_ISO)
    except ValueError:
        result = _datetime.strptime(
            value, _constants.DATETIME_FORMAT_ISO_DETAILED)
    result = _pytz.utc.localize(result)
    return result


def pss_enum(value: str, enum: _Type[_StrEnum]) -> _Optional[_StrEnum]:
    if not value:
        return None
    for enum_value in enum:
        if value == enum_value.value:
            return enum_value
    raise TypeError(f'{enum} does not have a member with value: {value}')


def pss_float(value: str, default: float = None) -> _Optional[float]:
    if not value:
        return default
    return float(value)


def pss_int(value: str, default: int = None) -> _Optional[int]:
    if not value:
        return default
    return int(value)


def pss_str(value: str, default: str = None) -> _Optional[str]:
    if not value or value == '0' or value.lower() == 'none':
        return default
    return str(value)
