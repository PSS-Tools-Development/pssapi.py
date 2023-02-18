
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import NewsDesignRaw as _NewsDesignRaw
from ..types import EntityInfo as _EntityInfo


class NewsDesign(_EntityWithIdBase, _NewsDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<NewsDesign {self.id}>'

    def __str__(self) -> str:
        return f'<NewsDesign {self.id}>'

    @property
    def id(self) -> int:
        return self.news_design_id
