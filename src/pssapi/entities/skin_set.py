from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .metadata import SkinSetMetadata as _SkinSetMetadata
from .raw import SkinSetRaw as _SkinSetRaw


class SkinSet(_SkinSetRaw, _EntityWithIdBase):
    def __init__(self, skin_set_info: _EntityInfo) -> None:
        super().__init__(skin_set_info)
        self._skin_set_metadata: _SkinSetMetadata = _SkinSetMetadata(self.metadata)

    @property
    def id(self) -> int:
        return self.skin_set_id

    @property
    def skin_set_metadata(self) -> _SkinSetMetadata:
        return self._skin_set_metadata
