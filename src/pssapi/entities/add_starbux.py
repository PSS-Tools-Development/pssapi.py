from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityBase as _EntityBase
from .raw import AddStarbuxRaw as _AddStarbuxRaw


class AddStarbux(_AddStarbuxRaw, _EntityBase):
    def __init__(self, add_starbux_info: _EntityInfo) -> None:
        super().__init__(add_starbux_info)
