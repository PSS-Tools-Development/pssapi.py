"""
This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class MissionDesignRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "MissionDesign"

    def __init__(self, mission_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._available_every_x_days: int = _parse.pss_int(mission_design_info.pop("AvailableEveryXDays", None))
        self._available_from: _datetime = _parse.pss_datetime(mission_design_info.pop("AvailableFrom", None))
        self._available_to: _datetime = _parse.pss_datetime(mission_design_info.pop("AvailableTo", None))
        self._background_sprite_id: int = _parse.pss_int(mission_design_info.pop("BackgroundSpriteId", None))
        self._chance: int = _parse.pss_int(mission_design_info.pop("Chance", None))
        self._condition: str = _parse.pss_str(mission_design_info.pop("Condition", None))
        self._exploration_percentage: int = _parse.pss_int(mission_design_info.pop("ExplorationPercentage", None))
        self._flags: int = _parse.pss_int(mission_design_info.pop("Flags", None))
        self._is_single_play: bool = _parse.pss_bool(mission_design_info.pop("IsSinglePlay", None))
        self._max_attempts_per_day: int = _parse.pss_int(mission_design_info.pop("MaxAttemptsPerDay", None))
        self._max_ship_level: int = _parse.pss_int(mission_design_info.pop("MaxShipLevel", None))
        self._metadata: str = _parse.pss_str(mission_design_info.pop("Metadata", None))
        self._min_duration_since_last_event: int = _parse.pss_int(mission_design_info.pop("MinDurationSinceLastEvent", None))
        self._min_ship_level: int = _parse.pss_int(mission_design_info.pop("MinShipLevel", None))
        self._mission_description: str = _parse.pss_str(mission_design_info.pop("MissionDescription", None))
        self._mission_design_id: int = _parse.pss_int(mission_design_info.pop("MissionDesignId", None))
        self._mission_design_status: str = _parse.pss_str(mission_design_info.pop("MissionDesignStatus", None))
        self._mission_design_type: str = _parse.pss_str(mission_design_info.pop("MissionDesignType", None))
        self._mission_title: str = _parse.pss_str(mission_design_info.pop("MissionTitle", None))
        self._required_mission_design_id: int = _parse.pss_int(mission_design_info.pop("RequiredMissionDesignId", None))
        self._requirement_description: str = _parse.pss_str(mission_design_info.pop("RequirementDescription", None))
        self._requirement_string: str = _parse.pss_str(mission_design_info.pop("RequirementString", None))
        self._star_system_id: int = _parse.pss_int(mission_design_info.pop("StarSystemId", None))
        self._story_animation_id: int = _parse.pss_int(mission_design_info.pop("StoryAnimationId", None))
        self._story_description: str = _parse.pss_str(mission_design_info.pop("StoryDescription", None))
        self._weight: int = _parse.pss_int(mission_design_info.pop("Weight", None))
        super().__init__(mission_design_info)

    @property
    def available_every_x_days(self) -> int:
        return self._available_every_x_days

    @property
    def available_from(self) -> _datetime:
        return self._available_from

    @property
    def available_to(self) -> _datetime:
        return self._available_to

    @property
    def background_sprite_id(self) -> int:
        return self._background_sprite_id

    @property
    def chance(self) -> int:
        return self._chance

    @property
    def condition(self) -> str:
        return self._condition

    @property
    def exploration_percentage(self) -> int:
        return self._exploration_percentage

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def is_single_play(self) -> bool:
        return self._is_single_play

    @property
    def max_attempts_per_day(self) -> int:
        return self._max_attempts_per_day

    @property
    def max_ship_level(self) -> int:
        return self._max_ship_level

    @property
    def metadata(self) -> str:
        return self._metadata

    @property
    def min_duration_since_last_event(self) -> int:
        return self._min_duration_since_last_event

    @property
    def min_ship_level(self) -> int:
        return self._min_ship_level

    @property
    def mission_description(self) -> str:
        return self._mission_description

    @property
    def mission_design_id(self) -> int:
        return self._mission_design_id

    @property
    def mission_design_status(self) -> str:
        return self._mission_design_status

    @property
    def mission_design_type(self) -> str:
        return self._mission_design_type

    @property
    def mission_title(self) -> str:
        return self._mission_title

    @property
    def required_mission_design_id(self) -> int:
        return self._required_mission_design_id

    @property
    def requirement_description(self) -> str:
        return self._requirement_description

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def star_system_id(self) -> int:
        return self._star_system_id

    @property
    def story_animation_id(self) -> int:
        return self._story_animation_id

    @property
    def story_description(self) -> str:
        return self._story_description

    @property
    def weight(self) -> int:
        return self._weight

    def _key(self):
        return (
            self.available_every_x_days,
            self.available_from,
            self.available_to,
            self.background_sprite_id,
            self.chance,
            self.condition,
            self.exploration_percentage,
            self.flags,
            self.is_single_play,
            self.max_attempts_per_day,
            self.max_ship_level,
            self.metadata,
            self.min_duration_since_last_event,
            self.min_ship_level,
            self.mission_description,
            self.mission_design_id,
            self.mission_design_status,
            self.mission_design_type,
            self.mission_title,
            self.required_mission_design_id,
            self.requirement_description,
            self.requirement_string,
            self.star_system_id,
            self.story_animation_id,
            self.story_description,
            self.weight,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AvailableEveryXDays": self.available_every_x_days,
                "AvailableFrom": self.available_from,
                "AvailableTo": self.available_to,
                "BackgroundSpriteId": self.background_sprite_id,
                "Chance": self.chance,
                "Condition": self.condition,
                "ExplorationPercentage": self.exploration_percentage,
                "Flags": self.flags,
                "IsSinglePlay": self.is_single_play,
                "MaxAttemptsPerDay": self.max_attempts_per_day,
                "MaxShipLevel": self.max_ship_level,
                "Metadata": self.metadata,
                "MinDurationSinceLastEvent": self.min_duration_since_last_event,
                "MinShipLevel": self.min_ship_level,
                "MissionDescription": self.mission_description,
                "MissionDesignId": self.mission_design_id,
                "MissionDesignStatus": self.mission_design_status,
                "MissionDesignType": self.mission_design_type,
                "MissionTitle": self.mission_title,
                "RequiredMissionDesignId": self.required_mission_design_id,
                "RequirementDescription": self.requirement_description,
                "RequirementString": self.requirement_string,
                "StarSystemId": self.star_system_id,
                "StoryAnimationId": self.story_animation_id,
                "StoryDescription": self.story_description,
                "Weight": self.weight,
            }
            self._dict.update(super().__dict__())

        return self._dict
