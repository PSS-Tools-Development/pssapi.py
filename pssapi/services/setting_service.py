from .service_base import PssServiceBase as _ServiceBase
from ..entities import Setting as _Setting
from ..enums import DeviceType as _DeviceType
from ..enums import LanguageKey as _LanguageKey

from .raw import SettingServiceRaw as _SettingServiceRaw


########################################################################################
##   This file will be generated automatically from API inspection on the first run   ##
########################################################################################


class SettingService(_ServiceBase):
    async def get_latest_version_3(self, device_type: _DeviceType) -> _Setting:
        result = await _SettingServiceRaw.get_latest_version_3(self.production_server, device_type, self.language_key)
        return result[0]