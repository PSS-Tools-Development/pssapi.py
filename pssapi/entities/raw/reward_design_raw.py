"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class RewardDesignRaw:
    XML_NODE_NAME: str = 'RewardDesign'

    def __init__(self, reward_design_info: _EntityInfo) -> None:
        self.__reward_design_id: int = _parse.pss_int(
            reward_design_info.get('RewardDesignId'))
        self.__reward_name: str = _parse.pss_str(
            reward_design_info.get('RewardName'))
        self.__reward_description: str = _parse.pss_str(
            reward_design_info.get('RewardDescription'))
        self.__reward_type: str = _parse.pss_str(
            reward_design_info.get('RewardType'))
        self.__argument_string: str = _parse.pss_str(
            reward_design_info.get('ArgumentString'))
        self.__price_string: str = _parse.pss_str(
            reward_design_info.get('PriceString'))
        self.__available_quantity: int = _parse.pss_int(
            reward_design_info.get('AvailableQuantity'))
        self.__max_per_user: int = _parse.pss_int(
            reward_design_info.get('MaxPerUser'))
        self.__available_every_x_days: int = _parse.pss_int(
            reward_design_info.get('AvailableEveryXDays'))
        self.__grids: int = _parse.pss_int(reward_design_info.get('Grids'))
        self.__order_index: int = _parse.pss_int(
            reward_design_info.get('OrderIndex'))
        self.__flags: int = _parse.pss_int(reward_design_info.get('Flags'))
        self.__requirement_string: str = _parse.pss_str(
            reward_design_info.get('RequirementString'))
        self.__metadata: str = _parse.pss_str(
            reward_design_info.get('Metadata'))
        self.__season_design_id: int = _parse.pss_int(
            reward_design_info.get('SeasonDesignId'))
        self.__battle_pass_tier_index: int = _parse.pss_int(
            reward_design_info.get('BattlePassTierIndex'))
        self.__available_from: datetime = _parse.pss_datetime(
            reward_design_info.get('AvailableFrom'))
        self.__available_to: datetime = _parse.pss_datetime(
            reward_design_info.get('AvailableTo'))
        self.__background_sprite_id: int = _parse.pss_int(
            reward_design_info.get('BackgroundSpriteId'))
        self.__sprite_id: int = _parse.pss_int(
            reward_design_info.get('SpriteId'))

    @property
    def reward_design_id(self) -> int:
        return self.__reward_design_id

    @property
    def reward_name(self) -> str:
        return self.__reward_name

    @property
    def reward_description(self) -> str:
        return self.__reward_description

    @property
    def reward_type(self) -> str:
        return self.__reward_type

    @property
    def argument_string(self) -> str:
        return self.__argument_string

    @property
    def price_string(self) -> str:
        return self.__price_string

    @property
    def available_quantity(self) -> int:
        return self.__available_quantity

    @property
    def max_per_user(self) -> int:
        return self.__max_per_user

    @property
    def available_every_x_days(self) -> int:
        return self.__available_every_x_days

    @property
    def grids(self) -> int:
        return self.__grids

    @property
    def order_index(self) -> int:
        return self.__order_index

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def metadata(self) -> str:
        return self.__metadata

    @property
    def season_design_id(self) -> int:
        return self.__season_design_id

    @property
    def battle_pass_tier_index(self) -> int:
        return self.__battle_pass_tier_index

    @property
    def available_from(self) -> datetime:
        return self.__available_from

    @property
    def available_to(self) -> datetime:
        return self.__available_to

    @property
    def background_sprite_id(self) -> int:
        return self.__background_sprite_id

    @property
    def sprite_id(self) -> int:
        return self.__sprite_id
