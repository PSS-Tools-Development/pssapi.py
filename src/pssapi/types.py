from typing import Dict as _Dict
from typing import List as _List
from typing import Union as _Union

EntitiesData = _Dict[str, "EntityInfo"]
EntityInfo = _Dict[str, _Union["EntityInfo", str, _List["EntityInfo"]]]

__all__ = [EntitiesData, EntityInfo]
