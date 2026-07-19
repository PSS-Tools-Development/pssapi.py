# Version 0.7.1
## Updated Library
The library has been updated to Pixel Starships v0.999.44.15532 (Steam)
### Changes to Services
- Added `BattleService`
  - Added method `get_engagement`
  - Added `BattleServiceUtils`
- Changed `AllianceService`
  - Changed return types of method `list_users`
- Changed `DesignService`
  - Added method `list_all_static_designs`
- Changed `GalaxyService`
  - Added method `get_star_system_details`
- Changed `PublicService`
  - Added method `get_ship_characters_by_username`
- Changed `UserService`
  - Added method `list_all_user_data_first`
  - Changed method `steam_login` to use new method `UserServiceRaw.steam_login_8`
### Changed to Raw Services
- Added `BattleServiceRaw`
  - Added method `get_engagement`
- Changed `AllianceServiceRaw`
  - Changed return types of method `list_users_2`
- Changed `DesignServiceRaw`
  - Added method `list_all_static_designs_2`
- Changed `GalaxyService`
  - Added method `get_star_system_details`
- Changed `PublicService`
  - Added method `get_ship_characters_by_username`
- Changed `ShipServiceRaw`
  - Added method `list_ship_layouts`
- Changed `UserServiceRaw`
  - Added method `list_all_user_data_first_2`
  - Added method `steam_login_8`
### Changes to Entities
- Added `Achievement`
- Added `AllianceTask`
- Added `AttackingEngagementGroup`
- Added `DefendingEngagementGroup`
- Added `Engagement`
- Added `EngagementGroupUser`
- Added `InfrastructureDesign`
- Added `Situation`
- Added `StarSystemDetail`
- Added `StarSystemInfrastructureDesign`
- Added `StarSystemInfrastructures`
- Added `Task`
- Added `UserSkin`
- Changed `AchievementDesign`
  - Added property `achievement_scoring_type_enum` (`pssapi.enums.AchievementScoringType`)
- Changed `CraftDesign`
  - Added property `craft_pathing_type_enum` (`pssapi.enums.CraftPathingType`)
### Changes to Raw Entities
- Added `AchievementRaw`
- Added `AllianceTaskRaw`
- Added `AttackingEngagementGroupRaw`
- Added `DefendingEngagementGroupRaw`
- Added `EngagementRaw`
- Added `EngagementGroupUserRaw`
- Added `InfrastructureDesignRaw`
- Added `SituationRaw`
- Added `StarSystemDetailRaw`
- Added `StarSystemInfrastructureDesignRaw`
- Added `StarSystemInfrastructuresRaw`
- Added `TaskRaw`
- Added `UserSkinRaw`
- Changed `AchievementDesignRaw`
  - Added property `achievement_scoring_type` (`str`)
  - Added property `achievement_type_argument` (`int`)
  - Added property `objective_argument` (`str`)
  - Added property `objective_type` (`str`)
  - Added property `ribbon_sprite_id` (`int`)
- Changed `BattleRaw`
  - Added property `attacking_engagement_group_user_id` (`int`)
  - Added property `attacking_ship_design_id` (`int`)
  - Added property `attacking_user_type` (`str`)
  - Added property `client_version` (`str`)
  - Added property `defending_engagement_group_user_id` (`int`)
  - Added property `defending_ship_design_id` (`int`)
  - Added property `defending_user_type` (`str`)
  - Added property `engagement_id` (`int`)
- Changed `ChallengeDesignRaw`
  - Added property `objective_argument` (`str`)
  - Added property `objective_condition` (`str`)
  - Added property `score_title` (`str`)
- Changed `CharacterDesignRaw`
  - Added property `metadata` (`str`)
- Changed `CharacterPartRaw`
  - Added property `flags` (`int`)
- Changed `CharacterRaw`
  - Changed property `character_id` type (`int` -> `str`)
- Changed `ConditionTypeRaw`
  - Added property `condition_category_argument` (`str`)
- Changed `CraftDesignRaw`
  - Added property `capacity` (`int`)
  - Added property `root_craft_design_id` (`int`)
- Changed `DrawDesignRaw`
  - Added property `guaranteed_heroic_draws` (`int`)
  - Added property `visibility_flags` (`str`)
