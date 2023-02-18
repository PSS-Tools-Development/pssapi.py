"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class StarSystemMarkerRaw:
    XML_NODE_NAME: str = 'StarSystemMarker'

    def __init__(self, star_system_marker_info: _EntityInfo) -> None:
        self.completion_date: _datetime = _parse.pss_datetime(star_system_marker_info.get('CompletionDate'))
        self.completion_original_value: int = _parse.pss_int(star_system_marker_info.get('CompletionOriginalValue'))
        self.completion_remaining_value: int = _parse.pss_int(star_system_marker_info.get('CompletionRemainingValue'))
        self.completion_value_type: str = _parse.pss_str(star_system_marker_info.get('CompletionValueType'))
        self.cost_string: str = _parse.pss_str(star_system_marker_info.get('CostString'))
        self.cost_type: str = _parse.pss_str(star_system_marker_info.get('CostType'))
        self.description: str = _parse.pss_str(star_system_marker_info.get('Description'))
        self.expiry_date: _datetime = _parse.pss_datetime(star_system_marker_info.get('ExpiryDate'))
        self.from_star_system_id: int = _parse.pss_int(star_system_marker_info.get('FromStarSystemId'))
        self.is_collected: bool = _parse.pss_bool(star_system_marker_info.get('IsCollected'))
        self.is_repeatable: bool = _parse.pss_bool(star_system_marker_info.get('IsRepeatable'))
        self.last_update_date: _datetime = _parse.pss_datetime(star_system_marker_info.get('LastUpdateDate'))
        self.marker_design_id: int = _parse.pss_int(star_system_marker_info.get('MarkerDesignId'))
        self.marker_flags: int = _parse.pss_int(star_system_marker_info.get('MarkerFlags'))
        self.marker_type: str = _parse.pss_str(star_system_marker_info.get('MarkerType'))
        self.metadata: str = _parse.pss_str(star_system_marker_info.get('Metadata'))
        self.mission_design_id: int = _parse.pss_int(star_system_marker_info.get('MissionDesignId'))
        self.mission_event_id: int = _parse.pss_int(star_system_marker_info.get('MissionEventId'))
        self.movement_type: str = _parse.pss_str(star_system_marker_info.get('MovementType'))
        self.next_star_system_id: int = _parse.pss_int(star_system_marker_info.get('NextStarSystemId'))
        self.origin_next_star_system_id: int = _parse.pss_int(star_system_marker_info.get('OriginNextStarSystemId'))
        self.origin_star_system_id: int = _parse.pss_int(star_system_marker_info.get('OriginStarSystemId'))
        self.purchase_flags: int = _parse.pss_int(star_system_marker_info.get('PurchaseFlags'))
        self.requirement_string: str = _parse.pss_str(star_system_marker_info.get('RequirementString'))
        self.reward_string: str = _parse.pss_str(star_system_marker_info.get('RewardString'))
        self.ship_id: int = _parse.pss_int(star_system_marker_info.get('ShipId'))
        self.ship_ids: str = _parse.pss_str(star_system_marker_info.get('ShipIds'))
        self.sprite_id: int = _parse.pss_int(star_system_marker_info.get('SpriteId'))
        self.star_system_arrival_date: _datetime = _parse.pss_datetime(star_system_marker_info.get('StarSystemArrivalDate'))
        self.star_system_id: int = _parse.pss_int(star_system_marker_info.get('StarSystemId'))
        self.star_system_marker_generator_id: str = _parse.pss_str(star_system_marker_info.get('StarSystemMarkerGeneratorId'))
        self.star_system_marker_id: int = _parse.pss_int(star_system_marker_info.get('StarSystemMarkerId'))
        self.title: str = _parse.pss_str(star_system_marker_info.get('Title'))
        self.travel_cool_down_time: int = _parse.pss_int(star_system_marker_info.get('TravelCoolDownTime'))
        self.travel_start_date: _datetime = _parse.pss_datetime(star_system_marker_info.get('TravelStartDate'))
        self.travel_time_multiplier: int = _parse.pss_int(star_system_marker_info.get('TravelTimeMultiplier'))
        self.user_id: int = _parse.pss_int(star_system_marker_info.get('UserId'))
