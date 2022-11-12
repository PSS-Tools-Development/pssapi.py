"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class SituationDesignRaw:
    XML_NODE_NAME: str = 'SituationDesign'

    def __init__(self, situation_design_info: _EntityInfo) -> None:
        self.chance: int = _parse.pss_int(situation_design_info.get('Chance'))
        self.change_argument_string: str = _parse.pss_str(
            situation_design_info.get('ChangeArgumentString'))
        self.change_type: str = _parse.pss_str(
            situation_design_info.get('ChangeType'))
        self.daily_occurrence_limit: int = _parse.pss_int(
            situation_design_info.get('DailyOccurrenceLimit'))
        self.end_date: datetime = _parse.pss_datetime(
            situation_design_info.get('EndDate'))
        self.flags: int = _parse.pss_int(situation_design_info.get('Flags'))
        self.from_date: datetime = _parse.pss_datetime(
            situation_design_info.get('FromDate'))
        self.icon_sprite_id: int = _parse.pss_int(
            situation_design_info.get('IconSpriteId'))
        self.requirement_string: str = _parse.pss_str(
            situation_design_info.get('RequirementString'))
        self.situation_description: str = _parse.pss_str(
            situation_design_info.get('SituationDescription'))
        self.situation_design_id: int = _parse.pss_int(
            situation_design_info.get('SituationDesignId'))
        self.situation_name: str = _parse.pss_str(
            situation_design_info.get('SituationName'))
        self.situation_type: str = _parse.pss_str(
            situation_design_info.get('SituationType'))
        self.trigger_type: str = _parse.pss_str(
            situation_design_info.get('TriggerType'))
