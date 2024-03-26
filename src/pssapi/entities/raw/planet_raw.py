"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from .entity_base_raw import EntityBaseRaw


class PlanetRaw(EntityBaseRaw):
    XML_NODE_NAME: str = "Planet"

    def __init__(self, planet_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}

    def _key(self):
        return tuple()

    def __dict__(self):
        if not self._dict:
            self._dict = {}
            self._dict.update(super().__dict__())

        return self._dict
