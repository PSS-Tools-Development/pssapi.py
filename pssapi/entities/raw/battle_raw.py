####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class BattleRaw():
    XML_NODE_NAME: str = 'Battle'

    def __init__(self, battle_info: _EntityInfo) -> None:
        self.__lose_rewards: str = _parse.pss_str(battle_info.get('LoseRewards'))
        self.__attacking_user_xml: str = _parse.pss_str(battle_info.get('AttackingUserXml'))
        self.__attacker_lose_rewards: str = _parse.pss_str(battle_info.get('AttackerLoseRewards'))
        self.__alliance_war_id: int = _parse.pss_int(battle_info.get('AllianceWarId'))
        self.__attacking_ship_xml: str = _parse.pss_str(battle_info.get('AttackingShipXml'))
        self.__background_id: int = _parse.pss_int(battle_info.get('BackgroundId'))
        self.__win_gas_result: int = _parse.pss_int(battle_info.get('WinGasResult'))
        self.__server_outcome_type: str = _parse.pss_str(battle_info.get('ServerOutcomeType'))
        self.__defending_alliance_sprite_id: int = _parse.pss_int(battle_info.get('DefendingAllianceSpriteId'))
        self.__defender_lose_rewards: str = _parse.pss_str(battle_info.get('DefenderLoseRewards'))
        self.__lose_gas_result: int = _parse.pss_int(battle_info.get('LoseGasResult'))
        self.__mission_event_id: int = _parse.pss_int(battle_info.get('MissionEventId'))
        self.__defending_ship_id: int = _parse.pss_int(battle_info.get('DefendingShipId'))
        self.__station_room_design_ids: str = _parse.pss_str(battle_info.get('StationRoomDesignIds'))
        self.__defending_user_xml: str = _parse.pss_str(battle_info.get('DefendingUserXml'))
        self.__challenge_design_id: int = _parse.pss_int(battle_info.get('ChallengeDesignId'))
        self.__lose_trophy_result: int = _parse.pss_int(battle_info.get('LoseTrophyResult'))
        self.__attacking_ship_name: str = _parse.pss_str(battle_info.get('AttackingShipName'))
        self.__defending_user_id: int = _parse.pss_int(battle_info.get('DefendingUserId'))
        self.__league_type: str = _parse.pss_str(battle_info.get('LeagueType'))
        self.__adventure_xml: str = _parse.pss_str(battle_info.get('AdventureXml'))
        self.__is_star_battle: bool = _parse.pss_bool(battle_info.get('IsStarBattle'))
        self.__battle_date: datetime = _parse.pss_datetime(battle_info.get('BattleDate'))
        self.__attacking_user_trophy: int = _parse.pss_int(battle_info.get('AttackingUserTrophy'))
        self.__is_online_battle: bool = _parse.pss_bool(battle_info.get('IsOnlineBattle'))
        self.__attacking_ship_id: int = _parse.pss_int(battle_info.get('AttackingShipId'))
        self.__defender_win_rewards: str = _parse.pss_str(battle_info.get('DefenderWinRewards'))
        self.__defending_user_trophy: int = _parse.pss_int(battle_info.get('DefendingUserTrophy'))
        self.__outcome_type: str = _parse.pss_str(battle_info.get('OutcomeType'))
        self.__defending_ship_name: str = _parse.pss_str(battle_info.get('DefendingShipName'))
        self.__defending_client_outcome_type: str = _parse.pss_str(battle_info.get('DefendingClientOutcomeType'))
        self.__client_outcome_type: str = _parse.pss_str(battle_info.get('ClientOutcomeType'))
        self.__win_minerals_result: int = _parse.pss_int(battle_info.get('WinMineralsResult'))
        self.__defending_alliance_id: int = _parse.pss_int(battle_info.get('DefendingAllianceId'))
        self.__win_rewards: str = _parse.pss_str(battle_info.get('WinRewards'))
        self.__station_ship_design_id: int = _parse.pss_int(battle_info.get('StationShipDesignId'))
        self.__defending_alliance_name: str = _parse.pss_str(battle_info.get('DefendingAllianceName'))
        self.__attacking_alliance_id: int = _parse.pss_int(battle_info.get('AttackingAllianceId'))
        self.__client_end_frame: int = _parse.pss_int(battle_info.get('ClientEndFrame'))
        self.__defending_client_end_frame: int = _parse.pss_int(battle_info.get('DefendingClientEndFrame'))
        self.__commands: str = _parse.pss_str(battle_info.get('Commands'))
        self.__attacking_alliance_sprite_id: int = _parse.pss_int(battle_info.get('AttackingAllianceSpriteId'))
        self.__battle_id: int = _parse.pss_int(battle_info.get('BattleId'))
        self.__attacking_alliance_name: str = _parse.pss_str(battle_info.get('AttackingAllianceName'))
        self.__defending_ship_xml: str = _parse.pss_str(battle_info.get('DefendingShipXml'))
        self.__attacker_base_win_rewards: str = _parse.pss_str(battle_info.get('AttackerBaseWinRewards'))
        self.__lose_minerals_result: int = _parse.pss_int(battle_info.get('LoseMineralsResult'))
        self.__attacking_user_id: int = _parse.pss_int(battle_info.get('AttackingUserId'))
        self.__battle_end_frame: int = _parse.pss_int(battle_info.get('BattleEndFrame'))
        self.__win_trophy_result: int = _parse.pss_int(battle_info.get('WinTrophyResult'))
        self.__battle_type: str = _parse.pss_str(battle_info.get('BattleType'))
        self.__attacker_win_rewards: str = _parse.pss_str(battle_info.get('AttackerWinRewards'))
        self.__random_seed: int = _parse.pss_int(battle_info.get('RandomSeed'))
        self.__battle_end_date: datetime = _parse.pss_datetime(battle_info.get('BattleEndDate'))
        self.__rewards: str = _parse.pss_str(battle_info.get('Rewards'))
        self.__mission_design_id: int = _parse.pss_int(battle_info.get('MissionDesignId'))

    @property
    def lose_rewards(self) -> str:
        return self.__lose_rewards

    @property
    def attacking_user_xml(self) -> str:
        return self.__attacking_user_xml

    @property
    def attacker_lose_rewards(self) -> str:
        return self.__attacker_lose_rewards

    @property
    def alliance_war_id(self) -> int:
        return self.__alliance_war_id

    @property
    def attacking_ship_xml(self) -> str:
        return self.__attacking_ship_xml

    @property
    def background_id(self) -> int:
        return self.__background_id

    @property
    def win_gas_result(self) -> int:
        return self.__win_gas_result

    @property
    def server_outcome_type(self) -> str:
        return self.__server_outcome_type

    @property
    def defending_alliance_sprite_id(self) -> int:
        return self.__defending_alliance_sprite_id

    @property
    def defender_lose_rewards(self) -> str:
        return self.__defender_lose_rewards

    @property
    def lose_gas_result(self) -> int:
        return self.__lose_gas_result

    @property
    def mission_event_id(self) -> int:
        return self.__mission_event_id

    @property
    def defending_ship_id(self) -> int:
        return self.__defending_ship_id

    @property
    def station_room_design_ids(self) -> str:
        return self.__station_room_design_ids

    @property
    def defending_user_xml(self) -> str:
        return self.__defending_user_xml

    @property
    def challenge_design_id(self) -> int:
        return self.__challenge_design_id

    @property
    def lose_trophy_result(self) -> int:
        return self.__lose_trophy_result

    @property
    def attacking_ship_name(self) -> str:
        return self.__attacking_ship_name

    @property
    def defending_user_id(self) -> int:
        return self.__defending_user_id

    @property
    def league_type(self) -> str:
        return self.__league_type

    @property
    def adventure_xml(self) -> str:
        return self.__adventure_xml

    @property
    def is_star_battle(self) -> bool:
        return self.__is_star_battle

    @property
    def battle_date(self) -> datetime:
        return self.__battle_date

    @property
    def attacking_user_trophy(self) -> int:
        return self.__attacking_user_trophy

    @property
    def is_online_battle(self) -> bool:
        return self.__is_online_battle

    @property
    def attacking_ship_id(self) -> int:
        return self.__attacking_ship_id

    @property
    def defender_win_rewards(self) -> str:
        return self.__defender_win_rewards

    @property
    def defending_user_trophy(self) -> int:
        return self.__defending_user_trophy

    @property
    def outcome_type(self) -> str:
        return self.__outcome_type

    @property
    def defending_ship_name(self) -> str:
        return self.__defending_ship_name

    @property
    def defending_client_outcome_type(self) -> str:
        return self.__defending_client_outcome_type

    @property
    def client_outcome_type(self) -> str:
        return self.__client_outcome_type

    @property
    def win_minerals_result(self) -> int:
        return self.__win_minerals_result

    @property
    def defending_alliance_id(self) -> int:
        return self.__defending_alliance_id

    @property
    def win_rewards(self) -> str:
        return self.__win_rewards

    @property
    def station_ship_design_id(self) -> int:
        return self.__station_ship_design_id

    @property
    def defending_alliance_name(self) -> str:
        return self.__defending_alliance_name

    @property
    def attacking_alliance_id(self) -> int:
        return self.__attacking_alliance_id

    @property
    def client_end_frame(self) -> int:
        return self.__client_end_frame

    @property
    def defending_client_end_frame(self) -> int:
        return self.__defending_client_end_frame

    @property
    def commands(self) -> str:
        return self.__commands

    @property
    def attacking_alliance_sprite_id(self) -> int:
        return self.__attacking_alliance_sprite_id

    @property
    def battle_id(self) -> int:
        return self.__battle_id

    @property
    def attacking_alliance_name(self) -> str:
        return self.__attacking_alliance_name

    @property
    def defending_ship_xml(self) -> str:
        return self.__defending_ship_xml

    @property
    def attacker_base_win_rewards(self) -> str:
        return self.__attacker_base_win_rewards

    @property
    def lose_minerals_result(self) -> int:
        return self.__lose_minerals_result

    @property
    def attacking_user_id(self) -> int:
        return self.__attacking_user_id

    @property
    def battle_end_frame(self) -> int:
        return self.__battle_end_frame

    @property
    def win_trophy_result(self) -> int:
        return self.__win_trophy_result

    @property
    def battle_type(self) -> str:
        return self.__battle_type

    @property
    def attacker_win_rewards(self) -> str:
        return self.__attacker_win_rewards

    @property
    def random_seed(self) -> int:
        return self.__random_seed

    @property
    def battle_end_date(self) -> datetime:
        return self.__battle_end_date

    @property
    def rewards(self) -> str:
        return self.__rewards

    @property
    def mission_design_id(self) -> int:
        return self.__mission_design_id
