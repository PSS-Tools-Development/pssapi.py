from . import client_base as _client_base
from . import entities as _entities
from . import enums as _enums
from . import utils as _utils


class PssApiClient(_client_base.PssApiClientBase):
    def __init__(self, device_type: "_enums.DeviceType" = None, language_key: "_enums.LanguageKey" = None, production_server: str = None):
        super().__init__(device_type, language_key, production_server)

    def _update_services(self):
        super()._update_services()

    async def device_login(self, device_key: str, checksum_key: str) -> _entities.UserLogin:
        client_date_time = _utils.get_utc_now()
        checksum = self.user_service.utils.create_device_login_checksum(device_key, self.device_type, client_date_time, checksum_key)
        return await self.user_service.device_login(checksum, client_date_time, device_key, self.device_type)
