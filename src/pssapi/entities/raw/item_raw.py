"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class ItemRaw(EntityBaseRaw, tag="Item"):
    XML_NODE_NAME: str = "Item"

    action_frame: Optional[int] = attr(name="ActionFrame", default=None)
    battle_hp: Optional[int] = attr(name="BattleHp", default=None)
    bonus_enhancement_type: Optional[str] = attr(name="BonusEnhancementType", default=None)
    bonus_enhancement_value: Optional[str] = attr(name="BonusEnhancementValue", default=None)
    is_new: Optional[bool] = attr(name="IsNew", default=None)
    item_design_id: Optional[int] = attr(name="ItemDesignId", default=None)
    item_id: Optional[int] = attr(name="ItemId", default=None)
    quantity: Optional[int] = attr(name="Quantity", default=None)
    ship_id: Optional[int] = attr(name="ShipId", default=None)
    skin_key: Optional[int] = attr(name="SkinKey", default=None)

    def _key(self):
        return (
            self.action_frame,
            self.battle_hp,
            self.bonus_enhancement_type,
            self.bonus_enhancement_value,
            self.is_new,
            self.item_design_id,
            self.item_id,
            self.quantity,
            self.ship_id,
            self.skin_key,
        )


__all__ = [
    "ItemRaw",
]
