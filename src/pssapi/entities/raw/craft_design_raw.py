"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CraftDesignRaw:
    XML_NODE_NAME: str = "CraftDesign"

    def __init__(self, craft_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._craft_attack_type: str = _parse.pss_str(craft_design_info.get("CraftAttackType"))
        self._craft_design_id: int = _parse.pss_int(craft_design_info.get("CraftDesignId"))
        self._craft_name: str = _parse.pss_str(craft_design_info.get("CraftName"))
        self._craft_target_type: str = _parse.pss_str(craft_design_info.get("CraftTargetType"))
        self._flight_speed: int = _parse.pss_int(craft_design_info.get("FlightSpeed"))
        self._hp: int = _parse.pss_int(craft_design_info.get("Hp"))
        self._missile_design_id: int = _parse.pss_int(craft_design_info.get("MissileDesignId"))
        self._reload: int = _parse.pss_int(craft_design_info.get("Reload"))
        self._sprite_id: int = _parse.pss_int(craft_design_info.get("SpriteId"))
        self._volley: int = _parse.pss_int(craft_design_info.get("Volley"))
        self._volley_delay: int = _parse.pss_int(craft_design_info.get("VolleyDelay"))

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

        return self._dict
