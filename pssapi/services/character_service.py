from typing import List as _List

from .raw import CharacterServiceRaw as _CharacterServiceRaw
import pssapi.services.service_base as _service_base
from ..entities import CharacterDesign as _CharacterDesign
from ..entities import CharacterDesignAction as _CharacterDesignAction
from ..entities import DrawDesign as _DrawDesign


class CharacterService(_service_base.ServiceBase):
    async def list_all_character_design_actions(self, design_version: int = None) -> _List[_CharacterDesignAction]:
        production_server = await self.get_production_server()
        result = await _CharacterServiceRaw.list_all_character_design_actions(production_server, design_version)
        return result

    async def list_all_character_designs(self, design_version: int = None) -> _List[_CharacterDesign]:
        production_server = await self.get_production_server()
        result = await _CharacterServiceRaw.list_all_character_designs_2(production_server, design_version, self.language_key)
        return result

    async def list_all_draw_designs(self, design_version: int = None) -> _List[_DrawDesign]:
        production_server = await self.get_production_server()
        result = await _CharacterServiceRaw.list_all_draw_designs(production_server, design_version, self.language_key)
        return result
