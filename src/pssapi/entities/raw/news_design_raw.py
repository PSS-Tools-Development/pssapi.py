"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class NewsDesignRaw(EntityBaseRaw, tag="NewsDesign"):
    XML_NODE_NAME: str = "NewsDesign"

    description: Optional[str] = attr(name="Description", default=None)
    expiry_date: Optional[datetime] = attr(name="ExpiryDate", default=None)
    from_date: Optional[datetime] = attr(name="FromDate", default=None)
    link: Optional[str] = attr(name="Link", default=None)
    news_design_id: Optional[int] = attr(name="NewsDesignId", default=None)
    sprite_id: Optional[int] = attr(name="SpriteId", default=None)
    title: Optional[str] = attr(name="Title", default=None)
    update_date: Optional[datetime] = attr(name="UpdateDate", default=None)
    user_id: Optional[int] = attr(name="UserId", default=None)

    def _key(self):
        return (
            self.description,
            self.expiry_date,
            self.from_date,
            self.link,
            self.news_design_id,
            self.sprite_id,
            self.title,
            self.update_date,
            self.user_id,
        )


__all__ = [
    "NewsDesignRaw",
]
