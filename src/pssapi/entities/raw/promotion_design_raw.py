"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class PromotionDesignRaw(EntityBaseRaw, tag="PromotionDesign"):
    XML_NODE_NAME: str = "PromotionDesign"

    available_every_x_days: Optional[int] = attr(name="AvailableEveryXDays", default=None)
    available_for_days: Optional[int] = attr(name="AvailableForDays", default=None)
    background_sprite_id: Optional[int] = attr(name="BackgroundSpriteId", default=None)
    bonus_frame_sprite_id: Optional[int] = attr(name="BonusFrameSpriteId", default=None)
    button_sprite_id: Optional[int] = attr(name="ButtonSpriteId", default=None)
    close_button_sprite_id: Optional[int] = attr(name="CloseButtonSpriteId", default=None)
    cost_string: Optional[str] = attr(name="CostString", default=None)
    description: Optional[str] = attr(name="Description", default=None)
    extra_crew_draws: Optional[int] = attr(name="ExtraCrewDraws", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    from_date: Optional[datetime] = attr(name="FromDate", default=None)
    icon_sprite_id: Optional[int] = attr(name="IconSpriteId", default=None)
    metadata: Optional[str] = attr(name="Metadata", default=None)
    name: Optional[str] = attr(name="Name", default=None)
    order_index: Optional[int] = attr(name="OrderIndex", default=None)
    pack_id: Optional[str] = attr(name="PackId", default=None)
    product_key: Optional[str] = attr(name="ProductKey", default=None)
    promotion_design_id: Optional[int] = attr(name="PromotionDesignId", default=None)
    promotion_type: Optional[str] = attr(name="PromotionType", default=None)
    purchase_mask: Optional[int] = attr(name="PurchaseMask", default=None)
    purchase_sprite_id: Optional[int] = attr(name="PurchaseSpriteId", default=None)
    remaining_quantity: Optional[int] = attr(name="RemainingQuantity", default=None)
    required_promotion_design_id: Optional[int] = attr(name="RequiredPromotionDesignId", default=None)
    requirement_string: Optional[str] = attr(name="RequirementString", default=None)
    resource_conversion_discount_percentage: Optional[int] = attr(name="ResourceConversionDiscountPercentage", default=None)
    reward_store_discount_percentage: Optional[int] = attr(name="RewardStoreDiscountPercentage", default=None)
    reward_string: Optional[str] = attr(name="RewardString", default=None)
    speed_up_discount_percentage: Optional[int] = attr(name="SpeedUpDiscountPercentage", default=None)
    sprite_id: Optional[int] = attr(name="SpriteId", default=None)
    starbux_bonus_percentage: Optional[int] = attr(name="StarbuxBonusPercentage", default=None)
    sub_title: Optional[str] = attr(name="SubTitle", default=None)
    title: Optional[str] = attr(name="Title", default=None)
    title_sprite_id: Optional[int] = attr(name="TitleSpriteId", default=None)
    to_date: Optional[datetime] = attr(name="ToDate", default=None)
    xp_bonus_percentage: Optional[int] = attr(name="XPBonusPercentage", default=None)

    def _key(self):
        return (
            self.available_every_x_days,
            self.available_for_days,
            self.background_sprite_id,
            self.bonus_frame_sprite_id,
            self.button_sprite_id,
            self.close_button_sprite_id,
            self.cost_string,
            self.description,
            self.extra_crew_draws,
            self.flags,
            self.from_date,
            self.icon_sprite_id,
            self.metadata,
            self.name,
            self.order_index,
            self.pack_id,
            self.product_key,
            self.promotion_design_id,
            self.promotion_type,
            self.purchase_mask,
            self.purchase_sprite_id,
            self.remaining_quantity,
            self.required_promotion_design_id,
            self.requirement_string,
            self.resource_conversion_discount_percentage,
            self.reward_store_discount_percentage,
            self.reward_string,
            self.speed_up_discount_percentage,
            self.sprite_id,
            self.starbux_bonus_percentage,
            self.sub_title,
            self.title,
            self.title_sprite_id,
            self.to_date,
            self.xp_bonus_percentage,
        )


__all__ = [
    "PromotionDesignRaw",
]
