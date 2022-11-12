"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class CharacterDesignActionRaw:
    XML_NODE_NAME: str = 'CharacterDesignAction'

    def __init__(self, character_design_action_info: _EntityInfo) -> None:
        self.action_type_id: int = _parse.pss_int(
            character_design_action_info.get('ActionTypeId'))
        self.character_design_action_id: int = _parse.pss_int(
            character_design_action_info.get('CharacterDesignActionId'))
        self.character_design_action_index: int = _parse.pss_int(
            character_design_action_info.get('CharacterDesignActionIndex'))
        self.character_design_id: int = _parse.pss_int(
            character_design_action_info.get('CharacterDesignId'))
        self.condition_type_id: int = _parse.pss_int(
            character_design_action_info.get('ConditionTypeId'))
