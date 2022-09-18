"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import ShipDesign as _ShipDesign


class ShipServiceRaw:

    SERVICE_NAME = 'ShipService'
    LIST_ALL_SHIP_DESIGNS_2_BASE_PATH: str = 'ShipService/ListAllShipDesigns2'

    @staticmethod
    async def _list_all_ship_designs_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_ShipDesign]:
        params = {
            'languageKey': language_key,
            'designVersion': design_version,
            **params
        }
        result = await _core.get_entities_from_path(_ShipDesign, 'ShipDesigns', production_server, ShipServiceRaw.LIST_ALL_SHIP_DESIGNS_2_BASE_PATH, **params)
        return result
