from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import SettingRaw as _SettingRaw


class Setting(_SettingRaw, _EntityWithIdBase):
    def __init__(self, setting_info: _EntityInfo) -> None:
        super().__init__(setting_info)

    @property
    def id(self) -> int:
        return self.setting_id
