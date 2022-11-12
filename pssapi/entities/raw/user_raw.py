"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class UserRaw:
    XML_NODE_NAME: str = 'User'

    def __init__(self, user_info: _EntityInfo) -> None:
        self.activated_promotions: str = _parse.pss_str(
            user_info.get('ActivatedPromotions'))
        self.alliance_id: int = _parse.pss_int(user_info.get('AllianceId'))
        self.alliance_join_date: datetime = _parse.pss_datetime(
            user_info.get('AllianceJoinDate'))
        self.alliance_membership: str = _parse.pss_str(
            user_info.get('AllianceMembership'))
        self.alliance_name: str = _parse.pss_str(user_info.get('AllianceName'))
        self.alliance_qualify_division_design_id: int = _parse.pss_int(
            user_info.get('AllianceQualifyDivisionDesignId'))
        self.alliance_score: int = _parse.pss_int(
            user_info.get('AllianceScore'))
        self.alliance_sprite_id: int = _parse.pss_int(
            user_info.get('AllianceSpriteId'))
        self.alliance_supply_donation: int = _parse.pss_int(
            user_info.get('AllianceSupplyDonation'))
        self.authentication_type: str = _parse.pss_str(
            user_info.get('AuthenticationType'))
        self.block_auth_attempts_until_date: datetime = _parse.pss_datetime(
            user_info.get('BlockAuthAttemptsUntilDate'))
        self.boost_amount: int = _parse.pss_int(user_info.get('BoostAmount'))
        self.boost_end_date: datetime = _parse.pss_datetime(
            user_info.get('BoostEndDate'))
        self.captain_character_design_id: int = _parse.pss_int(
            user_info.get('CaptainCharacterDesignId'))
        self.challenge_design_id: int = _parse.pss_int(
            user_info.get('ChallengeDesignId'))
        self.challenge_losses: int = _parse.pss_int(
            user_info.get('ChallengeLosses'))
        self.challenge_wins: int = _parse.pss_int(
            user_info.get('ChallengeWins'))
        self.championship_score: int = _parse.pss_int(
            user_info.get('ChampionshipScore'))
        self.chat_appearance: int = _parse.pss_int(
            user_info.get('ChatAppearance'))
        self.completed_mission_designs: str = _parse.pss_str(
            user_info.get('CompletedMissionDesigns'))
        self.completed_mission_event_ids: str = _parse.pss_str(
            user_info.get('CompletedMissionEventIds'))
        self.cooldown_expiry: datetime = _parse.pss_datetime(
            user_info.get('CooldownExpiry'))
        self.creation_date: datetime = _parse.pss_datetime(
            user_info.get('CreationDate'))
        self.credits: str = _parse.pss_str(user_info.get('Credits'))
        self.crew_donated: int = _parse.pss_int(user_info.get('CrewDonated'))
        self.crew_received: int = _parse.pss_int(user_info.get('CrewReceived'))
        self.daily_challenge_win_streak: int = _parse.pss_int(
            user_info.get('DailyChallengeWinStreak'))
        self.daily_missions_attempted: str = _parse.pss_str(
            user_info.get('DailyMissionsAttempted'))
        self.daily_pvp_attacks: int = _parse.pss_int(
            user_info.get('DailyPVPAttacks'))
        self.daily_pv_p_defence: int = _parse.pss_int(
            user_info.get('DailyPvPDefence'))
        self.daily_reward_status: int = _parse.pss_int(
            user_info.get('DailyRewardStatus'))
        self.draws_used_today: int = _parse.pss_int(
            user_info.get('DrawsUsedToday'))
        self.email: str = _parse.pss_str(user_info.get('Email'))
        self.email_verification_status: str = _parse.pss_str(
            user_info.get('EmailVerificationStatus'))
        self.explored_star_system_ids: str = _parse.pss_str(
            user_info.get('ExploredStarSystemIds'))
        self.facebook_token: str = _parse.pss_str(
            user_info.get('FacebookToken'))
        self.facebook_token_expiry_date: datetime = _parse.pss_datetime(
            user_info.get('FacebookTokenExpiryDate'))
        self.flags: int = _parse.pss_int(user_info.get('Flags'))
        self.free_starbux_received_today: int = _parse.pss_int(
            user_info.get('FreeStarbuxReceivedToday'))
        self.game_center_friend_count: int = _parse.pss_int(
            user_info.get('GameCenterFriendCount'))
        self.game_center_name: str = _parse.pss_str(
            user_info.get('GameCenterName'))
        self.gender_type: str = _parse.pss_str(user_info.get('GenderType'))
        self.google_play_access_token_expiry_date: str = _parse.pss_str(
            user_info.get('GooglePlayAccessTokenExpiryDate'))
        self.google_play_id_token: str = _parse.pss_str(
            user_info.get('GooglePlayIdToken'))
        self.google_play_name: str = _parse.pss_str(
            user_info.get('GooglePlayName'))
        self.goole_play_auth_code: str = _parse.pss_str(
            user_info.get('GoolePlayAuthCode'))
        self.hero_bonus_chance: int = _parse.pss_int(
            user_info.get('HeroBonusChance'))
        self.highest_trophy: int = _parse.pss_int(
            user_info.get('HighestTrophy'))
        self.icon_sprite_id: int = _parse.pss_int(
            user_info.get('IconSpriteId'))
        self.id: int = _parse.pss_int(user_info.get('Id'))
        self.language_key: str = _parse.pss_str(user_info.get('LanguageKey'))
        self.last_alert_date: str = _parse.pss_str(
            user_info.get('LastAlertDate'))
        self.last_boost_date: datetime = _parse.pss_datetime(
            user_info.get('LastBoostDate'))
        self.last_catalog_purchase_date: datetime = _parse.pss_datetime(
            user_info.get('LastCatalogPurchaseDate'))
        self.last_challenge_design_id: int = _parse.pss_int(
            user_info.get('LastChallengeDesignId'))
        self.last_heart_beat_date: datetime = _parse.pss_datetime(
            user_info.get('LastHeartBeatDate'))
        self.last_login_date: datetime = _parse.pss_datetime(
            user_info.get('LastLoginDate'))
        self.last_purchase_date: str = _parse.pss_str(
            user_info.get('LastPurchaseDate'))
        self.last_reward_action_date: datetime = _parse.pss_datetime(
            user_info.get('LastRewardActionDate'))
        self.last_vip_claim_date: datetime = _parse.pss_datetime(
            user_info.get('LastVipClaimDate'))
        self.league_type: str = _parse.pss_str(user_info.get('LeagueType'))
        self.loading_percentage: int = _parse.pss_int(
            user_info.get('LoadingPercentage'))
        self.matching_status: str = _parse.pss_str(
            user_info.get('MatchingStatus'))
        self.name: str = _parse.pss_str(user_info.get('Name'))
        self.nowgg_user_id: str = _parse.pss_str(user_info.get('NowggUserId'))
        self.owner_user_id: int = _parse.pss_int(user_info.get('OwnerUserId'))
        self.pvp_attack_draws: int = _parse.pss_int(
            user_info.get('PVPAttackDraws'))
        self.pvp_attack_losses: int = _parse.pss_int(
            user_info.get('PVPAttackLosses'))
        self.pvp_attack_wins: int = _parse.pss_int(
            user_info.get('PVPAttackWins'))
        self.pvp_defence_draws: int = _parse.pss_int(
            user_info.get('PVPDefenceDraws'))
        self.pvp_defence_losses: int = _parse.pss_int(
            user_info.get('PVPDefenceLosses'))
        self.pvp_defence_wins: int = _parse.pss_int(
            user_info.get('PVPDefenceWins'))
        self.pass_points: int = _parse.pss_int(user_info.get('PassPoints'))
        self.profile_image_url: str = _parse.pss_str(
            user_info.get('ProfileImageUrl'))
        self.purchase_reward_points: int = _parse.pss_int(
            user_info.get('PurchaseRewardPoints'))
        self.race_type: str = _parse.pss_str(user_info.get('RaceType'))
        self.ranking: int = _parse.pss_int(user_info.get('Ranking'))
        self.rewards_collectable: bool = _parse.pss_bool(
            user_info.get('RewardsCollectable'))
        self.ship_design_id: int = _parse.pss_int(
            user_info.get('ShipDesignId'))
        self.situation_occurrences: str = _parse.pss_str(
            user_info.get('SituationOccurrences'))
        self.situation_occurrences_today: int = _parse.pss_int(
            user_info.get('SituationOccurrencesToday'))
        self.status: int = _parse.pss_int(user_info.get('Status'))
        self.steam_id: str = _parse.pss_str(user_info.get('SteamId'))
        self.task_reroll_count: int = _parse.pss_int(
            user_info.get('TaskRerollCount'))
        self.tip_status: int = _parse.pss_int(user_info.get('TipStatus'))
        self.total_supply_donation: int = _parse.pss_int(
            user_info.get('TotalSupplyDonation'))
        self.tournament_bonus_score: int = _parse.pss_int(
            user_info.get('TournamentBonusScore'))
        self.tournament_reset_date: datetime = _parse.pss_datetime(
            user_info.get('TournamentResetDate'))
        self.tournament_reward_points: int = _parse.pss_int(
            user_info.get('TournamentRewardPoints'))
        self.trophy: int = _parse.pss_int(user_info.get('Trophy'))
        self.trophy_gained: int = _parse.pss_int(user_info.get('TrophyGained'))
        self.tutorial_status: int = _parse.pss_int(
            user_info.get('TutorialStatus'))
        self.unlocked_character_design_ids: str = _parse.pss_str(
            user_info.get('UnlockedCharacterDesignIds'))
        self.unlocked_ship_design_ids: str = _parse.pss_str(
            user_info.get('UnlockedShipDesignIds'))
        self.unlocked_skin_keys: str = _parse.pss_str(
            user_info.get('UnlockedSkinKeys'))
        self.unread_message_count: str = _parse.pss_str(
            user_info.get('UnreadMessageCount'))
        self.update_date: datetime = _parse.pss_datetime(
            user_info.get('UpdateDate'))
        self.used_reward_points: int = _parse.pss_int(
            user_info.get('UsedRewardPoints'))
        self.user_type: str = _parse.pss_str(user_info.get('UserType'))
        self.vip_expiry_date: datetime = _parse.pss_datetime(
            user_info.get('VipExpiryDate'))
