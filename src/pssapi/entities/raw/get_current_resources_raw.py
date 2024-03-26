"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw


class GetCurrentResourcesRaw(EntityBaseRaw):
    XML_NODE_NAME: str = "GetCurrentResources"

    def __init__(self, get_current_resources_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._credits: int = _parse.pss_int(get_current_resources_info.pop("Credits", None))
        self._gas: int = _parse.pss_int(get_current_resources_info.pop("Gas", None))
        self._minerals: int = _parse.pss_int(get_current_resources_info.pop("Minerals", None))
        self._supply: int = _parse.pss_int(get_current_resources_info.pop("Supply", None))
        super().__init__(get_current_resources_info)

    @property
    def credits(self) -> int:
        return self._credits

    @property
    def gas(self) -> int:
        return self._gas

    @property
    def minerals(self) -> int:
        return self._minerals

    @property
    def supply(self) -> int:
        return self._supply

    def _key(self):
        return (
            self.credits,
            self.gas,
            self.minerals,
            self.supply,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "Credits": self.credits,
                "Gas": self.gas,
                "Minerals": self.minerals,
                "Supply": self.supply,
            }
            self._dict.update(super().__dict__())

        return self._dict
