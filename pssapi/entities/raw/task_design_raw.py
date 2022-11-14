"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class TaskDesignRaw:
    XML_NODE_NAME: str = 'TaskDesign'

    def __init__(self, task_design_info: _EntityInfo) -> None:
        self.available_from: _datetime = _parse.pss__datetime(task_design_info.get('AvailableFrom'))
        self.available_to: _datetime = _parse.pss__datetime(task_design_info.get('AvailableTo'))
        self.description: str = _parse.pss_str(task_design_info.get('Description'))
        self.flags: int = _parse.pss_int(task_design_info.get('Flags'))
        self.global_progress: int = _parse.pss_int(task_design_info.get('GlobalProgress'))
        self.icon_sprite_id: int = _parse.pss_int(task_design_info.get('IconSpriteId'))
        self.name: str = _parse.pss_str(task_design_info.get('Name'))
        self.objective_amount: int = _parse.pss_int(task_design_info.get('ObjectiveAmount'))
        self.objective_argument: str = _parse.pss_str(task_design_info.get('ObjectiveArgument'))
        self.objective_type: str = _parse.pss_str(task_design_info.get('ObjectiveType'))
        self.requirement_string: str = _parse.pss_str(task_design_info.get('RequirementString'))
        self.reward_distribution_string: str = _parse.pss_str(task_design_info.get('RewardDistributionString'))
        self.reward_string: str = _parse.pss_str(task_design_info.get('RewardString'))
        self.season_design_id: int = _parse.pss_int(task_design_info.get('SeasonDesignId'))
        self.task_category: str = _parse.pss_str(task_design_info.get('TaskCategory'))
        self.task_design_id: int = _parse.pss_int(task_design_info.get('TaskDesignId'))
