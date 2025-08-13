import pssapi.client_base as _client_base
import pssapi.enums as _enums


class PssApiClient(_client_base.PssApiClientBase):
    def __init__(self, device_type: "_enums.DeviceType" = None, language_key: "_enums.LanguageKey" = None, production_server: str = None):
        super().__init__(device_type, language_key, production_server)

    def _update_services(self):
        super()._update_services()
