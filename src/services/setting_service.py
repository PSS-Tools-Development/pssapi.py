from .service_base import PssServiceBase as _ServiceBase
from .. import core as _core
from ..entities import LatestVersion as _LatestVersion
from ..enums import DeviceType as _DeviceType
from ..enums import LanguageKey as _LanguageKey
from ..utils import convert as _convert


#######################################################################
##   This file will be generated automatically from API inspection   ##
#######################################################################


class SettingService(_ServiceBase):
    GET_LATEST_VERSION_BASE_PATH: str = 'SettingService/GetLatestVersion3'


    async def get_latest_version(self, device_type: _DeviceType, language_key: _LanguageKey) -> _LatestVersion:
        params = {
            'deviceType': str(device_type),
            'languageKey': str(language_key),
        }
        raw_xml = await _core.get_data_from_path(self.production_server, SettingService.GET_LATEST_VERSION_BASE_PATH, **params)
        raw_dict = _convert.xmltree_to_dict3(raw_xml)
        result = [_LatestVersion(d) for d in raw_dict.values()]
        return result[0]