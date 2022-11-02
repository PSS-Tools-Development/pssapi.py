"""
    This file has been generated automatically
"""

from datetime import datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class SettingRaw:
    XML_NODE_NAME: str = 'Setting'

    def __init__(self, setting_info: _EntityInfo) -> None:
        self.__limited_catalog_restock_quantity: str = _parse.pss_str(
            setting_info.get('LimitedCatalogRestockQuantity'))
        self.__ab_testing_rollout: int = _parse.pss_int(
            setting_info.get('ABTestingRollout'))
        self.__room_design_sprite_version: int = _parse.pss_int(
            setting_info.get('RoomDesignSpriteVersion'))
        self.__star_system_version: int = _parse.pss_int(
            setting_info.get('StarSystemVersion'))
        self.__animation_version: int = _parse.pss_int(
            setting_info.get('AnimationVersion'))
        self.__item_design_version: int = _parse.pss_int(
            setting_info.get('ItemDesignVersion'))
        self.__mission_design_version: int = _parse.pss_int(
            setting_info.get('MissionDesignVersion'))
        self.__server_setting_version: int = _parse.pss_int(
            setting_info.get('ServerSettingVersion'))
        self.__common_crew_id: str = _parse.pss_str(
            setting_info.get('CommonCrewId'))
        self.__is_debug: bool = _parse.pss_bool(setting_info.get('IsDebug'))
        self.__right_loading_sprite_id: int = _parse.pss_int(
            setting_info.get('RightLoadingSpriteId'))
        self.__alliance_badge_sprite_ids: str = _parse.pss_str(
            setting_info.get('AllianceBadgeSpriteIds'))
        self.__prestige_top_character_design_id: int = _parse.pss_int(
            setting_info.get('PrestigeTopCharacterDesignId'))
        self.__reward_design_version: int = _parse.pss_int(
            setting_info.get('RewardDesignVersion'))
        self.__file_version: int = _parse.pss_int(
            setting_info.get('FileVersion'))
        self.__task_reroll_max_count: int = _parse.pss_int(
            setting_info.get('TaskRerollMaxCount'))
        self.__sale_item_mask: str = _parse.pss_str(
            setting_info.get('SaleItemMask'))
        self.__boost_duration: int = _parse.pss_int(
            setting_info.get('BoostDuration'))
        self.__daily_reward_argument: str = _parse.pss_str(
            setting_info.get('DailyRewardArgument'))
        self.__item_design_action_version: int = _parse.pss_int(
            setting_info.get('ItemDesignActionVersion'))
        self.__tournament_final_duration: int = _parse.pss_int(
            setting_info.get('TournamentFinalDuration'))
        self.__season_design_version: int = _parse.pss_int(
            setting_info.get('SeasonDesignVersion'))
        self.__marker_generator_design_version: str = _parse.pss_str(
            setting_info.get('MarkerGeneratorDesignVersion'))
        self.__current_android_version: str = _parse.pss_str(
            setting_info.get('CurrentAndroidVersion'))
        self.__character_part_version: int = _parse.pss_int(
            setting_info.get('CharacterPartVersion'))
        self.__ship_design_version: int = _parse.pss_int(
            setting_info.get('ShipDesignVersion'))
        self.__minimum_version: str = _parse.pss_str(
            setting_info.get('MinimumVersion'))
        self.__legendary_trophy_out: int = _parse.pss_int(
            setting_info.get('LegendaryTrophyOut'))
        self.__star_system_link_version: int = _parse.pss_int(
            setting_info.get('StarSystemLinkVersion'))
        self.__flags: int = _parse.pss_int(setting_info.get('Flags'))
        self.__room_design_purchase_version: int = _parse.pss_int(
            setting_info.get('RoomDesignPurchaseVersion'))
        self.__research_design_version: int = _parse.pss_int(
            setting_info.get('ResearchDesignVersion'))
        self.__grace_period: int = _parse.pss_int(
            setting_info.get('GracePeriod'))
        self.__legendary_result_trophy_modifiers: str = _parse.pss_str(
            setting_info.get('LegendaryResultTrophyModifiers'))
        self.__limited_catalog_currency_type: str = _parse.pss_str(
            setting_info.get('LimitedCatalogCurrencyType'))
        self.__replay_available_date: datetime = _parse.pss_datetime(
            setting_info.get('ReplayAvailableDate'))
        self.__task_design_version: int = _parse.pss_int(
            setting_info.get('TaskDesignVersion'))
        self.__purge_period: int = _parse.pss_int(
            setting_info.get('PurgePeriod'))
        self.__craft_design_version: int = _parse.pss_int(
            setting_info.get('CraftDesignVersion'))
        self.__missile_design_version: int = _parse.pss_int(
            setting_info.get('MissileDesignVersion'))
        self.__sale_start_date: str = _parse.pss_str(
            setting_info.get('SaleStartDate'))
        self.__recommended_version: str = _parse.pss_str(
            setting_info.get('RecommendedVersion'))
        self.__b_feature_mask: int = _parse.pss_int(
            setting_info.get('BFeatureMask'))
        self.__news: str = _parse.pss_str(setting_info.get('News'))
        self.__client_translation_version: int = _parse.pss_int(
            setting_info.get('ClientTranslationVersion'))
        self.__task_reroll_cost: int = _parse.pss_int(
            setting_info.get('TaskRerollCost'))
        self.__legendary_result_reward_modifiers: str = _parse.pss_str(
            setting_info.get('LegendaryResultRewardModifiers'))
        self.__loading_title_sprite_id: int = _parse.pss_int(
            setting_info.get('LoadingTitleSpriteId'))
        self.__limited_catalog_quantity: str = _parse.pss_str(
            setting_info.get('LimitedCatalogQuantity'))
        self.__rush_tier_cost: int = _parse.pss_int(
            setting_info.get('RushTierCost'))
        self.__situation_design_version: int = _parse.pss_int(
            setting_info.get('SituationDesignVersion'))
        self.__checksum_type: str = _parse.pss_str(
            setting_info.get('ChecksumType'))
        self.__collection_design_version: int = _parse.pss_int(
            setting_info.get('CollectionDesignVersion'))
        self.__maintenance_message: str = _parse.pss_str(
            setting_info.get('MaintenanceMessage'))
        self.__minimum_client_version: str = _parse.pss_str(
            setting_info.get('MinimumClientVersion'))
        self.__limited_catalog_type: str = _parse.pss_str(
            setting_info.get('LimitedCatalogType'))
        self.__legendary_rules_text: str = _parse.pss_str(
            setting_info.get('LegendaryRulesText'))
        self.__loading_subtitle_sprite_id: int = _parse.pss_int(
            setting_info.get('LoadingSubtitleSpriteId'))
        self.__legendary_battle_count: int = _parse.pss_int(
            setting_info.get('LegendaryBattleCount'))
        self.__feature_mask: int = _parse.pss_int(
            setting_info.get('FeatureMask'))
        self.__background_version: int = _parse.pss_int(
            setting_info.get('BackgroundVersion'))
        self.__sale_argument: str = _parse.pss_str(
            setting_info.get('SaleArgument'))
        self.__sale_quantity: str = _parse.pss_str(
            setting_info.get('SaleQuantity'))
        self.__max_boost_duration: int = _parse.pss_int(
            setting_info.get('MaxBoostDuration'))
        self.__a_feature_mask: int = _parse.pss_int(
            setting_info.get('AFeatureMask'))
        self.__tournament_bonus_score: int = _parse.pss_int(
            setting_info.get('TournamentBonusScore'))
        self.__loot_modifiers: str = _parse.pss_str(
            setting_info.get('LootModifiers'))
        self.__vip_design_version: int = _parse.pss_int(
            setting_info.get('VipDesignVersion'))
        self.__asset_version: int = _parse.pss_int(
            setting_info.get('AssetVersion'))
        self.__reward_point_percentage: int = _parse.pss_int(
            setting_info.get('RewardPointPercentage'))
        self.__league_version: int = _parse.pss_int(
            setting_info.get('LeagueVersion'))
        self.__tournament_sprite_id: int = _parse.pss_int(
            setting_info.get('TournamentSpriteId'))
        self.__daily_item_rewards: str = _parse.pss_str(
            setting_info.get('DailyItemRewards'))
        self.__tournament_news: str = _parse.pss_str(
            setting_info.get('TournamentNews'))
        self.__loading_ship_sprite_id: int = _parse.pss_int(
            setting_info.get('LoadingShipSpriteId'))
        self.__cargo_items: str = _parse.pss_str(
            setting_info.get('CargoItems'))
        self.__battle_background_id: int = _parse.pss_int(
            setting_info.get('BattleBackgroundId'))
        self.__new_user_count: int = _parse.pss_int(
            setting_info.get('NewUserCount'))
        self.__legendary_doves_amount: int = _parse.pss_int(
            setting_info.get('LegendaryDovesAmount'))
        self.__daily_reward_type: str = _parse.pss_str(
            setting_info.get('DailyRewardType'))
        self.__production_server: str = _parse.pss_str(
            setting_info.get('ProductionServer'))
        self.__character_design_version: int = _parse.pss_int(
            setting_info.get('CharacterDesignVersion'))
        self.__limited_catalog_expiry_date: str = _parse.pss_str(
            setting_info.get('LimitedCatalogExpiryDate'))
        self.__max_daily_draws: int = _parse.pss_int(
            setting_info.get('MaxDailyDraws'))
        self.__news_sprite_id: str = _parse.pss_str(
            setting_info.get('NewsSpriteId'))
        self.__sale_title: str = _parse.pss_str(setting_info.get('SaleTitle'))
        self.__division_design_version: int = _parse.pss_int(
            setting_info.get('DivisionDesignVersion'))
        self.__draw_design_version: int = _parse.pss_int(
            setting_info.get('DrawDesignVersion'))
        self.__achievement_design_version: int = _parse.pss_int(
            setting_info.get('AchievementDesignVersion'))
        self.__training_design_version: int = _parse.pss_int(
            setting_info.get('TrainingDesignVersion'))
        self.__pro_bono_limit: int = _parse.pss_int(
            setting_info.get('ProBonoLimit'))
        self.__setting_id: int = _parse.pss_int(setting_info.get('SettingId'))
        self.__sale_type: str = _parse.pss_str(setting_info.get('SaleType'))
        self.__challenge_design_version: int = _parse.pss_int(
            setting_info.get('ChallengeDesignVersion'))
        self.__background_id: int = _parse.pss_int(
            setting_info.get('BackgroundId'))
        self.__sprite_version: int = _parse.pss_int(
            setting_info.get('SpriteVersion'))
        self.__legendary_loot_percentage: int = _parse.pss_int(
            setting_info.get('LegendaryLootPercentage'))
        self.__sale_once_only: str = _parse.pss_str(
            setting_info.get('SaleOnceOnly'))
        self.__limited_catalog_max_total: str = _parse.pss_str(
            setting_info.get('LimitedCatalogMaxTotal'))
        self.__promotion_design_version: int = _parse.pss_int(
            setting_info.get('PromotionDesignVersion'))
        self.__condition_type_version: int = _parse.pss_int(
            setting_info.get('ConditionTypeVersion'))
        self.__boost_multiplier: int = _parse.pss_int(
            setting_info.get('BoostMultiplier'))
        self.__sale_end_date: str = _parse.pss_str(
            setting_info.get('SaleEndDate'))
        self.__planet_version: int = _parse.pss_int(
            setting_info.get('PlanetVersion'))
        self.__character_design_action_version: int = _parse.pss_int(
            setting_info.get('CharacterDesignActionVersion'))
        self.__legendary_rewards_text: str = _parse.pss_str(
            setting_info.get('LegendaryRewardsText'))
        self.__room_design_version: int = _parse.pss_int(
            setting_info.get('RoomDesignVersion'))
        self.__news_update_date: datetime = _parse.pss_datetime(
            setting_info.get('NewsUpdateDate'))
        self.__limited_catalog_currency_amount: str = _parse.pss_str(
            setting_info.get('LimitedCatalogCurrencyAmount'))
        self.__cargo_prices: str = _parse.pss_str(
            setting_info.get('CargoPrices'))
        self.__ab_testing_start_date: datetime = _parse.pss_datetime(
            setting_info.get('ABTestingStartDate'))
        self.__action_type_version: int = _parse.pss_int(
            setting_info.get('ActionTypeVersion'))
        self.__news_design_version: int = _parse.pss_int(
            setting_info.get('NewsDesignVersion'))
        self.__support_task_ran_date: datetime = _parse.pss_datetime(
            setting_info.get('SupportTaskRanDate'))
        self.__hero_crew_id: str = _parse.pss_str(
            setting_info.get('HeroCrewId'))
        self.__limited_catalog_argument: str = _parse.pss_str(
            setting_info.get('LimitedCatalogArgument'))
        self.__ability_design_version: int = _parse.pss_int(
            setting_info.get('AbilityDesignVersion'))
        self.__reward_video_time_reduction: int = _parse.pss_int(
            setting_info.get('RewardVideoTimeReduction'))
        self.__left_loading_sprite_id: int = _parse.pss_int(
            setting_info.get('LeftLoadingSpriteId'))
        self.__legendary_trophy_in: int = _parse.pss_int(
            setting_info.get('LegendaryTrophyIn'))

    @property
    def limited_catalog_restock_quantity(self) -> str:
        return self.__limited_catalog_restock_quantity

    @property
    def ab_testing_rollout(self) -> int:
        return self.__ab_testing_rollout

    @property
    def room_design_sprite_version(self) -> int:
        return self.__room_design_sprite_version

    @property
    def star_system_version(self) -> int:
        return self.__star_system_version

    @property
    def animation_version(self) -> int:
        return self.__animation_version

    @property
    def item_design_version(self) -> int:
        return self.__item_design_version

    @property
    def mission_design_version(self) -> int:
        return self.__mission_design_version

    @property
    def server_setting_version(self) -> int:
        return self.__server_setting_version

    @property
    def common_crew_id(self) -> str:
        return self.__common_crew_id

    @property
    def is_debug(self) -> bool:
        return self.__is_debug

    @property
    def right_loading_sprite_id(self) -> int:
        return self.__right_loading_sprite_id

    @property
    def alliance_badge_sprite_ids(self) -> str:
        return self.__alliance_badge_sprite_ids

    @property
    def prestige_top_character_design_id(self) -> int:
        return self.__prestige_top_character_design_id

    @property
    def reward_design_version(self) -> int:
        return self.__reward_design_version

    @property
    def file_version(self) -> int:
        return self.__file_version

    @property
    def task_reroll_max_count(self) -> int:
        return self.__task_reroll_max_count

    @property
    def sale_item_mask(self) -> str:
        return self.__sale_item_mask

    @property
    def boost_duration(self) -> int:
        return self.__boost_duration

    @property
    def daily_reward_argument(self) -> str:
        return self.__daily_reward_argument

    @property
    def item_design_action_version(self) -> int:
        return self.__item_design_action_version

    @property
    def tournament_final_duration(self) -> int:
        return self.__tournament_final_duration

    @property
    def season_design_version(self) -> int:
        return self.__season_design_version

    @property
    def marker_generator_design_version(self) -> str:
        return self.__marker_generator_design_version

    @property
    def current_android_version(self) -> str:
        return self.__current_android_version

    @property
    def character_part_version(self) -> int:
        return self.__character_part_version

    @property
    def ship_design_version(self) -> int:
        return self.__ship_design_version

    @property
    def minimum_version(self) -> str:
        return self.__minimum_version

    @property
    def legendary_trophy_out(self) -> int:
        return self.__legendary_trophy_out

    @property
    def star_system_link_version(self) -> int:
        return self.__star_system_link_version

    @property
    def flags(self) -> int:
        return self.__flags

    @property
    def room_design_purchase_version(self) -> int:
        return self.__room_design_purchase_version

    @property
    def research_design_version(self) -> int:
        return self.__research_design_version

    @property
    def grace_period(self) -> int:
        return self.__grace_period

    @property
    def legendary_result_trophy_modifiers(self) -> str:
        return self.__legendary_result_trophy_modifiers

    @property
    def limited_catalog_currency_type(self) -> str:
        return self.__limited_catalog_currency_type

    @property
    def replay_available_date(self) -> datetime:
        return self.__replay_available_date

    @property
    def task_design_version(self) -> int:
        return self.__task_design_version

    @property
    def purge_period(self) -> int:
        return self.__purge_period

    @property
    def craft_design_version(self) -> int:
        return self.__craft_design_version

    @property
    def missile_design_version(self) -> int:
        return self.__missile_design_version

    @property
    def sale_start_date(self) -> str:
        return self.__sale_start_date

    @property
    def recommended_version(self) -> str:
        return self.__recommended_version

    @property
    def b_feature_mask(self) -> int:
        return self.__b_feature_mask

    @property
    def news(self) -> str:
        return self.__news

    @property
    def client_translation_version(self) -> int:
        return self.__client_translation_version

    @property
    def task_reroll_cost(self) -> int:
        return self.__task_reroll_cost

    @property
    def legendary_result_reward_modifiers(self) -> str:
        return self.__legendary_result_reward_modifiers

    @property
    def loading_title_sprite_id(self) -> int:
        return self.__loading_title_sprite_id

    @property
    def limited_catalog_quantity(self) -> str:
        return self.__limited_catalog_quantity

    @property
    def rush_tier_cost(self) -> int:
        return self.__rush_tier_cost

    @property
    def situation_design_version(self) -> int:
        return self.__situation_design_version

    @property
    def checksum_type(self) -> str:
        return self.__checksum_type

    @property
    def collection_design_version(self) -> int:
        return self.__collection_design_version

    @property
    def maintenance_message(self) -> str:
        return self.__maintenance_message

    @property
    def minimum_client_version(self) -> str:
        return self.__minimum_client_version

    @property
    def limited_catalog_type(self) -> str:
        return self.__limited_catalog_type

    @property
    def legendary_rules_text(self) -> str:
        return self.__legendary_rules_text

    @property
    def loading_subtitle_sprite_id(self) -> int:
        return self.__loading_subtitle_sprite_id

    @property
    def legendary_battle_count(self) -> int:
        return self.__legendary_battle_count

    @property
    def feature_mask(self) -> int:
        return self.__feature_mask

    @property
    def background_version(self) -> int:
        return self.__background_version

    @property
    def sale_argument(self) -> str:
        return self.__sale_argument

    @property
    def sale_quantity(self) -> str:
        return self.__sale_quantity

    @property
    def max_boost_duration(self) -> int:
        return self.__max_boost_duration

    @property
    def a_feature_mask(self) -> int:
        return self.__a_feature_mask

    @property
    def tournament_bonus_score(self) -> int:
        return self.__tournament_bonus_score

    @property
    def loot_modifiers(self) -> str:
        return self.__loot_modifiers

    @property
    def vip_design_version(self) -> int:
        return self.__vip_design_version

    @property
    def asset_version(self) -> int:
        return self.__asset_version

    @property
    def reward_point_percentage(self) -> int:
        return self.__reward_point_percentage

    @property
    def league_version(self) -> int:
        return self.__league_version

    @property
    def tournament_sprite_id(self) -> int:
        return self.__tournament_sprite_id

    @property
    def daily_item_rewards(self) -> str:
        return self.__daily_item_rewards

    @property
    def tournament_news(self) -> str:
        return self.__tournament_news

    @property
    def loading_ship_sprite_id(self) -> int:
        return self.__loading_ship_sprite_id

    @property
    def cargo_items(self) -> str:
        return self.__cargo_items

    @property
    def battle_background_id(self) -> int:
        return self.__battle_background_id

    @property
    def new_user_count(self) -> int:
        return self.__new_user_count

    @property
    def legendary_doves_amount(self) -> int:
        return self.__legendary_doves_amount

    @property
    def daily_reward_type(self) -> str:
        return self.__daily_reward_type

    @property
    def production_server(self) -> str:
        return self.__production_server

    @property
    def character_design_version(self) -> int:
        return self.__character_design_version

    @property
    def limited_catalog_expiry_date(self) -> str:
        return self.__limited_catalog_expiry_date

    @property
    def max_daily_draws(self) -> int:
        return self.__max_daily_draws

    @property
    def news_sprite_id(self) -> str:
        return self.__news_sprite_id

    @property
    def sale_title(self) -> str:
        return self.__sale_title

    @property
    def division_design_version(self) -> int:
        return self.__division_design_version

    @property
    def draw_design_version(self) -> int:
        return self.__draw_design_version

    @property
    def achievement_design_version(self) -> int:
        return self.__achievement_design_version

    @property
    def training_design_version(self) -> int:
        return self.__training_design_version

    @property
    def pro_bono_limit(self) -> int:
        return self.__pro_bono_limit

    @property
    def setting_id(self) -> int:
        return self.__setting_id

    @property
    def sale_type(self) -> str:
        return self.__sale_type

    @property
    def challenge_design_version(self) -> int:
        return self.__challenge_design_version

    @property
    def background_id(self) -> int:
        return self.__background_id

    @property
    def sprite_version(self) -> int:
        return self.__sprite_version

    @property
    def legendary_loot_percentage(self) -> int:
        return self.__legendary_loot_percentage

    @property
    def sale_once_only(self) -> str:
        return self.__sale_once_only

    @property
    def limited_catalog_max_total(self) -> str:
        return self.__limited_catalog_max_total

    @property
    def promotion_design_version(self) -> int:
        return self.__promotion_design_version

    @property
    def condition_type_version(self) -> int:
        return self.__condition_type_version

    @property
    def boost_multiplier(self) -> int:
        return self.__boost_multiplier

    @property
    def sale_end_date(self) -> str:
        return self.__sale_end_date

    @property
    def planet_version(self) -> int:
        return self.__planet_version

    @property
    def character_design_action_version(self) -> int:
        return self.__character_design_action_version

    @property
    def legendary_rewards_text(self) -> str:
        return self.__legendary_rewards_text

    @property
    def room_design_version(self) -> int:
        return self.__room_design_version

    @property
    def news_update_date(self) -> datetime:
        return self.__news_update_date

    @property
    def limited_catalog_currency_amount(self) -> str:
        return self.__limited_catalog_currency_amount

    @property
    def cargo_prices(self) -> str:
        return self.__cargo_prices

    @property
    def ab_testing_start_date(self) -> datetime:
        return self.__ab_testing_start_date

    @property
    def action_type_version(self) -> int:
        return self.__action_type_version

    @property
    def news_design_version(self) -> int:
        return self.__news_design_version

    @property
    def support_task_ran_date(self) -> datetime:
        return self.__support_task_ran_date

    @property
    def hero_crew_id(self) -> str:
        return self.__hero_crew_id

    @property
    def limited_catalog_argument(self) -> str:
        return self.__limited_catalog_argument

    @property
    def ability_design_version(self) -> int:
        return self.__ability_design_version

    @property
    def reward_video_time_reduction(self) -> int:
        return self.__reward_video_time_reduction

    @property
    def left_loading_sprite_id(self) -> int:
        return self.__left_loading_sprite_id

    @property
    def legendary_trophy_in(self) -> int:
        return self.__legendary_trophy_in
