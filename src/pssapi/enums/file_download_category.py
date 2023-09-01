from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class FileDownloadCategory(_StrEnumBase):
    NONE = "None"
    NEW_GAME = "NewGame"
    MAIN_SCENE = "MainScene"
    BATTLE_SCENE = "BattleScene"
    CHARACTER_SCENE = "CharacterScene"
    SCRATCHY_SCENE = "ScratchyScene"
    WAR_SCENE = "WarScene"
    BATTLE_PASS = "BattlePass"
