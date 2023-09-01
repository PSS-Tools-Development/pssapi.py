from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class OutcomeType(_StrEnumBase):
    ATTACKER_RETREATED = "AttackerRetreated"
    ATTACKER_WON = "AttackerWon"
    DEFENDER_WON = "DefenderWon"
    DRAW = "Draw"
    PLAYING = "Playing"
    PROCESSING = "Processing"
    REVIEWING = "Reviewing"
    WAITING = "Waiting"
    WAITING_FOR_RESULT_TO_FINALSE = "WaitingForResultToFinalse"
