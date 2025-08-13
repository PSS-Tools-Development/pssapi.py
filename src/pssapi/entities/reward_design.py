from .entity_base import EntityWithIdBase
from .raw import RewardDesignRaw


class RewardDesign(RewardDesignRaw, EntityWithIdBase):
    @property
    def id(self) -> int:
        return self.reward_design_id


__all__ = [
    "RewardDesign",
]
