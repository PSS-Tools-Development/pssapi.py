from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import UserMarkerRaw as _UserMarkerRaw


class UserMarker(_UserMarkerRaw, _EntityWithIdBase):
    def __init__(self, user_marker_info: _EntityInfo) -> None:
        super().__init__(user_marker_info)
        # self._purchase_flags_enum: _enums. = _parse.pss_int_flag(self._purchase_flags, _enums.)   # enum doesn't exist up to PSS v0.994.1

    @property
    def id(self) -> int:
        return self.user_marker_id

    # @property   # enum doesn't exist up to PSS v0.994.1
    # def purchase_flags_enum(self) -> "_enums.":
    #    return self._purchase_flags_enum
