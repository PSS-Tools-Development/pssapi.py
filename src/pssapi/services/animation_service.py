from typing import List

from pssapi.services import service_base

from ..entities import Animation
from .raw import AnimationServiceRaw


class AnimationService(service_base.CacheableServiceBase):
    @service_base.cache_endpoint("AnimationVersion")
    async def list_animations(self, client_date_time: str, design_version: int = None) -> List[Animation]:
        production_server = await self.get_production_server()
        result = await AnimationServiceRaw.list_animations(production_server, client_date_time, design_version)
        return result
