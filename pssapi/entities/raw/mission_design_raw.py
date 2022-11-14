"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class MissionDesignRaw:
    XML_NODE_NAME: str = 'MissionDesign'

    def __init__(self, mission_design_info: _EntityInfo) -> None:
        self.available_every_x_days: int = _parse.pss_int(mission_design_info.get('AvailableEveryXDays'))
        self.available_from: _datetime = _parse.pss_datetime(mission_design_info.get('AvailableFrom'))
        self.available_to: _datetime = _parse.pss_datetime(mission_design_info.get('AvailableTo'))
        self.background_sprite_id: int = _parse.pss_int(mission_design_info.get('BackgroundSpriteId'))
        self.chance: int = _parse.pss_int(mission_design_info.get('Chance'))
        self.condition: str = _parse.pss_str(mission_design_info.get('Condition'))
        self.exploration_percentage: int = _parse.pss_int(mission_design_info.get('ExplorationPercentage'))
        self.flags: int = _parse.pss_int(mission_design_info.get('Flags'))
        self.is_single_play: bool = _parse.pss_bool(mission_design_info.get('IsSinglePlay'))
        self.max_attempts_per_day: int = _parse.pss_int(mission_design_info.get('MaxAttemptsPerDay'))
        self.max_ship_level: int = _parse.pss_int(mission_design_info.get('MaxShipLevel'))
        self.min_duration_since_last_event: int = _parse.pss_int(mission_design_info.get('MinDurationSinceLastEvent'))
        self.min_ship_level: int = _parse.pss_int(mission_design_info.get('MinShipLevel'))
        self.mission_description: str = _parse.pss_str(mission_design_info.get('MissionDescription'))
        self.mission_design_id: int = _parse.pss_int(mission_design_info.get('MissionDesignId'))
        self.mission_design_status: str = _parse.pss_str(mission_design_info.get('MissionDesignStatus'))
        self.mission_design_type: str = _parse.pss_str(mission_design_info.get('MissionDesignType'))
        self.mission_title: str = _parse.pss_str(mission_design_info.get('MissionTitle'))
        self.required_mission_design_id: int = _parse.pss_int(mission_design_info.get('RequiredMissionDesignId'))
        self.requirement_description: str = _parse.pss_str(mission_design_info.get('RequirementDescription'))
        self.requirement_string: str = _parse.pss_str(mission_design_info.get('RequirementString'))
        self.star_system_id: int = _parse.pss_int(mission_design_info.get('StarSystemId'))
        self.story_animation_id: int = _parse.pss_int(mission_design_info.get('StoryAnimationId'))
        self.story_description: str = _parse.pss_str(mission_design_info.get('StoryDescription'))
        self.weight: int = _parse.pss_int(mission_design_info.get('Weight'))
