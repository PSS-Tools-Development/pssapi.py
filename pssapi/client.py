from .client_base import PssApiClientBase as _PssApiClientBase
from .enums import DeviceType as _DeviceType
from .enums import LanguageKey as _LanguageKey


class PssApiClient(_PssApiClientBase):
    def __init__(self, device_type: _DeviceType = None, language_key: _LanguageKey = None, production_server: str = None) -> None:
        super().__init__(device_type, language_key, production_server)

    def _update_services(self):
        super()._update_services()

        # declare here custom services
