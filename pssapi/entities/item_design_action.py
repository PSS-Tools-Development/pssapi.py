
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ItemDesignActionRaw as _ItemDesignActionRaw
from ..types import EntityInfo as _EntityInfo


class ItemDesignAction(_EntityWithIdBase, _ItemDesignActionRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<ItemDesignAction {self.id}>'

    def __str__(self) -> str:
        return f'<ItemDesignAction {self.id}>'

    @property
    def id(self) -> int:
        return self.item_design_action_id
