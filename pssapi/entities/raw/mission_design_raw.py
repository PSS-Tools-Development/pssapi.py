"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class MissionDesignRaw:
    XML_NODE_NAME: str = 'MissionDesign'

    def __init__(self, mission_design_info: _EntityInfo) -> None:
        self.__chance: int = _parse.pss_int(mission_design_info.get('Chance'))
        self.__max_attempts_per_day: int = _parse.pss_int(
            mission_design_info.get('MaxAttemptsPerDay'))
        self.__available_to: datetime = _parse.pss_datetime(
            mission_design_info.get('AvailableTo'))
        self.__required_mission_design_id: int = _parse.pss_int(
            mission_design_info.get('RequiredMissionDesignId'))
        self.__mission_design_type: str = _parse.pss_str(
            mission_design_info.get('MissionDesignType'))
        self.__exploration_percentage: int = _parse.pss_int(
            mission_design_info.get('ExplorationPercentage'))
        self.__star_system_id: int = _parse.pss_int(
            mission_design_info.get('StarSystemId'))
        self.__weight: int = _parse.pss_int(mission_design_info.get('Weight'))
        self.__background_sprite_id: int = _parse.pss_int(
            mission_design_info.get('BackgroundSpriteId'))
        self.__flags: int = _parse.pss_int(mission_design_info.get('Flags'))
        self.__available_every_x_days: int = _parse.pss_int(
            mission_design_info.get('AvailableEveryXDays'))
        self.__available_from: datetime = _parse.pss_datetime(
            mission_design_info.get('AvailableFrom'))
        self.__requirement_description: str = _parse.pss_str(
            mission_design_info.get('RequirementDescription'))
        self.__mission_design_id: int = _parse.pss_int(
            mission_design_info.get('MissionDesignId'))
        self.__mission_design_status: str = _parse.pss_str(
            mission_design_info.get('MissionDesignStatus'))
        self.__condition: str = _parse.pss_str(
            mission_design_info.get('Condition'))
        self.__story_animation_id: int = _parse.pss_int(
            mission_design_info.get('StoryAnimationId'))
        self.__mission_description: str = _parse.pss_str(
            mission_design_info.get('MissionDescription'))
        self.__is_single_play: bool = _parse.pss_bool(
            mission_design_info.get('IsSinglePlay'))
        self.__min_ship_level: int = _parse.pss_int(
            mission_design_info.get('MinShipLevel'))
        self.__max_ship_level: int = _parse.pss_int(
            mission_design_info.get('MaxShipLevel'))
        self.__mission_title: str = _parse.pss_str(
            mission_design_info.get('MissionTitle'))
        self.__requirement_string: str = _parse.pss_str(
            mission_design_info.get('RequirementString'))
        self.__story_description: str = _parse.pss_str(
            mission_design_info.get('StoryDescription'))
        self.__min_duration_since_last_event: int = _parse.pss_int(
            mission_design_info.get('MinDurationSinceLastEvent'))

    @property
    def chance(self) -> int:
        return self.__chance

    @property
    def max_attempts_per_day(self) -> int:
        return self.__max_attempts_per_day

    @property
    def available_to(self) -> datetime:
        return self.__available_to

    @property
    def required_mission_design_id(self) -> int:
        return self.__required_mission_design_id

    @property
    def mission_design_type(self) -> str:
        return self.__mission_design_type

    @property
    def exploration_percentage(self) -> int:
        return self.__exploration_percentage

    @property
    def star_system_id(self) -> int:
        return self.__star_system_id

    @property
    def weight(self) -> int:
        return self.__weight

    @property
    def background_sprite_id(self) -> int:
        return self.__background_sprite_id

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def available_every_x_days(self) -> int:
        return self.__available_every_x_days

    @property
    def available_from(self) -> datetime:
        return self.__available_from

    @property
    def requirement_description(self) -> str:
        return self.__requirement_description

    @property
    def mission_design_id(self) -> int:
        return self.__mission_design_id

    @property
    def mission_design_status(self) -> str:
        return self.__mission_design_status

    @property
    def condition(self) -> str:
        return self.__condition

    @property
    def story_animation_id(self) -> int:
        return self.__story_animation_id

    @property
    def mission_description(self) -> str:
        return self.__mission_description

    @property
    def is_single_play(self) -> bool:
        return self.__is_single_play

    @property
    def min_ship_level(self) -> int:
        return self.__min_ship_level

    @property
    def max_ship_level(self) -> int:
        return self.__max_ship_level

    @property
    def mission_title(self) -> str:
        return self.__mission_title

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def story_description(self) -> str:
        return self.__story_description

    @property
    def min_duration_since_last_event(self) -> int:
        return self.__min_duration_since_last_event
