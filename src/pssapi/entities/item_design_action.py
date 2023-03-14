from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ItemDesignActionRaw as _ItemDesignActionRaw


class ItemDesignAction(_ItemDesignActionRaw, _EntityWithIdBase):
    def __init__(self, item_design_action_info: _EntityInfo) -> None:
        super().__init__(item_design_action_info)

    @property
    def id(self) -> int:
        return self.item_design_action_id
