from typing import Dict as _Dict


BOOL_VALUE_LOOKUP: _Dict[str, bool] = {
    "true": True,
    "false": False,
}

DATETIME_FORMAT_ISO: str = "%Y-%m-%dT%H:%M:%S"
DATETIME_FORMAT_ISO_DETAILED: str = "%Y-%m-%dT%H:%M:%S.%f"

DEFAULT_PRODUCTION_SERVER: str = "api.pixelstarships.com"

PUSHER_APP_CLUSTER: str = "mt1"
PUSHER_APP_ID: str = "258a49f843d21115d7f7"
PUSHER_AUTH_URL: str = f"http://{DEFAULT_PRODUCTION_SERVER}/UserService/PusherAuth"
