from datetime import datetime
from enum import IntEnum, IntFlag
from typing import Optional, Type

import pytz

from pssapi import constants
from pssapi.entities import metadata
from pssapi.enums import StrEnumBase


def pss_bool(value: Optional[str] | bool, default: Optional[bool] = None) -> Optional[bool]:
    if isinstance(value, bool):
        return value
    if not value:
        return default
    return constants.BOOL_VALUE_LOOKUP[value.lower()]


def pss_color(value: Optional[str]) -> Optional["metadata.Color"]:
    if not value or not value.strip():
        return None
    return metadata.Color(value)


def pss_datetime(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None

    try:
        result = datetime.strptime(value, constants.DATETIME_FORMAT_ISO)
    except ValueError:
        result = datetime.strptime(value, constants.DATETIME_FORMAT_ISO_DETAILED)
    result = pytz.utc.localize(result)
    return result


def pss_int_enum(value: Optional[str], enum: Type[IntEnum]) -> Optional[IntEnum]:
    int_value = pss_int(value)
    if int_value is None:
        return None
    try:
        return enum(int_value)
    except ValueError:
        return None


def pss_int_flag(value: Optional[str], enum: Type[IntFlag]) -> Optional[IntFlag]:
    int_value = pss_int(value)
    if int_value is None:  # Return None if the value parses to 0 or None
        return None
    max_value = int(enum(-1))
    int_value = int_value & max_value
    if not int_value:
        return None
    return enum(int_value)


def pss_str_enum(value: Optional[str], enum: Type[StrEnumBase]) -> Optional[StrEnumBase]:
    try:
        return enum(value)
    except ValueError:
        return None


def pss_float(value: Optional[str], default: Optional[float] = None) -> Optional[float]:
    if not value:
        return default
    return float(value)


def pss_int(value: Optional[str], default: Optional[int] = None) -> Optional[int]:
    if value is None or value == "":
        return default
    return int(value)


def pss_str(value: Optional[str], default: Optional[str] = None) -> Optional[str]:
    if not value or value == "0" or value.lower() == "none":
        return default
    return str(value)
