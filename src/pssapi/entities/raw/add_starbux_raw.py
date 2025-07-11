"""
This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class AddStarbuxRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "AddStarbux"

    def __init__(self, add_starbux_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._error_message: str = _parse.pss_str(add_starbux_info.pop("errorMessage", None))
        super().__init__(add_starbux_info)

    @property
    def error_message(self) -> str:
        return self._error_message

    def _key(self):
        return (self.error_message,)

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "errorMessage": self.error_message,
            }
            self._dict.update(super().__dict__())

        return self._dict
