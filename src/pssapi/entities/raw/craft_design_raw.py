"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class CraftDesignRaw(EntityBaseRaw, tag="CraftDesign"):
    XML_NODE_NAME: str = "CraftDesign"

    attack_distance: Optional[int] = attr(name="AttackDistance", default=None)
    attack_range: Optional[int] = attr(name="AttackRange", default=None)
    craft_attack_type: Optional[str] = attr(name="CraftAttackType", default=None)
    craft_design_id: Optional[int] = attr(name="CraftDesignId", default=None)
    craft_name: Optional[str] = attr(name="CraftName", default=None)
    craft_pathing_type: Optional[str] = attr(name="CraftPathingType", default=None)
    craft_target_type: Optional[str] = attr(name="CraftTargetType", default=None)
    entity_count: Optional[int] = attr(name="EntityCount", default=None)
    flight_speed: Optional[int] = attr(name="FlightSpeed", default=None)
    hp: Optional[int] = attr(name="Hp", default=None)
    missile_design_id: Optional[int] = attr(name="MissileDesignId", default=None)
    reload: Optional[int] = attr(name="Reload", default=None)
    sprite_id: Optional[int] = attr(name="SpriteId", default=None)
    volley: Optional[int] = attr(name="Volley", default=None)
    volley_delay: Optional[int] = attr(name="VolleyDelay", default=None)

    def _key(self):
        return (
            self.attack_distance,
            self.attack_range,
            self.craft_attack_type,
            self.craft_design_id,
            self.craft_name,
            self.craft_pathing_type,
            self.craft_target_type,
            self.entity_count,
            self.flight_speed,
            self.hp,
            self.missile_design_id,
            self.reload,
            self.sprite_id,
            self.volley,
            self.volley_delay,
        )


__all__ = [
    "CraftDesignRaw",
]
