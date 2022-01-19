from abc import abstractmethod

from .raw import EntityBaseRaw as _EntityBaseRaw


class EntityBase(_EntityBaseRaw):
    @property
    def entity_name(self):
        return self.XML_NODE_NAME


class EntityWithIdBase(EntityBase):
    @property
    @abstractmethod
    def id(self) -> int:
        raise NotImplementedError()

    def __str__(self):
        return f"<{type(self).__name__} id={self.id}>"
