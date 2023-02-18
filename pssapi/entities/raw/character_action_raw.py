"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CharacterActionRaw:
    XML_NODE_NAME: str = 'CharacterAction'

    def __init__(self, character_action_info: _EntityInfo) -> None:
        self.action_type_id: int = _parse.pss_int(character_action_info.get('ActionTypeId'))
        self.character_action_id: int = _parse.pss_int(character_action_info.get('CharacterActionId'))
        self.character_action_index: int = _parse.pss_int(character_action_info.get('CharacterActionIndex'))
        self.character_id: int = _parse.pss_int(character_action_info.get('CharacterId'))
        self.condition_type_id: int = _parse.pss_int(character_action_info.get('ConditionTypeId'))
