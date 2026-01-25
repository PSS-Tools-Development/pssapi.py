"""
This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class AchievementRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "Achievement"

    def __init__(self, achievement_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._achievement_design_id: int = _parse.pss_int(achievement_info.pop("AchievementDesignId", None))
        self._achievement_id: int = _parse.pss_int(achievement_info.pop("AchievementId", None))
        self._collected: bool = _parse.pss_bool(achievement_info.pop("Collected", None))
        self._progress_value: int = _parse.pss_int(achievement_info.pop("ProgressValue", None))
        self._user_id: int = _parse.pss_int(achievement_info.pop("UserId", None))
        super().__init__(achievement_info)

    @property
    def achievement_design_id(self) -> int:
        return self._achievement_design_id

    @property
    def achievement_id(self) -> int:
        return self._achievement_id

    @property
    def collected(self) -> bool:
        return self._collected

    @property
    def progress_value(self) -> int:
        return self._progress_value

    @property
    def user_id(self) -> int:
        return self._user_id

    def _key(self):
        return (
            self.achievement_design_id,
            self.achievement_id,
            self.collected,
            self.progress_value,
            self.user_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AchievementDesignId": self.achievement_design_id,
                "AchievementId": self.achievement_id,
                "Collected": self.collected,
                "ProgressValue": self.progress_value,
                "UserId": self.user_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
