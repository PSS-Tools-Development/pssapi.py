"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import DivisionDesign as _DivisionDesign


class DivisionServiceRaw:

    SERVICE_NAME = 'DivisionService'
    LIST_ALL_DIVISION_DESIGNS_2_BASE_PATH: str = 'DivisionService/ListAllDivisionDesigns2'

    @staticmethod
    async def _list_all_division_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_DivisionDesign]:
        params = {
            'languageKey': language_key,
            'designVersion': design_version,
            **params
        }

        result = await _core.get_entities_from_path(_DivisionDesign, 'DivisionDesigns', production_server, DivisionServiceRaw.LIST_ALL_DIVISION_DESIGNS_2_BASE_PATH, **params)
        return result
