from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class OutcomeType(_StrEnum):
    ATTACKER_RETREATED = "AttackerRetreated"
    ATTACKER_WON = "AttackerWon"
    DEFENDER_WON = "DefenderWon"
    DRAW = "Draw"
    PLAYING = "Playing"
    PROCESSING = "Processing"
    REVIEWING = "Reviewing"
    WAITING = "Waiting"
    WAITING_FOR_RESULT_TO_FINALSE = "WaitingForResultToFinalse"
