"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class TaskDesignRaw:
    XML_NODE_NAME: str = 'TaskDesign'

    def __init__(self, task_design_info: _EntityInfo) -> None:
        self.__task_design_id: int = _parse.pss_int(
            task_design_info.get('TaskDesignId'))
        self.__icon_sprite_id: int = _parse.pss_int(
            task_design_info.get('IconSpriteId'))
        self.__available_to: datetime = _parse.pss_datetime(
            task_design_info.get('AvailableTo'))
        self.__reward_distribution_string: str = _parse.pss_str(
            task_design_info.get('RewardDistributionString'))
        self.__name: str = _parse.pss_str(task_design_info.get('Name'))
        self.__objective_amount: int = _parse.pss_int(
            task_design_info.get('ObjectiveAmount'))
        self.__season_design_id: int = _parse.pss_int(
            task_design_info.get('SeasonDesignId'))
        self.__objective_type: str = _parse.pss_str(
            task_design_info.get('ObjectiveType'))
        self.__requirement_string: str = _parse.pss_str(
            task_design_info.get('RequirementString'))
        self.__objective_argument: str = _parse.pss_str(
            task_design_info.get('ObjectiveArgument'))
        self.__task_category: str = _parse.pss_str(
            task_design_info.get('TaskCategory'))
        self.__reward_string: str = _parse.pss_str(
            task_design_info.get('RewardString'))
        self.__global_progress: int = _parse.pss_int(
            task_design_info.get('GlobalProgress'))
        self.__available_from: datetime = _parse.pss_datetime(
            task_design_info.get('AvailableFrom'))
        self.__flags: int = _parse.pss_int(task_design_info.get('Flags'))
        self.__description: str = _parse.pss_str(
            task_design_info.get('Description'))

    @property
    def task_design_id(self) -> int:
        return self.__task_design_id

    @property
    def icon_sprite_id(self) -> int:
        return self.__icon_sprite_id

    @property
    def available_to(self) -> datetime:
        return self.__available_to

    @property
    def reward_distribution_string(self) -> str:
        return self.__reward_distribution_string

    @property
    def name(self) -> str:
        return self.__name

    @property
    def objective_amount(self) -> int:
        return self.__objective_amount

    @property
    def season_design_id(self) -> int:
        return self.__season_design_id

    @property
    def objective_type(self) -> str:
        return self.__objective_type

    @property
    def requirement_string(self) -> str:
        return self.__requirement_string

    @property
    def objective_argument(self) -> str:
        return self.__objective_argument

    @property
    def task_category(self) -> str:
        return self.__task_category

    @property
    def reward_string(self) -> str:
        return self.__reward_string

    @property
    def global_progress(self) -> int:
        return self.__global_progress

    @property
    def available_from(self) -> datetime:
        return self.__available_from

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def description(self) -> str:
        return self.__description
