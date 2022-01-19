from typing import List as _List

from .service_base import PssServiceBase as _ServiceBase
from .. import core as _core
from ..entities import ItemDesign as _ItemDesign
from ..enums import LanguageKey as _LanguageKey
from ..utils import convert as _convert


#######################################################################
##   This file will be generated automatically from API inspection   ##
#######################################################################


class ItemService(_ServiceBase):
    LIST_ITEM_DESIGNS_2_BASE_PATH: str = 'ItemService/ListItemDesigns2'


    async def list_item_designs_2(self, language_key: _LanguageKey) -> _List[_ItemDesign]:
        params = {
            'languageKey': language_key,
        }
        raw_xml = await _core.get_data_from_path(self.production_server, ItemService.LIST_ITEM_DESIGNS_BASE_PATH, **params)
        raw_dict = _convert.xmltree_to_dict3(raw_xml)
        result = [_ItemDesign(d) for d in raw_dict.values()]
        return result