from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import UserFleetCollectionRaw as _UserFleetCollectionRaw


class UserFleetCollection(_UserFleetCollectionRaw, _EntityWithIdBase):
    def __init__(self, user_fleet_collection_info: _EntityInfo) -> None:
        super().__init__(user_fleet_collection_info)

    @property
    def id(self) -> int:
        return self.user_fleet_collection_id
