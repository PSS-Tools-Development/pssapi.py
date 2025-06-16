import datetime as _datetime
from typing import List as _List

import pssapi.services.service_base as _service_base

from .. import utils as _utils
from ..entities import CharacterDesign as _CharacterDesign
from ..entities import CharacterDesignAction as _CharacterDesignAction
from ..entities import DrawDesign as _DrawDesign
from ..entities import Prestige as _Prestige
from .raw import CharacterServiceRaw as _CharacterServiceRaw


class CharacterService(_service_base.CacheableServiceBase):
    async def to_character(self, character_name: str, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_CharacterDesign]:
        characters = await self.list_all_character_designs(client_date_time, design_version)
        result = list(filter(lambda character: character_name.lower() in character.character_design_name.lower(), characters))

        return result

    @_service_base.cache_endpoint("CharacterDesignActionVersion")
    async def list_all_character_design_actions(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_CharacterDesignAction]:
        production_server = await self.get_production_server()
        result = await _CharacterServiceRaw.list_all_character_design_actions(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version)
        return result

    @_service_base.cache_endpoint("CharacterDesignVersion")
    async def list_all_character_designs(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_CharacterDesign]:
        production_server = await self.get_production_server()
        result = await _CharacterServiceRaw.list_all_character_designs_2(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version, self.language_key)
        return result

    @_service_base.cache_endpoint("DrawDesignVersion")
    async def list_all_draw_designs(self, client_date_time: _datetime.datetime = None, design_version: int = None) -> _List[_DrawDesign]:
        production_server = await self.get_production_server()
        result = await _CharacterServiceRaw.list_all_draw_designs(production_server, _utils.datetime.convert_to_pss_timestamp(client_date_time), design_version, self.language_key)
        return result

    async def prestige_character_from(self, character_design_id: int) -> _List[_Prestige]:
        production_server = await self.get_production_server()
        result = await _CharacterServiceRaw.prestige_character_from(production_server, character_design_id)
        return result

    async def prestige_character_to(self, character_design_id: int) -> _List[_Prestige]:
        production_server = await self.get_production_server()
        result = await _CharacterServiceRaw.prestige_character_to(production_server, character_design_id)
        return result
