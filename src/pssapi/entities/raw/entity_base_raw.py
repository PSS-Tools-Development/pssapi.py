from typing import Any

from pydantic import ConfigDict
from pydantic_xml import BaseXmlModel
from pydantic_xml.fields import XmlEntityInfo

from ...types import EntityInfo


class T(BaseXmlModel):
    pass


class EntityBaseRaw(BaseXmlModel):
    @property
    def untracked_properties(self) -> EntityInfo:
        return self.model_extra or {}

    def _key(self):
        return tuple()

    def __contains__(self, key):
        return key in self.to_dict().keys()

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return other._key() == self._key()
        return False

    def __getitem__(self, key):
        return self.to_dict()[key]

    def __hash__(self):
        return hash(self._key())

    def __iter__(self):
        for key, value in self.to_dict().items():
            yield key, value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        attributes = ", ".join(f"{key}={value}" for key, value in self.__iter__())
        return f"<{type(self).__name__} {attributes}>"

    def __str__(self):
        return self.__repr__()

    def to_dict(self) -> dict[str, Any]:
        model_dump = self.model_dump()
        original_attributes = {field.path: model_dump[property_name] for property_name, field in self.__class__.model_fields.items() if isinstance(field, XmlEntityInfo)}
        return model_dump | original_attributes

    model_config = ConfigDict(extra="allow")


__all__ = [
    "EntityBaseRaw",
]
