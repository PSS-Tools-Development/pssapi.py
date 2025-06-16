from abc import abstractmethod
from xml.etree import ElementTree as _ElementTree

from ..types import EntityInfo as _EntityInfo
from .raw import EntityBaseRaw as _EntityBaseRaw


class EntityBase(_EntityBaseRaw):
    def __init__(self, entity_info: _EntityInfo):
        super().__init__(entity_info)
        self._node: _ElementTree.Element = None

    @property
    def entity_name(self):
        return self.XML_NODE_NAME

    @property
    def node(self) -> _ElementTree.Element:
        return self._node

    @node.setter
    def node(self, node: _ElementTree.Element):
        self._node = node


class EntityWithIdBase(EntityBase):
    @property
    @abstractmethod
    def id(self) -> int:
        raise NotImplementedError()

    def __str__(self):
        return f"<{type(self).__name__} id={self.id}>"
