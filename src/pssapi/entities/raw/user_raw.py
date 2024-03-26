"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

import pssapi.entities as _entities

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw


class UserRaw(EntityBaseRaw):
    XML_NODE_NAME: str = "User"

    def __init__(self, user_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._activated_promotions: str = _parse.pss_str(user_info.pop("ActivatedPromotions", None))
        self._ads_platform_user_id: str = _parse.pss_str(user_info.pop("AdsPlatformUserId", None))
        self._alliance: _entities.Alliance = _entities.Alliance(user_info.pop("Alliance")[0]) if user_info.get("Alliance", []) else None
        self._alliance_id: int = _parse.pss_int(user_info.pop("AllianceId", None))
        self._alliance_join_date: _datetime = _parse.pss_datetime(user_info.pop("AllianceJoinDate", None))
        self._alliance_membership: str = _parse.pss_str(user_info.pop("AllianceMembership", None))
        self._alliance_name: str = _parse.pss_str(user_info.pop("AllianceName", None))
        self._alliance_qualify_division_design_id: int = _parse.pss_int(user_info.pop("AllianceQualifyDivisionDesignId", None))
        self._alliance_score: int = _parse.pss_int(user_info.pop("AllianceScore", None))
        self._alliance_sprite_id: int = _parse.pss_int(user_info.pop("AllianceSpriteId", None))
        self._alliance_supply_donation: int = _parse.pss_int(user_info.pop("AllianceSupplyDonation", None))
        self._authentication_type: str = _parse.pss_str(user_info.pop("AuthenticationType", None))
        self._block_auth_attempts_until_date: _datetime = _parse.pss_datetime(user_info.pop("BlockAuthAttemptsUntilDate", None))
        self._boost_amount: int = _parse.pss_int(user_info.pop("BoostAmount", None))
        self._boost_end_date: _datetime = _parse.pss_datetime(user_info.pop("BoostEndDate", None))
        self._captain_character_design_id: int = _parse.pss_int(user_info.pop("CaptainCharacterDesignId", None))
        self._challenge_design_id: int = _parse.pss_int(user_info.pop("ChallengeDesignId", None))
        self._challenge_losses: int = _parse.pss_int(user_info.pop("ChallengeLosses", None))
        self._challenge_wins: int = _parse.pss_int(user_info.pop("ChallengeWins", None))
        self._championship_score: int = _parse.pss_int(user_info.pop("ChampionshipScore", None))
        self._chat_appearance: int = _parse.pss_int(user_info.pop("ChatAppearance", None))
        self._completed_mission_designs: str = _parse.pss_str(user_info.pop("CompletedMissionDesigns", None))
        self._completed_mission_event_ids: str = _parse.pss_str(user_info.pop("CompletedMissionEventIds", None))
        self._cooldown_expiry: _datetime = _parse.pss_datetime(user_info.pop("CooldownExpiry", None))
        self._creation_date: _datetime = _parse.pss_datetime(user_info.pop("CreationDate", None))
        self._credits: str = _parse.pss_str(user_info.pop("Credits", None))
        self._crew_donated: int = _parse.pss_int(user_info.pop("CrewDonated", None))
        self._crew_received: int = _parse.pss_int(user_info.pop("CrewReceived", None))
        self._daily_challenge_win_streak: int = _parse.pss_int(user_info.pop("DailyChallengeWinStreak", None))
        self._daily_heartbeat_seconds: int = _parse.pss_int(user_info.pop("DailyHeartbeatSeconds", None))
        self._daily_missions_attempted: str = _parse.pss_str(user_info.pop("DailyMissionsAttempted", None))
        self._daily_pvp_attacks: int = _parse.pss_int(user_info.pop("DailyPVPAttacks", None))
        self._daily_pv_p_defence: int = _parse.pss_int(user_info.pop("DailyPvPDefence", None))
        self._daily_reward_status: int = _parse.pss_int(user_info.pop("DailyRewardStatus", None))
        self._draws_used_today: int = _parse.pss_int(user_info.pop("DrawsUsedToday", None))
        self._email: str = _parse.pss_str(user_info.pop("Email", None))
        self._email_verification_status: str = _parse.pss_str(user_info.pop("EmailVerificationStatus", None))
        self._explored_star_system_ids: str = _parse.pss_str(user_info.pop("ExploredStarSystemIds", None))
        self._facebook_token: str = _parse.pss_str(user_info.pop("FacebookToken", None))
        self._facebook_token_expiry_date: _datetime = _parse.pss_datetime(user_info.pop("FacebookTokenExpiryDate", None))
        self._flags: int = _parse.pss_int(user_info.pop("Flags", None))
        self._free_starbux_received_today: int = _parse.pss_int(user_info.pop("FreeStarbuxReceivedToday", None))
        self._game_center_friend_count: int = _parse.pss_int(user_info.pop("GameCenterFriendCount", None))
        self._game_center_name: str = _parse.pss_str(user_info.pop("GameCenterName", None))
        self._gender_type: str = _parse.pss_str(user_info.pop("GenderType", None))
        self._google_play_access_token_expiry_date: _datetime = _parse.pss_datetime(user_info.pop("GooglePlayAccessTokenExpiryDate", None))
        self._google_play_id_token: str = _parse.pss_str(user_info.pop("GooglePlayIdToken", None))
        self._google_play_name: str = _parse.pss_str(user_info.pop("GooglePlayName", None))
        self._goole_play_auth_code: str = _parse.pss_str(user_info.pop("GoolePlayAuthCode", None))
        self._hero_bonus_chance: int = _parse.pss_int(user_info.pop("HeroBonusChance", None))
        self._highest_trophy: int = _parse.pss_int(user_info.pop("HighestTrophy", None))
        self._icon_sprite_id: int = _parse.pss_int(user_info.pop("IconSpriteId", None))
        self._id_: int = _parse.pss_int(user_info.pop("Id", None))
        self._is_under_age: bool = _parse.pss_bool(user_info.pop("IsUnderAge", None))
        self._language_key: str = _parse.pss_str(user_info.pop("LanguageKey", None))
        self._last_alert_date: str = _parse.pss_str(user_info.pop("LastAlertDate", None))
        self._last_boost_date: _datetime = _parse.pss_datetime(user_info.pop("LastBoostDate", None))
        self._last_catalog_purchase_date: _datetime = _parse.pss_datetime(user_info.pop("LastCatalogPurchaseDate", None))
        self._last_challenge_design_id: int = _parse.pss_int(user_info.pop("LastChallengeDesignId", None))
        self._last_heart_beat_date: _datetime = _parse.pss_datetime(user_info.pop("LastHeartBeatDate", None))
        self._last_login_date: _datetime = _parse.pss_datetime(user_info.pop("LastLoginDate", None))
        self._last_purchase_date: _datetime = _parse.pss_datetime(user_info.pop("LastPurchaseDate", None))
        self._last_reward_action_date: _datetime = _parse.pss_datetime(user_info.pop("LastRewardActionDate", None))
        self._last_vip_claim_date: _datetime = _parse.pss_datetime(user_info.pop("LastVipClaimDate", None))
        self._league_type: str = _parse.pss_str(user_info.pop("LeagueType", None))
        self._loading_percentage: int = _parse.pss_int(user_info.pop("LoadingPercentage", None))
        self._matching_status: str = _parse.pss_str(user_info.pop("MatchingStatus", None))
        self._name: str = _parse.pss_str(user_info.pop("Name", None))
        self._nowgg_user_id: str = _parse.pss_str(user_info.pop("NowggUserId", None))
        self._owner_user_id: int = _parse.pss_int(user_info.pop("OwnerUserId", None))
        self._pvp_attack_draws: int = _parse.pss_int(user_info.pop("PVPAttackDraws", None))
        self._pvp_attack_losses: int = _parse.pss_int(user_info.pop("PVPAttackLosses", None))
        self._pvp_attack_wins: int = _parse.pss_int(user_info.pop("PVPAttackWins", None))
        self._pvp_defence_draws: int = _parse.pss_int(user_info.pop("PVPDefenceDraws", None))
        self._pvp_defence_losses: int = _parse.pss_int(user_info.pop("PVPDefenceLosses", None))
        self._pvp_defence_wins: int = _parse.pss_int(user_info.pop("PVPDefenceWins", None))
        self._pass_points: int = _parse.pss_int(user_info.pop("PassPoints", None))
        self._profile_image_url: str = _parse.pss_str(user_info.pop("ProfileImageUrl", None))
        self._purchase_reward_points: int = _parse.pss_int(user_info.pop("PurchaseRewardPoints", None))
        self._race_type: str = _parse.pss_str(user_info.pop("RaceType", None))
        self._ranking: int = _parse.pss_int(user_info.pop("Ranking", None))
        self._rewards_collectable: bool = _parse.pss_bool(user_info.pop("RewardsCollectable", None))
        self._rewards_collectable_amount: int = _parse.pss_int(user_info.pop("RewardsCollectableAmount", None))
        self._ship_design_id: int = _parse.pss_int(user_info.pop("ShipDesignId", None))
        self._situation_occurrences: str = _parse.pss_str(user_info.pop("SituationOccurrences", None))
        self._situation_occurrences_today: int = _parse.pss_int(user_info.pop("SituationOccurrencesToday", None))
        self._status: int = _parse.pss_int(user_info.pop("Status", None))
        self._steam_id: str = _parse.pss_str(user_info.pop("SteamId", None))
        self._task_reroll_count: int = _parse.pss_int(user_info.pop("TaskRerollCount", None))
        self._tip_status: int = _parse.pss_int(user_info.pop("TipStatus", None))
        self._total_supply_donation: int = _parse.pss_int(user_info.pop("TotalSupplyDonation", None))
        self._tournament_bonus_score: int = _parse.pss_int(user_info.pop("TournamentBonusScore", None))
        self._tournament_reset_date: _datetime = _parse.pss_datetime(user_info.pop("TournamentResetDate", None))
        self._tournament_reward_points: int = _parse.pss_int(user_info.pop("TournamentRewardPoints", None))
        self._trail_user_id: str = _parse.pss_str(user_info.pop("TrailUserId", None))
        self._trophy: int = _parse.pss_int(user_info.pop("Trophy", None))
        self._trophy_gained: int = _parse.pss_int(user_info.pop("TrophyGained", None))
        self._tutorial_status: int = _parse.pss_int(user_info.pop("TutorialStatus", None))
        self._unlocked_character_design_ids: str = _parse.pss_str(user_info.pop("UnlockedCharacterDesignIds", None))
        self._unlocked_ship_design_ids: str = _parse.pss_str(user_info.pop("UnlockedShipDesignIds", None))
        self._unlocked_skin_keys: str = _parse.pss_str(user_info.pop("UnlockedSkinKeys", None))
        self._unread_message_count: str = _parse.pss_str(user_info.pop("UnreadMessageCount", None))
        self._update_date: _datetime = _parse.pss_datetime(user_info.pop("UpdateDate", None))
        self._used_reward_points: int = _parse.pss_int(user_info.pop("UsedRewardPoints", None))
        self._user_season: _entities.UserSeason = _entities.UserSeason(user_info.pop("UserSeason")[0]) if user_info.get("UserSeason", []) else None
        self._user_source_ads_platform_type: str = _parse.pss_str(user_info.pop("UserSourceAdsPlatformType", None))
        self._user_type: str = _parse.pss_str(user_info.pop("UserType", None))
        self._vip_expiry_date: _datetime = _parse.pss_datetime(user_info.pop("VipExpiryDate", None))
        super().__init__(user_info)

    @property
    def activated_promotions(self) -> str:
        return self._activated_promotions

    @property
    def ads_platform_user_id(self) -> str:
        return self._ads_platform_user_id

    @property
    def alliance(self) -> "_entities.Alliance":
        return self._alliance

    @property
    def alliance_id(self) -> int:
        return self._alliance_id

    @property
    def alliance_join_date(self) -> _datetime:
        return self._alliance_join_date

    @property
    def alliance_membership(self) -> str:
        return self._alliance_membership

    @property
    def alliance_name(self) -> str:
        return self._alliance_name

    @property
    def alliance_qualify_division_design_id(self) -> int:
        return self._alliance_qualify_division_design_id

    @property
    def alliance_score(self) -> int:
        return self._alliance_score

    @property
    def alliance_sprite_id(self) -> int:
        return self._alliance_sprite_id

    @property
    def alliance_supply_donation(self) -> int:
        return self._alliance_supply_donation

    @property
    def authentication_type(self) -> str:
        return self._authentication_type

    @property
    def block_auth_attempts_until_date(self) -> _datetime:
        return self._block_auth_attempts_until_date

    @property
    def boost_amount(self) -> int:
        return self._boost_amount

    @property
    def boost_end_date(self) -> _datetime:
        return self._boost_end_date

    @property
    def captain_character_design_id(self) -> int:
        return self._captain_character_design_id

    @property
    def challenge_design_id(self) -> int:
        return self._challenge_design_id

    @property
    def challenge_losses(self) -> int:
        return self._challenge_losses

    @property
    def challenge_wins(self) -> int:
        return self._challenge_wins

    @property
    def championship_score(self) -> int:
        return self._championship_score

    @property
    def chat_appearance(self) -> int:
        return self._chat_appearance

    @property
    def completed_mission_designs(self) -> str:
        return self._completed_mission_designs

    @property
    def completed_mission_event_ids(self) -> str:
        return self._completed_mission_event_ids

    @property
    def cooldown_expiry(self) -> _datetime:
        return self._cooldown_expiry

    @property
    def creation_date(self) -> _datetime:
        return self._creation_date

    @property
    def credits(self) -> str:
        return self._credits

    @property
    def crew_donated(self) -> int:
        return self._crew_donated

    @property
    def crew_received(self) -> int:
        return self._crew_received

    @property
    def daily_challenge_win_streak(self) -> int:
        return self._daily_challenge_win_streak

    @property
    def daily_heartbeat_seconds(self) -> int:
        return self._daily_heartbeat_seconds

    @property
    def daily_missions_attempted(self) -> str:
        return self._daily_missions_attempted

    @property
    def daily_pvp_attacks(self) -> int:
        return self._daily_pvp_attacks

    @property
    def daily_pv_p_defence(self) -> int:
        return self._daily_pv_p_defence

    @property
    def daily_reward_status(self) -> int:
        return self._daily_reward_status

    @property
    def draws_used_today(self) -> int:
        return self._draws_used_today

    @property
    def email(self) -> str:
        return self._email

    @property
    def email_verification_status(self) -> str:
        return self._email_verification_status

    @property
    def explored_star_system_ids(self) -> str:
        return self._explored_star_system_ids

    @property
    def facebook_token(self) -> str:
        return self._facebook_token

    @property
    def facebook_token_expiry_date(self) -> _datetime:
        return self._facebook_token_expiry_date

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def free_starbux_received_today(self) -> int:
        return self._free_starbux_received_today

    @property
    def game_center_friend_count(self) -> int:
        return self._game_center_friend_count

    @property
    def game_center_name(self) -> str:
        return self._game_center_name

    @property
    def gender_type(self) -> str:
        return self._gender_type

    @property
    def google_play_access_token_expiry_date(self) -> _datetime:
        return self._google_play_access_token_expiry_date

    @property
    def google_play_id_token(self) -> str:
        return self._google_play_id_token

    @property
    def google_play_name(self) -> str:
        return self._google_play_name

    @property
    def goole_play_auth_code(self) -> str:
        return self._goole_play_auth_code

    @property
    def hero_bonus_chance(self) -> int:
        return self._hero_bonus_chance

    @property
    def highest_trophy(self) -> int:
        return self._highest_trophy

    @property
    def icon_sprite_id(self) -> int:
        return self._icon_sprite_id

    @property
    def id_(self) -> int:
        return self._id_

    @property
    def is_under_age(self) -> bool:
        return self._is_under_age

    @property
    def language_key(self) -> str:
        return self._language_key

    @property
    def last_alert_date(self) -> str:
        return self._last_alert_date

    @property
    def last_boost_date(self) -> _datetime:
        return self._last_boost_date

    @property
    def last_catalog_purchase_date(self) -> _datetime:
        return self._last_catalog_purchase_date

    @property
    def last_challenge_design_id(self) -> int:
        return self._last_challenge_design_id

    @property
    def last_heart_beat_date(self) -> _datetime:
        return self._last_heart_beat_date

    @property
    def last_login_date(self) -> _datetime:
        return self._last_login_date

    @property
    def last_purchase_date(self) -> _datetime:
        return self._last_purchase_date

    @property
    def last_reward_action_date(self) -> _datetime:
        return self._last_reward_action_date

    @property
    def last_vip_claim_date(self) -> _datetime:
        return self._last_vip_claim_date

    @property
    def league_type(self) -> str:
        return self._league_type

    @property
    def loading_percentage(self) -> int:
        return self._loading_percentage

    @property
    def matching_status(self) -> str:
        return self._matching_status

    @property
    def name(self) -> str:
        return self._name

    @property
    def nowgg_user_id(self) -> str:
        return self._nowgg_user_id

    @property
    def owner_user_id(self) -> int:
        return self._owner_user_id

    @property
    def pvp_attack_draws(self) -> int:
        return self._pvp_attack_draws

    @property
    def pvp_attack_losses(self) -> int:
        return self._pvp_attack_losses

    @property
    def pvp_attack_wins(self) -> int:
        return self._pvp_attack_wins

    @property
    def pvp_defence_draws(self) -> int:
        return self._pvp_defence_draws

    @property
    def pvp_defence_losses(self) -> int:
        return self._pvp_defence_losses

    @property
    def pvp_defence_wins(self) -> int:
        return self._pvp_defence_wins

    @property
    def pass_points(self) -> int:
        return self._pass_points

    @property
    def profile_image_url(self) -> str:
        return self._profile_image_url

    @property
    def purchase_reward_points(self) -> int:
        return self._purchase_reward_points

    @property
    def race_type(self) -> str:
        return self._race_type

    @property
    def ranking(self) -> int:
        return self._ranking

    @property
    def rewards_collectable(self) -> bool:
        return self._rewards_collectable

    @property
    def rewards_collectable_amount(self) -> int:
        return self._rewards_collectable_amount

    @property
    def ship_design_id(self) -> int:
        return self._ship_design_id

    @property
    def situation_occurrences(self) -> str:
        return self._situation_occurrences

    @property
    def situation_occurrences_today(self) -> int:
        return self._situation_occurrences_today

    @property
    def status(self) -> int:
        return self._status

    @property
    def steam_id(self) -> str:
        return self._steam_id

    @property
    def task_reroll_count(self) -> int:
        return self._task_reroll_count

    @property
    def tip_status(self) -> int:
        return self._tip_status

    @property
    def total_supply_donation(self) -> int:
        return self._total_supply_donation

    @property
    def tournament_bonus_score(self) -> int:
        return self._tournament_bonus_score

    @property
    def tournament_reset_date(self) -> _datetime:
        return self._tournament_reset_date

    @property
    def tournament_reward_points(self) -> int:
        return self._tournament_reward_points

    @property
    def trail_user_id(self) -> str:
        return self._trail_user_id

    @property
    def trophy(self) -> int:
        return self._trophy

    @property
    def trophy_gained(self) -> int:
        return self._trophy_gained

    @property
    def tutorial_status(self) -> int:
        return self._tutorial_status

    @property
    def unlocked_character_design_ids(self) -> str:
        return self._unlocked_character_design_ids

    @property
    def unlocked_ship_design_ids(self) -> str:
        return self._unlocked_ship_design_ids

    @property
    def unlocked_skin_keys(self) -> str:
        return self._unlocked_skin_keys

    @property
    def unread_message_count(self) -> str:
        return self._unread_message_count

    @property
    def update_date(self) -> _datetime:
        return self._update_date

    @property
    def used_reward_points(self) -> int:
        return self._used_reward_points

    @property
    def user_season(self) -> "_entities.UserSeason":
        return self._user_season

    @property
    def user_source_ads_platform_type(self) -> str:
        return self._user_source_ads_platform_type

    @property
    def user_type(self) -> str:
        return self._user_type

    @property
    def vip_expiry_date(self) -> _datetime:
        return self._vip_expiry_date

    def _key(self):
        return (
            self.activated_promotions,
            self.ads_platform_user_id,
            self.alliance._key() if self.alliance else None,
            self.alliance_id,
            self.alliance_join_date,
            self.alliance_membership,
            self.alliance_name,
            self.alliance_qualify_division_design_id,
            self.alliance_score,
            self.alliance_sprite_id,
            self.alliance_supply_donation,
            self.authentication_type,
            self.block_auth_attempts_until_date,
            self.boost_amount,
            self.boost_end_date,
            self.captain_character_design_id,
            self.challenge_design_id,
            self.challenge_losses,
            self.challenge_wins,
            self.championship_score,
            self.chat_appearance,
            self.completed_mission_designs,
            self.completed_mission_event_ids,
            self.cooldown_expiry,
            self.creation_date,
            self.credits,
            self.crew_donated,
            self.crew_received,
            self.daily_challenge_win_streak,
            self.daily_heartbeat_seconds,
            self.daily_missions_attempted,
            self.daily_pvp_attacks,
            self.daily_pv_p_defence,
            self.daily_reward_status,
            self.draws_used_today,
            self.email,
            self.email_verification_status,
            self.explored_star_system_ids,
            self.facebook_token,
            self.facebook_token_expiry_date,
            self.flags,
            self.free_starbux_received_today,
            self.game_center_friend_count,
            self.game_center_name,
            self.gender_type,
            self.google_play_access_token_expiry_date,
            self.google_play_id_token,
            self.google_play_name,
            self.goole_play_auth_code,
            self.hero_bonus_chance,
            self.highest_trophy,
            self.icon_sprite_id,
            self.id_,
            self.is_under_age,
            self.language_key,
            self.last_alert_date,
            self.last_boost_date,
            self.last_catalog_purchase_date,
            self.last_challenge_design_id,
            self.last_heart_beat_date,
            self.last_login_date,
            self.last_purchase_date,
            self.last_reward_action_date,
            self.last_vip_claim_date,
            self.league_type,
            self.loading_percentage,
            self.matching_status,
            self.name,
            self.nowgg_user_id,
            self.owner_user_id,
            self.pvp_attack_draws,
            self.pvp_attack_losses,
            self.pvp_attack_wins,
            self.pvp_defence_draws,
            self.pvp_defence_losses,
            self.pvp_defence_wins,
            self.pass_points,
            self.profile_image_url,
            self.purchase_reward_points,
            self.race_type,
            self.ranking,
            self.rewards_collectable,
            self.rewards_collectable_amount,
            self.ship_design_id,
            self.situation_occurrences,
            self.situation_occurrences_today,
            self.status,
            self.steam_id,
            self.task_reroll_count,
            self.tip_status,
            self.total_supply_donation,
            self.tournament_bonus_score,
            self.tournament_reset_date,
            self.tournament_reward_points,
            self.trail_user_id,
            self.trophy,
            self.trophy_gained,
            self.tutorial_status,
            self.unlocked_character_design_ids,
            self.unlocked_ship_design_ids,
            self.unlocked_skin_keys,
            self.unread_message_count,
            self.update_date,
            self.used_reward_points,
            self.user_season._key() if self.user_season else None,
            self.user_source_ads_platform_type,
            self.user_type,
            self.vip_expiry_date,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ActivatedPromotions": self.activated_promotions,
                "AdsPlatformUserId": self.ads_platform_user_id,
                "Alliance": dict(self.alliance) if self.alliance else None,
                "AllianceId": self.alliance_id,
                "AllianceJoinDate": self.alliance_join_date,
                "AllianceMembership": self.alliance_membership,
                "AllianceName": self.alliance_name,
                "AllianceQualifyDivisionDesignId": self.alliance_qualify_division_design_id,
                "AllianceScore": self.alliance_score,
                "AllianceSpriteId": self.alliance_sprite_id,
                "AllianceSupplyDonation": self.alliance_supply_donation,
                "AuthenticationType": self.authentication_type,
                "BlockAuthAttemptsUntilDate": self.block_auth_attempts_until_date,
                "BoostAmount": self.boost_amount,
                "BoostEndDate": self.boost_end_date,
                "CaptainCharacterDesignId": self.captain_character_design_id,
                "ChallengeDesignId": self.challenge_design_id,
                "ChallengeLosses": self.challenge_losses,
                "ChallengeWins": self.challenge_wins,
                "ChampionshipScore": self.championship_score,
                "ChatAppearance": self.chat_appearance,
                "CompletedMissionDesigns": self.completed_mission_designs,
                "CompletedMissionEventIds": self.completed_mission_event_ids,
                "CooldownExpiry": self.cooldown_expiry,
                "CreationDate": self.creation_date,
                "Credits": self.credits,
                "CrewDonated": self.crew_donated,
                "CrewReceived": self.crew_received,
                "DailyChallengeWinStreak": self.daily_challenge_win_streak,
                "DailyHeartbeatSeconds": self.daily_heartbeat_seconds,
                "DailyMissionsAttempted": self.daily_missions_attempted,
                "DailyPVPAttacks": self.daily_pvp_attacks,
                "DailyPvPDefence": self.daily_pv_p_defence,
                "DailyRewardStatus": self.daily_reward_status,
                "DrawsUsedToday": self.draws_used_today,
                "Email": self.email,
                "EmailVerificationStatus": self.email_verification_status,
                "ExploredStarSystemIds": self.explored_star_system_ids,
                "FacebookToken": self.facebook_token,
                "FacebookTokenExpiryDate": self.facebook_token_expiry_date,
                "Flags": self.flags,
                "FreeStarbuxReceivedToday": self.free_starbux_received_today,
                "GameCenterFriendCount": self.game_center_friend_count,
                "GameCenterName": self.game_center_name,
                "GenderType": self.gender_type,
                "GooglePlayAccessTokenExpiryDate": self.google_play_access_token_expiry_date,
                "GooglePlayIdToken": self.google_play_id_token,
                "GooglePlayName": self.google_play_name,
                "GoolePlayAuthCode": self.goole_play_auth_code,
                "HeroBonusChance": self.hero_bonus_chance,
                "HighestTrophy": self.highest_trophy,
                "IconSpriteId": self.icon_sprite_id,
                "Id": self.id_,
                "IsUnderAge": self.is_under_age,
                "LanguageKey": self.language_key,
                "LastAlertDate": self.last_alert_date,
                "LastBoostDate": self.last_boost_date,
                "LastCatalogPurchaseDate": self.last_catalog_purchase_date,
                "LastChallengeDesignId": self.last_challenge_design_id,
                "LastHeartBeatDate": self.last_heart_beat_date,
                "LastLoginDate": self.last_login_date,
                "LastPurchaseDate": self.last_purchase_date,
                "LastRewardActionDate": self.last_reward_action_date,
                "LastVipClaimDate": self.last_vip_claim_date,
                "LeagueType": self.league_type,
                "LoadingPercentage": self.loading_percentage,
                "MatchingStatus": self.matching_status,
                "Name": self.name,
                "NowggUserId": self.nowgg_user_id,
                "OwnerUserId": self.owner_user_id,
                "PVPAttackDraws": self.pvp_attack_draws,
                "PVPAttackLosses": self.pvp_attack_losses,
                "PVPAttackWins": self.pvp_attack_wins,
                "PVPDefenceDraws": self.pvp_defence_draws,
                "PVPDefenceLosses": self.pvp_defence_losses,
                "PVPDefenceWins": self.pvp_defence_wins,
                "PassPoints": self.pass_points,
                "ProfileImageUrl": self.profile_image_url,
                "PurchaseRewardPoints": self.purchase_reward_points,
                "RaceType": self.race_type,
                "Ranking": self.ranking,
                "RewardsCollectable": self.rewards_collectable,
                "RewardsCollectableAmount": self.rewards_collectable_amount,
                "ShipDesignId": self.ship_design_id,
                "SituationOccurrences": self.situation_occurrences,
                "SituationOccurrencesToday": self.situation_occurrences_today,
                "Status": self.status,
                "SteamId": self.steam_id,
                "TaskRerollCount": self.task_reroll_count,
                "TipStatus": self.tip_status,
                "TotalSupplyDonation": self.total_supply_donation,
                "TournamentBonusScore": self.tournament_bonus_score,
                "TournamentResetDate": self.tournament_reset_date,
                "TournamentRewardPoints": self.tournament_reward_points,
                "TrailUserId": self.trail_user_id,
                "Trophy": self.trophy,
                "TrophyGained": self.trophy_gained,
                "TutorialStatus": self.tutorial_status,
                "UnlockedCharacterDesignIds": self.unlocked_character_design_ids,
                "UnlockedShipDesignIds": self.unlocked_ship_design_ids,
                "UnlockedSkinKeys": self.unlocked_skin_keys,
                "UnreadMessageCount": self.unread_message_count,
                "UpdateDate": self.update_date,
                "UsedRewardPoints": self.used_reward_points,
                "UserSeason": dict(self.user_season) if self.user_season else None,
                "UserSourceAdsPlatformType": self.user_source_ads_platform_type,
                "UserType": self.user_type,
                "VipExpiryDate": self.vip_expiry_date,
            }
            self._dict.update(super().__dict__())

        return self._dict
