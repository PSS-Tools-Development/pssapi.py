####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class UserRaw():
    XML_NODE_NAME: str = 'User'

    def __init__(self, user_info: _EntityInfo) -> None:
        self.__facebook_token: str = _parse.pss_str(user_info.get('FacebookToken'))
        self.__purchase_reward_points: int = _parse.pss_int(user_info.get('PurchaseRewardPoints'))
        self.__boost_end_date: datetime = _parse.pss_datetime(user_info.get('BoostEndDate'))
        self.__unlocked_ship_design_ids: str = _parse.pss_str(user_info.get('UnlockedShipDesignIds'))
        self.__activated_promotions: str = _parse.pss_str(user_info.get('ActivatedPromotions'))
        self.__last_catalog_purchase_date: datetime = _parse.pss_datetime(user_info.get('LastCatalogPurchaseDate'))
        self.__total_supply_donation: int = _parse.pss_int(user_info.get('TotalSupplyDonation'))
        self.__email: str = _parse.pss_str(user_info.get('Email'))
        self.__alliance_sprite_id: int = _parse.pss_int(user_info.get('AllianceSpriteId'))
        self.__tournament_bonus_score: int = _parse.pss_int(user_info.get('TournamentBonusScore'))
        self.__draws_used_today: int = _parse.pss_int(user_info.get('DrawsUsedToday'))
        self.__ship_design_id: int = _parse.pss_int(user_info.get('ShipDesignId'))
        self.__block_auth_attempts_until_date: datetime = _parse.pss_datetime(user_info.get('BlockAuthAttemptsUntilDate'))
        self.__hero_bonus_chance: int = _parse.pss_int(user_info.get('HeroBonusChance'))
        self.__pvp_attack_losses: int = _parse.pss_int(user_info.get('PVPAttackLosses'))
        self.__unlocked_skin_keys: str = _parse.pss_str(user_info.get('UnlockedSkinKeys'))
        self.__alliance_membership: str = _parse.pss_str(user_info.get('AllianceMembership'))
        self.__boost_amount: int = _parse.pss_int(user_info.get('BoostAmount'))
        self.__tutorial_status: int = _parse.pss_int(user_info.get('TutorialStatus'))
        self.__race_type: str = _parse.pss_str(user_info.get('RaceType'))
        self.__challenge_wins: int = _parse.pss_int(user_info.get('ChallengeWins'))
        self.__pvp_attack_draws: int = _parse.pss_int(user_info.get('PVPAttackDraws'))
        self.__last_vip_claim_date: datetime = _parse.pss_datetime(user_info.get('LastVipClaimDate'))
        self.__crew_received: int = _parse.pss_int(user_info.get('CrewReceived'))
        self.__cooldown_expiry: datetime = _parse.pss_datetime(user_info.get('CooldownExpiry'))
        self.__last_login_date: datetime = _parse.pss_datetime(user_info.get('LastLoginDate'))
        self.__challenge_losses: int = _parse.pss_int(user_info.get('ChallengeLosses'))
        self.__trophy: int = _parse.pss_int(user_info.get('Trophy'))
        self.__goole_play_auth_code: str = _parse.pss_str(user_info.get('GoolePlayAuthCode'))
        self.__alliance_score: int = _parse.pss_int(user_info.get('AllianceScore'))
        self.__situation_occurrences_today: int = _parse.pss_int(user_info.get('SituationOccurrencesToday'))
        self.__last_heart_beat_date: datetime = _parse.pss_datetime(user_info.get('LastHeartBeatDate'))
        self.__flags: int = _parse.pss_int(user_info.get('Flags'))
        self.__last_alert_date: datetime = _parse.pss_datetime(user_info.get('LastAlertDate'))
        self.__trophy_gained: int = _parse.pss_int(user_info.get('TrophyGained'))
        self.__highest_trophy: int = _parse.pss_int(user_info.get('HighestTrophy'))
        self.__creation_date: datetime = _parse.pss_datetime(user_info.get('CreationDate'))
        self.__update_date: datetime = _parse.pss_datetime(user_info.get('UpdateDate'))
        self.__user_type: str = _parse.pss_str(user_info.get('UserType'))
        self.__ranking: int = _parse.pss_int(user_info.get('Ranking'))
        self.__completed_mission_event_ids: str = _parse.pss_str(user_info.get('CompletedMissionEventIds'))
        self.__vip_expiry_date: datetime = _parse.pss_datetime(user_info.get('VipExpiryDate'))
        self.__matching_status: str = _parse.pss_str(user_info.get('MatchingStatus'))
        self.__name: str = _parse.pss_str(user_info.get('Name'))
        self.__gender_type: str = _parse.pss_str(user_info.get('GenderType'))
        self.__captain_character_design_id: int = _parse.pss_int(user_info.get('CaptainCharacterDesignId'))
        self.__status: int = _parse.pss_int(user_info.get('Status'))
        self.__alliance_name: str = _parse.pss_str(user_info.get('AllianceName'))
        self.__pvp_attack_wins: int = _parse.pss_int(user_info.get('PVPAttackWins'))
        self.__last_reward_action_date: datetime = _parse.pss_datetime(user_info.get('LastRewardActionDate'))
        self.__championship_score: int = _parse.pss_int(user_info.get('ChampionshipScore'))
        self.__daily_pvp_attacks: int = _parse.pss_int(user_info.get('DailyPVPAttacks'))
        self.__alliance_join_date: datetime = _parse.pss_datetime(user_info.get('AllianceJoinDate'))
        self.__google_play_id_token: str = _parse.pss_str(user_info.get('GooglePlayIdToken'))
        self.__crew_donated: int = _parse.pss_int(user_info.get('CrewDonated'))
        self.__facebook_token_expiry_date: datetime = _parse.pss_datetime(user_info.get('FacebookTokenExpiryDate'))
        self.__free_starbux_received_today: int = _parse.pss_int(user_info.get('FreeStarbuxReceivedToday'))
        self.__explored_star_system_ids: str = _parse.pss_str(user_info.get('ExploredStarSystemIds'))
        self.__tip_status: int = _parse.pss_int(user_info.get('TipStatus'))
        self.__pass_points: int = _parse.pss_int(user_info.get('PassPoints'))
        self.__challenge_design_id: int = _parse.pss_int(user_info.get('ChallengeDesignId'))
        self.__unread_message_count: int = _parse.pss_int(user_info.get('UnreadMessageCount'))
        self.__rewards_collectable: bool = _parse.pss_bool(user_info.get('RewardsCollectable'))
        self.__league_type: str = _parse.pss_str(user_info.get('LeagueType'))
        self.__pvp_defence_wins: int = _parse.pss_int(user_info.get('PVPDefenceWins'))
        self.__loading_percentage: int = _parse.pss_int(user_info.get('LoadingPercentage'))
        self.__pvp_defence_losses: int = _parse.pss_int(user_info.get('PVPDefenceLosses'))
        self.__daily_missions_attempted: str = _parse.pss_str(user_info.get('DailyMissionsAttempted'))
        self.__unlocked_character_design_ids: str = _parse.pss_str(user_info.get('UnlockedCharacterDesignIds'))
        self.__daily_pv_p_defence: int = _parse.pss_int(user_info.get('DailyPvPDefence'))
        self.__used_reward_points: int = _parse.pss_int(user_info.get('UsedRewardPoints'))
        self.__icon_sprite_id: int = _parse.pss_int(user_info.get('IconSpriteId'))
        self.__id: int = _parse.pss_int(user_info.get('Id'))
        self.__language_key: str = _parse.pss_str(user_info.get('LanguageKey'))
        self.__last_purchase_date: datetime = _parse.pss_datetime(user_info.get('LastPurchaseDate'))
        self.__tournament_reward_points: int = _parse.pss_int(user_info.get('TournamentRewardPoints'))
        self.__last_boost_date: datetime = _parse.pss_datetime(user_info.get('LastBoostDate'))
        self.__credits: int = _parse.pss_int(user_info.get('Credits'))
        self.__owner_user_id: int = _parse.pss_int(user_info.get('OwnerUserId'))
        self.__completed_mission_designs: str = _parse.pss_str(user_info.get('CompletedMissionDesigns'))
        self.__alliance_qualify_division_design_id: int = _parse.pss_int(user_info.get('AllianceQualifyDivisionDesignId'))
        self.__game_center_name: str = _parse.pss_str(user_info.get('GameCenterName'))
        self.__profile_image_url: str = _parse.pss_str(user_info.get('ProfileImageUrl'))
        self.__daily_challenge_win_streak: int = _parse.pss_int(user_info.get('DailyChallengeWinStreak'))
        self.__pvp_defence_draws: int = _parse.pss_int(user_info.get('PVPDefenceDraws'))
        self.__last_challenge_design_id: int = _parse.pss_int(user_info.get('LastChallengeDesignId'))
        self.__alliance_supply_donation: int = _parse.pss_int(user_info.get('AllianceSupplyDonation'))
        self.__chat_appearance: int = _parse.pss_int(user_info.get('ChatAppearance'))
        self.__email_verification_status: str = _parse.pss_str(user_info.get('EmailVerificationStatus'))
        self.__task_reroll_count: int = _parse.pss_int(user_info.get('TaskRerollCount'))
        self.__game_center_friend_count: int = _parse.pss_int(user_info.get('GameCenterFriendCount'))
        self.__daily_reward_status: int = _parse.pss_int(user_info.get('DailyRewardStatus'))
        self.__google_play_name: str = _parse.pss_str(user_info.get('GooglePlayName'))
        self.__tournament_reset_date: datetime = _parse.pss_datetime(user_info.get('TournamentResetDate'))
        self.__alliance_id: int = _parse.pss_int(user_info.get('AllianceId'))
        self.__authentication_type: str = _parse.pss_str(user_info.get('AuthenticationType'))

    @property
    def facebook_token(self) -> str:
        return self.__facebook_token

    @property
    def purchase_reward_points(self) -> int:
        return self.__purchase_reward_points

    @property
    def boost_end_date(self) -> datetime:
        return self.__boost_end_date

    @property
    def unlocked_ship_design_ids(self) -> str:
        return self.__unlocked_ship_design_ids

    @property
    def activated_promotions(self) -> str:
        return self.__activated_promotions

    @property
    def last_catalog_purchase_date(self) -> datetime:
        return self.__last_catalog_purchase_date

    @property
    def total_supply_donation(self) -> int:
        return self.__total_supply_donation

    @property
    def email(self) -> str:
        return self.__email

    @property
    def alliance_sprite_id(self) -> int:
        return self.__alliance_sprite_id

    @property
    def tournament_bonus_score(self) -> int:
        return self.__tournament_bonus_score

    @property
    def draws_used_today(self) -> int:
        return self.__draws_used_today

    @property
    def ship_design_id(self) -> int:
        return self.__ship_design_id

    @property
    def block_auth_attempts_until_date(self) -> datetime:
        return self.__block_auth_attempts_until_date

    @property
    def hero_bonus_chance(self) -> int:
        return self.__hero_bonus_chance

    @property
    def pvp_attack_losses(self) -> int:
        return self.__pvp_attack_losses

    @property
    def unlocked_skin_keys(self) -> str:
        return self.__unlocked_skin_keys

    @property
    def alliance_membership(self) -> str:
        return self.__alliance_membership

    @property
    def boost_amount(self) -> int:
        return self.__boost_amount

    @property
    def tutorial_status(self) -> int:
        return self.__tutorial_status

    @property
    def race_type(self) -> str:
        return self.__race_type

    @property
    def challenge_wins(self) -> int:
        return self.__challenge_wins

    @property
    def pvp_attack_draws(self) -> int:
        return self.__pvp_attack_draws

    @property
    def last_vip_claim_date(self) -> datetime:
        return self.__last_vip_claim_date

    @property
    def crew_received(self) -> int:
        return self.__crew_received

    @property
    def cooldown_expiry(self) -> datetime:
        return self.__cooldown_expiry

    @property
    def last_login_date(self) -> datetime:
        return self.__last_login_date

    @property
    def challenge_losses(self) -> int:
        return self.__challenge_losses

    @property
    def trophy(self) -> int:
        return self.__trophy

    @property
    def goole_play_auth_code(self) -> str:
        return self.__goole_play_auth_code

    @property
    def alliance_score(self) -> int:
        return self.__alliance_score

    @property
    def situation_occurrences_today(self) -> int:
        return self.__situation_occurrences_today

    @property
    def last_heart_beat_date(self) -> datetime:
        return self.__last_heart_beat_date

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def last_alert_date(self) -> datetime:
        return self.__last_alert_date

    @property
    def trophy_gained(self) -> int:
        return self.__trophy_gained

    @property
    def highest_trophy(self) -> int:
        return self.__highest_trophy

    @property
    def creation_date(self) -> datetime:
        return self.__creation_date

    @property
    def update_date(self) -> datetime:
        return self.__update_date

    @property
    def user_type(self) -> str:
        return self.__user_type

    @property
    def ranking(self) -> int:
        return self.__ranking

    @property
    def completed_mission_event_ids(self) -> str:
        return self.__completed_mission_event_ids

    @property
    def vip_expiry_date(self) -> datetime:
        return self.__vip_expiry_date

    @property
    def matching_status(self) -> str:
        return self.__matching_status

    @property
    def name(self) -> str:
        return self.__name

    @property
    def gender_type(self) -> str:
        return self.__gender_type

    @property
    def captain_character_design_id(self) -> int:
        return self.__captain_character_design_id

    @property
    def status(self) -> int:
        return self.__status

    @property
    def alliance_name(self) -> str:
        return self.__alliance_name

    @property
    def pvp_attack_wins(self) -> int:
        return self.__pvp_attack_wins

    @property
    def last_reward_action_date(self) -> datetime:
        return self.__last_reward_action_date

    @property
    def championship_score(self) -> int:
        return self.__championship_score

    @property
    def daily_pvp_attacks(self) -> int:
        return self.__daily_pvp_attacks

    @property
    def alliance_join_date(self) -> datetime:
        return self.__alliance_join_date

    @property
    def google_play_id_token(self) -> str:
        return self.__google_play_id_token

    @property
    def crew_donated(self) -> int:
        return self.__crew_donated

    @property
    def facebook_token_expiry_date(self) -> datetime:
        return self.__facebook_token_expiry_date

    @property
    def free_starbux_received_today(self) -> int:
        return self.__free_starbux_received_today

    @property
    def explored_star_system_ids(self) -> str:
        return self.__explored_star_system_ids

    @property
    def tip_status(self) -> int:
        return self.__tip_status

    @property
    def pass_points(self) -> int:
        return self.__pass_points

    @property
    def challenge_design_id(self) -> int:
        return self.__challenge_design_id

    @property
    def unread_message_count(self) -> int:
        return self.__unread_message_count

    @property
    def rewards_collectable(self) -> bool:
        return self.__rewards_collectable

    @property
    def league_type(self) -> str:
        return self.__league_type

    @property
    def pvp_defence_wins(self) -> int:
        return self.__pvp_defence_wins

    @property
    def loading_percentage(self) -> int:
        return self.__loading_percentage

    @property
    def pvp_defence_losses(self) -> int:
        return self.__pvp_defence_losses

    @property
    def daily_missions_attempted(self) -> str:
        return self.__daily_missions_attempted

    @property
    def unlocked_character_design_ids(self) -> str:
        return self.__unlocked_character_design_ids

    @property
    def daily_pv_p_defence(self) -> int:
        return self.__daily_pv_p_defence

    @property
    def used_reward_points(self) -> int:
        return self.__used_reward_points

    @property
    def icon_sprite_id(self) -> int:
        return self.__icon_sprite_id

    @property
    def id(self) -> int:
        return self.__id

    @property
    def language_key(self) -> str:
        return self.__language_key

    @property
    def last_purchase_date(self) -> datetime:
        return self.__last_purchase_date

    @property
    def tournament_reward_points(self) -> int:
        return self.__tournament_reward_points

    @property
    def last_boost_date(self) -> datetime:
        return self.__last_boost_date

    @property
    def credits(self) -> int:
        return self.__credits

    @property
    def owner_user_id(self) -> int:
        return self.__owner_user_id

    @property
    def completed_mission_designs(self) -> str:
        return self.__completed_mission_designs

    @property
    def alliance_qualify_division_design_id(self) -> int:
        return self.__alliance_qualify_division_design_id

    @property
    def game_center_name(self) -> str:
        return self.__game_center_name

    @property
    def profile_image_url(self) -> str:
        return self.__profile_image_url

    @property
    def daily_challenge_win_streak(self) -> int:
        return self.__daily_challenge_win_streak

    @property
    def pvp_defence_draws(self) -> int:
        return self.__pvp_defence_draws

    @property
    def last_challenge_design_id(self) -> int:
        return self.__last_challenge_design_id

    @property
    def alliance_supply_donation(self) -> int:
        return self.__alliance_supply_donation

    @property
    def chat_appearance(self) -> int:
        return self.__chat_appearance

    @property
    def email_verification_status(self) -> str:
        return self.__email_verification_status

    @property
    def task_reroll_count(self) -> int:
        return self.__task_reroll_count

    @property
    def game_center_friend_count(self) -> int:
        return self.__game_center_friend_count

    @property
    def daily_reward_status(self) -> int:
        return self.__daily_reward_status

    @property
    def google_play_name(self) -> str:
        return self.__google_play_name

    @property
    def tournament_reset_date(self) -> datetime:
        return self.__tournament_reset_date

    @property
    def alliance_id(self) -> int:
        return self.__alliance_id

    @property
    def authentication_type(self) -> str:
        return self.__authentication_type