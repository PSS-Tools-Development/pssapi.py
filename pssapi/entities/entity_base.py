from abc import abstractmethod

from .raw import EntityBaseRaw as _EntityBaseRaw


class EntityBase(_EntityBaseRaw):
    pass


class EntityWithIdBase(EntityBase):
    @property
    @abstractmethod
    def id(self) -> int:
        raise NotImplemented()
