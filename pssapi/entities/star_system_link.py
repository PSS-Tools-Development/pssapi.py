
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import StarSystemLinkRaw as _StarSystemLinkRaw
from ..types import EntityInfo as _EntityInfo


class StarSystemLink(_EntityWithIdBase, _StarSystemLinkRaw):
    def __init__(self, _info: _EntityInfo) -> None:
        super().__init__(_info)

    def __repr__(self) -> str:
        return f'<StarSystemLink {self.id}>'

    def __str__(self) -> str:
        return f'<StarSystemLink {self.id}>'

    @property
    def id(self) -> int:
        return self.star_system_link_id
