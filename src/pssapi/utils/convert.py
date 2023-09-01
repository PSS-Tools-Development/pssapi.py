def to_pss_bool(value: bool) -> str:
    return str(bool(value or False)).lower()
