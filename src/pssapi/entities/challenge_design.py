from .entity_base import EntityWithIdBase
from .raw import ChallengeDesignRaw


class ChallengeDesign(ChallengeDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.challenge_design_id


__all__ = [
    "ChallengeDesign",
]
