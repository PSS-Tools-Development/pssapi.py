
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CraftDesignRaw as _CraftDesignRaw
from ..types import EntityInfo as _EntityInfo


class CraftDesign(_EntityWithIdBase, _CraftDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<CraftDesign {self.id}>'

    def __str__(self) -> str:
        return f'<CraftDesign {self.id}>'

    @property
    def id(self) -> int:
        return self.craft_design_id
