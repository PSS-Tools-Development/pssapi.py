"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class BattleRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "Battle"

    def __init__(self, battle_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._adventure_xml: str = _parse.pss_str(battle_info.pop("AdventureXml", None))
        self._alliance_war_id: int = _parse.pss_int(battle_info.pop("AllianceWarId", None))
        self._attacker_base_win_rewards: str = _parse.pss_str(battle_info.pop("AttackerBaseWinRewards", None))
        self._attacker_lose_rewards: str = _parse.pss_str(battle_info.pop("AttackerLoseRewards", None))
        self._attacker_win_rewards: str = _parse.pss_str(battle_info.pop("AttackerWinRewards", None))
        self._attacking_alliance_id: int = _parse.pss_int(battle_info.pop("AttackingAllianceId", None))
        self._attacking_alliance_name: str = _parse.pss_str(battle_info.pop("AttackingAllianceName", None))
        self._attacking_alliance_sprite_id: int = _parse.pss_int(battle_info.pop("AttackingAllianceSpriteId", None))
        self._attacking_ship_id: int = _parse.pss_int(battle_info.pop("AttackingShipId", None))
        self._attacking_ship_name: str = _parse.pss_str(battle_info.pop("AttackingShipName", None))
        self._attacking_ship_xml: str = _parse.pss_str(battle_info.pop("AttackingShipXml", None))
        self._attacking_user_id: int = _parse.pss_int(battle_info.pop("AttackingUserId", None))
        self._attacking_user_trophy: int = _parse.pss_int(battle_info.pop("AttackingUserTrophy", None))
        self._attacking_user_xml: str = _parse.pss_str(battle_info.pop("AttackingUserXml", None))
        self._background_id: int = _parse.pss_int(battle_info.pop("BackgroundId", None))
        self._battle_date: _datetime = _parse.pss_datetime(battle_info.pop("BattleDate", None))
        self._battle_end_date: _datetime = _parse.pss_datetime(battle_info.pop("BattleEndDate", None))
        self._battle_end_frame: int = _parse.pss_int(battle_info.pop("BattleEndFrame", None))
        self._battle_id: int = _parse.pss_int(battle_info.pop("BattleId", None))
        self._battle_type: str = _parse.pss_str(battle_info.pop("BattleType", None))
        self._challenge_design_id: int = _parse.pss_int(battle_info.pop("ChallengeDesignId", None))
        self._client_end_frame: int = _parse.pss_int(battle_info.pop("ClientEndFrame", None))
        self._client_outcome_type: str = _parse.pss_str(battle_info.pop("ClientOutcomeType", None))
        self._commands: str = _parse.pss_str(battle_info.pop("Commands", None))
        self._defender_lose_rewards: str = _parse.pss_str(battle_info.pop("DefenderLoseRewards", None))
        self._defender_win_rewards: str = _parse.pss_str(battle_info.pop("DefenderWinRewards", None))
        self._defending_alliance_id: int = _parse.pss_int(battle_info.pop("DefendingAllianceId", None))
        self._defending_alliance_name: str = _parse.pss_str(battle_info.pop("DefendingAllianceName", None))
        self._defending_alliance_sprite_id: int = _parse.pss_int(battle_info.pop("DefendingAllianceSpriteId", None))
        self._defending_client_end_frame: int = _parse.pss_int(battle_info.pop("DefendingClientEndFrame", None))
        self._defending_client_outcome_type: str = _parse.pss_str(battle_info.pop("DefendingClientOutcomeType", None))
        self._defending_ship_id: int = _parse.pss_int(battle_info.pop("DefendingShipId", None))
        self._defending_ship_name: str = _parse.pss_str(battle_info.pop("DefendingShipName", None))
        self._defending_ship_xml: str = _parse.pss_str(battle_info.pop("DefendingShipXml", None))
        self._defending_user_id: int = _parse.pss_int(battle_info.pop("DefendingUserId", None))
        self._defending_user_trophy: int = _parse.pss_int(battle_info.pop("DefendingUserTrophy", None))
        self._defending_user_xml: str = _parse.pss_str(battle_info.pop("DefendingUserXml", None))
        self._is_online_battle: bool = _parse.pss_bool(battle_info.pop("IsOnlineBattle", None))
        self._is_star_battle: bool = _parse.pss_bool(battle_info.pop("IsStarBattle", None))
        self._league_type: str = _parse.pss_str(battle_info.pop("LeagueType", None))
        self._lose_gas_result: int = _parse.pss_int(battle_info.pop("LoseGasResult", None))
        self._lose_minerals_result: int = _parse.pss_int(battle_info.pop("LoseMineralsResult", None))
        self._lose_rewards: str = _parse.pss_str(battle_info.pop("LoseRewards", None))
        self._lose_trophy_result: int = _parse.pss_int(battle_info.pop("LoseTrophyResult", None))
        self._mission_design_id: int = _parse.pss_int(battle_info.pop("MissionDesignId", None))
        self._mission_event_id: int = _parse.pss_int(battle_info.pop("MissionEventId", None))
        self._outcome_type: str = _parse.pss_str(battle_info.pop("OutcomeType", None))
        self._random_seed: int = _parse.pss_int(battle_info.pop("RandomSeed", None))
        self._rewards: str = _parse.pss_str(battle_info.pop("Rewards", None))
        self._server_outcome_type: str = _parse.pss_str(battle_info.pop("ServerOutcomeType", None))
        self._star_system_marker_id: int = _parse.pss_int(battle_info.pop("StarSystemMarkerId", None))
        self._station_room_design_ids: str = _parse.pss_str(battle_info.pop("StationRoomDesignIds", None))
        self._station_ship_design_id: int = _parse.pss_int(battle_info.pop("StationShipDesignId", None))
        self._win_gas_result: int = _parse.pss_int(battle_info.pop("WinGasResult", None))
        self._win_minerals_result: int = _parse.pss_int(battle_info.pop("WinMineralsResult", None))
        self._win_rewards: str = _parse.pss_str(battle_info.pop("WinRewards", None))
        self._win_trophy_result: int = _parse.pss_int(battle_info.pop("WinTrophyResult", None))
        super().__init__(battle_info)

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
            self._dict.update(super().__dict__())

        return self._dict
