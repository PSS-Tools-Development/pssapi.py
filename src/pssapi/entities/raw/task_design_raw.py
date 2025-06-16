"""
This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class TaskDesignRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "TaskDesign"

    def __init__(self, task_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._available_from: _datetime = _parse.pss_datetime(task_design_info.pop("AvailableFrom", None))
        self._available_to: _datetime = _parse.pss_datetime(task_design_info.pop("AvailableTo", None))
        self._description: str = _parse.pss_str(task_design_info.pop("Description", None))
        self._flags: int = _parse.pss_int(task_design_info.pop("Flags", None))
        self._global_progress: int = _parse.pss_int(task_design_info.pop("GlobalProgress", None))
        self._icon_sprite_id: int = _parse.pss_int(task_design_info.pop("IconSpriteId", None))
        self._name: str = _parse.pss_str(task_design_info.pop("Name", None))
        self._objective_amount: int = _parse.pss_int(task_design_info.pop("ObjectiveAmount", None))
        self._objective_argument: str = _parse.pss_str(task_design_info.pop("ObjectiveArgument", None))
        self._objective_type: str = _parse.pss_str(task_design_info.pop("ObjectiveType", None))
        self._requirement_string: str = _parse.pss_str(task_design_info.pop("RequirementString", None))
        self._reward_distribution_string: str = _parse.pss_str(task_design_info.pop("RewardDistributionString", None))
        self._reward_string: str = _parse.pss_str(task_design_info.pop("RewardString", None))
        self._season_design_id: int = _parse.pss_int(task_design_info.pop("SeasonDesignId", None))
        self._task_category: str = _parse.pss_str(task_design_info.pop("TaskCategory", None))
        self._task_design_id: int = _parse.pss_int(task_design_info.pop("TaskDesignId", None))
        super().__init__(task_design_info)

    @property
    def available_from(self) -> _datetime:
        return self._available_from

    @property
    def available_to(self) -> _datetime:
        return self._available_to

    @property
    def description(self) -> str:
        return self._description

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def global_progress(self) -> int:
        return self._global_progress

    @property
    def icon_sprite_id(self) -> int:
        return self._icon_sprite_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def objective_amount(self) -> int:
        return self._objective_amount

    @property
    def objective_argument(self) -> str:
        return self._objective_argument

    @property
    def objective_type(self) -> str:
        return self._objective_type

    @property
    def requirement_string(self) -> str:
        return self._requirement_string

    @property
    def reward_distribution_string(self) -> str:
        return self._reward_distribution_string

    @property
    def reward_string(self) -> str:
        return self._reward_string

    @property
    def season_design_id(self) -> int:
        return self._season_design_id

    @property
    def task_category(self) -> str:
        return self._task_category

    @property
    def task_design_id(self) -> int:
        return self._task_design_id

    def _key(self):
        return (
            self.available_from,
            self.available_to,
            self.description,
            self.flags,
            self.global_progress,
            self.icon_sprite_id,
            self.name,
            self.objective_amount,
            self.objective_argument,
            self.objective_type,
            self.requirement_string,
            self.reward_distribution_string,
            self.reward_string,
            self.season_design_id,
            self.task_category,
            self.task_design_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AvailableFrom": self.available_from,
                "AvailableTo": self.available_to,
                "Description": self.description,
                "Flags": self.flags,
                "GlobalProgress": self.global_progress,
                "IconSpriteId": self.icon_sprite_id,
                "Name": self.name,
                "ObjectiveAmount": self.objective_amount,
                "ObjectiveArgument": self.objective_argument,
                "ObjectiveType": self.objective_type,
                "RequirementString": self.requirement_string,
                "RewardDistributionString": self.reward_distribution_string,
                "RewardString": self.reward_string,
                "SeasonDesignId": self.season_design_id,
                "TaskCategory": self.task_category,
                "TaskDesignId": self.task_design_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
