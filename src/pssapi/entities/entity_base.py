from abc import abstractmethod
from xml.etree import ElementTree

from pydantic import computed_field

from .raw import EntityBaseRaw


class EntityBase(EntityBaseRaw):
    @property
    def entity_name(self):
        return self.__xml_tag__

    @property
    def node(self) -> ElementTree.Element:
        return self._node

    @node.setter
    def node(self, node: ElementTree.Element):
        self._node = node


class EntityWithIdBase(EntityBase):
    @computed_field
    @property
    @abstractmethod
    def id(self) -> int:
        raise NotImplementedError()

    def __str__(self):
        return f"<{type(self).__name__} id={self.id}>"


__all__ = [
    "EntityBase",
    "EntityWithIdBase",
]
