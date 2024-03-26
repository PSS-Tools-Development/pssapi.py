"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class CraftDesignRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "CraftDesign"

    def __init__(self, craft_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._attack_distance: int = _parse.pss_int(craft_design_info.pop("AttackDistance", None))
        self._attack_range: int = _parse.pss_int(craft_design_info.pop("AttackRange", None))
        self._craft_attack_type: str = _parse.pss_str(craft_design_info.pop("CraftAttackType", None))
        self._craft_design_id: int = _parse.pss_int(craft_design_info.pop("CraftDesignId", None))
        self._craft_name: str = _parse.pss_str(craft_design_info.pop("CraftName", None))
        self._craft_target_type: str = _parse.pss_str(craft_design_info.pop("CraftTargetType", None))
        self._flight_speed: int = _parse.pss_int(craft_design_info.pop("FlightSpeed", None))
        self._hp: int = _parse.pss_int(craft_design_info.pop("Hp", None))
        self._missile_design_id: int = _parse.pss_int(craft_design_info.pop("MissileDesignId", None))
        self._reload: int = _parse.pss_int(craft_design_info.pop("Reload", None))
        self._sprite_id: int = _parse.pss_int(craft_design_info.pop("SpriteId", None))
        self._volley: int = _parse.pss_int(craft_design_info.pop("Volley", None))
        self._volley_delay: int = _parse.pss_int(craft_design_info.pop("VolleyDelay", None))
        super().__init__(craft_design_info)

    @property
    def attack_distance(self) -> int:
        return self._attack_distance

    @property
    def attack_range(self) -> int:
        return self._attack_range

    @property
    def craft_attack_type(self) -> str:
        return self._craft_attack_type

    @property
    def craft_design_id(self) -> int:
        return self._craft_design_id

    @property
    def craft_name(self) -> str:
        return self._craft_name

    @property
    def craft_target_type(self) -> str:
        return self._craft_target_type

    @property
    def flight_speed(self) -> int:
        return self._flight_speed

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def missile_design_id(self) -> int:
        return self._missile_design_id

    @property
    def reload(self) -> int:
        return self._reload

    @property
    def sprite_id(self) -> int:
        return self._sprite_id

    @property
    def volley(self) -> int:
        return self._volley

    @property
    def volley_delay(self) -> int:
        return self._volley_delay

    def _key(self):
        return (
            self.attack_distance,
            self.attack_range,
            self.craft_attack_type,
            self.craft_design_id,
            self.craft_name,
            self.craft_target_type,
            self.flight_speed,
            self.hp,
            self.missile_design_id,
            self.reload,
            self.sprite_id,
            self.volley,
            self.volley_delay,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AttackDistance": self.attack_distance,
                "AttackRange": self.attack_range,
                "CraftAttackType": self.craft_attack_type,
                "CraftDesignId": self.craft_design_id,
                "CraftName": self.craft_name,
                "CraftTargetType": self.craft_target_type,
                "FlightSpeed": self.flight_speed,
                "Hp": self.hp,
                "MissileDesignId": self.missile_design_id,
                "Reload": self.reload,
                "SpriteId": self.sprite_id,
                "Volley": self.volley,
                "VolleyDelay": self.volley_delay,
            }
            self._dict.update(super().__dict__())

        return self._dict
