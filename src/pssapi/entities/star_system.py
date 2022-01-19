from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import StarSystemRaw as _StarSystemRaw


class StarSystem(_StarSystemRaw, _EntityWithIdBase):
    def __init__(self, star_system_info: _EntityInfo) -> None:
        super().__init__(star_system_info)

    @property
    def id(self) -> int:
        return self.star_system_id
