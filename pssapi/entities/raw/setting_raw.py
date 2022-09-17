from ...utils import parse as _parse
from ...types import EntityInfo as _EntityInfo

"""
    This file will be generated automatically from API inspection
"""


class SettingRaw:
    XML_NODE_NAME: str = 'Setting'

    def __init__(self, setting_info: _EntityInfo) -> None:
        self.__production_server: str = setting_info.get('ProductionServer')
        self.__setting_id: int = _parse.pss_int(setting_info.get('SettingId'))

    @property
    def setting_id(self) -> int:
        return self.__setting_id

    @property
    def production_server(self) -> str:
        return self.__production_server

    # @property
    # def ...
