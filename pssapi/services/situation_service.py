from datetime import datetime as _datetime
from typing import List as _List

from .raw import SituationServiceRaw as _SituationServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import SituationDesign as _SituationDesign
from ...entities import Situation as _Situation


class SituationService(_ServiceBase):
    async def list_situation_designs(self, language_key: str, design_version: int) -> _List[_SituationDesign]:
        raise NotImplemented()
        result = await _SituationServiceRaw.list_situation_designs(self.production_server, language_key: str, design_version: int)
        return result


    async def list_situations(self, access_token: str, client_date_time: _datetime) -> _List[_Situation]:
        raise NotImplemented()
        result = await _SituationServiceRaw.list_situations(self.production_server, access_token: str, client_date_time: _datetime)
        return result


