"""
This file has been generated automatically
"""

from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class ResearchDesignRaw(EntityBaseRaw, tag="ResearchDesign"):
    XML_NODE_NAME: str = "ResearchDesign"

    argument: Optional[int] = attr(name="Argument", default=None)
    availability_mask: Optional[int] = attr(name="AvailabilityMask", default=None)
    gas_cost: Optional[int] = attr(name="GasCost", default=None)
    image_sprite_id: Optional[int] = attr(name="ImageSpriteId", default=None)
    logo_sprite_id: Optional[int] = attr(name="LogoSpriteId", default=None)
    required_item_design_id: Optional[int] = attr(name="RequiredItemDesignId", default=None)
    required_lab_level: Optional[int] = attr(name="RequiredLabLevel", default=None)
    required_research_design_id: Optional[int] = attr(name="RequiredResearchDesignId", default=None)
    research_description: Optional[str] = attr(name="ResearchDescription", default=None)
    research_design_id: Optional[int] = attr(name="ResearchDesignId", default=None)
    research_design_type: Optional[str] = attr(name="ResearchDesignType", default=None)
    research_name: Optional[str] = attr(name="ResearchName", default=None)
    research_time: Optional[int] = attr(name="ResearchTime", default=None)
    root_research_design_id: Optional[int] = attr(name="RootResearchDesignId", default=None)
    starbux_cost: Optional[int] = attr(name="StarbuxCost", default=None)
    visibility_flags: Optional[str] = attr(name="VisibilityFlags", default=None)

    def _key(self):
        return (
            self.argument,
            self.availability_mask,
            self.gas_cost,
            self.image_sprite_id,
            self.logo_sprite_id,
            self.required_item_design_id,
            self.required_lab_level,
            self.required_research_design_id,
            self.research_description,
            self.research_design_id,
            self.research_design_type,
            self.research_name,
            self.research_time,
            self.root_research_design_id,
            self.starbux_cost,
            self.visibility_flags,
        )


__all__ = [
    "ResearchDesignRaw",
]
