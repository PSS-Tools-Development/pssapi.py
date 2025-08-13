from .entity_base import EntityWithIdBase
from .raw import SettingRaw


class Setting(SettingRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.setting_id


__all__ = [
    "Setting",
]
