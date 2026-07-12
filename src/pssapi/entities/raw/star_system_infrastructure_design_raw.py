"""
This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class StarSystemInfrastructureDesignRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "StarSystemInfrastructureDesign"

    def __init__(self, star_system_infrastructure_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._infrastructure_design_id: int = _parse.pss_int(star_system_infrastructure_design_info.pop("InfrastructureDesignId", None))
        self._max_infrastructure_level: int = _parse.pss_int(star_system_infrastructure_design_info.pop("MaxInfrastructureLevel", None))
        self._star_system_id: int = _parse.pss_int(star_system_infrastructure_design_info.pop("StarSystemId", None))
        self._star_system_infrastructure_design_id: int = _parse.pss_int(star_system_infrastructure_design_info.pop("StarSystemInfrastructureDesignId", None))
        super().__init__(star_system_infrastructure_design_info)

    @property
    def infrastructure_design_id(self) -> int:
        return self._infrastructure_design_id

    @property
    def max_infrastructure_level(self) -> int:
        return self._max_infrastructure_level

    @property
    def star_system_id(self) -> int:
        return self._star_system_id

    @property
    def star_system_infrastructure_design_id(self) -> int:
        return self._star_system_infrastructure_design_id

    def _key(self):
        return (
            self.infrastructure_design_id,
            self.max_infrastructure_level,
            self.star_system_id,
            self.star_system_infrastructure_design_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "InfrastructureDesignId": self.infrastructure_design_id,
                "MaxInfrastructureLevel": self.max_infrastructure_level,
                "StarSystemId": self.star_system_id,
                "StarSystemInfrastructureDesignId": self.star_system_infrastructure_design_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
