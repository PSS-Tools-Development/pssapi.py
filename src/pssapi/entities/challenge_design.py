from ..types import EntityInfo as _EntityInfo
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ChallengeDesignRaw as _ChallengeDesignRaw


class ChallengeDesign(_ChallengeDesignRaw, _EntityWithIdBase):
    def __init__(self, challenge_design_info: _EntityInfo) -> None:
        super().__init__(challenge_design_info)

    @property
    def id(self) -> int:
        return self.challenge_design_id
