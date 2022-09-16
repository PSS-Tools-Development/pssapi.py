####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class TaskRaw():
    XML_NODE_NAME: str = 'Task'

    def __init__(self, task_info: _EntityInfo) -> None:
        self.__task_id: int = _parse.pss_int(task_info.get('TaskId'))
        self.__task_design_id: int = _parse.pss_int(task_info.get('TaskDesignId'))
        self.__user_id: int = _parse.pss_int(task_info.get('UserId'))
        self.__progress_value: int = _parse.pss_int(task_info.get('ProgressValue'))
        self.__collected: bool = _parse.pss_bool(task_info.get('Collected'))

    @property
    def task_id(self) -> int:
        return self.__task_id

    @property
    def task_design_id(self) -> int:
        return self.__task_design_id

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def progress_value(self) -> int:
        return self.__progress_value

    @property
    def collected(self) -> bool:
        return self.__collected
