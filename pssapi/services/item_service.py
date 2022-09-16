from typing import List as _List

from .service_base import PssServiceBase as _ServiceBase
from ..entities import ItemDesign as _ItemDesign
from ..enums import LanguageKey as _LanguageKey
from .raw import ItemServiceRaw as _ItemServiceRaw


########################################################################################
##   This file will be generated automatically from API inspection on the first run   ##
########################################################################################


class ItemService(_ServiceBase):
    async def list_item_designs_2(self) -> _List[_ItemDesign]:
        result = await _ItemServiceRaw.list_item_designs_2(self.production_server, self.language_key)
        return result