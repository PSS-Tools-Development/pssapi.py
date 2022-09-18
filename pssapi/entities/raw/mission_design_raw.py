"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class MissionDesignRaw:
    XML_NODE_NAME: str = 'MissionDesign'

    def __init__(self, mission_design_info: _EntityInfo) -> None:
        self.__mission_design_id: int = _parse.pss_int(
            mission_design_info.get('MissionDesignId'))
        self.__mission_title: str = _parse.pss_str(
            mission_design_info.get('MissionTitle'))
        self.__mission_description: str = _parse.pss_str(
            mission_design_info.get('MissionDescription'))
        self.__min_ship_level: int = _parse.pss_int(
            mission_design_info.get('MinShipLevel'))
        self.__max_ship_level: int = _parse.pss_int(
            mission_design_info.get('MaxShipLevel'))
        self.__max_attempts_per_day: int = _parse.pss_int(
            mission_design_info.get('MaxAttemptsPerDay'))
        self.__is_single_play: bool = _parse.pss_bool(
            mission_design_info.get('IsSinglePlay'))
        self.__available_from: datetime = _parse.pss_datetime(
            mission_design_info.get('AvailableFrom'))
        self.__available_to: datetime = _parse.pss_datetime(
            mission_design_info.get('AvailableTo'))
        self.__available_every_x_days: int = _parse.pss_int(
            mission_design_info.get('AvailableEveryXDays'))
        self.__story_description: str = _parse.pss_str(
            mission_design_info.get('StoryDescription'))
        self.__condition: str = _parse.pss_str(
            mission_design_info.get('Condition'))
        self.__mission_design_status: str = _parse.pss_str(
            mission_design_info.get('MissionDesignStatus'))
        self.__mission_design_type: str = _parse.pss_str(
            mission_design_info.get('MissionDesignType'))
        self.__chance: int = _parse.pss_int(mission_design_info.get('Chance'))
        self.__min_duration_since_last_event: int = _parse.pss_int(
            mission_design_info.get('MinDurationSinceLastEvent'))
        self.__weight: int = _parse.pss_int(mission_design_info.get('Weight'))
        self.__requirement_string: str = _parse.pss_str(
            mission_design_info.get('RequirementString'))
        self.__exploration_percentage: int = _parse.pss_int(
            mission_design_info.get('ExplorationPercentage'))
        self.__flags: int = _parse.pss_int(mission_design_info.get('Flags'))
        self.__requirement_description: str = _parse.pss_str(
            mission_design_info.get('RequirementDescription'))
        self.__star_system_id: int = _parse.pss_int(
            mission_design_info.get('StarSystemId'))
        self.__background_sprite_id: int = _parse.pss_int(
            mission_design_info.get('BackgroundSpriteId'))
        self.__required_mission_design_id: int = _parse.pss_int(
            mission_design_info.get('RequiredMissionDesignId'))
        self.__story_animation_id: int = _parse.pss_int(
            mission_design_info.get('StoryAnimationId'))

    @property
    def mission_design_id(self) -> int:
        return self.__mission_design_id

    @property
    def mission_title(self) -> str:
        return self.__mission_title

    @property
    def mission_description(self) -> str:
        return self.__mission_description

    @property
    def min_ship_level(self) -> int:
        return self.__min_ship_level

    @property
    def max_ship_level(self) -> int:
        return self.__max_ship_level

    @property
    def max_attempts_per_day(self) -> int:
        return self.__max_attempts_per_day

    @property
    def is_single_play(self) -> bool:
        return self.__is_single_play

    @property
    def available_from(self) -> datetime:
        return self.__available_from

    @property
    def available_to(self) -> datetime:
        return self.__available_to

    @property
    def available_every_x_days(self) -> int:
        return self.__available_every_x_days

    @property
    def story_description(self) -> str:
        return self.__story_description

    @property
    def condition(self) -> str:
        return self.__condition

    @property
    def mission_design_status(self) -> str:
        return self.__mission_design_status

    @property
    def mission_design_type(self) -> str:
        return self.__mission_design_type

    @property
    def chance(self) -> int:
        return self.__chance

    @property
    def min_duration_since_last_event(self) -> int:
        return self.__min_duration_since_last_event

    @property
    def weight(self) -> int:
        return self.__weight

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def exploration_percentage(self) -> int:
        return self.__exploration_percentage

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def requirement_description(self) -> str:
        return self.__requirement_description

    @property
    def star_system_id(self) -> int:
        return self.__star_system_id

    @property
    def background_sprite_id(self) -> int:
        return self.__background_sprite_id

    @property
    def required_mission_design_id(self) -> int:
        return self.__required_mission_design_id

    @property
    def story_animation_id(self) -> int:
        return self.__story_animation_id
