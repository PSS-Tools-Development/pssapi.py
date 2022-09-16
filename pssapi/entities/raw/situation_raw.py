####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class SituationRaw():
    XML_NODE_NAME: str = 'Situation'

    def __init__(self, situation_info: _EntityInfo) -> None:
        self.__situation_id: int = _parse.pss_int(situation_info.get('SituationId'))
        self.__situation_design_id: int = _parse.pss_int(situation_info.get('SituationDesignId'))
        self.__user_id: int = _parse.pss_int(situation_info.get('UserId'))
        self.__situation_category: str = _parse.pss_str(situation_info.get('SituationCategory'))
        self.__remaining_count: int = _parse.pss_int(situation_info.get('RemainingCount'))
        self.__from_date: datetime = _parse.pss_datetime(situation_info.get('FromDate'))
        self.__end_date: datetime = _parse.pss_datetime(situation_info.get('EndDate'))
        self.__reset_date: datetime = _parse.pss_datetime(situation_info.get('ResetDate'))

    @property
    def situation_id(self) -> int:
        return self.__situation_id

    @property
    def situation_design_id(self) -> int:
        return self.__situation_design_id

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def situation_category(self) -> str:
        return self.__situation_category

    @property
    def remaining_count(self) -> int:
        return self.__remaining_count

    @property
    def from_date(self) -> datetime:
        return self.__from_date

    @property
    def end_date(self) -> datetime:
        return self.__end_date

    @property
    def reset_date(self) -> datetime:
        return self.__reset_date
