from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import CharacterDesignRaw as _CharacterDesignRaw


class CharacterDesign(_CharacterDesignRaw, _EntityWithIdBase):
    def __init__(self, character_design_info: _EntityInfo) -> None:
        super().__init__(character_design_info)
        self._equipment_mask_enum: _enums.EquipmentMaskFlag = _parse.pss_int_flag(self.equipment_mask, _enums.EquipmentMaskFlag)
        self._flags_enum: _enums.CharacterDesignFlagType = _parse.pss_int_flag(self.flags, _enums.CharacterDesignFlagType)
        self._gender_type_enum: _enums.GenderType = _parse.pss_str_enum(self.gender_type, _enums.GenderType)
        self._progression_type_enum: _enums.ProgressionType = _parse.pss_str_enum(self.progression_type, _enums.ProgressionType)
        self._race_type_enum: _enums.RaceType = _parse.pss_str_enum(self.race_type, _enums.RaceType)
        self._rarity_enum: _enums.Rarity = _parse.pss_str_enum(self.rarity, _enums.Rarity)
        self._special_ability_type_enum: _enums.SpecialAbilityType = _parse.pss_str_enum(self.special_ability_type, _enums.SpecialAbilityType)

    @property
    def id(self) -> int:
        return self.character_design_id

    @property
    def equipment_mask_enum(self) -> "_enums.EquipmentMaskFlag":
        return self._equipment_mask_enum

    @property
    def flags_enum(self) -> "_enums.CharacterDesignFlagType":
        return self._flags_enum

    @property
    def gender_type_enum(self) -> "_enums.GenderType":
        return self._gender_type_enum

    @property
    def progression_type_enum(self) -> "_enums.ProgressionType":
        return self._progression_type_enum

    @property
    def race_type_enum(self) -> "_enums.RaceType":
        return self._race_type_enum

    @property
    def rarity_enum(self) -> "_enums.Rarity":
        return self._rarity_enum

    @property
    def special_ability_type_enum(self) -> "_enums.SpecialAbilityType":
        return self._special_ability_type_enum
