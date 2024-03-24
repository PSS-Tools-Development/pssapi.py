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
  - Updated method `list_animations` with new parameter `client_date_time`
- Changed `BackgroundService`
  - Updated method `list_backgrounds` with new parameter `client_date_time`
- Changed `ChallengeService`
  - Updated method `list_all_challenge_designs` with new parameter `client_date_time`
- Changed `CharacterService`
  - Updated method `to_character` with new parameter `client_date_time`
  - Updated method `list_all_character_design_actions` with new parameter `client_date_time`
  - Updated method `list_all_character_designs` with new parameter `client_date_time`
  - Updated method `list_all_draw_designs` with new parameter `client_date_time`
- Changed `CollectionService`
  - Updated method `list_all_collection_designs` with new parameter `client_date_time`
- Changed `DivisionService`
  - Updated method `list_all_division_designs` with new parameter `client_date_time`
- Changed `GalaxyService`
  - Updated method `list_marker_generator_designs` with new parameter `client_date_time`
  - Updated method `list_star_system_links` with new parameter `client_date_time`
  - Updated method `list_star_systems` with new parameter `client_date_time`
- Changed `ItemService`
  - Updated method `to_item` with new parameter `client_date_time`
  - Updated method `list_item_design_actions` with new parameter `client_date_time`
  - Updated method `list_item_designs` with new parameter `client_date_time`
- Changed `LeagueService`
  - Updated method `list_leagues` with new parameter `client_date_time`
- Changed `MissionService`
  - Updated method `list_all_mission_designs` with new parameter `client_date_time`
- Changed `PromotionService`
  - Updated method `list_all_promotion_designs` with new parameter `client_date_time`
- Changed `ResearchService`
  - Updated method `list_all_research_designs` with new parameter `client_date_time`
- Changed `RewardService`
  - Updated method `list_all_reward_designs` with new parameter `client_date_time`
- Changed `RoomDesignSpriteService`
  - Updated method `list_room_design_sprites` with new parameter `client_date_time`
- Changed `RoomService`
  - Updated method `list_craft_designs` with new parameter `client_date_time`
  - Updated method `list_missile_designs` with new parameter `client_date_time`
  - Updated method `list_room_design_purchase` with new parameter `client_date_time`
  - Updated method `list_room_designs` with new parameter `client_date_time`
- Changed `SeasonService`
  - Updated method `list_all_season_designs` with new parameter `client_date_time`
- Changed `SettingService`
  - Updated method `list_all_news_designs` with new parameter `client_date_time`
- Changed `ShipService`
  - Updated method `to_ship` with new parameter `client_date_time`
  - Updated type of parameter `client_date_time` for method `get_ship_by_user_id` to `datetime.datetime`
  - Updated method `list_all_ship_designs` with new parameter `client_date_time`
- Changed `SituationService`
  - Updated method `list_situation_designs` with new parameter `client_date_time`
- Changed `TrainingService`
  - Updated method `list_all_training_designs` with new parameter `client_date_time`
- Changed `UserService`
  - Updated endpoint `list_skins` with new parameter `client_date_time`
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
- Updated deviceKey used for login methods
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
  - Updated type of property `sprite_type_enum` to `SpriteType`
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
  - Updated endpoint `list_room_design_sprites` to use `RoomDesignSpriteServiceRaw.list_room_design_sprites_2`
- Changed `UserService`
  - Added endpoint `list_skins`
  - Updated endpoint `user_email_password_authorize` to use `UserServiceRaw.user_email_password_authorize_4`
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
