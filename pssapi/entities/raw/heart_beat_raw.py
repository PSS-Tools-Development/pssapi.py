####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class HeartBeatRaw():
    XML_NODE_NAME: str = 'HeartBeat'

    def __init__(self, heart_beat_info: _EntityInfo) -> None:
        self.__success: bool = _parse.pss_bool(heart_beat_info.get('success'))

    @property
    def success(self) -> bool:
        return self.__success
