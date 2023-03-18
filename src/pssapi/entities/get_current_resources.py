from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityBase as _EntityBase
from .raw import GetCurrentResourcesRaw as _GetCurrentResourcesRaw


class GetCurrentResources(_GetCurrentResourcesRaw, _EntityBase):
    def __init__(self, get_current_resources_info: _EntityInfo) -> None:
        super().__init__(get_current_resources_info)
