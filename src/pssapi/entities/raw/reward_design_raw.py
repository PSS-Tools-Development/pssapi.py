"""
This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class RewardDesignRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "RewardDesign"

    def __init__(self, reward_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._argument_string: str = _parse.pss_str(reward_design_info.pop("ArgumentString", None))
        self._available_every_x_days: int = _parse.pss_int(reward_design_info.pop("AvailableEveryXDays", None))
        self._available_from: _datetime = _parse.pss_datetime(reward_design_info.pop("AvailableFrom", None))
        self._available_quantity: int = _parse.pss_int(reward_design_info.pop("AvailableQuantity", None))
        self._available_to: _datetime = _parse.pss_datetime(reward_design_info.pop("AvailableTo", None))
        self._background_sprite_id: int = _parse.pss_int(reward_design_info.pop("BackgroundSpriteId", None))
        self._battle_pass_tier_index: int = _parse.pss_int(reward_design_info.pop("BattlePassTierIndex", None))
        self._flags: int = _parse.pss_int(reward_design_info.pop("Flags", None))
        self._grids: int = _parse.pss_int(reward_design_info.pop("Grids", None))
        self._max_per_user: int = _parse.pss_int(reward_design_info.pop("MaxPerUser", None))
        self._metadata: str = _parse.pss_str(reward_design_info.pop("Metadata", None))
        self._order_index: int = _parse.pss_int(reward_design_info.pop("OrderIndex", None))
        self._price_string: str = _parse.pss_str(reward_design_info.pop("PriceString", None))
        self._requirement_string: str = _parse.pss_str(reward_design_info.pop("RequirementString", None))
        self._reward_description: str = _parse.pss_str(reward_design_info.pop("RewardDescription", None))
        self._reward_design_id: int = _parse.pss_int(reward_design_info.pop("RewardDesignId", None))
        self._reward_name: str = _parse.pss_str(reward_design_info.pop("RewardName", None))
        self._reward_type: str = _parse.pss_str(reward_design_info.pop("RewardType", None))
        self._season_design_id: int = _parse.pss_int(reward_design_info.pop("SeasonDesignId", None))
        self._sprite_id: int = _parse.pss_int(reward_design_info.pop("SpriteId", None))
        super().__init__(reward_design_info)

    @property
    def argument_string(self) -> str:
        return self._argument_string

    @property
    def available_every_x_days(self) -> int:
        return self._available_every_x_days

    @property
    def available_from(self) -> _datetime:
        return self._available_from

    @property
    def available_quantity(self) -> int:
        return self._available_quantity

    @property
    def available_to(self) -> _datetime:
        return self._available_to

    @property
    def background_sprite_id(self) -> int:
        return self._background_sprite_id

    @property
    def battle_pass_tier_index(self) -> int:
        return self._battle_pass_tier_index

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def grids(self) -> int:
        return self._grids

    @property
    def max_per_user(self) -> int:
        return self._max_per_user

    @property
    def metadata(self) -> str:
        return self._metadata

    @property
    def order_index(self) -> int:
        return self._order_index

    @property
    def price_string(self) -> str:
        return self._price_string

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def reward_description(self) -> str:
        return self._reward_description

    @property
    def reward_design_id(self) -> int:
        return self._reward_design_id

    @property
    def reward_name(self) -> str:
        return self._reward_name

    @property
    def reward_type(self) -> str:
        return self._reward_type

    @property
    def season_design_id(self) -> int:
        return self._season_design_id

    @property
    def sprite_id(self) -> int:
        return self._sprite_id

    def _key(self):
        return (
            self.argument_string,
            self.available_every_x_days,
            self.available_from,
            self.available_quantity,
            self.available_to,
            self.background_sprite_id,
            self.battle_pass_tier_index,
            self.flags,
            self.grids,
            self.max_per_user,
            self.metadata,
            self.order_index,
            self.price_string,
            self.requirement_string,
            self.reward_description,
            self.reward_design_id,
            self.reward_name,
            self.reward_type,
            self.season_design_id,
            self.sprite_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ArgumentString": self.argument_string,
                "AvailableEveryXDays": self.available_every_x_days,
                "AvailableFrom": self.available_from,
                "AvailableQuantity": self.available_quantity,
                "AvailableTo": self.available_to,
                "BackgroundSpriteId": self.background_sprite_id,
                "BattlePassTierIndex": self.battle_pass_tier_index,
                "Flags": self.flags,
                "Grids": self.grids,
                "MaxPerUser": self.max_per_user,
                "Metadata": self.metadata,
                "OrderIndex": self.order_index,
                "PriceString": self.price_string,
                "RequirementString": self.requirement_string,
                "RewardDescription": self.reward_description,
                "RewardDesignId": self.reward_design_id,
                "RewardName": self.reward_name,
                "RewardType": self.reward_type,
                "SeasonDesignId": self.season_design_id,
                "SpriteId": self.sprite_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
