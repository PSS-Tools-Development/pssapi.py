"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class DrawDesignRaw(EntityBaseRaw, tag="DrawDesign"):
    XML_NODE_NAME: str = "DrawDesign"

    background_sprite_id: Optional[int] = attr(name="BackgroundSpriteId", default=None)
    bonus_increase: Optional[int] = attr(name="BonusIncrease", default=None)
    collection_design_id: Optional[int] = attr(name="CollectionDesignId", default=None)
    cost: Optional[str] = attr(name="Cost", default=None)
    cost_percentage_increase: Optional[int] = attr(name="CostPercentageIncrease", default=None)
    draw_description: Optional[str] = attr(name="DrawDescription", default=None)
    draw_design_id: Optional[int] = attr(name="DrawDesignId", default=None)
    draw_name: Optional[str] = attr(name="DrawName", default=None)
    draw_sprite_id: Optional[int] = attr(name="DrawSpriteId", default=None)
    draw_type: Optional[str] = attr(name="DrawType", default=None)
    max_cost_percentage_increase: Optional[int] = attr(name="MaxCostPercentageIncrease", default=None)
    max_crew_rarity: Optional[int] = attr(name="MaxCrewRarity", default=None)
    max_crews_drawn: Optional[int] = attr(name="MaxCrewsDrawn", default=None)
    max_items: Optional[int] = attr(name="MaxItems", default=None)
    min_crew_rarity: Optional[int] = attr(name="MinCrewRarity", default=None)
    min_crews_drawn: Optional[int] = attr(name="MinCrewsDrawn", default=None)
    min_items: Optional[int] = attr(name="MinItems", default=None)
    order_index: Optional[int] = attr(name="OrderIndex", default=None)
    required_research_design_id: Optional[int] = attr(name="RequiredResearchDesignId", default=None)

    def _key(self):
        return (
            self.background_sprite_id,
            self.bonus_increase,
            self.collection_design_id,
            self.cost,
            self.cost_percentage_increase,
            self.draw_description,
            self.draw_design_id,
            self.draw_name,
            self.draw_sprite_id,
            self.draw_type,
            self.max_cost_percentage_increase,
            self.max_crew_rarity,
            self.max_crews_drawn,
            self.max_items,
            self.min_crew_rarity,
            self.min_crews_drawn,
            self.min_items,
            self.order_index,
            self.required_research_design_id,
        )


__all__ = [
    "DrawDesignRaw",
]
