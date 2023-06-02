from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import AllianceRaw as _AllianceRaw


class Alliance(_AllianceRaw, _EntityWithIdBase):
    def __init__(self, alliance_info: _EntityInfo) -> None:
        super().__init__(alliance_info)
        self._alliance_country_code_enum: _enums.LanguageKey = _parse.pss_str_enum(self.alliance_country_code, _enums.LanguageKey)

    @property
    def id(self) -> int:
        return self.alliance_id

    @property
    def alliance_country_code_enum(self) -> "_enums.LanguageKey":
        return self._alliance_country_code_enum
