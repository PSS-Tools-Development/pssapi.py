from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import UserSkinRaw as _UserSkinRaw


class UserSkin(_UserSkinRaw, _EntityWithIdBase):
    def __init__(self, user_skin_info: _EntityInfo) -> None:
        super().__init__(user_skin_info)

    @property
    def id(self) -> int:
        return self.user_skin_id
