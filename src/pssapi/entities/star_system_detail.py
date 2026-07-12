from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import StarSystemDetailRaw as _StarSystemDetailRaw


class StarSystemDetail(_StarSystemDetailRaw, _EntityWithIdBase):
    def __init__(self, star_system_detail_info: _EntityInfo) -> None:
        super().__init__(star_system_detail_info)

    @property
    def id(self) -> int:
        return self.star_system_detail_id
