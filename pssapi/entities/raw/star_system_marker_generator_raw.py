"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class StarSystemMarkerGeneratorRaw:
    XML_NODE_NAME: str = 'StarSystemMarkerGenerator'

    def __init__(self, star_system_marker_generator_info: _EntityInfo) -> None:
        self.behavior_flags: int = _parse.pss_int(
            star_system_marker_generator_info.get('BehaviorFlags'))
        self.completion_original_value: int = _parse.pss_int(
            star_system_marker_generator_info.get('CompletionOriginalValue'))
        self.completion_value_type: str = _parse.pss_str(
            star_system_marker_generator_info.get('CompletionValueType'))
        self.cost_string: str = _parse.pss_str(
            star_system_marker_generator_info.get('CostString'))
        self.cost_type: str = _parse.pss_str(
            star_system_marker_generator_info.get('CostType'))
        self.description: str = _parse.pss_str(
            star_system_marker_generator_info.get('Description'))
        self.end_date: datetime = _parse.pss_datetime(
            star_system_marker_generator_info.get('EndDate'))
        self.from_star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('FromStarSystemId'))
        self.generation_flags: int = _parse.pss_int(
            star_system_marker_generator_info.get('GenerationFlags'))
        self.generation_interval: int = _parse.pss_int(
            star_system_marker_generator_info.get('GenerationInterval'))
        self.marker_design_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('MarkerDesignId'))
        self.marker_duration: int = _parse.pss_int(
            star_system_marker_generator_info.get('MarkerDuration'))
        self.marker_flags: int = _parse.pss_int(
            star_system_marker_generator_info.get('MarkerFlags'))
        self.marker_requirement_string: str = _parse.pss_str(
            star_system_marker_generator_info.get('MarkerRequirementString'))
        self.marker_type: str = _parse.pss_str(
            star_system_marker_generator_info.get('MarkerType'))
        self.max_active_markers: int = _parse.pss_int(
            star_system_marker_generator_info.get('MaxActiveMarkers'))
        self.metadata: str = _parse.pss_str(
            star_system_marker_generator_info.get('Metadata'))
        self.movement_type: str = _parse.pss_str(
            star_system_marker_generator_info.get('MovementType'))
        self.name: str = _parse.pss_str(
            star_system_marker_generator_info.get('Name'))
        self.next_star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('NextStarSystemId'))
        self.number_of_markers: int = _parse.pss_int(
            star_system_marker_generator_info.get('NumberOfMarkers'))
        self.number_of_ships: int = _parse.pss_int(
            star_system_marker_generator_info.get('NumberOfShips'))
        self.origin_next_star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('OriginNextStarSystemId'))
        self.origin_star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('OriginStarSystemId'))
        self.requirement_string: str = _parse.pss_str(
            star_system_marker_generator_info.get('RequirementString'))
        self.reward_string: str = _parse.pss_str(
            star_system_marker_generator_info.get('RewardString'))
        self.ship_ids: str = _parse.pss_str(
            star_system_marker_generator_info.get('ShipIds'))
        self.ship_tags: str = _parse.pss_str(
            star_system_marker_generator_info.get('ShipTags'))
        self.slots: str = _parse.pss_str(
            star_system_marker_generator_info.get('Slots'))
        self.sprite_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('SpriteId'))
        self.star_system_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('StarSystemId'))
        self.star_system_marker_generator_id: int = _parse.pss_int(
            star_system_marker_generator_info.get('StarSystemMarkerGeneratorId'))
        self.start_date: datetime = _parse.pss_datetime(
            star_system_marker_generator_info.get('StartDate'))
        self.tags: str = _parse.pss_str(
            star_system_marker_generator_info.get('Tags'))
        self.title: str = _parse.pss_str(
            star_system_marker_generator_info.get('Title'))
        self.travel_cool_down_time: int = _parse.pss_int(
            star_system_marker_generator_info.get('TravelCoolDownTime'))
        self.travel_duration: int = _parse.pss_int(
            star_system_marker_generator_info.get('TravelDuration'))
        self.travel_start_date: datetime = _parse.pss_datetime(
            star_system_marker_generator_info.get('TravelStartDate'))
        self.travel_time_multiplier: int = _parse.pss_int(
            star_system_marker_generator_info.get('TravelTimeMultiplier'))
