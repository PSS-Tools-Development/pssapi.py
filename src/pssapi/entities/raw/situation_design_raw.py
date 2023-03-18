"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class SituationDesignRaw:
    XML_NODE_NAME: str = "SituationDesign"

    def __init__(self, situation_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._chance: int = _parse.pss_int(situation_design_info.get("Chance"))
        self._change_argument_string: str = _parse.pss_str(situation_design_info.get("ChangeArgumentString"))
        self._change_type: str = _parse.pss_str(situation_design_info.get("ChangeType"))
        self._daily_occurrence_limit: int = _parse.pss_int(situation_design_info.get("DailyOccurrenceLimit"))
        self._end_date: _datetime = _parse.pss_datetime(situation_design_info.get("EndDate"))
        self._flags: int = _parse.pss_int(situation_design_info.get("Flags"))
        self._from_date: _datetime = _parse.pss_datetime(situation_design_info.get("FromDate"))
        self._icon_sprite_id: int = _parse.pss_int(situation_design_info.get("IconSpriteId"))
        self._requirement_string: str = _parse.pss_str(situation_design_info.get("RequirementString"))
        self._situation_description: str = _parse.pss_str(situation_design_info.get("SituationDescription"))
        self._situation_design_id: int = _parse.pss_int(situation_design_info.get("SituationDesignId"))
        self._situation_name: str = _parse.pss_str(situation_design_info.get("SituationName"))
        self._situation_tags: str = _parse.pss_str(situation_design_info.get("SituationTags"))
        self._situation_type: str = _parse.pss_str(situation_design_info.get("SituationType"))
        self._trigger_type: str = _parse.pss_str(situation_design_info.get("TriggerType"))

    @property
    def chance(self) -> int:
        return self._chance

    @property
    def change_argument_string(self) -> str:
        return self._change_argument_string

    @property
    def change_type(self) -> str:
        return self._change_type

    @property
    def daily_occurrence_limit(self) -> int:
        return self._daily_occurrence_limit

    @property
    def end_date(self) -> _datetime:
        return self._end_date

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def from_date(self) -> _datetime:
        return self._from_date

    @property
    def icon_sprite_id(self) -> int:
        return self._icon_sprite_id

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def situation_description(self) -> str:
        return self._situation_description

    @property
    def situation_design_id(self) -> int:
        return self._situation_design_id

    @property
    def situation_name(self) -> str:
        return self._situation_name

    @property
    def situation_tags(self) -> str:
        return self._situation_tags

    @property
    def situation_type(self) -> str:
        return self._situation_type

    @property
    def trigger_type(self) -> str:
        return self._trigger_type

    def _key(self):
        return (
            self.chance,
            self.change_argument_string,
            self.change_type,
            self.daily_occurrence_limit,
            self.end_date,
            self.flags,
            self.from_date,
            self.icon_sprite_id,
            self.requirement_string,
            self.situation_description,
            self.situation_design_id,
            self.situation_name,
            self.situation_tags,
            self.situation_type,
            self.trigger_type,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "Chance": self.chance,
                "ChangeArgumentString": self.change_argument_string,
                "ChangeType": self.change_type,
                "DailyOccurrenceLimit": self.daily_occurrence_limit,
                "EndDate": self.end_date,
                "Flags": self.flags,
                "FromDate": self.from_date,
                "IconSpriteId": self.icon_sprite_id,
                "RequirementString": self.requirement_string,
                "SituationDescription": self.situation_description,
                "SituationDesignId": self.situation_design_id,
                "SituationName": self.situation_name,
                "SituationTags": self.situation_tags,
                "SituationType": self.situation_type,
                "TriggerType": self.trigger_type,
            }

        return self._dict
