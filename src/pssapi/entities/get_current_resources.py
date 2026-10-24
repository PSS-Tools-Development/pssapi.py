from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityBase as _EntityBase
from .raw.get_current_resources_raw import GetCurrentResourcesRaw as _GetCurrentResourcesRaw


class GetCurrentResources(_GetCurrentResourcesRaw, _EntityBase):
    """Deprecated: GetCurrentResources was added on accident and will be removed in a future version."""

    def __init__(self, get_current_resources_info: _EntityInfo) -> None:
        super().__init__(get_current_resources_info)
