
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import ChallengeDesignRaw as _ChallengeDesignRaw
from ..types import EntityInfo as _EntityInfo


class ChallengeDesign(_EntityWithIdBase, _ChallengeDesignRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<ChallengeDesign {self.id}>'

    def __str__(self) -> str:
        return f'<ChallengeDesign {self.id}>'

    @property
    def id(self) -> int:
        return self.challenge_design_id
