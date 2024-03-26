from abc import ABC as _ABC

from ...types import EntityInfo as _EntityInfo


class EntityBaseRaw(_ABC):
    XML_NODE_NAME: str = None

    def __init__(self, entity_info: _EntityInfo):
        self._untracked_fields = entity_info or {}

    @property
    def untracked_properties(self) -> _EntityInfo:
        return self._untracked_fields

    def _key(self):
        return tuple()

    def __contains__(self, key):
        return key in self.__dict__().keys()

    def __dict__(self):
        return self.untracked_properties

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return other._key() == self._key()
        return False

    def __getitem__(self, key):
        return self.__dict__()[key]

    def __hash__(self):
        return hash(self._key())

    def __iter__(self):
        for key, value in self.__dict__().items():
            yield key, value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        attributes = ", ".join(f"{key}={value}" for key, value in self.__iter__())
        return f"<{type(self).__name__} {attributes}"

    def __str__(self):
        return self.__repr__()
