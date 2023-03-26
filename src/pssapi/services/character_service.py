from typing import List as _List

import pssapi.services.service_base as _service_base

from ..entities import CharacterDesign as _CharacterDesign
from ..entities import CharacterDesignAction as _CharacterDesignAction
from ..entities import DrawDesign as _DrawDesign
from ..entities import Prestige as _Prestige
from .raw import CharacterServiceRaw as _CharacterServiceRaw


class CharacterService(_service_base.CacheableServiceBase):
    @_service_base.cache_endpoint("CharacterDesignActionVersion")
    async def list_all_character_design_actions(self, design_version: int = None) -> _List[_CharacterDesignAction]:
        production_server = await self.get_production_server()
        result = await _CharacterServiceRaw.list_all_character_design_actions(production_server, design_version)
        return result

    @_service_base.cache_endpoint("CharacterDesignVersion")
    async def list_all_character_designs(self, design_version: int = None) -> _List[_CharacterDesign]:
        production_server = await self.get_production_server()
        result = await _CharacterServiceRaw.list_all_character_designs_2(production_server, design_version, self.language_key)
        return result

    @_service_base.cache_endpoint("DrawDesignVersion")
    async def list_all_draw_designs(self, design_version: int = None) -> _List[_DrawDesign]:
        production_server = await self.get_production_server()
        result = await _CharacterServiceRaw.list_all_draw_designs(production_server, design_version, self.language_key)
        return result

    async def prestige_character_from(self, character_design_id: int) -> _List[_Prestige]:
        production_server = await self.get_production_server()
        result = await _CharacterServiceRaw.prestige_character_from(production_server, character_design_id)
        return result

    async def prestige_character_to(self, character_design_id: int) -> _List[_Prestige]:
        production_server = await self.get_production_server()
        result = await _CharacterServiceRaw.prestige_character_to(production_server, character_design_id)
        return result
