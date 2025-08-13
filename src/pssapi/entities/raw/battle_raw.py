"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class BattleRaw(EntityBaseRaw, tag="Battle"):
    XML_NODE_NAME: str = "Battle"

    adventure_xml: Optional[str] = attr(name="AdventureXml", default=None)
    alliance_war_id: Optional[int] = attr(name="AllianceWarId", default=None)
    attacker_base_win_rewards: Optional[str] = attr(name="AttackerBaseWinRewards", default=None)
    attacker_lose_rewards: Optional[str] = attr(name="AttackerLoseRewards", default=None)
    attacker_win_rewards: Optional[str] = attr(name="AttackerWinRewards", default=None)
    attacking_alliance_id: Optional[int] = attr(name="AttackingAllianceId", default=None)
    attacking_alliance_name: Optional[str] = attr(name="AttackingAllianceName", default=None)
    attacking_alliance_sprite_id: Optional[int] = attr(name="AttackingAllianceSpriteId", default=None)
    attacking_ship_id: Optional[int] = attr(name="AttackingShipId", default=None)
    attacking_ship_name: Optional[str] = attr(name="AttackingShipName", default=None)
    attacking_ship_xml: Optional[str] = attr(name="AttackingShipXml", default=None)
    attacking_user_id: Optional[int] = attr(name="AttackingUserId", default=None)
    attacking_user_trophy: Optional[int] = attr(name="AttackingUserTrophy", default=None)
    attacking_user_xml: Optional[str] = attr(name="AttackingUserXml", default=None)
    background_id: Optional[int] = attr(name="BackgroundId", default=None)
    battle_date: Optional[datetime] = attr(name="BattleDate", default=None)
    battle_end_date: Optional[datetime] = attr(name="BattleEndDate", default=None)
    battle_end_frame: Optional[int] = attr(name="BattleEndFrame", default=None)
    battle_id: Optional[int] = attr(name="BattleId", default=None)
    battle_type: Optional[str] = attr(name="BattleType", default=None)
    challenge_design_id: Optional[int] = attr(name="ChallengeDesignId", default=None)
    client_end_frame: Optional[int] = attr(name="ClientEndFrame", default=None)
    client_outcome_type: Optional[str] = attr(name="ClientOutcomeType", default=None)
    commands: Optional[str] = attr(name="Commands", default=None)
    defender_lose_rewards: Optional[str] = attr(name="DefenderLoseRewards", default=None)
    defender_win_rewards: Optional[str] = attr(name="DefenderWinRewards", default=None)
    defending_alliance_id: Optional[int] = attr(name="DefendingAllianceId", default=None)
    defending_alliance_name: Optional[str] = attr(name="DefendingAllianceName", default=None)
    defending_alliance_sprite_id: Optional[int] = attr(name="DefendingAllianceSpriteId", default=None)
    defending_client_end_frame: Optional[int] = attr(name="DefendingClientEndFrame", default=None)
    defending_client_outcome_type: Optional[str] = attr(name="DefendingClientOutcomeType", default=None)
    defending_ship_id: Optional[int] = attr(name="DefendingShipId", default=None)
    defending_ship_name: Optional[str] = attr(name="DefendingShipName", default=None)
    defending_ship_xml: Optional[str] = attr(name="DefendingShipXml", default=None)
    defending_user_id: Optional[int] = attr(name="DefendingUserId", default=None)
    defending_user_trophy: Optional[int] = attr(name="DefendingUserTrophy", default=None)
    defending_user_xml: Optional[str] = attr(name="DefendingUserXml", default=None)
    is_online_battle: Optional[bool] = attr(name="IsOnlineBattle", default=None)
    is_star_battle: Optional[bool] = attr(name="IsStarBattle", default=None)
    league_type: Optional[str] = attr(name="LeagueType", default=None)
    lose_gas_result: Optional[int] = attr(name="LoseGasResult", default=None)
    lose_minerals_result: Optional[int] = attr(name="LoseMineralsResult", default=None)
    lose_rewards: Optional[str] = attr(name="LoseRewards", default=None)
    lose_trophy_result: Optional[int] = attr(name="LoseTrophyResult", default=None)
    mission_design_id: Optional[int] = attr(name="MissionDesignId", default=None)
    mission_event_id: Optional[int] = attr(name="MissionEventId", default=None)
    outcome_type: Optional[str] = attr(name="OutcomeType", default=None)
    random_seed: Optional[int] = attr(name="RandomSeed", default=None)
    rewards: Optional[str] = attr(name="Rewards", default=None)
    server_outcome_type: Optional[str] = attr(name="ServerOutcomeType", default=None)
    star_system_marker_id: Optional[int] = attr(name="StarSystemMarkerId", default=None)
    station_room_design_ids: Optional[str] = attr(name="StationRoomDesignIds", default=None)
    station_ship_design_id: Optional[int] = attr(name="StationShipDesignId", default=None)
    win_gas_result: Optional[int] = attr(name="WinGasResult", default=None)
    win_minerals_result: Optional[int] = attr(name="WinMineralsResult", default=None)
    win_rewards: Optional[str] = attr(name="WinRewards", default=None)
    win_trophy_result: Optional[int] = attr(name="WinTrophyResult", default=None)

    def _key(self):
        return (
            self.adventure_xml,
            self.alliance_war_id,
            self.attacker_base_win_rewards,
            self.attacker_lose_rewards,
            self.attacker_win_rewards,
            self.attacking_alliance_id,
            self.attacking_alliance_name,
            self.attacking_alliance_sprite_id,
            self.attacking_ship_id,
            self.attacking_ship_name,
            self.attacking_ship_xml,
            self.attacking_user_id,
            self.attacking_user_trophy,
            self.attacking_user_xml,
            self.background_id,
            self.battle_date,
            self.battle_end_date,
            self.battle_end_frame,
            self.battle_id,
            self.battle_type,
            self.challenge_design_id,
            self.client_end_frame,
            self.client_outcome_type,
            self.commands,
            self.defender_lose_rewards,
            self.defender_win_rewards,
            self.defending_alliance_id,
            self.defending_alliance_name,
            self.defending_alliance_sprite_id,
            self.defending_client_end_frame,
            self.defending_client_outcome_type,
            self.defending_ship_id,
            self.defending_ship_name,
            self.defending_ship_xml,
            self.defending_user_id,
            self.defending_user_trophy,
            self.defending_user_xml,
            self.is_online_battle,
            self.is_star_battle,
            self.league_type,
            self.lose_gas_result,
            self.lose_minerals_result,
            self.lose_rewards,
            self.lose_trophy_result,
            self.mission_design_id,
            self.mission_event_id,
            self.outcome_type,
            self.random_seed,
            self.rewards,
            self.server_outcome_type,
            self.star_system_marker_id,
            self.station_room_design_ids,
            self.station_ship_design_id,
            self.win_gas_result,
            self.win_minerals_result,
            self.win_rewards,
            self.win_trophy_result,
        )


__all__ = [
    "BattleRaw",
]
