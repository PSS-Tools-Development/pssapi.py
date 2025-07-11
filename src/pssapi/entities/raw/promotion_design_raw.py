"""
This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class PromotionDesignRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "PromotionDesign"

    def __init__(self, promotion_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._available_every_x_days: int = _parse.pss_int(promotion_design_info.pop("AvailableEveryXDays", None))
        self._available_for_days: int = _parse.pss_int(promotion_design_info.pop("AvailableForDays", None))
        self._background_sprite_id: int = _parse.pss_int(promotion_design_info.pop("BackgroundSpriteId", None))
        self._bonus_frame_sprite_id: int = _parse.pss_int(promotion_design_info.pop("BonusFrameSpriteId", None))
        self._button_sprite_id: int = _parse.pss_int(promotion_design_info.pop("ButtonSpriteId", None))
        self._close_button_sprite_id: int = _parse.pss_int(promotion_design_info.pop("CloseButtonSpriteId", None))
        self._cost_string: str = _parse.pss_str(promotion_design_info.pop("CostString", None))
        self._description: str = _parse.pss_str(promotion_design_info.pop("Description", None))
        self._extra_crew_draws: int = _parse.pss_int(promotion_design_info.pop("ExtraCrewDraws", None))
        self._flags: int = _parse.pss_int(promotion_design_info.pop("Flags", None))
        self._from_date: _datetime = _parse.pss_datetime(promotion_design_info.pop("FromDate", None))
        self._icon_sprite_id: int = _parse.pss_int(promotion_design_info.pop("IconSpriteId", None))
        self._metadata: str = _parse.pss_str(promotion_design_info.pop("Metadata", None))
        self._name: str = _parse.pss_str(promotion_design_info.pop("Name", None))
        self._order_index: int = _parse.pss_int(promotion_design_info.pop("OrderIndex", None))
        self._pack_id: str = _parse.pss_str(promotion_design_info.pop("PackId", None))
        self._product_key: str = _parse.pss_str(promotion_design_info.pop("ProductKey", None))
        self._promotion_design_id: int = _parse.pss_int(promotion_design_info.pop("PromotionDesignId", None))
        self._promotion_type: str = _parse.pss_str(promotion_design_info.pop("PromotionType", None))
        self._purchase_mask: int = _parse.pss_int(promotion_design_info.pop("PurchaseMask", None))
        self._purchase_sprite_id: int = _parse.pss_int(promotion_design_info.pop("PurchaseSpriteId", None))
        self._remaining_quantity: int = _parse.pss_int(promotion_design_info.pop("RemainingQuantity", None))
        self._required_promotion_design_id: int = _parse.pss_int(promotion_design_info.pop("RequiredPromotionDesignId", None))
        self._requirement_string: str = _parse.pss_str(promotion_design_info.pop("RequirementString", None))
        self._resource_conversion_discount_percentage: int = _parse.pss_int(promotion_design_info.pop("ResourceConversionDiscountPercentage", None))
        self._reward_store_discount_percentage: int = _parse.pss_int(promotion_design_info.pop("RewardStoreDiscountPercentage", None))
        self._reward_string: str = _parse.pss_str(promotion_design_info.pop("RewardString", None))
        self._speed_up_discount_percentage: int = _parse.pss_int(promotion_design_info.pop("SpeedUpDiscountPercentage", None))
        self._sprite_id: int = _parse.pss_int(promotion_design_info.pop("SpriteId", None))
        self._starbux_bonus_percentage: int = _parse.pss_int(promotion_design_info.pop("StarbuxBonusPercentage", None))
        self._sub_title: str = _parse.pss_str(promotion_design_info.pop("SubTitle", None))
        self._title: str = _parse.pss_str(promotion_design_info.pop("Title", None))
        self._title_sprite_id: int = _parse.pss_int(promotion_design_info.pop("TitleSpriteId", None))
        self._to_date: _datetime = _parse.pss_datetime(promotion_design_info.pop("ToDate", None))
        self._xp_bonus_percentage: int = _parse.pss_int(promotion_design_info.pop("XPBonusPercentage", None))
        super().__init__(promotion_design_info)

    @property
    def available_every_x_days(self) -> int:
        return self._available_every_x_days

    @property
    def available_for_days(self) -> int:
        return self._available_for_days

    @property
    def background_sprite_id(self) -> int:
        return self._background_sprite_id

    @property
    def bonus_frame_sprite_id(self) -> int:
        return self._bonus_frame_sprite_id

    @property
    def button_sprite_id(self) -> int:
        return self._button_sprite_id

    @property
    def close_button_sprite_id(self) -> int:
        return self._close_button_sprite_id

    @property
    def cost_string(self) -> str:
        return self._cost_string

    @property
    def description(self) -> str:
        return self._description

    @property
    def extra_crew_draws(self) -> int:
        return self._extra_crew_draws

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def from_date(self) -> _datetime:
        return self._from_date

    @property
    def icon_sprite_id(self) -> int:
        return self._icon_sprite_id

    @property
    def metadata(self) -> str:
        return self._metadata

    @property
    def name(self) -> str:
        return self._name

    @property
    def order_index(self) -> int:
        return self._order_index

    @property
    def pack_id(self) -> str:
        return self._pack_id

    @property
    def product_key(self) -> str:
        return self._product_key

    @property
    def promotion_design_id(self) -> int:
        return self._promotion_design_id

    @property
    def promotion_type(self) -> str:
        return self._promotion_type

    @property
    def purchase_mask(self) -> int:
        return self._purchase_mask

    @property
    def purchase_sprite_id(self) -> int:
        return self._purchase_sprite_id

    @property
    def remaining_quantity(self) -> int:
        return self._remaining_quantity

    @property
    def required_promotion_design_id(self) -> int:
        return self._required_promotion_design_id

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def resource_conversion_discount_percentage(self) -> int:
        return self._resource_conversion_discount_percentage

    @property
    def reward_store_discount_percentage(self) -> int:
        return self._reward_store_discount_percentage

    @property
    def reward_string(self) -> str:
        return self._reward_string

    @property
    def speed_up_discount_percentage(self) -> int:
        return self._speed_up_discount_percentage

    @property
    def sprite_id(self) -> int:
        return self._sprite_id

    @property
    def starbux_bonus_percentage(self) -> int:
        return self._starbux_bonus_percentage

    @property
    def sub_title(self) -> str:
        return self._sub_title

    @property
    def title(self) -> str:
        return self._title

    @property
    def title_sprite_id(self) -> int:
        return self._title_sprite_id

    @property
    def to_date(self) -> _datetime:
        return self._to_date

    @property
    def xp_bonus_percentage(self) -> int:
        return self._xp_bonus_percentage

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

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AvailableEveryXDays": self.available_every_x_days,
                "AvailableForDays": self.available_for_days,
                "BackgroundSpriteId": self.background_sprite_id,
                "BonusFrameSpriteId": self.bonus_frame_sprite_id,
                "ButtonSpriteId": self.button_sprite_id,
                "CloseButtonSpriteId": self.close_button_sprite_id,
                "CostString": self.cost_string,
                "Description": self.description,
                "ExtraCrewDraws": self.extra_crew_draws,
                "Flags": self.flags,
                "FromDate": self.from_date,
                "IconSpriteId": self.icon_sprite_id,
                "Metadata": self.metadata,
                "Name": self.name,
                "OrderIndex": self.order_index,
                "PackId": self.pack_id,
                "ProductKey": self.product_key,
                "PromotionDesignId": self.promotion_design_id,
                "PromotionType": self.promotion_type,
                "PurchaseMask": self.purchase_mask,
                "PurchaseSpriteId": self.purchase_sprite_id,
                "RemainingQuantity": self.remaining_quantity,
                "RequiredPromotionDesignId": self.required_promotion_design_id,
                "RequirementString": self.requirement_string,
                "ResourceConversionDiscountPercentage": self.resource_conversion_discount_percentage,
                "RewardStoreDiscountPercentage": self.reward_store_discount_percentage,
                "RewardString": self.reward_string,
                "SpeedUpDiscountPercentage": self.speed_up_discount_percentage,
                "SpriteId": self.sprite_id,
                "StarbuxBonusPercentage": self.starbux_bonus_percentage,
                "SubTitle": self.sub_title,
                "Title": self.title,
                "TitleSpriteId": self.title_sprite_id,
                "ToDate": self.to_date,
                "XPBonusPercentage": self.xp_bonus_percentage,
            }
            self._dict.update(super().__dict__())

        return self._dict
