from abc import abstractproperty as _abstractproperty

from .raw import EntityBaseRaw as _EntityBaseRaw



class EntityBase(_EntityBaseRaw):
    @_abstractproperty
    def id(self) -> int:
        raise NotImplemented()