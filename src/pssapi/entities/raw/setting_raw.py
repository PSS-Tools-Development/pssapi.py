"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class SettingRaw(EntityBaseRaw, tag="Setting"):
    XML_NODE_NAME: str = "Setting"

    ab_testing_rollout: Optional[int] = attr(name="ABTestingRollout", default=None)
    ab_testing_start_date: Optional[datetime] = attr(name="ABTestingStartDate", default=None)
    a_feature_mask: Optional[int] = attr(name="AFeatureMask", default=None)
    ability_design_version: Optional[int] = attr(name="AbilityDesignVersion", default=None)
    achievement_design_version: Optional[int] = attr(name="AchievementDesignVersion", default=None)
    action_type_version: Optional[int] = attr(name="ActionTypeVersion", default=None)
    alliance_badge_sprite_ids: Optional[str] = attr(name="AllianceBadgeSpriteIds", default=None)
    animation_version: Optional[int] = attr(name="AnimationVersion", default=None)
    asset_version: Optional[int] = attr(name="AssetVersion", default=None)
    b_feature_mask: Optional[int] = attr(name="BFeatureMask", default=None)
    background_id: Optional[int] = attr(name="BackgroundId", default=None)
    background_version: Optional[int] = attr(name="BackgroundVersion", default=None)
    battle_background_id: Optional[int] = attr(name="BattleBackgroundId", default=None)
    boost_duration: Optional[int] = attr(name="BoostDuration", default=None)
    boost_gauge_mobile: Optional[int] = attr(name="BoostGaugeMobile", default=None)
    boost_gauge_pc: Optional[int] = attr(name="BoostGaugePC", default=None)
    boost_multiplier: Optional[int] = attr(name="BoostMultiplier", default=None)
    cargo_items: Optional[str] = attr(name="CargoItems", default=None)
    cargo_prices: Optional[str] = attr(name="CargoPrices", default=None)
    challenge_design_version: Optional[int] = attr(name="ChallengeDesignVersion", default=None)
    character_design_action_version: Optional[int] = attr(name="CharacterDesignActionVersion", default=None)
    character_design_version: Optional[int] = attr(name="CharacterDesignVersion", default=None)
    character_part_version: Optional[int] = attr(name="CharacterPartVersion", default=None)
    checksum_type: Optional[str] = attr(name="ChecksumType", default=None)
    client_translation_version: Optional[int] = attr(name="ClientTranslationVersion", default=None)
    collection_design_version: Optional[int] = attr(name="CollectionDesignVersion", default=None)
    common_crew_id: Optional[int] = attr(name="CommonCrewId", default=None)
    condition_type_version: Optional[int] = attr(name="ConditionTypeVersion", default=None)
    craft_design_version: Optional[int] = attr(name="CraftDesignVersion", default=None)
    current_android_version: Optional[str] = attr(name="CurrentAndroidVersion", default=None)
    daily_item_rewards: Optional[str] = attr(name="DailyItemRewards", default=None)
    daily_reward_argument: Optional[int] = attr(name="DailyRewardArgument", default=None)
    daily_reward_type: Optional[str] = attr(name="DailyRewardType", default=None)
    division_design_version: Optional[int] = attr(name="DivisionDesignVersion", default=None)
    draw_design_version: Optional[int] = attr(name="DrawDesignVersion", default=None)
    engine_efficiency_loss: Optional[float] = attr(name="EngineEfficiencyLoss", default=None)
    feature_mask: Optional[int] = attr(name="FeatureMask", default=None)
    file_version: Optional[int] = attr(name="FileVersion", default=None)
    flags: Optional[int] = attr(name="Flags", default=None)
    grace_period: Optional[int] = attr(name="GracePeriod", default=None)
    hero_crew_id: Optional[int] = attr(name="HeroCrewId", default=None)
    is_debug: Optional[bool] = attr(name="IsDebug", default=None)
    item_design_action_version: Optional[int] = attr(name="ItemDesignActionVersion", default=None)
    item_design_version: Optional[int] = attr(name="ItemDesignVersion", default=None)
    league_version: Optional[int] = attr(name="LeagueVersion", default=None)
    left_loading_sprite_id: Optional[int] = attr(name="LeftLoadingSpriteId", default=None)
    legendary_battle_count: Optional[int] = attr(name="LegendaryBattleCount", default=None)
    legendary_doves_amount: Optional[int] = attr(name="LegendaryDovesAmount", default=None)
    legendary_loot_percentage: Optional[int] = attr(name="LegendaryLootPercentage", default=None)
    legendary_result_reward_modifiers: Optional[str] = attr(name="LegendaryResultRewardModifiers", default=None)
    legendary_result_trophy_modifiers: Optional[str] = attr(name="LegendaryResultTrophyModifiers", default=None)
    legendary_rewards_text: Optional[str] = attr(name="LegendaryRewardsText", default=None)
    legendary_rules_text: Optional[str] = attr(name="LegendaryRulesText", default=None)
    legendary_trophy_in: Optional[int] = attr(name="LegendaryTrophyIn", default=None)
    legendary_trophy_out: Optional[int] = attr(name="LegendaryTrophyOut", default=None)
    limited_catalog_argument: Optional[int] = attr(name="LimitedCatalogArgument", default=None)
    limited_catalog_currency_amount: Optional[int] = attr(name="LimitedCatalogCurrencyAmount", default=None)
    limited_catalog_currency_type: Optional[str] = attr(name="LimitedCatalogCurrencyType", default=None)
    limited_catalog_expiry_date: Optional[datetime] = attr(name="LimitedCatalogExpiryDate", default=None)
    limited_catalog_max_total: Optional[int] = attr(name="LimitedCatalogMaxTotal", default=None)
    limited_catalog_quantity: Optional[int] = attr(name="LimitedCatalogQuantity", default=None)
    limited_catalog_restock_quantity: Optional[int] = attr(name="LimitedCatalogRestockQuantity", default=None)
    limited_catalog_type: Optional[str] = attr(name="LimitedCatalogType", default=None)
    loading_ship_sprite_id: Optional[int] = attr(name="LoadingShipSpriteId", default=None)
    loading_subtitle_sprite_id: Optional[int] = attr(name="LoadingSubtitleSpriteId", default=None)
    loading_title_sprite_id: Optional[int] = attr(name="LoadingTitleSpriteId", default=None)
    loot_modifiers: Optional[str] = attr(name="LootModifiers", default=None)
    maintenance_date: Optional[datetime] = attr(name="MaintenanceDate", default=None)
    maintenance_message: Optional[str] = attr(name="MaintenanceMessage", default=None)
    maintenance_title: Optional[str] = attr(name="MaintenanceTitle", default=None)
    marker_generator_design_version: Optional[int] = attr(name="MarkerGeneratorDesignVersion", default=None)
    max_boost_duration: Optional[int] = attr(name="MaxBoostDuration", default=None)
    max_crews: Optional[int] = attr(name="MaxCrews", default=None)
    max_daily_draws: Optional[int] = attr(name="MaxDailyDraws", default=None)
    max_redemption_count: Optional[int] = attr(name="MaxRedemptionCount", default=None)
    max_redemption_count_per_month: Optional[int] = attr(name="MaxRedemptionCountPerMonth", default=None)
    merchant_ship_exterior_sprite_id: Optional[int] = attr(name="MerchantShipExteriorSpriteId", default=None)
    merchant_ship_sprite_id: Optional[int] = attr(name="MerchantShipSpriteId", default=None)
    min_purchase_reward_points_for_starbux_trading: Optional[int] = attr(name="MinPurchaseRewardPointsForStarbuxTrading", default=None)
    min_trophies_for_starbux_trading: Optional[int] = attr(name="MinTrophiesForStarbuxTrading", default=None)
    minimum_client_version: Optional[str] = attr(name="MinimumClientVersion", default=None)
    minimum_version: Optional[str] = attr(name="MinimumVersion", default=None)
    missile_design_version: Optional[int] = attr(name="MissileDesignVersion", default=None)
    mission_design_version: Optional[int] = attr(name="MissionDesignVersion", default=None)
    new_user_count: Optional[int] = attr(name="NewUserCount", default=None)
    news: Optional[str] = attr(name="News", default=None)
    news_design_version: Optional[int] = attr(name="NewsDesignVersion", default=None)
    news_sprite_id: Optional[int] = attr(name="NewsSpriteId", default=None)
    news_update_date: Optional[datetime] = attr(name="NewsUpdateDate", default=None)
    number_of_vote_options: Optional[int] = attr(name="NumberOfVoteOptions", default=None)
    planet_version: Optional[int] = attr(name="PlanetVersion", default=None)
    prestige_top_character_design_id: Optional[int] = attr(name="PrestigeTopCharacterDesignId", default=None)
    pro_bono_limit: Optional[int] = attr(name="ProBonoLimit", default=None)
    production_server: Optional[str] = attr(name="ProductionServer", default=None)
    promotion_design_version: Optional[int] = attr(name="PromotionDesignVersion", default=None)
    purge_period: Optional[int] = attr(name="PurgePeriod", default=None)
    recommended_version: Optional[str] = attr(name="RecommendedVersion", default=None)
    replay_available_date: Optional[datetime] = attr(name="ReplayAvailableDate", default=None)
    research_design_version: Optional[int] = attr(name="ResearchDesignVersion", default=None)
    reward_design_version: Optional[int] = attr(name="RewardDesignVersion", default=None)
    reward_point_percentage: Optional[int] = attr(name="RewardPointPercentage", default=None)
    reward_video_time_reduction: Optional[int] = attr(name="RewardVideoTimeReduction", default=None)
    right_loading_sprite_id: Optional[int] = attr(name="RightLoadingSpriteId", default=None)
    room_design_purchase_version: Optional[int] = attr(name="RoomDesignPurchaseVersion", default=None)
    room_design_sprite_version: Optional[int] = attr(name="RoomDesignSpriteVersion", default=None)
    room_design_version: Optional[int] = attr(name="RoomDesignVersion", default=None)
    rush_tier_cost: Optional[int] = attr(name="RushTierCost", default=None)
    sale_argument: Optional[int] = attr(name="SaleArgument", default=None)
    sale_end_date: Optional[datetime] = attr(name="SaleEndDate", default=None)
    sale_item_mask: Optional[int] = attr(name="SaleItemMask", default=None)
    sale_once_only: Optional[bool] = attr(name="SaleOnceOnly", default=None)
    sale_quantity: Optional[int] = attr(name="SaleQuantity", default=None)
    sale_start_date: Optional[datetime] = attr(name="SaleStartDate", default=None)
    sale_title: Optional[str] = attr(name="SaleTitle", default=None)
    sale_type: Optional[str] = attr(name="SaleType", default=None)
    season_design_version: Optional[int] = attr(name="SeasonDesignVersion", default=None)
    server_setting_version: Optional[int] = attr(name="ServerSettingVersion", default=None)
    setting_id: Optional[int] = attr(name="SettingId", default=None)
    ship_design_version: Optional[int] = attr(name="ShipDesignVersion", default=None)
    situation_design_version: Optional[int] = attr(name="SituationDesignVersion", default=None)
    situation_tags: Optional[str] = attr(name="SituationTags", default=None)
    skin_set_version: Optional[int] = attr(name="SkinSetVersion", default=None)
    skin_version: Optional[int] = attr(name="SkinVersion", default=None)
    sprite_version: Optional[int] = attr(name="SpriteVersion", default=None)
    star_system_link_version: Optional[int] = attr(name="StarSystemLinkVersion", default=None)
    star_system_version: Optional[int] = attr(name="StarSystemVersion", default=None)
    support_email: Optional[str] = attr(name="SupportEmail", default=None)
    support_task_ran_date: Optional[datetime] = attr(name="SupportTaskRanDate", default=None)
    task_design_version: Optional[int] = attr(name="TaskDesignVersion", default=None)
    task_reroll_cost: Optional[int] = attr(name="TaskRerollCost", default=None)
    task_reroll_max_count: Optional[int] = attr(name="TaskRerollMaxCount", default=None)
    tournament_bonus_score: Optional[int] = attr(name="TournamentBonusScore", default=None)
    tournament_final_duration: Optional[int] = attr(name="TournamentFinalDuration", default=None)
    tournament_news: Optional[str] = attr(name="TournamentNews", default=None)
    tournament_sprite_id: Optional[int] = attr(name="TournamentSpriteId", default=None)
    training_design_version: Optional[int] = attr(name="TrainingDesignVersion", default=None)
    vip_design_version: Optional[int] = attr(name="VipDesignVersion", default=None)
    voting_duration: Optional[int] = attr(name="VotingDuration", default=None)

    def _key(self):
        return (
            self.ab_testing_rollout,
            self.ab_testing_start_date,
            self.a_feature_mask,
            self.ability_design_version,
            self.achievement_design_version,
            self.action_type_version,
            self.alliance_badge_sprite_ids,
            self.animation_version,
            self.asset_version,
            self.b_feature_mask,
            self.background_id,
            self.background_version,
            self.battle_background_id,
            self.boost_duration,
            self.boost_gauge_mobile,
            self.boost_gauge_pc,
            self.boost_multiplier,
            self.cargo_items,
            self.cargo_prices,
            self.challenge_design_version,
            self.character_design_action_version,
            self.character_design_version,
            self.character_part_version,
            self.checksum_type,
            self.client_translation_version,
            self.collection_design_version,
            self.common_crew_id,
            self.condition_type_version,
            self.craft_design_version,
            self.current_android_version,
            self.daily_item_rewards,
            self.daily_reward_argument,
            self.daily_reward_type,
            self.division_design_version,
            self.draw_design_version,
            self.engine_efficiency_loss,
            self.feature_mask,
            self.file_version,
            self.flags,
            self.grace_period,
            self.hero_crew_id,
            self.is_debug,
            self.item_design_action_version,
            self.item_design_version,
            self.league_version,
            self.left_loading_sprite_id,
            self.legendary_battle_count,
            self.legendary_doves_amount,
            self.legendary_loot_percentage,
            self.legendary_result_reward_modifiers,
            self.legendary_result_trophy_modifiers,
            self.legendary_rewards_text,
            self.legendary_rules_text,
            self.legendary_trophy_in,
            self.legendary_trophy_out,
            self.limited_catalog_argument,
            self.limited_catalog_currency_amount,
            self.limited_catalog_currency_type,
            self.limited_catalog_expiry_date,
            self.limited_catalog_max_total,
            self.limited_catalog_quantity,
            self.limited_catalog_restock_quantity,
            self.limited_catalog_type,
            self.loading_ship_sprite_id,
            self.loading_subtitle_sprite_id,
            self.loading_title_sprite_id,
            self.loot_modifiers,
            self.maintenance_date,
            self.maintenance_message,
            self.maintenance_title,
            self.marker_generator_design_version,
            self.max_boost_duration,
            self.max_crews,
            self.max_daily_draws,
            self.max_redemption_count,
            self.max_redemption_count_per_month,
            self.merchant_ship_exterior_sprite_id,
            self.merchant_ship_sprite_id,
            self.min_purchase_reward_points_for_starbux_trading,
            self.min_trophies_for_starbux_trading,
            self.minimum_client_version,
            self.minimum_version,
            self.missile_design_version,
            self.mission_design_version,
            self.new_user_count,
            self.news,
            self.news_design_version,
            self.news_sprite_id,
            self.news_update_date,
            self.number_of_vote_options,
            self.planet_version,
            self.prestige_top_character_design_id,
            self.pro_bono_limit,
            self.production_server,
            self.promotion_design_version,
            self.purge_period,
            self.recommended_version,
            self.replay_available_date,
            self.research_design_version,
            self.reward_design_version,
            self.reward_point_percentage,
            self.reward_video_time_reduction,
            self.right_loading_sprite_id,
            self.room_design_purchase_version,
            self.room_design_sprite_version,
            self.room_design_version,
            self.rush_tier_cost,
            self.sale_argument,
            self.sale_end_date,
            self.sale_item_mask,
            self.sale_once_only,
            self.sale_quantity,
            self.sale_start_date,
            self.sale_title,
            self.sale_type,
            self.season_design_version,
            self.server_setting_version,
            self.setting_id,
            self.ship_design_version,
            self.situation_design_version,
            self.situation_tags,
            self.skin_set_version,
            self.skin_version,
            self.sprite_version,
            self.star_system_link_version,
            self.star_system_version,
            self.support_email,
            self.support_task_ran_date,
            self.task_design_version,
            self.task_reroll_cost,
            self.task_reroll_max_count,
            self.tournament_bonus_score,
            self.tournament_final_duration,
            self.tournament_news,
            self.tournament_sprite_id,
            self.training_design_version,
            self.vip_design_version,
            self.voting_duration,
        )


__all__ = [
    "SettingRaw",
]
