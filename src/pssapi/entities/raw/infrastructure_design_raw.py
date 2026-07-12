"""
This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class InfrastructureDesignRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "InfrastructureDesign"

    def __init__(self, infrastructure_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._base_investment_cost_string: str = _parse.pss_str(infrastructure_design_info.pop("BaseInvestmentCostString", None))
        self._base_reward_argument: int = _parse.pss_int(infrastructure_design_info.pop("BaseRewardArgument", None))
        self._base_reward_string: str = _parse.pss_str(infrastructure_design_info.pop("BaseRewardString", None))
        self._cost_increment: int = _parse.pss_int(infrastructure_design_info.pop("CostIncrement", None))
        self._description: str = _parse.pss_str(infrastructure_design_info.pop("Description", None))
        self._infrastructure_design_id: int = _parse.pss_int(infrastructure_design_info.pop("InfrastructureDesignId", None))
        self._infrastructure_reward_type: str = _parse.pss_str(infrastructure_design_info.pop("InfrastructureRewardType", None))
        self._infrastructure_type: str = _parse.pss_str(infrastructure_design_info.pop("InfrastructureType", None))
        self._investment_level_multiplier: int = _parse.pss_int(infrastructure_design_info.pop("InvestmentLevelMultiplier", None))
        self._name: str = _parse.pss_str(infrastructure_design_info.pop("Name", None))
        self._reward_duration: int = _parse.pss_int(infrastructure_design_info.pop("RewardDuration", None))
        self._reward_increment: int = _parse.pss_int(infrastructure_design_info.pop("RewardIncrement", None))
        self._reward_level_multiplier: float = _parse.pss_float(infrastructure_design_info.pop("RewardLevelMultiplier", None))
        super().__init__(infrastructure_design_info)

    @property
    def base_investment_cost_string(self) -> str:
        return self._base_investment_cost_string

    @property
    def base_reward_argument(self) -> int:
        return self._base_reward_argument

    @property
    def base_reward_string(self) -> str:
        return self._base_reward_string

    @property
    def cost_increment(self) -> int:
        return self._cost_increment

    @property
    def description(self) -> str:
        return self._description

    @property
    def infrastructure_design_id(self) -> int:
        return self._infrastructure_design_id

    @property
    def infrastructure_reward_type(self) -> str:
        return self._infrastructure_reward_type

    @property
    def infrastructure_type(self) -> str:
        return self._infrastructure_type

    @property
    def investment_level_multiplier(self) -> int:
        return self._investment_level_multiplier

    @property
    def name(self) -> str:
        return self._name

    @property
    def reward_duration(self) -> int:
        return self._reward_duration

    @property
    def reward_increment(self) -> int:
        return self._reward_increment

    @property
    def reward_level_multiplier(self) -> float:
        return self._reward_level_multiplier

    def _key(self):
        return (
            self.base_investment_cost_string,
            self.base_reward_argument,
            self.base_reward_string,
            self.cost_increment,
            self.description,
            self.infrastructure_design_id,
            self.infrastructure_reward_type,
            self.infrastructure_type,
            self.investment_level_multiplier,
            self.name,
            self.reward_duration,
            self.reward_increment,
            self.reward_level_multiplier,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "BaseInvestmentCostString": self.base_investment_cost_string,
                "BaseRewardArgument": self.base_reward_argument,
                "BaseRewardString": self.base_reward_string,
                "CostIncrement": self.cost_increment,
                "Description": self.description,
                "InfrastructureDesignId": self.infrastructure_design_id,
                "InfrastructureRewardType": self.infrastructure_reward_type,
                "InfrastructureType": self.infrastructure_type,
                "InvestmentLevelMultiplier": self.investment_level_multiplier,
                "Name": self.name,
                "RewardDuration": self.reward_duration,
                "RewardIncrement": self.reward_increment,
                "RewardLevelMultiplier": self.reward_level_multiplier,
            }
            self._dict.update(super().__dict__())

        return self._dict
