from .entity_base import EntityWithIdBase
from .raw import NewsDesignRaw


class NewsDesign(NewsDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.news_design_id


__all__ = [
    "NewsDesign",
]
