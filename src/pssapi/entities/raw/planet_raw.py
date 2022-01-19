"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo


class PlanetRaw:
    XML_NODE_NAME: str = "Planet"

    def __init__(self, planet_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}

    def _key(self):
        return ()

    def __dict__(self):
        if not self._dict:
            self._dict = {}

        return self._dict
