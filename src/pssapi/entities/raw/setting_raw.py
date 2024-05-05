"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw as _EntityBaseRaw


class SettingRaw(_EntityBaseRaw):
    XML_NODE_NAME: str = "Setting"

    def __init__(self, setting_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._ab_testing_rollout: int = _parse.pss_int(setting_info.pop("ABTestingRollout", None))
        self._ab_testing_start_date: _datetime = _parse.pss_datetime(setting_info.pop("ABTestingStartDate", None))
        self._a_feature_mask: int = _parse.pss_int(setting_info.pop("AFeatureMask", None))
        self._ability_design_version: int = _parse.pss_int(setting_info.pop("AbilityDesignVersion", None))
        self._achievement_design_version: int = _parse.pss_int(setting_info.pop("AchievementDesignVersion", None))
        self._action_type_version: int = _parse.pss_int(setting_info.pop("ActionTypeVersion", None))
        self._alliance_badge_sprite_ids: str = _parse.pss_str(setting_info.pop("AllianceBadgeSpriteIds", None))
        self._animation_version: int = _parse.pss_int(setting_info.pop("AnimationVersion", None))
        self._asset_version: int = _parse.pss_int(setting_info.pop("AssetVersion", None))
        self._b_feature_mask: int = _parse.pss_int(setting_info.pop("BFeatureMask", None))
        self._background_id: int = _parse.pss_int(setting_info.pop("BackgroundId", None))
        self._background_version: int = _parse.pss_int(setting_info.pop("BackgroundVersion", None))
        self._battle_background_id: int = _parse.pss_int(setting_info.pop("BattleBackgroundId", None))
        self._boost_duration: int = _parse.pss_int(setting_info.pop("BoostDuration", None))
        self._boost_gauge_mobile: int = _parse.pss_int(setting_info.pop("BoostGaugeMobile", None))
        self._boost_gauge_pc: int = _parse.pss_int(setting_info.pop("BoostGaugePC", None))
        self._boost_multiplier: int = _parse.pss_int(setting_info.pop("BoostMultiplier", None))
        self._cargo_items: str = _parse.pss_str(setting_info.pop("CargoItems", None))
        self._cargo_prices: str = _parse.pss_str(setting_info.pop("CargoPrices", None))
        self._challenge_design_version: int = _parse.pss_int(setting_info.pop("ChallengeDesignVersion", None))
        self._character_design_action_version: int = _parse.pss_int(setting_info.pop("CharacterDesignActionVersion", None))
        self._character_design_version: int = _parse.pss_int(setting_info.pop("CharacterDesignVersion", None))
        self._character_part_version: int = _parse.pss_int(setting_info.pop("CharacterPartVersion", None))
        self._checksum_type: str = _parse.pss_str(setting_info.pop("ChecksumType", None))
        self._client_translation_version: int = _parse.pss_int(setting_info.pop("ClientTranslationVersion", None))
        self._collection_design_version: int = _parse.pss_int(setting_info.pop("CollectionDesignVersion", None))
        self._common_crew_id: int = _parse.pss_int(setting_info.pop("CommonCrewId", None))
        self._condition_type_version: int = _parse.pss_int(setting_info.pop("ConditionTypeVersion", None))
        self._craft_design_version: int = _parse.pss_int(setting_info.pop("CraftDesignVersion", None))
        self._current_android_version: str = _parse.pss_str(setting_info.pop("CurrentAndroidVersion", None))
        self._daily_item_rewards: str = _parse.pss_str(setting_info.pop("DailyItemRewards", None))
        self._daily_reward_argument: int = _parse.pss_int(setting_info.pop("DailyRewardArgument", None))
        self._daily_reward_type: str = _parse.pss_str(setting_info.pop("DailyRewardType", None))
        self._division_design_version: int = _parse.pss_int(setting_info.pop("DivisionDesignVersion", None))
        self._draw_design_version: int = _parse.pss_int(setting_info.pop("DrawDesignVersion", None))
        self._engine_efficiency_loss: float = _parse.pss_float(setting_info.pop("EngineEfficiencyLoss", None))
        self._feature_mask: int = _parse.pss_int(setting_info.pop("FeatureMask", None))
        self._file_version: int = _parse.pss_int(setting_info.pop("FileVersion", None))
        self._flags: int = _parse.pss_int(setting_info.pop("Flags", None))
        self._grace_period: int = _parse.pss_int(setting_info.pop("GracePeriod", None))
        self._hero_crew_id: int = _parse.pss_int(setting_info.pop("HeroCrewId", None))
        self._is_debug: bool = _parse.pss_bool(setting_info.pop("IsDebug", None))
        self._item_design_action_version: int = _parse.pss_int(setting_info.pop("ItemDesignActionVersion", None))
        self._item_design_version: int = _parse.pss_int(setting_info.pop("ItemDesignVersion", None))
        self._league_version: int = _parse.pss_int(setting_info.pop("LeagueVersion", None))
        self._left_loading_sprite_id: int = _parse.pss_int(setting_info.pop("LeftLoadingSpriteId", None))
        self._legendary_battle_count: int = _parse.pss_int(setting_info.pop("LegendaryBattleCount", None))
        self._legendary_doves_amount: int = _parse.pss_int(setting_info.pop("LegendaryDovesAmount", None))
        self._legendary_loot_percentage: int = _parse.pss_int(setting_info.pop("LegendaryLootPercentage", None))
        self._legendary_result_reward_modifiers: str = _parse.pss_str(setting_info.pop("LegendaryResultRewardModifiers", None))
        self._legendary_result_trophy_modifiers: str = _parse.pss_str(setting_info.pop("LegendaryResultTrophyModifiers", None))
        self._legendary_rewards_text: str = _parse.pss_str(setting_info.pop("LegendaryRewardsText", None))
        self._legendary_rules_text: str = _parse.pss_str(setting_info.pop("LegendaryRulesText", None))
        self._legendary_trophy_in: int = _parse.pss_int(setting_info.pop("LegendaryTrophyIn", None))
        self._legendary_trophy_out: int = _parse.pss_int(setting_info.pop("LegendaryTrophyOut", None))
        self._limited_catalog_argument: int = _parse.pss_int(setting_info.pop("LimitedCatalogArgument", None))
        self._limited_catalog_currency_amount: int = _parse.pss_int(setting_info.pop("LimitedCatalogCurrencyAmount", None))
        self._limited_catalog_currency_type: str = _parse.pss_str(setting_info.pop("LimitedCatalogCurrencyType", None))
        self._limited_catalog_expiry_date: _datetime = _parse.pss_datetime(setting_info.pop("LimitedCatalogExpiryDate", None))
        self._limited_catalog_max_total: int = _parse.pss_int(setting_info.pop("LimitedCatalogMaxTotal", None))
        self._limited_catalog_quantity: int = _parse.pss_int(setting_info.pop("LimitedCatalogQuantity", None))
        self._limited_catalog_restock_quantity: int = _parse.pss_int(setting_info.pop("LimitedCatalogRestockQuantity", None))
        self._limited_catalog_type: str = _parse.pss_str(setting_info.pop("LimitedCatalogType", None))
        self._loading_ship_sprite_id: int = _parse.pss_int(setting_info.pop("LoadingShipSpriteId", None))
        self._loading_subtitle_sprite_id: int = _parse.pss_int(setting_info.pop("LoadingSubtitleSpriteId", None))
        self._loading_title_sprite_id: int = _parse.pss_int(setting_info.pop("LoadingTitleSpriteId", None))
        self._loot_modifiers: str = _parse.pss_str(setting_info.pop("LootModifiers", None))
        self._maintenance_date: _datetime = _parse.pss_datetime(setting_info.pop("MaintenanceDate", None))
        self._maintenance_message: str = _parse.pss_str(setting_info.pop("MaintenanceMessage", None))
        self._maintenance_title: str = _parse.pss_str(setting_info.pop("MaintenanceTitle", None))
        self._marker_generator_design_version: int = _parse.pss_int(setting_info.pop("MarkerGeneratorDesignVersion", None))
        self._max_boost_duration: int = _parse.pss_int(setting_info.pop("MaxBoostDuration", None))
        self._max_crews: int = _parse.pss_int(setting_info.pop("MaxCrews", None))
        self._max_daily_draws: int = _parse.pss_int(setting_info.pop("MaxDailyDraws", None))
        self._max_redemption_count: int = _parse.pss_int(setting_info.pop("MaxRedemptionCount", None))
        self._max_redemption_count_per_month: int = _parse.pss_int(setting_info.pop("MaxRedemptionCountPerMonth", None))
        self._merchant_ship_exterior_sprite_id: int = _parse.pss_int(setting_info.pop("MerchantShipExteriorSpriteId", None))
        self._merchant_ship_sprite_id: int = _parse.pss_int(setting_info.pop("MerchantShipSpriteId", None))
        self._min_purchase_reward_points_for_starbux_trading: int = _parse.pss_int(setting_info.pop("MinPurchaseRewardPointsForStarbuxTrading", None))
        self._min_trophies_for_starbux_trading: int = _parse.pss_int(setting_info.pop("MinTrophiesForStarbuxTrading", None))
        self._minimum_client_version: str = _parse.pss_str(setting_info.pop("MinimumClientVersion", None))
        self._minimum_version: str = _parse.pss_str(setting_info.pop("MinimumVersion", None))
        self._missile_design_version: int = _parse.pss_int(setting_info.pop("MissileDesignVersion", None))
        self._mission_design_version: int = _parse.pss_int(setting_info.pop("MissionDesignVersion", None))
        self._new_user_count: int = _parse.pss_int(setting_info.pop("NewUserCount", None))
        self._news: str = _parse.pss_str(setting_info.pop("News", None))
        self._news_design_version: int = _parse.pss_int(setting_info.pop("NewsDesignVersion", None))
        self._news_sprite_id: int = _parse.pss_int(setting_info.pop("NewsSpriteId", None))
        self._news_update_date: _datetime = _parse.pss_datetime(setting_info.pop("NewsUpdateDate", None))
        self._number_of_vote_options: int = _parse.pss_int(setting_info.pop("NumberOfVoteOptions", None))
        self._planet_version: int = _parse.pss_int(setting_info.pop("PlanetVersion", None))
        self._prestige_top_character_design_id: int = _parse.pss_int(setting_info.pop("PrestigeTopCharacterDesignId", None))
        self._pro_bono_limit: int = _parse.pss_int(setting_info.pop("ProBonoLimit", None))
        self._production_server: str = _parse.pss_str(setting_info.pop("ProductionServer", None))
        self._promotion_design_version: int = _parse.pss_int(setting_info.pop("PromotionDesignVersion", None))
        self._purge_period: int = _parse.pss_int(setting_info.pop("PurgePeriod", None))
        self._recommended_version: str = _parse.pss_str(setting_info.pop("RecommendedVersion", None))
        self._replay_available_date: _datetime = _parse.pss_datetime(setting_info.pop("ReplayAvailableDate", None))
        self._research_design_version: int = _parse.pss_int(setting_info.pop("ResearchDesignVersion", None))
        self._reward_design_version: int = _parse.pss_int(setting_info.pop("RewardDesignVersion", None))
        self._reward_point_percentage: int = _parse.pss_int(setting_info.pop("RewardPointPercentage", None))
        self._reward_video_time_reduction: int = _parse.pss_int(setting_info.pop("RewardVideoTimeReduction", None))
        self._right_loading_sprite_id: int = _parse.pss_int(setting_info.pop("RightLoadingSpriteId", None))
        self._room_design_purchase_version: int = _parse.pss_int(setting_info.pop("RoomDesignPurchaseVersion", None))
        self._room_design_sprite_version: int = _parse.pss_int(setting_info.pop("RoomDesignSpriteVersion", None))
        self._room_design_version: int = _parse.pss_int(setting_info.pop("RoomDesignVersion", None))
        self._rush_tier_cost: int = _parse.pss_int(setting_info.pop("RushTierCost", None))
        self._sale_argument: int = _parse.pss_int(setting_info.pop("SaleArgument", None))
        self._sale_end_date: _datetime = _parse.pss_datetime(setting_info.pop("SaleEndDate", None))
        self._sale_item_mask: int = _parse.pss_int(setting_info.pop("SaleItemMask", None))
        self._sale_once_only: bool = _parse.pss_bool(setting_info.pop("SaleOnceOnly", None))
        self._sale_quantity: int = _parse.pss_int(setting_info.pop("SaleQuantity", None))
        self._sale_start_date: _datetime = _parse.pss_datetime(setting_info.pop("SaleStartDate", None))
        self._sale_title: str = _parse.pss_str(setting_info.pop("SaleTitle", None))
        self._sale_type: str = _parse.pss_str(setting_info.pop("SaleType", None))
        self._season_design_version: int = _parse.pss_int(setting_info.pop("SeasonDesignVersion", None))
        self._server_setting_version: int = _parse.pss_int(setting_info.pop("ServerSettingVersion", None))
        self._setting_id: int = _parse.pss_int(setting_info.pop("SettingId", None))
        self._ship_design_version: int = _parse.pss_int(setting_info.pop("ShipDesignVersion", None))
        self._situation_design_version: int = _parse.pss_int(setting_info.pop("SituationDesignVersion", None))
        self._situation_tags: str = _parse.pss_str(setting_info.pop("SituationTags", None))
        self._skin_set_version: int = _parse.pss_int(setting_info.pop("SkinSetVersion", None))
        self._skin_version: int = _parse.pss_int(setting_info.pop("SkinVersion", None))
        self._sprite_version: int = _parse.pss_int(setting_info.pop("SpriteVersion", None))
        self._star_system_link_version: int = _parse.pss_int(setting_info.pop("StarSystemLinkVersion", None))
        self._star_system_version: int = _parse.pss_int(setting_info.pop("StarSystemVersion", None))
        self._support_email: str = _parse.pss_str(setting_info.pop("SupportEmail", None))
        self._support_task_ran_date: _datetime = _parse.pss_datetime(setting_info.pop("SupportTaskRanDate", None))
        self._task_design_version: int = _parse.pss_int(setting_info.pop("TaskDesignVersion", None))
        self._task_reroll_cost: int = _parse.pss_int(setting_info.pop("TaskRerollCost", None))
        self._task_reroll_max_count: int = _parse.pss_int(setting_info.pop("TaskRerollMaxCount", None))
        self._tournament_bonus_score: int = _parse.pss_int(setting_info.pop("TournamentBonusScore", None))
        self._tournament_final_duration: int = _parse.pss_int(setting_info.pop("TournamentFinalDuration", None))
        self._tournament_news: str = _parse.pss_str(setting_info.pop("TournamentNews", None))
        self._tournament_sprite_id: int = _parse.pss_int(setting_info.pop("TournamentSpriteId", None))
        self._training_design_version: int = _parse.pss_int(setting_info.pop("TrainingDesignVersion", None))
        self._vip_design_version: int = _parse.pss_int(setting_info.pop("VipDesignVersion", None))
        self._voting_duration: int = _parse.pss_int(setting_info.pop("VotingDuration", None))
        super().__init__(setting_info)

    @property
    def ab_testing_rollout(self) -> int:
        return self._ab_testing_rollout

    @property
    def ab_testing_start_date(self) -> _datetime:
        return self._ab_testing_start_date

    @property
    def a_feature_mask(self) -> int:
        return self._a_feature_mask

    @property
    def ability_design_version(self) -> int:
        return self._ability_design_version

    @property
    def achievement_design_version(self) -> int:
        return self._achievement_design_version

    @property
    def action_type_version(self) -> int:
        return self._action_type_version

    @property
    def alliance_badge_sprite_ids(self) -> str:
        return self._alliance_badge_sprite_ids

    @property
    def animation_version(self) -> int:
        return self._animation_version

    @property
    def asset_version(self) -> int:
        return self._asset_version

    @property
    def b_feature_mask(self) -> int:
        return self._b_feature_mask

    @property
    def background_id(self) -> int:
        return self._background_id

    @property
    def background_version(self) -> int:
        return self._background_version

    @property
    def battle_background_id(self) -> int:
        return self._battle_background_id

    @property
    def boost_duration(self) -> int:
        return self._boost_duration

    @property
    def boost_gauge_mobile(self) -> int:
        return self._boost_gauge_mobile

    @property
    def boost_gauge_pc(self) -> int:
        return self._boost_gauge_pc

    @property
    def boost_multiplier(self) -> int:
        return self._boost_multiplier

    @property
    def cargo_items(self) -> str:
        return self._cargo_items

    @property
    def cargo_prices(self) -> str:
        return self._cargo_prices

    @property
    def challenge_design_version(self) -> int:
        return self._challenge_design_version

    @property
    def character_design_action_version(self) -> int:
        return self._character_design_action_version

    @property
    def character_design_version(self) -> int:
        return self._character_design_version

    @property
    def character_part_version(self) -> int:
        return self._character_part_version

    @property
    def checksum_type(self) -> str:
        return self._checksum_type

    @property
    def client_translation_version(self) -> int:
        return self._client_translation_version

    @property
    def collection_design_version(self) -> int:
        return self._collection_design_version

    @property
    def common_crew_id(self) -> int:
        return self._common_crew_id

    @property
    def condition_type_version(self) -> int:
        return self._condition_type_version

    @property
    def craft_design_version(self) -> int:
        return self._craft_design_version

    @property
    def current_android_version(self) -> str:
        return self._current_android_version

    @property
    def daily_item_rewards(self) -> str:
        return self._daily_item_rewards

    @property
    def daily_reward_argument(self) -> int:
        return self._daily_reward_argument

    @property
    def daily_reward_type(self) -> str:
        return self._daily_reward_type

    @property
    def division_design_version(self) -> int:
        return self._division_design_version

    @property
    def draw_design_version(self) -> int:
        return self._draw_design_version

    @property
    def engine_efficiency_loss(self) -> float:
        return self._engine_efficiency_loss

    @property
    def feature_mask(self) -> int:
        return self._feature_mask

    @property
    def file_version(self) -> int:
        return self._file_version

    @property
    def flags(self) -> int:
        return self._flags

    @property
    def grace_period(self) -> int:
        return self._grace_period

    @property
    def hero_crew_id(self) -> int:
        return self._hero_crew_id

    @property
    def is_debug(self) -> bool:
        return self._is_debug

    @property
    def item_design_action_version(self) -> int:
        return self._item_design_action_version

    @property
    def item_design_version(self) -> int:
        return self._item_design_version

    @property
    def league_version(self) -> int:
        return self._league_version

    @property
    def left_loading_sprite_id(self) -> int:
        return self._left_loading_sprite_id

    @property
    def legendary_battle_count(self) -> int:
        return self._legendary_battle_count

    @property
    def legendary_doves_amount(self) -> int:
        return self._legendary_doves_amount

    @property
    def legendary_loot_percentage(self) -> int:
        return self._legendary_loot_percentage

    @property
    def legendary_result_reward_modifiers(self) -> str:
        return self._legendary_result_reward_modifiers

    @property
    def legendary_result_trophy_modifiers(self) -> str:
        return self._legendary_result_trophy_modifiers

    @property
    def legendary_rewards_text(self) -> str:
        return self._legendary_rewards_text

    @property
    def legendary_rules_text(self) -> str:
        return self._legendary_rules_text

    @property
    def legendary_trophy_in(self) -> int:
        return self._legendary_trophy_in

    @property
    def legendary_trophy_out(self) -> int:
        return self._legendary_trophy_out

    @property
    def limited_catalog_argument(self) -> int:
        return self._limited_catalog_argument

    @property
    def limited_catalog_currency_amount(self) -> int:
        return self._limited_catalog_currency_amount

    @property
    def limited_catalog_currency_type(self) -> str:
        return self._limited_catalog_currency_type

    @property
    def limited_catalog_expiry_date(self) -> _datetime:
        return self._limited_catalog_expiry_date

    @property
    def limited_catalog_max_total(self) -> int:
        return self._limited_catalog_max_total

    @property
    def limited_catalog_quantity(self) -> int:
        return self._limited_catalog_quantity

    @property
    def limited_catalog_restock_quantity(self) -> int:
        return self._limited_catalog_restock_quantity

    @property
    def limited_catalog_type(self) -> str:
        return self._limited_catalog_type

    @property
    def loading_ship_sprite_id(self) -> int:
        return self._loading_ship_sprite_id

    @property
    def loading_subtitle_sprite_id(self) -> int:
        return self._loading_subtitle_sprite_id

    @property
    def loading_title_sprite_id(self) -> int:
        return self._loading_title_sprite_id

    @property
    def loot_modifiers(self) -> str:
        return self._loot_modifiers

    @property
    def maintenance_date(self) -> _datetime:
        return self._maintenance_date

    @property
    def maintenance_message(self) -> str:
        return self._maintenance_message

    @property
    def maintenance_title(self) -> str:
        return self._maintenance_title

    @property
    def marker_generator_design_version(self) -> int:
        return self._marker_generator_design_version

    @property
    def max_boost_duration(self) -> int:
        return self._max_boost_duration

    @property
    def max_crews(self) -> int:
        return self._max_crews

    @property
    def max_daily_draws(self) -> int:
        return self._max_daily_draws

    @property
    def max_redemption_count(self) -> int:
        return self._max_redemption_count

    @property
    def max_redemption_count_per_month(self) -> int:
        return self._max_redemption_count_per_month

    @property
    def merchant_ship_exterior_sprite_id(self) -> int:
        return self._merchant_ship_exterior_sprite_id

    @property
    def merchant_ship_sprite_id(self) -> int:
        return self._merchant_ship_sprite_id

    @property
    def min_purchase_reward_points_for_starbux_trading(self) -> int:
        return self._min_purchase_reward_points_for_starbux_trading

    @property
    def min_trophies_for_starbux_trading(self) -> int:
        return self._min_trophies_for_starbux_trading

    @property
    def minimum_client_version(self) -> str:
        return self._minimum_client_version

    @property
    def minimum_version(self) -> str:
        return self._minimum_version

    @property
    def missile_design_version(self) -> int:
        return self._missile_design_version

    @property
    def mission_design_version(self) -> int:
        return self._mission_design_version

    @property
    def new_user_count(self) -> int:
        return self._new_user_count

    @property
    def news(self) -> str:
        return self._news

    @property
    def news_design_version(self) -> int:
        return self._news_design_version

    @property
    def news_sprite_id(self) -> int:
        return self._news_sprite_id

    @property
    def news_update_date(self) -> _datetime:
        return self._news_update_date

    @property
    def number_of_vote_options(self) -> int:
        return self._number_of_vote_options

    @property
    def planet_version(self) -> int:
        return self._planet_version

    @property
    def prestige_top_character_design_id(self) -> int:
        return self._prestige_top_character_design_id

    @property
    def pro_bono_limit(self) -> int:
        return self._pro_bono_limit

    @property
    def production_server(self) -> str:
        return self._production_server

    @property
    def promotion_design_version(self) -> int:
        return self._promotion_design_version

    @property
    def purge_period(self) -> int:
        return self._purge_period

    @property
    def recommended_version(self) -> str:
        return self._recommended_version

    @property
    def replay_available_date(self) -> _datetime:
        return self._replay_available_date

    @property
    def research_design_version(self) -> int:
        return self._research_design_version

    @property
    def reward_design_version(self) -> int:
        return self._reward_design_version

    @property
    def reward_point_percentage(self) -> int:
        return self._reward_point_percentage

    @property
    def reward_video_time_reduction(self) -> int:
        return self._reward_video_time_reduction

    @property
    def right_loading_sprite_id(self) -> int:
        return self._right_loading_sprite_id

    @property
    def room_design_purchase_version(self) -> int:
        return self._room_design_purchase_version

    @property
    def room_design_sprite_version(self) -> int:
        return self._room_design_sprite_version

    @property
    def room_design_version(self) -> int:
        return self._room_design_version

    @property
    def rush_tier_cost(self) -> int:
        return self._rush_tier_cost

    @property
    def sale_argument(self) -> int:
        return self._sale_argument

    @property
    def sale_end_date(self) -> _datetime:
        return self._sale_end_date

    @property
    def sale_item_mask(self) -> int:
        return self._sale_item_mask

    @property
    def sale_once_only(self) -> bool:
        return self._sale_once_only

    @property
    def sale_quantity(self) -> int:
        return self._sale_quantity

    @property
    def sale_start_date(self) -> _datetime:
        return self._sale_start_date

    @property
    def sale_title(self) -> str:
        return self._sale_title

    @property
    def sale_type(self) -> str:
        return self._sale_type

    @property
    def season_design_version(self) -> int:
        return self._season_design_version

    @property
    def server_setting_version(self) -> int:
        return self._server_setting_version

    @property
    def setting_id(self) -> int:
        return self._setting_id

    @property
    def ship_design_version(self) -> int:
        return self._ship_design_version

    @property
    def situation_design_version(self) -> int:
        return self._situation_design_version

    @property
    def situation_tags(self) -> str:
        return self._situation_tags

    @property
    def skin_set_version(self) -> int:
        return self._skin_set_version

    @property
    def skin_version(self) -> int:
        return self._skin_version

    @property
    def sprite_version(self) -> int:
        return self._sprite_version

    @property
    def star_system_link_version(self) -> int:
        return self._star_system_link_version

    @property
    def star_system_version(self) -> int:
        return self._star_system_version

    @property
    def support_email(self) -> str:
        return self._support_email

    @property
    def support_task_ran_date(self) -> _datetime:
        return self._support_task_ran_date

    @property
    def task_design_version(self) -> int:
        return self._task_design_version

    @property
    def task_reroll_cost(self) -> int:
        return self._task_reroll_cost

    @property
    def task_reroll_max_count(self) -> int:
        return self._task_reroll_max_count

    @property
    def tournament_bonus_score(self) -> int:
        return self._tournament_bonus_score

    @property
    def tournament_final_duration(self) -> int:
        return self._tournament_final_duration

    @property
    def tournament_news(self) -> str:
        return self._tournament_news

    @property
    def tournament_sprite_id(self) -> int:
        return self._tournament_sprite_id

    @property
    def training_design_version(self) -> int:
        return self._training_design_version

    @property
    def vip_design_version(self) -> int:
        return self._vip_design_version

    @property
    def voting_duration(self) -> int:
        return self._voting_duration

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

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "ABTestingRollout": self.ab_testing_rollout,
                "ABTestingStartDate": self.ab_testing_start_date,
                "AFeatureMask": self.a_feature_mask,
                "AbilityDesignVersion": self.ability_design_version,
                "AchievementDesignVersion": self.achievement_design_version,
                "ActionTypeVersion": self.action_type_version,
                "AllianceBadgeSpriteIds": self.alliance_badge_sprite_ids,
                "AnimationVersion": self.animation_version,
                "AssetVersion": self.asset_version,
                "BFeatureMask": self.b_feature_mask,
                "BackgroundId": self.background_id,
                "BackgroundVersion": self.background_version,
                "BattleBackgroundId": self.battle_background_id,
                "BoostDuration": self.boost_duration,
                "BoostGaugeMobile": self.boost_gauge_mobile,
                "BoostGaugePC": self.boost_gauge_pc,
                "BoostMultiplier": self.boost_multiplier,
                "CargoItems": self.cargo_items,
                "CargoPrices": self.cargo_prices,
                "ChallengeDesignVersion": self.challenge_design_version,
                "CharacterDesignActionVersion": self.character_design_action_version,
                "CharacterDesignVersion": self.character_design_version,
                "CharacterPartVersion": self.character_part_version,
                "ChecksumType": self.checksum_type,
                "ClientTranslationVersion": self.client_translation_version,
                "CollectionDesignVersion": self.collection_design_version,
                "CommonCrewId": self.common_crew_id,
                "ConditionTypeVersion": self.condition_type_version,
                "CraftDesignVersion": self.craft_design_version,
                "CurrentAndroidVersion": self.current_android_version,
                "DailyItemRewards": self.daily_item_rewards,
                "DailyRewardArgument": self.daily_reward_argument,
                "DailyRewardType": self.daily_reward_type,
                "DivisionDesignVersion": self.division_design_version,
                "DrawDesignVersion": self.draw_design_version,
                "EngineEfficiencyLoss": self.engine_efficiency_loss,
                "FeatureMask": self.feature_mask,
                "FileVersion": self.file_version,
                "Flags": self.flags,
                "GracePeriod": self.grace_period,
                "HeroCrewId": self.hero_crew_id,
                "IsDebug": self.is_debug,
                "ItemDesignActionVersion": self.item_design_action_version,
                "ItemDesignVersion": self.item_design_version,
                "LeagueVersion": self.league_version,
                "LeftLoadingSpriteId": self.left_loading_sprite_id,
                "LegendaryBattleCount": self.legendary_battle_count,
                "LegendaryDovesAmount": self.legendary_doves_amount,
                "LegendaryLootPercentage": self.legendary_loot_percentage,
                "LegendaryResultRewardModifiers": self.legendary_result_reward_modifiers,
                "LegendaryResultTrophyModifiers": self.legendary_result_trophy_modifiers,
                "LegendaryRewardsText": self.legendary_rewards_text,
                "LegendaryRulesText": self.legendary_rules_text,
                "LegendaryTrophyIn": self.legendary_trophy_in,
                "LegendaryTrophyOut": self.legendary_trophy_out,
                "LimitedCatalogArgument": self.limited_catalog_argument,
                "LimitedCatalogCurrencyAmount": self.limited_catalog_currency_amount,
                "LimitedCatalogCurrencyType": self.limited_catalog_currency_type,
                "LimitedCatalogExpiryDate": self.limited_catalog_expiry_date,
                "LimitedCatalogMaxTotal": self.limited_catalog_max_total,
                "LimitedCatalogQuantity": self.limited_catalog_quantity,
                "LimitedCatalogRestockQuantity": self.limited_catalog_restock_quantity,
                "LimitedCatalogType": self.limited_catalog_type,
                "LoadingShipSpriteId": self.loading_ship_sprite_id,
                "LoadingSubtitleSpriteId": self.loading_subtitle_sprite_id,
                "LoadingTitleSpriteId": self.loading_title_sprite_id,
                "LootModifiers": self.loot_modifiers,
                "MaintenanceDate": self.maintenance_date,
                "MaintenanceMessage": self.maintenance_message,
                "MaintenanceTitle": self.maintenance_title,
                "MarkerGeneratorDesignVersion": self.marker_generator_design_version,
                "MaxBoostDuration": self.max_boost_duration,
                "MaxCrews": self.max_crews,
                "MaxDailyDraws": self.max_daily_draws,
                "MaxRedemptionCount": self.max_redemption_count,
                "MaxRedemptionCountPerMonth": self.max_redemption_count_per_month,
                "MerchantShipExteriorSpriteId": self.merchant_ship_exterior_sprite_id,
                "MerchantShipSpriteId": self.merchant_ship_sprite_id,
                "MinPurchaseRewardPointsForStarbuxTrading": self.min_purchase_reward_points_for_starbux_trading,
                "MinTrophiesForStarbuxTrading": self.min_trophies_for_starbux_trading,
                "MinimumClientVersion": self.minimum_client_version,
                "MinimumVersion": self.minimum_version,
                "MissileDesignVersion": self.missile_design_version,
                "MissionDesignVersion": self.mission_design_version,
                "NewUserCount": self.new_user_count,
                "News": self.news,
                "NewsDesignVersion": self.news_design_version,
                "NewsSpriteId": self.news_sprite_id,
                "NewsUpdateDate": self.news_update_date,
                "NumberOfVoteOptions": self.number_of_vote_options,
                "PlanetVersion": self.planet_version,
                "PrestigeTopCharacterDesignId": self.prestige_top_character_design_id,
                "ProBonoLimit": self.pro_bono_limit,
                "ProductionServer": self.production_server,
                "PromotionDesignVersion": self.promotion_design_version,
                "PurgePeriod": self.purge_period,
                "RecommendedVersion": self.recommended_version,
                "ReplayAvailableDate": self.replay_available_date,
                "ResearchDesignVersion": self.research_design_version,
                "RewardDesignVersion": self.reward_design_version,
                "RewardPointPercentage": self.reward_point_percentage,
                "RewardVideoTimeReduction": self.reward_video_time_reduction,
                "RightLoadingSpriteId": self.right_loading_sprite_id,
                "RoomDesignPurchaseVersion": self.room_design_purchase_version,
                "RoomDesignSpriteVersion": self.room_design_sprite_version,
                "RoomDesignVersion": self.room_design_version,
                "RushTierCost": self.rush_tier_cost,
                "SaleArgument": self.sale_argument,
                "SaleEndDate": self.sale_end_date,
                "SaleItemMask": self.sale_item_mask,
                "SaleOnceOnly": self.sale_once_only,
                "SaleQuantity": self.sale_quantity,
                "SaleStartDate": self.sale_start_date,
                "SaleTitle": self.sale_title,
                "SaleType": self.sale_type,
                "SeasonDesignVersion": self.season_design_version,
                "ServerSettingVersion": self.server_setting_version,
                "SettingId": self.setting_id,
                "ShipDesignVersion": self.ship_design_version,
                "SituationDesignVersion": self.situation_design_version,
                "SituationTags": self.situation_tags,
                "SkinSetVersion": self.skin_set_version,
                "SkinVersion": self.skin_version,
                "SpriteVersion": self.sprite_version,
                "StarSystemLinkVersion": self.star_system_link_version,
                "StarSystemVersion": self.star_system_version,
                "SupportEmail": self.support_email,
                "SupportTaskRanDate": self.support_task_ran_date,
                "TaskDesignVersion": self.task_design_version,
                "TaskRerollCost": self.task_reroll_cost,
                "TaskRerollMaxCount": self.task_reroll_max_count,
                "TournamentBonusScore": self.tournament_bonus_score,
                "TournamentFinalDuration": self.tournament_final_duration,
                "TournamentNews": self.tournament_news,
                "TournamentSpriteId": self.tournament_sprite_id,
                "TrainingDesignVersion": self.training_design_version,
                "VipDesignVersion": self.vip_design_version,
                "VotingDuration": self.voting_duration,
            }
            self._dict.update(super().__dict__())

        return self._dict
