from enum import StrEnum as _StrEnum


class StrEnumBase(_StrEnum):
    @classmethod
    def _missing_(cls, value: str):
        value_lower = value.lower()
        for member in cls:
            if member.lower() == value_lower:
                return member
        raise ValueError(f"'{value}' is not a valid {cls.__name__}")
