from typing import List as _List

from .raw import CharacterServiceRaw as _CharacterServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import CharacterDesign as _CharacterDesign
from ..entities import CharacterDesignAction as _CharacterDesignAction
from ..entities import DrawDesign as _DrawDesign


class CharacterService(_ServiceBase):
    async def list_all_character_design_actions(self, design_version: int = None) -> _List[_CharacterDesignAction]:
        result = await _CharacterServiceRaw.list_all_character_design_actions(self.production_server, design_version)
        return result

    async def list_all_character_designs(self, design_version: int = None) -> _List[_CharacterDesign]:
        result = await _CharacterServiceRaw.list_all_character_designs_2(self.production_server, design_version, self.language_key)
        return result

    async def list_all_draw_designs(self, design_version: int = None) -> _List[_DrawDesign]:
        result = await _CharacterServiceRaw.list_all_draw_designs(self.production_server, design_version, self.language_key)
        return result
