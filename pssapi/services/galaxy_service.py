from datetime import datetime as _datetime
from typing import List as _List

from .raw import GalaxyServiceRaw as _GalaxyServiceRaw
from .service_base import PssServiceBase as _ServiceBase
from ...entities import StarSystemMarker as _StarSystemMarker
from ...entities import StarSystemLink as _StarSystemLink
from ...entities import UserStarSystem as _UserStarSystem
from ...entities import StarSystem as _StarSystem


class GalaxyService(_ServiceBase):
    async def list_star_system_links(self, design_version: int) -> _List[_StarSystemLink]:
        raise NotImplemented()
        result = await _GalaxyServiceRaw.list_star_system_links(self.production_server, design_version: int)
        return result


    async def list_star_systems(self, language_key: str, design_version: int) -> _List[_StarSystem]:
        raise NotImplemented()
        result = await _GalaxyServiceRaw.list_star_systems(self.production_server, language_key: str, design_version: int)
        return result


    async def list_user_markers(self, access_token: str, client_date_time: _datetime) -> _List[_StarSystemMarker]:
        raise NotImplemented()
        result = await _GalaxyServiceRaw.list_user_markers(self.production_server, access_token: str, client_date_time: _datetime)
        return result


    async def list_user_star_systems(self, access_token: str, client_date_time: _datetime) -> _List[_UserStarSystem]:
        raise NotImplemented()
        result = await _GalaxyServiceRaw.list_user_star_systems(self.production_server, access_token: str, client_date_time: _datetime)
        return result


