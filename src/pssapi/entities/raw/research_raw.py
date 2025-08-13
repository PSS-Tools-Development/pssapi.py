"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class ResearchRaw(EntityBaseRaw, tag="Research"):
    XML_NODE_NAME: str = "Research"

    research_design_id: Optional[int] = attr(name="ResearchDesignId", default=None)
    research_id: Optional[int] = attr(name="ResearchId", default=None)
    research_start_date: Optional[datetime] = attr(name="ResearchStartDate", default=None)
    research_state: Optional[str] = attr(name="ResearchState", default=None)
    ship_id: Optional[int] = attr(name="ShipId", default=None)

    def _key(self):
        return (
            self.research_design_id,
            self.research_id,
            self.research_start_date,
            self.research_state,
            self.ship_id,
        )


__all__ = [
    "ResearchRaw",
]
