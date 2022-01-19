from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CharacterDesignRaw as _CharacterDesignRaw


class CharacterDesign(_CharacterDesignRaw, _EntityWithIdBase):
    def __init__(self, character_design_info: _EntityInfo) -> None:
        super().__init__(character_design_info)

    @property
    def id(self) -> int:
        return self.character_design_id
