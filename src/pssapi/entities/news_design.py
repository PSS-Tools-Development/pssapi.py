from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import NewsDesignRaw as _NewsDesignRaw


class NewsDesign(_NewsDesignRaw, _EntityWithIdBase):
    def __init__(self, news_design_info: _EntityInfo) -> None:
        super().__init__(news_design_info)

    @property
    def id(self) -> int:
        return self.news_design_id
