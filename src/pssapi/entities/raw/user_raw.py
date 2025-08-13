"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr, element


if TYPE_CHECKING:
    from pssapi import entities

from .entity_base_raw import EntityBaseRaw


class UserRaw(EntityBaseRaw, tag="User"):
    XML_NODE_NAME: str = "User"

    activated_promotions: Optional[str] = attr(name="ActivatedPromotions", default=None)
    ads_platform_user_id: Optional[str] = attr(name="AdsPlatformUserId", default=None)
    alliance: Optional["entities.Alliance"] = element(tag="Alliance", default=None)
    alliance_id: Optional[int] = attr(name="AllianceId", default=None)
    alliance_join_date: Optional[datetime] = attr(name="AllianceJoinDate", default=None)
    alliance_membership: Optional[str] = attr(name="AllianceMembership", default=None)
    alliance_name: Optional[str] = attr(name="AllianceName", default=None)
    alliance_qualify_division_design_id: Optional[int] = attr(name="AllianceQualifyDivisionDesignId", default=None)
    alliance_score: Optional[int] = attr(name="AllianceScore", default=None)
    alliance_sprite_id: Optional[int] = attr(name="AllianceSpriteId", default=None)
    alliance_supply_donation: Optional[int] = attr(name="AllianceSupplyDonation", default=None)
    authentication_type: Optional[str] = attr(name="AuthenticationType", default=None)
    block_auth_attempts_until_date: Optional[datetime] = attr(name="BlockAuthAttemptsUntilDate", default=None)
    boost_amount: Optional[int] = attr(name="BoostAmount", default=None)
    boost_end_date: Optional[datetime] = attr(name="BoostEndDate", default=None)
    captain_character_design_id: Optional[int] = attr(name="CaptainCharacterDesignId", default=None)
    challenge_design_id: Optional[int] = attr(name="ChallengeDesignId", default=None)
    challenge_losses: Optional[int] = attr(name="ChallengeLosses", default=None)
    challenge_wins: Optional[int] = attr(name="ChallengeWins", default=None)
    championship_score: Optional[int] = attr(name="ChampionshipScore", default=None)
    chat_appearance: Optional[int] = attr(name="ChatAppearance", default=None)
    completed_mission_designs: Optional[str] = attr(name="CompletedMissionDesigns", default=None)
    completed_mission_event_ids: Optional[str] = attr(name="CompletedMissionEventIds", default=None)
    cooldown_expiry: Optional[datetime] = attr(name="CooldownExpiry", default=None)
    creation_date: Optional[datetime] = attr(name="CreationDate", default=None)
    credits: Optional[str] = attr(name="Credits", default=None)
    crew_donated: Optional[int] = attr(name="CrewDonated", default=None)
    crew_received: Optional[int] = attr(name="CrewReceived", default=None)
    daily_challenge_win_streak: Optional[int] = attr(name="DailyChallengeWinStreak", default=None)
    daily_heartbeat_seconds: Optional[int] = attr(name="DailyHeartbeatSeconds", default=None)
    daily_missions_attempted: Optional[str] = attr(name="DailyMissionsAttempted", default=None)
    daily_pvp_attacks: Optional[int] = attr(name="DailyPVPAttacks", default=None)
    daily_pv_p_defence: Optional[int] = attr(name="DailyPvPDefence", default=None)
    daily_reward_status: Optional[int] = attr(name="DailyRewardStatus", default=None)
    draws_used_today: Optional[int] = attr(name="DrawsUsedToday", default=None)
    email: Optional[str] = attr(name="Email", default=None)
    email_verification_status: Optional[str] = attr(name="EmailVerificationStatus", default=None)
    explored_star_system_ids: Optional[str] = attr(name="ExploredStarSystemIds", default=None)
    facebook_token: Optional[str] = attr(name="FacebookToken", default=None)
    facebook_token_expiry_date: Optional[datetime] = attr(name="FacebookTokenExpiryDate", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    free_starbux_received_today: Optional[int] = attr(name="FreeStarbuxReceivedToday", default=None)
    game_center_friend_count: Optional[int] = attr(name="GameCenterFriendCount", default=None)
    game_center_name: Optional[str] = attr(name="GameCenterName", default=None)
    gender_type: Optional[str] = attr(name="GenderType", default=None)
    google_play_access_token_expiry_date: Optional[datetime] = attr(name="GooglePlayAccessTokenExpiryDate", default=None)
    google_play_id_token: Optional[str] = attr(name="GooglePlayIdToken", default=None)
    google_play_name: Optional[str] = attr(name="GooglePlayName", default=None)
    goole_play_auth_code: Optional[str] = attr(name="GoolePlayAuthCode", default=None)
    hero_bonus_chance: Optional[int] = attr(name="HeroBonusChance", default=None)
    highest_trophy: Optional[int] = attr(name="HighestTrophy", default=None)
    icon_sprite_id: Optional[int] = attr(name="IconSpriteId", default=None)
    id_: Optional[int] = attr(name="Id", default=None)
    is_under_age: Optional[bool] = attr(name="IsUnderAge", default=None)
    language_key: Optional[str] = attr(name="LanguageKey", default=None)
    last_alert_date: Optional[str] = attr(name="LastAlertDate", default=None)
    last_boost_date: Optional[datetime] = attr(name="LastBoostDate", default=None)
    last_catalog_purchase_date: Optional[datetime] = attr(name="LastCatalogPurchaseDate", default=None)
    last_challenge_design_id: Optional[int] = attr(name="LastChallengeDesignId", default=None)
    last_heart_beat_date: Optional[datetime] = attr(name="LastHeartBeatDate", default=None)
    last_login_date: Optional[datetime] = attr(name="LastLoginDate", default=None)
    last_purchase_date: Optional[datetime] = attr(name="LastPurchaseDate", default=None)
    last_reward_action_date: Optional[datetime] = attr(name="LastRewardActionDate", default=None)
    last_vip_claim_date: Optional[datetime] = attr(name="LastVipClaimDate", default=None)
    league_type: Optional[str] = attr(name="LeagueType", default=None)
    loading_percentage: Optional[int] = attr(name="LoadingPercentage", default=None)
    matching_status: Optional[str] = attr(name="MatchingStatus", default=None)
    name: Optional[str] = attr(name="Name", default=None)
    nowgg_user_id: Optional[str] = attr(name="NowggUserId", default=None)
    owner_user_id: Optional[int] = attr(name="OwnerUserId", default=None)
    pvp_attack_draws: Optional[int] = attr(name="PVPAttackDraws", default=None)
    pvp_attack_losses: Optional[int] = attr(name="PVPAttackLosses", default=None)
    pvp_attack_wins: Optional[int] = attr(name="PVPAttackWins", default=None)
    pvp_defence_draws: Optional[int] = attr(name="PVPDefenceDraws", default=None)
    pvp_defence_losses: Optional[int] = attr(name="PVPDefenceLosses", default=None)
    pvp_defence_wins: Optional[int] = attr(name="PVPDefenceWins", default=None)
    pass_points: Optional[int] = attr(name="PassPoints", default=None)
    profile_image_url: Optional[str] = attr(name="ProfileImageUrl", default=None)
    purchase_reward_points: Optional[int] = attr(name="PurchaseRewardPoints", default=None)
    race_type: Optional[str] = attr(name="RaceType", default=None)
    ranking: Optional[int] = attr(name="Ranking", default=None)
    rewards_collectable: Optional[bool] = attr(name="RewardsCollectable", default=None)
    rewards_collectable_amount: Optional[int] = attr(name="RewardsCollectableAmount", default=None)
    ship_design_id: Optional[int] = attr(name="ShipDesignId", default=None)
    situation_occurrences: Optional[str] = attr(name="SituationOccurrences", default=None)
    situation_occurrences_today: Optional[int] = attr(name="SituationOccurrencesToday", default=None)
    status: Optional[int] = attr(name="Status", default=None)
    steam_id: Optional[str] = attr(name="SteamId", default=None)
    task_reroll_count: Optional[int] = attr(name="TaskRerollCount", default=None)
    tip_status: Optional[int] = attr(name="TipStatus", default=None)
    total_supply_donation: Optional[int] = attr(name="TotalSupplyDonation", default=None)
    tournament_bonus_score: Optional[int] = attr(name="TournamentBonusScore", default=None)
    tournament_reset_date: Optional[datetime] = attr(name="TournamentResetDate", default=None)
    tournament_reward_points: Optional[int] = attr(name="TournamentRewardPoints", default=None)
    trail_user_id: Optional[str] = attr(name="TrailUserId", default=None)
    trophy: Optional[int] = attr(name="Trophy", default=None)
    trophy_gained: Optional[int] = attr(name="TrophyGained", default=None)
    tutorial_status: Optional[int] = attr(name="TutorialStatus", default=None)
    unlocked_character_design_ids: Optional[str] = attr(name="UnlockedCharacterDesignIds", default=None)
    unlocked_ship_design_ids: Optional[str] = attr(name="UnlockedShipDesignIds", default=None)
    unlocked_skin_keys: Optional[str] = attr(name="UnlockedSkinKeys", default=None)
    unread_message_count: Optional[str] = attr(name="UnreadMessageCount", default=None)
    update_date: Optional[datetime] = attr(name="UpdateDate", default=None)
    used_reward_points: Optional[int] = attr(name="UsedRewardPoints", default=None)
    user_season: Optional["entities.UserSeason"] = element(tag="UserSeason", default=None)
    user_source_ads_platform_type: Optional[str] = attr(name="UserSourceAdsPlatformType", default=None)
    user_type: Optional[str] = attr(name="UserType", default=None)
    vip_expiry_date: Optional[datetime] = attr(name="VipExpiryDate", default=None)

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


__all__ = [
    "UserRaw",
]
