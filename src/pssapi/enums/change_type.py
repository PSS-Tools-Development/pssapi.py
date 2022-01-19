from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class ChangeType(_StrEnum):
    NONE = "None"
    ADD_CREW = "AddCrew"
    ADD_EXP = "AddEXP"
    ADD_LEAGUE_BONUS_GAS = "AddLeagueBonusGas"
    ADD_LOOT = "AddLoot"
    ADD_LOOT_BONUS_GAS = "AddLootBonusGas"
    ADD_LOOT_BONUS_MINERAL = "AddLootBonusMineral"
    BACKGROUND = "Background"
    MINING_BOOST = "MiningBoost"
    RESEARCH_BOOST = "ResearchBoost"
