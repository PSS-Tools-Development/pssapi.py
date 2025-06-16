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
        """Shortcut to self.user_service.device_login(), calculating the required information.

        Args:
            device_key (str): A UUID representing a "device".
            checksum_key (str): A secret required to generate a checksum for the login.

        Returns:
            _entities.UserLogin: An object containing information on the last user logged on the device with the provided `device_key` and an access token for that user.
        """
        client_date_time = _utils.get_utc_now()
        checksum = self.user_service.utils.create_device_login_checksum(self.device_type, client_date_time, checksum_key, device_key)
        return await self.user_service.device_login(checksum, client_date_time, device_key, self.device_type)
