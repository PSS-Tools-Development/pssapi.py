from typing import List as _List

from .raw import CharacterServiceRaw as _CharacterServiceRaw
from .service_base import ServiceBase as _ServiceBase
from ..entities import CharacterDesign as _CharacterDesign
from ..entities import CharacterDesignAction as _CharacterDesignAction
from ..entities import DrawDesign as _DrawDesign


class CharacterService(_ServiceBase, _CharacterServiceRaw):
    async def list_all_character_design_actions(self, design_version: int = None, **params) -> _List[_CharacterDesignAction]:
        return await self._list_all_character_design_actions(self.production_server, design_version, **params)

    async def list_all_character_designs_2(self, design_version: int = None, **params) -> _List[_CharacterDesign]:
        return await self._list_all_character_designs_2(self.production_server, self.language_key, design_version, **params)

    async def list_all_draw_designs(self, design_version: int = None, **params) -> _List[_DrawDesign]:
        return await self._list_all_draw_designs(self.production_server, self.language_key, design_version, **params)

    def __repr__(self) -> str:
        return f'<CharacterService: {self.name}>'

    def __str__(self) -> str:
        return f'<CharacterService: {self.name}>'
