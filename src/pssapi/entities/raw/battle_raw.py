"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class BattleRaw:
    XML_NODE_NAME: str = "Battle"

    def __init__(self, battle_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._adventure_xml: str = _parse.pss_str(battle_info.get("AdventureXml"))
        self._alliance_war_id: int = _parse.pss_int(battle_info.get("AllianceWarId"))
        self._attacker_base_win_rewards: str = _parse.pss_str(battle_info.get("AttackerBaseWinRewards"))
        self._attacker_lose_rewards: str = _parse.pss_str(battle_info.get("AttackerLoseRewards"))
        self._attacker_win_rewards: str = _parse.pss_str(battle_info.get("AttackerWinRewards"))
        self._attacking_alliance_id: int = _parse.pss_int(battle_info.get("AttackingAllianceId"))
        self._attacking_alliance_name: str = _parse.pss_str(battle_info.get("AttackingAllianceName"))
        self._attacking_alliance_sprite_id: int = _parse.pss_int(battle_info.get("AttackingAllianceSpriteId"))
        self._attacking_ship_id: int = _parse.pss_int(battle_info.get("AttackingShipId"))
        self._attacking_ship_name: str = _parse.pss_str(battle_info.get("AttackingShipName"))
        self._attacking_ship_xml: str = _parse.pss_str(battle_info.get("AttackingShipXml"))
        self._attacking_user_id: int = _parse.pss_int(battle_info.get("AttackingUserId"))
        self._attacking_user_trophy: int = _parse.pss_int(battle_info.get("AttackingUserTrophy"))
        self._attacking_user_xml: str = _parse.pss_str(battle_info.get("AttackingUserXml"))
        self._background_id: int = _parse.pss_int(battle_info.get("BackgroundId"))
        self._battle_date: _datetime = _parse.pss_datetime(battle_info.get("BattleDate"))
        self._battle_end_date: _datetime = _parse.pss_datetime(battle_info.get("BattleEndDate"))
        self._battle_end_frame: int = _parse.pss_int(battle_info.get("BattleEndFrame"))
        self._battle_id: int = _parse.pss_int(battle_info.get("BattleId"))
        self._battle_type: str = _parse.pss_str(battle_info.get("BattleType"))
        self._challenge_design_id: int = _parse.pss_int(battle_info.get("ChallengeDesignId"))
        self._client_end_frame: int = _parse.pss_int(battle_info.get("ClientEndFrame"))
        self._client_outcome_type: str = _parse.pss_str(battle_info.get("ClientOutcomeType"))
        self._commands: str = _parse.pss_str(battle_info.get("Commands"))
        self._defender_lose_rewards: str = _parse.pss_str(battle_info.get("DefenderLoseRewards"))
        self._defender_win_rewards: str = _parse.pss_str(battle_info.get("DefenderWinRewards"))
        self._defending_alliance_id: int = _parse.pss_int(battle_info.get("DefendingAllianceId"))
        self._defending_alliance_name: str = _parse.pss_str(battle_info.get("DefendingAllianceName"))
        self._defending_alliance_sprite_id: int = _parse.pss_int(battle_info.get("DefendingAllianceSpriteId"))
        self._defending_client_end_frame: int = _parse.pss_int(battle_info.get("DefendingClientEndFrame"))
        self._defending_client_outcome_type: str = _parse.pss_str(battle_info.get("DefendingClientOutcomeType"))
        self._defending_ship_id: int = _parse.pss_int(battle_info.get("DefendingShipId"))
        self._defending_ship_name: str = _parse.pss_str(battle_info.get("DefendingShipName"))
        self._defending_ship_xml: str = _parse.pss_str(battle_info.get("DefendingShipXml"))
        self._defending_user_id: int = _parse.pss_int(battle_info.get("DefendingUserId"))
        self._defending_user_trophy: int = _parse.pss_int(battle_info.get("DefendingUserTrophy"))
        self._defending_user_xml: str = _parse.pss_str(battle_info.get("DefendingUserXml"))
        self._is_online_battle: bool = _parse.pss_bool(battle_info.get("IsOnlineBattle"))
        self._is_star_battle: bool = _parse.pss_bool(battle_info.get("IsStarBattle"))
        self._league_type: str = _parse.pss_str(battle_info.get("LeagueType"))
        self._lose_gas_result: int = _parse.pss_int(battle_info.get("LoseGasResult"))
        self._lose_minerals_result: int = _parse.pss_int(battle_info.get("LoseMineralsResult"))
        self._lose_rewards: str = _parse.pss_str(battle_info.get("LoseRewards"))
        self._lose_trophy_result: int = _parse.pss_int(battle_info.get("LoseTrophyResult"))
        self._mission_design_id: int = _parse.pss_int(battle_info.get("MissionDesignId"))
        self._mission_event_id: int = _parse.pss_int(battle_info.get("MissionEventId"))
        self._outcome_type: str = _parse.pss_str(battle_info.get("OutcomeType"))
        self._random_seed: int = _parse.pss_int(battle_info.get("RandomSeed"))
        self._rewards: str = _parse.pss_str(battle_info.get("Rewards"))
        self._server_outcome_type: str = _parse.pss_str(battle_info.get("ServerOutcomeType"))
        self._star_system_marker_id: int = _parse.pss_int(battle_info.get("StarSystemMarkerId"))
        self._station_room_design_ids: str = _parse.pss_str(battle_info.get("StationRoomDesignIds"))
        self._station_ship_design_id: int = _parse.pss_int(battle_info.get("StationShipDesignId"))
        self._win_gas_result: int = _parse.pss_int(battle_info.get("WinGasResult"))
        self._win_minerals_result: int = _parse.pss_int(battle_info.get("WinMineralsResult"))
        self._win_rewards: str = _parse.pss_str(battle_info.get("WinRewards"))
        self._win_trophy_result: int = _parse.pss_int(battle_info.get("WinTrophyResult"))

    @property
    def adventure_xml(self) -> str:
        return self._adventure_xml

    @property
    def alliance_war_id(self) -> int:
        return self._alliance_war_id

    @property
    def attacker_base_win_rewards(self) -> str:
        return self._attacker_base_win_rewards

    @property
    def attacker_lose_rewards(self) -> str:
        return self._attacker_lose_rewards

    @property
    def attacker_win_rewards(self) -> str:
        return self._attacker_win_rewards

    @property
    def attacking_alliance_id(self) -> int:
        return self._attacking_alliance_id

    @property
    def attacking_alliance_name(self) -> str:
        return self._attacking_alliance_name

    @property
    def attacking_alliance_sprite_id(self) -> int:
        return self._attacking_alliance_sprite_id

    @property
    def attacking_ship_id(self) -> int:
        return self._attacking_ship_id

    @property
    def attacking_ship_name(self) -> str:
        return self._attacking_ship_name

    @property
    def attacking_ship_xml(self) -> str:
        return self._attacking_ship_xml

    @property
    def attacking_user_id(self) -> int:
        return self._attacking_user_id

    @property
    def attacking_user_trophy(self) -> int:
        return self._attacking_user_trophy

    @property
    def attacking_user_xml(self) -> str:
        return self._attacking_user_xml

    @property
    def background_id(self) -> int:
        return self._background_id

    @property
    def battle_date(self) -> _datetime:
        return self._battle_date

    @property
    def battle_end_date(self) -> _datetime:
        return self._battle_end_date

    @property
    def battle_end_frame(self) -> int:
        return self._battle_end_frame

    @property
    def battle_id(self) -> int:
        return self._battle_id

    @property
    def battle_type(self) -> str:
        return self._battle_type

    @property
    def challenge_design_id(self) -> int:
        return self._challenge_design_id

    @property
    def client_end_frame(self) -> int:
        return self._client_end_frame

    @property
    def client_outcome_type(self) -> str:
        return self._client_outcome_type

    @property
    def commands(self) -> str:
        return self._commands

    @property
    def defender_lose_rewards(self) -> str:
        return self._defender_lose_rewards

    @property
    def defender_win_rewards(self) -> str:
        return self._defender_win_rewards

    @property
    def defending_alliance_id(self) -> int:
        return self._defending_alliance_id

    @property
    def defending_alliance_name(self) -> str:
        return self._defending_alliance_name

    @property
    def defending_alliance_sprite_id(self) -> int:
        return self._defending_alliance_sprite_id

    @property
    def defending_client_end_frame(self) -> int:
        return self._defending_client_end_frame

    @property
    def defending_client_outcome_type(self) -> str:
        return self._defending_client_outcome_type

    @property
    def defending_ship_id(self) -> int:
        return self._defending_ship_id

    @property
    def defending_ship_name(self) -> str:
        return self._defending_ship_name

    @property
    def defending_ship_xml(self) -> str:
        return self._defending_ship_xml

    @property
    def defending_user_id(self) -> int:
        return self._defending_user_id

    @property
    def defending_user_trophy(self) -> int:
        return self._defending_user_trophy

    @property
    def defending_user_xml(self) -> str:
        return self._defending_user_xml

    @property
    def is_online_battle(self) -> bool:
        return self._is_online_battle

    @property
    def is_star_battle(self) -> bool:
        return self._is_star_battle

    @property
    def league_type(self) -> str:
        return self._league_type

    @property
    def lose_gas_result(self) -> int:
        return self._lose_gas_result

    @property
    def lose_minerals_result(self) -> int:
        return self._lose_minerals_result

    @property
    def lose_rewards(self) -> str:
        return self._lose_rewards

    @property
    def lose_trophy_result(self) -> int:
        return self._lose_trophy_result

    @property
    def mission_design_id(self) -> int:
        return self._mission_design_id

    @property
    def mission_event_id(self) -> int:
        return self._mission_event_id

    @property
    def outcome_type(self) -> str:
        return self._outcome_type

    @property
    def random_seed(self) -> int:
        return self._random_seed

    @property
    def rewards(self) -> str:
        return self._rewards

    @property
    def server_outcome_type(self) -> str:
        return self._server_outcome_type

    @property
    def star_system_marker_id(self) -> int:
        return self._star_system_marker_id

    @property
    def station_room_design_ids(self) -> str:
        return self._station_room_design_ids

    @property
    def station_ship_design_id(self) -> int:
        return self._station_ship_design_id

    @property
    def win_gas_result(self) -> int:
        return self._win_gas_result

    @property
    def win_minerals_result(self) -> int:
        return self._win_minerals_result

    @property
    def win_rewards(self) -> str:
        return self._win_rewards

    @property
    def win_trophy_result(self) -> int:
        return self._win_trophy_result

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

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AdventureXml": self.adventure_xml,
                "AllianceWarId": self.alliance_war_id,
                "AttackerBaseWinRewards": self.attacker_base_win_rewards,
                "AttackerLoseRewards": self.attacker_lose_rewards,
                "AttackerWinRewards": self.attacker_win_rewards,
                "AttackingAllianceId": self.attacking_alliance_id,
                "AttackingAllianceName": self.attacking_alliance_name,
                "AttackingAllianceSpriteId": self.attacking_alliance_sprite_id,
                "AttackingShipId": self.attacking_ship_id,
                "AttackingShipName": self.attacking_ship_name,
                "AttackingShipXml": self.attacking_ship_xml,
                "AttackingUserId": self.attacking_user_id,
                "AttackingUserTrophy": self.attacking_user_trophy,
                "AttackingUserXml": self.attacking_user_xml,
                "BackgroundId": self.background_id,
                "BattleDate": self.battle_date,
                "BattleEndDate": self.battle_end_date,
                "BattleEndFrame": self.battle_end_frame,
                "BattleId": self.battle_id,
                "BattleType": self.battle_type,
                "ChallengeDesignId": self.challenge_design_id,
                "ClientEndFrame": self.client_end_frame,
                "ClientOutcomeType": self.client_outcome_type,
                "Commands": self.commands,
                "DefenderLoseRewards": self.defender_lose_rewards,
                "DefenderWinRewards": self.defender_win_rewards,
                "DefendingAllianceId": self.defending_alliance_id,
                "DefendingAllianceName": self.defending_alliance_name,
                "DefendingAllianceSpriteId": self.defending_alliance_sprite_id,
                "DefendingClientEndFrame": self.defending_client_end_frame,
                "DefendingClientOutcomeType": self.defending_client_outcome_type,
                "DefendingShipId": self.defending_ship_id,
                "DefendingShipName": self.defending_ship_name,
                "DefendingShipXml": self.defending_ship_xml,
                "DefendingUserId": self.defending_user_id,
                "DefendingUserTrophy": self.defending_user_trophy,
                "DefendingUserXml": self.defending_user_xml,
                "IsOnlineBattle": self.is_online_battle,
                "IsStarBattle": self.is_star_battle,
                "LeagueType": self.league_type,
                "LoseGasResult": self.lose_gas_result,
                "LoseMineralsResult": self.lose_minerals_result,
                "LoseRewards": self.lose_rewards,
                "LoseTrophyResult": self.lose_trophy_result,
                "MissionDesignId": self.mission_design_id,
                "MissionEventId": self.mission_event_id,
                "OutcomeType": self.outcome_type,
                "RandomSeed": self.random_seed,
                "Rewards": self.rewards,
                "ServerOutcomeType": self.server_outcome_type,
                "StarSystemMarkerId": self.star_system_marker_id,
                "StationRoomDesignIds": self.station_room_design_ids,
                "StationShipDesignId": self.station_ship_design_id,
                "WinGasResult": self.win_gas_result,
                "WinMineralsResult": self.win_minerals_result,
                "WinRewards": self.win_rewards,
                "WinTrophyResult": self.win_trophy_result,
            }

        return self._dict
