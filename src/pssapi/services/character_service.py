from typing import List

from pssapi.services import service_base

from ..entities import CharacterDesign, CharacterDesignAction, DrawDesign, Prestige
from .raw import CharacterServiceRaw


class CharacterService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("CharacterDesignActionVersion")
    async def list_all_character_design_actions(self, client_date_time: str, design_version: int = None) -> List[CharacterDesignAction]:
        production_server = await self.get_production_server()
        result = await CharacterServiceRaw.list_all_character_design_actions(production_server, client_date_time, design_version)
        return result

    @service_base.cache_endpoint("CharacterDesignVersion")
    async def list_all_character_designs(self, client_date_time: str, design_version: int = None) -> List[CharacterDesign]:
        production_server = await self.get_production_server()
        result = await CharacterServiceRaw.list_all_character_designs_2(production_server, client_date_time, design_version, self.language_key)
        return result

    @service_base.cache_endpoint("DrawDesignVersion")
    async def list_all_draw_designs(self, client_date_time: str, design_version: int = None) -> List[DrawDesign]:
        production_server = await self.get_production_server()
        result = await CharacterServiceRaw.list_all_draw_designs(production_server, client_date_time, design_version, self.language_key)
        return result

    async def prestige_character_from(self, character_design_id: int) -> List[Prestige]:
        production_server = await self.get_production_server()
        result = await CharacterServiceRaw.prestige_character_from(production_server, character_design_id)
        return result

    async def prestige_character_to(self, character_design_id: int) -> List[Prestige]:
        production_server = await self.get_production_server()
        result = await CharacterServiceRaw.prestige_character_to(production_server, character_design_id)
        return result