- Changed `MessageRaw`
  - Added property `ribbon_sprite_id` (`int`)
- Changed `MissileDesignRaw`
  - Added property `root_missile_design_id` (`int`)
- Changed `RewardDesignRaw`
  - Added property `bonus_reward_string` (`str`)
- Changed `RoomDesignRaw`
  - Added property `min_starbase_ship_level` (`int`)
  - Added property `starbase_price_string` (`str`)
- Changed `RoomRaw`
  - Added property `priority` (`int`)
- Changed `SettingRaw`
  - Added property `ama_message` (`str`)
  - Added property `ama_start_date` (`datetime.datetime`)
  - Added property `bank_groups` (`str`)
  - Added property `battle_searches_hard_limit` (`int`)
  - Added property `capped_value_for_star_battle_max_range` (`int`)
  - Added property `cost_string_to_search` (`str`)
  - Added property `cost_to_search_multiplier` (`int`)
  - Added property `creator_code_duration` (`int`)
  - Added property `engagement_invasion_duration` (`int`)
  - Added property `engagement_power_per_supply_cost` (`int`)
  - Added property `engagement_raid_duration` (`int`)
  - Added property `engagement_supply_reward_percentage` (`int`)
  - Added property `featured_video_url` (`str`)
  - Added property `infrastructure_design_version` (`int`)
  - Added property `lower_base_value_for_star_battle` (`int`)
  - Added property `max_battle_searches` (`int`)
  - Added property `max_engagement_supply_cost` (`int`)
  - Added property `max_star_systems_per_fleet` (`int`)
  - Added property `min_engagement_supply_cost` (`int`)
  - Added property `min_ship_level_for_sync_server` (`int`)
  - Added property `star_system_cooldown_modifier` (`float`)
  - Added property `star_system_infrastructure_design_version` (`int`)
  - Added property `starbux_market_price_cap` (`int`)
  - Added property `step_for_star_battle_max_range` (`int`)
  - Added property `step_for_star_battle_min_range` (`int`)
  - Added property `tournament_immunity_time_in_seconds` (`int`)
  - Added property `upper_base_value_for_star_battle` (`int`)
  - Added property `user_engagement_cooldowntime` (`int`)
- Changed `ShipDesignRaw`
  - Added property `attacks` (`int`)
  - Added property `lives` (`int`)
  - Added property `metadata` (`str`)
- Changed `SkinSetRaw`
  - Added property `purchase_count` (`int`)
- Changed `StarSystemMarkerRaw`
  - Added property `engagement_id` (`int`)
- Changed `StarSystemRaw`
  - Added property `background_sprite_id` (`int`)
- Changed `TrainingRaw`
  - Added property `variable_chance` (`float`)
- Changed `UserLoginRaw`
  - Added property `battle` (`pssapi.entities.Battle`)
  - Added property `reward_string` (`str`)
- Changed `UserRaw`
  - Added property `alliance_score_at_start_of_day` (`int`)
  - Added property `creator_code` (`str`)
  - Added property `creator_support_date` (`datetime.datetime`)
  - Added property `draws_string` (`str`)
  - Added property `engagement_cooldown_end_date` (`datetime.datetime`)
  - Added property `pv_p_continuous_losses` (`int`)
  - Added property `ribbon_sprite_id` (`int`)
  - Added property `total_battle_searches` (`int`)
