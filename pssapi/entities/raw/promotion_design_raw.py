"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class PromotionDesignRaw:
    XML_NODE_NAME: str = 'PromotionDesign'

    def __init__(self, promotion_design_info: _EntityInfo) -> None:
        self.available_every_x_days: int = _parse.pss_int(promotion_design_info.get('AvailableEveryXDays'))
        self.available_for_days: int = _parse.pss_int(promotion_design_info.get('AvailableForDays'))
        self.background_sprite_id: int = _parse.pss_int(promotion_design_info.get('BackgroundSpriteId'))
        self.bonus_frame_sprite_id: int = _parse.pss_int(promotion_design_info.get('BonusFrameSpriteId'))
        self.button_sprite_id: int = _parse.pss_int(promotion_design_info.get('ButtonSpriteId'))
        self.close_button_sprite_id: int = _parse.pss_int(promotion_design_info.get('CloseButtonSpriteId'))
        self.cost_string: str = _parse.pss_str(promotion_design_info.get('CostString'))
        self.description: str = _parse.pss_str(promotion_design_info.get('Description'))
        self.extra_crew_draws: int = _parse.pss_int(promotion_design_info.get('ExtraCrewDraws'))
        self.flags: int = _parse.pss_int(promotion_design_info.get('Flags'))
        self.from_date: _datetime = _parse.pss_datetime(promotion_design_info.get('FromDate'))
        self.icon_sprite_id: int = _parse.pss_int(promotion_design_info.get('IconSpriteId'))
        self.metadata: str = _parse.pss_str(promotion_design_info.get('Metadata'))
        self.name: str = _parse.pss_str(promotion_design_info.get('Name'))
        self.order_index: int = _parse.pss_int(promotion_design_info.get('OrderIndex'))
        self.pack_id: str = _parse.pss_str(promotion_design_info.get('PackId'))
        self.promotion_design_id: int = _parse.pss_int(promotion_design_info.get('PromotionDesignId'))
        self.promotion_type: str = _parse.pss_str(promotion_design_info.get('PromotionType'))
        self.purchase_mask: int = _parse.pss_int(promotion_design_info.get('PurchaseMask'))
        self.purchase_sprite_id: int = _parse.pss_int(promotion_design_info.get('PurchaseSpriteId'))
        self.remaining_quantity: int = _parse.pss_int(promotion_design_info.get('RemainingQuantity'))
        self.required_promotion_design_id: int = _parse.pss_int(promotion_design_info.get('RequiredPromotionDesignId'))
        self.requirement_string: str = _parse.pss_str(promotion_design_info.get('RequirementString'))
        self.resource_conversion_discount_percentage: int = _parse.pss_int(promotion_design_info.get('ResourceConversionDiscountPercentage'))
        self.reward_store_discount_percentage: int = _parse.pss_int(promotion_design_info.get('RewardStoreDiscountPercentage'))
        self.reward_string: str = _parse.pss_str(promotion_design_info.get('RewardString'))
        self.speed_up_discount_percentage: int = _parse.pss_int(promotion_design_info.get('SpeedUpDiscountPercentage'))
        self.sprite_id: int = _parse.pss_int(promotion_design_info.get('SpriteId'))
        self.starbux_bonus_percentage: int = _parse.pss_int(promotion_design_info.get('StarbuxBonusPercentage'))
        self.sub_title: str = _parse.pss_str(promotion_design_info.get('SubTitle'))
        self.title: str = _parse.pss_str(promotion_design_info.get('Title'))
        self.title_sprite_id: int = _parse.pss_int(promotion_design_info.get('TitleSpriteId'))
        self.to_date: _datetime = _parse.pss_datetime(promotion_design_info.get('ToDate'))
        self.xp_bonus_percentage: int = _parse.pss_int(promotion_design_info.get('XPBonusPercentage'))
