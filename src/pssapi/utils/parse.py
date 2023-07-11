from datetime import datetime as _datetime
from enum import IntEnum as _IntEnum
from enum import IntFlag as _IntFlag
from typing import Optional as _Optional
from typing import Type as _Type

import pytz as _pytz

import pssapi.constants as _constants
from pssapi.entities import metadata as _metadata
from pssapi.enums import StrEnumBase as _StrEnumBase


def pss_bool(value: str, default: bool = None) -> _Optional[bool]:
    if isinstance(value, bool):
        return value
    if not value:
        return default
    return _constants.BOOL_VALUE_LOOKUP[value.lower()]


def pss_color(value: str) -> _Optional["_metadata.Color"]:
    if not value or not value.strip():
        return None
    return _metadata.Color(value)


def pss_datetime(value: str) -> _Optional[_datetime]:
    if not value:
        return None

    try:
        result = _datetime.strptime(value, _constants.DATETIME_FORMAT_ISO)
    except ValueError:
        result = _datetime.strptime(value, _constants.DATETIME_FORMAT_ISO_DETAILED)
    result = _pytz.utc.localize(result)
    return result


def pss_int_enum(value: str, enum: _Type[_IntEnum]) -> _Optional[_IntEnum]:
    value = pss_int(value)
    if value is None:
        return None
    return enum(value)


def pss_int_flag(value: str, enum: _Type[_IntFlag]) -> _Optional[_IntFlag]:
    int_value = pss_int(value)
    if not int_value:  # Return None if the value parses to 0 or None
        return None
    max_value = int(enum(-1))
    if int_value < -max_value or int_value > max_value:
        raise ValueError(f"{value} is not a valid member of {enum}!")
    return enum(int_value)


def pss_str_enum(value: str, enum: _Type[_StrEnumBase]) -> _Optional[_StrEnumBase]:
    if not value:
        return None
    return enum(value)


def pss_float(value: str, default: float = None) -> _Optional[float]:
    if not value:
        return default
    return float(value)


def pss_int(value: str, default: int = None) -> _Optional[int]:
    if value is None or value == "":
        return default
    return int(value)


def pss_str(value: str, default: str = None) -> _Optional[str]:
    if not value or value == "0" or value.lower() == "none":
        return default
    return str(value)
