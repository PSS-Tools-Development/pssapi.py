"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class PromotionDesignRaw:
    XML_NODE_NAME: str = 'PromotionDesign'

    def __init__(self, promotion_design_info: _EntityInfo) -> None:
        self.__promotion_design_id: int = _parse.pss_int(
            promotion_design_info.get('PromotionDesignId'))
        self.__name: str = _parse.pss_str(promotion_design_info.get('Name'))
        self.__promotion_type: str = _parse.pss_str(
            promotion_design_info.get('PromotionType'))
        self.__purchase_mask: int = _parse.pss_int(
            promotion_design_info.get('PurchaseMask'))
        self.__title: str = _parse.pss_str(promotion_design_info.get('Title'))
        self.__sub_title: str = _parse.pss_str(
            promotion_design_info.get('SubTitle'))
        self.__description: str = _parse.pss_str(
            promotion_design_info.get('Description'))
        self.__reward_string: str = _parse.pss_str(
            promotion_design_info.get('RewardString'))
        self.__starbux_bonus_percentage: int = _parse.pss_int(
            promotion_design_info.get('StarbuxBonusPercentage'))
        self.__resource_conversion_discount_percentage: int = _parse.pss_int(
            promotion_design_info.get('ResourceConversionDiscountPercentage'))
        self.__reward_store_discount_percentage: int = _parse.pss_int(
            promotion_design_info.get('RewardStoreDiscountPercentage'))
        self.__speed_up_discount_percentage: int = _parse.pss_int(
            promotion_design_info.get('SpeedUpDiscountPercentage'))
        self.__extra_crew_draws: int = _parse.pss_int(
            promotion_design_info.get('ExtraCrewDraws'))
        self.__flags: int = _parse.pss_int(promotion_design_info.get('Flags'))
        self.__order_index: int = _parse.pss_int(
            promotion_design_info.get('OrderIndex'))
        self.__requirement_string: str = _parse.pss_str(
            promotion_design_info.get('RequirementString'))
        self.__xp_bonus_percentage: int = _parse.pss_int(
            promotion_design_info.get('XPBonusPercentage'))
        self.__metadata: str = _parse.pss_str(
            promotion_design_info.get('Metadata'))
        self.__pack_id: str = _parse.pss_str(
            promotion_design_info.get('PackId'))
        self.__available_every_x_days: int = _parse.pss_int(
            promotion_design_info.get('AvailableEveryXDays'))
        self.__available_for_days: int = _parse.pss_int(
            promotion_design_info.get('AvailableForDays'))
        self.__remaining_quantity: int = _parse.pss_int(
            promotion_design_info.get('RemainingQuantity'))
        self.__cost_string: str = _parse.pss_str(
            promotion_design_info.get('CostString'))
        self.__background_sprite_id: int = _parse.pss_int(
            promotion_design_info.get('BackgroundSpriteId'))
        self.__sprite_id: int = _parse.pss_int(
            promotion_design_info.get('SpriteId'))
        self.__icon_sprite_id: int = _parse.pss_int(
            promotion_design_info.get('IconSpriteId'))
        self.__required_promotion_design_id: int = _parse.pss_int(
            promotion_design_info.get('RequiredPromotionDesignId'))
        self.__title_sprite_id: int = _parse.pss_int(
            promotion_design_info.get('TitleSpriteId'))
        self.__close_button_sprite_id: int = _parse.pss_int(
            promotion_design_info.get('CloseButtonSpriteId'))
        self.__button_sprite_id: int = _parse.pss_int(
            promotion_design_info.get('ButtonSpriteId'))
        self.__from_date: datetime = _parse.pss_datetime(
            promotion_design_info.get('FromDate'))
        self.__to_date: datetime = _parse.pss_datetime(
            promotion_design_info.get('ToDate'))
        self.__bonus_frame_sprite_id: int = _parse.pss_int(
            promotion_design_info.get('BonusFrameSpriteId'))
        self.__purchase_sprite_id: int = _parse.pss_int(
            promotion_design_info.get('PurchaseSpriteId'))

    @property
    def promotion_design_id(self) -> int:
        return self.__promotion_design_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def promotion_type(self) -> str:
        return self.__promotion_type

    @property
    def purchase_mask(self) -> int:
        return self.__purchase_mask

    @property
    def title(self) -> str:
        return self.__title

    @property
    def sub_title(self) -> str:
        return self.__sub_title

    @property
    def description(self) -> str:
        return self.__description

    @property
    def reward_string(self) -> str:
        return self.__reward_string

    @property
    def starbux_bonus_percentage(self) -> int:
        return self.__starbux_bonus_percentage

    @property
    def resource_conversion_discount_percentage(self) -> int:
        return self.__resource_conversion_discount_percentage

    @property
    def reward_store_discount_percentage(self) -> int:
        return self.__reward_store_discount_percentage

    @property
    def speed_up_discount_percentage(self) -> int:
        return self.__speed_up_discount_percentage

    @property
    def extra_crew_draws(self) -> int:
        return self.__extra_crew_draws

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def order_index(self) -> int:
        return self.__order_index

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def xp_bonus_percentage(self) -> int:
        return self.__xp_bonus_percentage

    @property
    def metadata(self) -> str:
        return self.__metadata

    @property
    def pack_id(self) -> str:
        return self.__pack_id

    @property
    def available_every_x_days(self) -> int:
        return self.__available_every_x_days

    @property
    def available_for_days(self) -> int:
        return self.__available_for_days

    @property
    def remaining_quantity(self) -> int:
        return self.__remaining_quantity

    @property
    def cost_string(self) -> str:
        return self.__cost_string

    @property
    def background_sprite_id(self) -> int:
        return self.__background_sprite_id

    @property
    def sprite_id(self) -> int:
        return self.__sprite_id

    @property
    def icon_sprite_id(self) -> int:
        return self.__icon_sprite_id

    @property
    def required_promotion_design_id(self) -> int:
        return self.__required_promotion_design_id

    @property
    def title_sprite_id(self) -> int:
        return self.__title_sprite_id

    @property
    def close_button_sprite_id(self) -> int:
        return self.__close_button_sprite_id

    @property
    def button_sprite_id(self) -> int:
        return self.__button_sprite_id

    @property
    def from_date(self) -> datetime:
        return self.__from_date

    @property
    def to_date(self) -> datetime:
        return self.__to_date

    @property
    def bonus_frame_sprite_id(self) -> int:
        return self.__bonus_frame_sprite_id

    @property
    def purchase_sprite_id(self) -> int:
        return self.__purchase_sprite_id
