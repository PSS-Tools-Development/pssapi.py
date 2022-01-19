from abc import ABC as _ABC
from abc import abstractproperty as _abstractproperty





class EntityBase(_ABC):
    @_abstractproperty
    def id(self) -> int:
        raise NotImplemented()