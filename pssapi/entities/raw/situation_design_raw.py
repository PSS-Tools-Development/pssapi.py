"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class SituationDesignRaw:
    XML_NODE_NAME: str = 'SituationDesign'

    def __init__(self, situation_design_info: _EntityInfo) -> None:
        self.__situation_design_id: int = _parse.pss_int(
            situation_design_info.get('SituationDesignId'))
        self.__situation_name: str = _parse.pss_str(
            situation_design_info.get('SituationName'))
        self.__situation_description: str = _parse.pss_str(
            situation_design_info.get('SituationDescription'))
        self.__situation_type: str = _parse.pss_str(
            situation_design_info.get('SituationType'))
        self.__flags: int = _parse.pss_int(situation_design_info.get('Flags'))
        self.__change_type: str = _parse.pss_str(
            situation_design_info.get('ChangeType'))
        self.__change_argument_string: str = _parse.pss_str(
            situation_design_info.get('ChangeArgumentString'))
        self.__requirement_string: str = _parse.pss_str(
            situation_design_info.get('RequirementString'))
        self.__daily_occurrence_limit: int = _parse.pss_int(
            situation_design_info.get('DailyOccurrenceLimit'))
        self.__trigger_type: str = _parse.pss_str(
            situation_design_info.get('TriggerType'))
        self.__chance: int = _parse.pss_int(
            situation_design_info.get('Chance'))
        self.__from_date: datetime = _parse.pss_datetime(
            situation_design_info.get('FromDate'))
        self.__end_date: datetime = _parse.pss_datetime(
            situation_design_info.get('EndDate'))
        self.__icon_sprite_id: int = _parse.pss_int(
            situation_design_info.get('IconSpriteId'))

    @property
    def situation_design_id(self) -> int:
        return self.__situation_design_id

    @property
    def situation_name(self) -> str:
        return self.__situation_name

    @property
    def situation_description(self) -> str:
        return self.__situation_description

    @property
    def situation_type(self) -> str:
        return self.__situation_type

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def change_type(self) -> str:
        return self.__change_type

    @property
    def change_argument_string(self) -> str:
        return self.__change_argument_string

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def daily_occurrence_limit(self) -> int:
        return self.__daily_occurrence_limit

    @property
    def trigger_type(self) -> str:
        return self.__trigger_type

    @property
    def chance(self) -> int:
        return self.__chance

    @property
    def from_date(self) -> datetime:
        return self.__from_date

    @property
    def end_date(self) -> datetime:
        return self.__end_date

    @property
    def icon_sprite_id(self) -> int:
        return self.__icon_sprite_id
