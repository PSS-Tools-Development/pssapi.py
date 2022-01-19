
from ...utils import parse as _parse
from ...types import EntityInfo as _EntityInfo


#######################################################################
##   This file will be generated automatically from API inspection   ##
#######################################################################


class LatestVersionRaw():
    def __init__(self, latest_version_info: _EntityInfo) -> None:
        self.__setting_id: int = _parse.int(latest_version_info.get('SettingsId'))


    @property
    def setting_id(self) -> int:
        return self.__setting_id


    # @property
    # def ...