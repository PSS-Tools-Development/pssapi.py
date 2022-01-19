from typing import Dict as _Dict

BOOL_VALUE_LOOKUP: _Dict[str, bool] = {
    "true": True,
    "false": False,
}

DATETIME_FORMAT_ISO: str = "%Y-%m-%dT%H:%M:%S"
DATETIME_FORMAT_ISO_DETAILED: str = "%Y-%m-%dT%H:%M:%S.%f"

DEFAULT_PRODUCTION_SERVER: str = "api.pixelstarships.com"
