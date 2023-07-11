from enum import StrEnum as _StrEnum


class StrEnumBase(_StrEnum):
    @classmethod
    def _missing_(cls, value: str):
        if isinstance(value, str):
            try:
                float_value = float(value)
                if not float_value:
                    return cls("None")
            except:
                pass

            try:
                int_value = int(value)
                if not int_value:
                    return cls("None")
            except:
                pass

            value_lower = value.lower()
            for member in cls:
                if member.lower() == value_lower:
                    return member
            raise ValueError(f"'{value}' is not a valid {cls.__qualname__}")
        return cls("None")
