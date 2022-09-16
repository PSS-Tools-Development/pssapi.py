from datetime import datetime as _datetime
from typing import List as _List

from .raw import CharacterServiceRaw as _CharacterServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import Character as _Character
from ...entities import DrawDesign as _DrawDesign
from ...entities import CharacterDesign as _CharacterDesign
from ...entities import CharacterDesignAction as _CharacterDesignAction
from ...entities import CharacterAction as _CharacterAction


class CharacterService(_ServiceBase):
    async def list_all_character_design_actions(self, design_version: int) -> _List[_CharacterDesignAction]:
        raise NotImplemented()
        result = await _CharacterServiceRaw.list_all_character_design_actions(self.production_server, design_version: int)
        return result


    async def list_all_character_designs_2(self, language_key: str, design_version: int) -> _List[_CharacterDesign]:
        raise NotImplemented()
        result = await _CharacterServiceRaw.list_all_character_designs_2(self.production_server, language_key: str, design_version: int)
        return result


    async def list_all_characters_of_user(self, access_token: str, client_date_time: _datetime) -> _List[_Character]:
        raise NotImplemented()
        result = await _CharacterServiceRaw.list_all_characters_of_user(self.production_server, access_token: str, client_date_time: _datetime)
        return result


    async def list_all_draw_designs(self, language_key: str, design_version: int) -> _List[_DrawDesign]:
        raise NotImplemented()
        result = await _CharacterServiceRaw.list_all_draw_designs(self.production_server, language_key: str, design_version: int)
        return result


    async def list_character_actions_by_ship_id(self, ship_id: int, access_token: str) -> _List[_CharacterAction]:
        raise NotImplemented()
        result = await _CharacterServiceRaw.list_character_actions_by_ship_id(self.production_server, ship_id: int, access_token: str)
        return result


