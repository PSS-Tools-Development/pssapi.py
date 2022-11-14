"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RewardDesignRaw:
    XML_NODE_NAME: str = 'RewardDesign'

    def __init__(self, reward_design_info: _EntityInfo) -> None:
        self.argument_string: str = _parse.pss_str(reward_design_info.get('ArgumentString'))
        self.available_every_x_days: int = _parse.pss_int(reward_design_info.get('AvailableEveryXDays'))
        self.available_from: _datetime = _parse.pss__datetime(reward_design_info.get('AvailableFrom'))
        self.available_quantity: int = _parse.pss_int(reward_design_info.get('AvailableQuantity'))
        self.available_to: _datetime = _parse.pss__datetime(reward_design_info.get('AvailableTo'))
        self.background_sprite_id: int = _parse.pss_int(reward_design_info.get('BackgroundSpriteId'))
        self.battle_pass_tier_index: int = _parse.pss_int(reward_design_info.get('BattlePassTierIndex'))
        self.flags: int = _parse.pss_int(reward_design_info.get('Flags'))
        self.grids: int = _parse.pss_int(reward_design_info.get('Grids'))
        self.max_per_user: int = _parse.pss_int(reward_design_info.get('MaxPerUser'))
        self.metadata: str = _parse.pss_str(reward_design_info.get('Metadata'))
        self.order_index: int = _parse.pss_int(reward_design_info.get('OrderIndex'))
        self.price_string: str = _parse.pss_str(reward_design_info.get('PriceString'))
        self.requirement_string: str = _parse.pss_str(reward_design_info.get('RequirementString'))
        self.reward_description: str = _parse.pss_str(reward_design_info.get('RewardDescription'))
        self.reward_design_id: int = _parse.pss_int(reward_design_info.get('RewardDesignId'))
        self.reward_name: str = _parse.pss_str(reward_design_info.get('RewardName'))
        self.reward_type: str = _parse.pss_str(reward_design_info.get('RewardType'))
        self.season_design_id: int = _parse.pss_int(reward_design_info.get('SeasonDesignId'))
        self.sprite_id: int = _parse.pss_int(reward_design_info.get('SpriteId'))