### Changes to Enums
- Added enum `AchievementScoringType`
- Added enum `CraftPathingType`
- Added enum `EngagementApprovalState`
- Added enum `EngagementGroupUserState`
- Added enum `EngagementScoringType`
- Added enum `EngagementType`
- Added enum `InfrastructureRewardType`
- Added enum `InfrastructureType`
- Added enum `SituationCategory`
# Version 0.6.0
tbd
# Version 0.5.0
## Changes
### Added
- Implemented Issue [#59](https://github.com/PSS-Tools-Development/pssapi.py/issues/59)
## Updated Library
The library has been updated to Pixel Starships v0.998.17.11192 (Steam) & v0.999.11374 (Steam, staging branch).
### Changes to Services
- Added `PublicService`
  - Added method `get_ship_details`
  - Added method `get_ship_room_details`
- Changed `UserService`
  - Added method `list_skin_sets`
  - Changed method `list_skins` to use new endpoint
### Changes to Raw Services
- Added `PublicServiceRaw`
  - Added method `get_ship_details`
  - Added method `get_ship_room_details`
- Changed `UserServiceRaw`
  - Added method `list_skin_sets_2`
  - Changed method `list_skins_2`
### Changes to Raw Entities
- Changed `ActionTypeRaw`
  - Added property `condition_parameter_argument` (`int`)
- Changed `CharacterDesignRaw`
  - Added property `boost_values_string` (`str`)
- Changed `CharacterRaw`
  - Added property `bonus_training_capacity` (`int`)
  - Added property `boost_level` (`int`)
- Changed `CollectionDesignRaw`
  - Added property `cooldown_time` (`int`)
  - Added property `metadata` (`str`)
  - Added property `step_enhancement_value` (`float`)
  - Added property `trigger_animation_id` (`int`)
- Changed `ConditionTypeRaw`
  - Added property `condition_parameter_argument` (`int`)
- Changed `CraftDesignRaw`
  - Added property `craft_pathing_type` (`str`)
  - Added property `entity_count` (`int`)
- Changed `RoomDesignRaw`
  - Added property `room_variant_type` (`int`)
- Changed `SeasonDesignRaw`
  - Added property `premium_reward_string` (`str`)
  - Added property `repeat_reward_string` (`str`)
- Changed `SettingRaw`
  - Added property `max_crews` (`int`)
### Changes to utilities
- Added sub-module `pss` with functions `is_tournament_time`
- Added function `get_first_of_next_month` to sub-module `datetime`
# Version 0.4.1
## Changes
### Added
- `EntityRaw` classes now store any properties parsed from the XML nodes that aren't currently tracked in fields and properties in this library. This allows consumers to access properties that SavySoda added, without having to wait for the library to get updated.
### Changed
- `EntityRaw` classes now inherit from `EntityBaseRaw` class.
### Fixed
- Error messages returned in XML root node by the PSS API now get recognized properly.
## Updated Library
Updated to Pixel Starships v0.998.16.11048 (Steam, testing branch).
The newly added endpoints `/DesignService/ListAllDynamicDesigns` & `/DesignService/ListAllStaticDesigns` will be added with a future version of the library.
## Testing
Changed the `record_mode` for `vcrpy` cassettes back to `once`. Set it to `rewrite` temporarily to have the cassettes updated for changes in existing API endpoints.
# Version 0.4.0
## Changes
- Implemented Issue [#55](https://github.com/PSS-Tools-Development/pssapi.py/issues/55)
- Implemented Issue [#54](https://github.com/PSS-Tools-Development/pssapi.py/issues/54)
## Fixes
- Fixed Issue [#53](https://github.com/PSS-Tools-Development/pssapi.py/issues/53)
## Updated Library
The library has been updated to Pixel Starships v0.998.16.10969 (Steam, testing branch).
### Changes to utilities
- `parse.pss_int_enum` will now return `None` on non-existent values, instead of raising an exception.
- `parse.pss_int_flag` will now ignore values that are too great, instead of raising an exception.
- `parse.pss_str_enum` will now return `None` on non-existent values, instead of raising an exception.
- `datetime.convert_to_pss_timestamp` now returns `None`, if the passed value is `None`, instead of raising an exception.
### Changes to Services
- Changed `AnimationService`
  - Changed method `list_animations` with new parameter `client_date_time`
- Changed `BackgroundService`
  - Changed method `list_backgrounds` with new parameter `client_date_time`
- Changed `ChallengeService`
  - Changed method `list_all_challenge_designs` with new parameter `client_date_time`
- Changed `CharacterService`
  - Changed method `to_character` with new parameter `client_date_time`
  - Changed method `list_all_character_design_actions` with new parameter `client_date_time`
  - Changed method `list_all_character_designs` with new parameter `client_date_time`
  - Changed method `list_all_draw_designs` with new parameter `client_date_time`
- Changed `CollectionService`
  - Changed method `list_all_collection_designs` with new parameter `client_date_time`
- Changed `DivisionService`
  - Changed method `list_all_division_designs` with new parameter `client_date_time`
- Changed `GalaxyService`
  - Changed method `list_marker_generator_designs` with new parameter `client_date_time`
  - Changed method `list_star_system_links` with new parameter `client_date_time`
  - Changed method `list_star_systems` with new parameter `client_date_time`
- Changed `ItemService`
  - Changed method `to_item` with new parameter `client_date_time`
  - Changed method `list_item_design_actions` with new parameter `client_date_time`
  - Changed method `list_item_designs` with new parameter `client_date_time`
- Changed `LeagueService`
  - Changed method `list_leagues` with new parameter `client_date_time`
- Changed `MissionService`
  - Changed method `list_all_mission_designs` with new parameter `client_date_time`
- Changed `PromotionService`
  - Changed method `list_all_promotion_designs` with new parameter `client_date_time`
- Changed `ResearchService`
  - Changed method `list_all_research_designs` with new parameter `client_date_time`
- Changed `RewardService`
  - Changed method `list_all_reward_designs` with new parameter `client_date_time`
- Changed `RoomDesignSpriteService`
  - Changed method `list_room_design_sprites` with new parameter `client_date_time`
- Changed `RoomService`
  - Changed method `list_craft_designs` with new parameter `client_date_time`
  - Changed method `list_missile_designs` with new parameter `client_date_time`
  - Changed method `list_room_design_purchase` with new parameter `client_date_time`
  - Changed method `list_room_designs` with new parameter `client_date_time`
- Changed `SeasonService`
  - Changed method `list_all_season_designs` with new parameter `client_date_time`
- Changed `SettingService`
  - Changed method `list_all_news_designs` with new parameter `client_date_time`
- Changed `ShipService`
  - Changed method `to_ship` with new parameter `client_date_time`
  - Changed type of parameter `client_date_time` for method `get_ship_by_user_id` to `datetime.datetime`
  - Changed method `list_all_ship_designs` with new parameter `client_date_time`
- Changed `SituationService`
  - Changed method `list_situation_designs` with new parameter `client_date_time`
- Changed `TrainingService`
  - Changed method `list_all_training_designs` with new parameter `client_date_time`
- Changed `UserService`
  - Changed endpoint `list_skins` with new parameter `client_date_time`
### Changes to Raw Services
- Changed `animation_service_raw`
  - Update endpoint `list_animations` with new parameter `client_date_time`
- Changed `background_service_raw`
  - Update endpoint `list_backgrounds` with new parameter `client_date_time`
- Changed `challenge_service_raw`
  - Update endpoint `list_all_challenge_designs_2` with new parameter `client_date_time`
- Changed `character_service_raw`
  - Update endpoint `list_all_character_design_actions` with new parameter `client_date_time`
  - Update endpoint `list_all_character_designs_2` with new parameter `client_date_time`
  - Update endpoint `list_all_draw_designs` with new parameter `client_date_time`
- Changed `collection_service_raw`
  - Update endpoint `list_all_collection_designs` with new parameter `client_date_time`
- Changed `division_service_raw`
  - Update endpoint `list_all_division_designs_2` with new parameter `client_date_time`
- Changed `galaxy_service_raw`
  - Update endpoint `list_marker_generator_designs` with new parameter `client_date_time`
  - Update endpoint `list_star_system_links` with new parameter `client_date_time`
  - Update endpoint `list_star_systems` with new parameter `client_date_time`
- Changed `item_service_raw`
  - Update endpoint `list_item_design_actions` with new parameter `client_date_time`
  - Update endpoint `list_item_designs_2` with new parameter `client_date_time`
- Changed `league_service_raw`
  - Update endpoint `list_leagues_2` with new parameter `client_date_time`
- Changed `mission_service_raw`
  - Update endpoint `list_all_mission_designs_4` with new parameter `client_date_time`
- Changed `promotion_service_raw`
  - Update endpoint `list_all_promotion_designs_2` with new parameter `client_date_time`
- Changed `research_service_raw`
  - Update endpoint `list_all_research_designs_2` with new parameter `client_date_time`
- Changed `reward_service_raw`
  - Update endpoint `list_all_reward_designs_2` with new parameter `client_date_time`
- Changed `room_design_sprite_service_raw`
  - Update endpoint `list_room_design_sprites_2` with new parameter `client_date_time`
- Changed `room_service_raw`
  - Update endpoint `list_craft_designs` with new parameter `client_date_time`
  - Update endpoint `list_missile_designs` with new parameter `client_date_time`
  - Update endpoint `list_room_design_purchase` with new parameter `client_date_time`
  - Update endpoint `list_room_designs_2` with new parameter `client_date_time`
- Changed `season_service_raw`
  - Update endpoint `list_all_season_designs` with new parameter `client_date_time`
- Changed `setting_service_raw`
  - Update endpoint `list_all_news_designs` with new parameter `client_date_time`
- Changed `ship_service_raw`
  - Update endpoint `list_all_ship_designs_2` with new parameter `client_date_time`
- Changed `situation_service_raw`
  - Update endpoint `list_situation_designs` with new parameter `client_date_time`
- Changed `training_service_raw`
  - Update endpoint `list_all_training_designs_2` with new parameter `client_date_time`
- Changed `user_service_raw`
  - Update endpoint `list_skins` with new parameter `client_date_time`
### Changes to Entities
- Changed `Alliance`
  - Removed property `alliance_country_code_enum`
- Changed `CollectionDesign`
  - Added property `flags_enum`
- Changed `User`
  - Removed property `language_key_enum`
### Changes to Raw Entities
- Changed `CollectionDesignRaw`
  - Added property `ability_icon_sprite_id` (`int`)
  - Added property `ability_name` (`str`)
  - Added property `argument` (`int`)
  - Added property `base_chance` (`int`)
  - Added property `max_use` (`int`)
  - Added property `step_chance` (`int`)
  - Added property `trigger_type` (`str`)
- Changed `CraftDesignRaw`
  - Added property `attack_range` (`int`)
### Changes to Enums
- Added enum `CollectionDesignFlag`
- Changed enum `RoomFlags`
  - Added value 64 (`HIDE_ON_UGC`)
## Changes to testing
- All tests for methods not requiring an access token now re-record cassettes each time.
- Changed deviceKey used for login methods
- Remove sensitive data from recorded requests and responses
- Update `vcrpy` version to `6.0.1`

# Version 0.3.0
## Added
- Pusher support
- New enum "PusherChannelType"
## Updated Library
The library has been updated to Pixel Starships v0.998.9.12852 (IOS) and v0.998.10.10557 (Steam).
### Changes to Services
- Changed `TaskService`
  - Update endpoint `list_all_task_designs_2` with new parameter `client_date_time`
### Changes to Raw Services
- Changed `DesignServiceRaw`
  - Added endpoint `list_all_designs_5`
- Changed `SettingServiceRaw`
  - Added endpoint `get_latest_version_4`
- Changed `TaskServiceRaw`
  - Update endpoint `list_all_task_designs_2` with new parameter `client_date_time`
### Changes to Entities
- Changed `Skin`
  - Changed type of property `sprite_type_enum` to `SpriteType`
### Changes to Raw Entities
- Changed `CharacterDesignRaw`
  - Added property `tags` (`str`)
- Changed `RoomDesignRaw`
  - Added property `tags` (`str`)
- Changed `RoomDesignRaw`
  - Added properties:
    - `maintenance_date` (`datetime`)
    - `min_purchase_reward_points_for_starbux_trading` (`int`)
    - `min_trophies_for_starbux_trading` (`int`)
- Changed `SkinRaw`
  - Added property `tags` (`str`)
- Changed `UserRaw`
  - Added property `rewards_collectable_amount` (`str`)
### Changes to Enums
- Added enums
  - `SpriteType` (`StrEnum`)
  - `UserSourceAdsPlatformType` (`StrEnum`)

# Version 0.2.3
## Added
- New ItemSubType "SkipBattlePassTiers"
- New LanguageKey "br"

## Fixed
- Fix CharacterPart list in CharacterDesign

# Version 0.2.2
## Added
- New ItemSubType "ShipSkin"

# Version 0.2.1
## Added
- PssApiError subclasses for later use
- UserService.device_login_11()

# Version 0.2.0
## Updated library
The library has been updated to Pixel Starships v0.997.4.12193 (IOS), v0.997.4.9873 (Steam) and v0.997.5.9898-beta (Steam, content testing version).
### Changes to Services
- Changed `MessageService`
  - Added endpoint `send_private_message`
- Changed `RoomDesignSpriteService`
  - Changed endpoint `list_room_design_sprites` to use `RoomDesignSpriteServiceRaw.list_room_design_sprites_2`
- Changed `UserService`
  - Added endpoint `list_skins`
  - Changed endpoint `user_email_password_authorize` to use `UserServiceRaw.user_email_password_authorize_4`
  - Endpoint `device_login_15` now provides default values
### Changes to Raw Services
- Changed `MessageServiceRaw`
  - Added endpoint `send_private_message_3`
- Changed `RoomDesignSpriteServiceRaw`
  - Added endpoint `list_room_design_sprites_2`
- Changed `UserServiceRaw`
  - Added endpoint `list_skins`
  - Added endpoint `user_email_password_authorize_4`
### Changes to Entities
- Added entities:
  - `Skin`
  - `SkinSet`
- Changed `UserRaw`
  - Added property `user_source_ads_platform_type_enum` (`enums.PlatformType`)
### Changes to Raw Entities
- Added entities:
  - `SkinRaw`
  - `SkinSetRaw`
- Changed `AllianceRaw`
  - Added property `min_score_contribution` (`int`)
- Changed `CharacterDesignRaw`
  - Changed type of property `final_pilot` from `int` to `float`
- Changed `CharacterRaw`
  - Added properties:
    - `battle_character_hp` (`int`)
    - `bloodlust_frame` (`int`)
    - `designated_room_id` (`int`)
    - `invulnerability_frame` (`int`)
    - `origin_room_id` (`int`)
    - `skill_points` (`int`)
    - `target_room_id` (`int`)
    - `x_coordinate` (`int`)
    - `x_coordinate_ship_relative` (`int`)
    - `y_coordinate` (`int`)
    - `y_coordinate_ship_relative` (`int`)
- Changed `CraftDesignRaw`
  - Added property `attack_distance` (`int`)
- Changed `ItemDesignRaw`
  - Added properties:
    - `build_price` (`int`)
    - `circulation` (`int`)
    - `transaction_volume` (`int`)
- Changed `ItemRaw`
  - Added properties:
    - `action_frame` (`int`)
    - `battle_hp` (`int`)
    - `skin_key` (`int`)
- Changed `RoomDesignRaw`
  - Added properties:
    - `activation_delay` (`int`)
    - `min_range` (`int`)
- Changed `RoomRaw`
  - Added properties:
    - `assigned_power` (`int`)
    - `center_x` (`int`)
    - `center_y` (`int`)
    - `current_capacity` (`int`)
    - `disable_count` (`int`)
    - `is_power_ai_active` (`bool`)
    - `is_set_item_ai_active` (`bool`)
    - `is_target_ai_active` (`bool`)
    - `item_skin_key` (`int`)
    - `local_center_x` (`int`)
    - `local_center_y` (`int`)
    - `progress` (`int`)
    - `protect_room_frame` (`int`)
    - `run_room_action` (`bool`)
    - `skin_key` (`int`)
    - `system_power` (`int`)
    - `target_craft_id` (`int`)
    - `target_room_id` (`int`)
    - `top_left_x` (`int`)
    - `top_left_y` (`int`)
    - `total_damage` (`int`)
- Changed `SettingsRaw`
  - Added properties:
    - `engine_efficiency_loss` (`float`)
    - `maintenance_title` (`str`)
    - `max_redemption_count` (`int`)
    - `max_redemption_count_per_month` (`int`)
    - `merchant_ship_exterior_sprite_id` (`int`)
    - `skin_version` (`int`)
- Changed `ShipRaw`
  - Added properties:
    - `center_x` (`int`)
    - `center_y` (`int`)
    - `next_android_character_id` (`int`)
    - `top_left_x` (`int`)
    - `top_left_y` (`int`)
- Changed `UserEmailPasswordAuthorizeRaw`
  - Added property `refresh_token` (`str`)
- Changed `UserRaw`
  - Added properties:
    - `ads_platform_user_id` (`str`)
    - `daily_heartbeat_seconds` (`int`)
    - `trail_user_id` (`str`)
    - `user_source_ads_platform_type` (`str`)
### Changes to Enums
- Added enums
  - `PlatformType` (`StrEnum`)
  - `SkinType` (`StrEnum`)
## Bugfixes
- Fixed `_key` method of `PlanetRaw` to return an empty `tuple`
## Test changes
- Added tests
