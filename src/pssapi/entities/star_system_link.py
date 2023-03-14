from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import StarSystemLinkRaw as _StarSystemLinkRaw


class StarSystemLink(_StarSystemLinkRaw, _EntityWithIdBase):
    def __init__(self, star_system_link_info: _EntityInfo) -> None:
        super().__init__(star_system_link_info)

    @property
    def id(self) -> int:
        return self.star_system_link_id
