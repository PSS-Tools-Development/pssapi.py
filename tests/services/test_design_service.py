import pytest

import pssapi


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
async def test_list_all_designs(client: pssapi.PssApiClient):
    types = [
        pssapi.entities.AchievementDesign,
        pssapi.entities.Animation,
        pssapi.entities.Asset,
        pssapi.entities.Background,
        pssapi.entities.ChallengeDesign,
        pssapi.entities.CharacterDesignAction,
        pssapi.entities.CharacterDesign,
        pssapi.entities.CollectionDesign,
        pssapi.entities.CraftDesign,
        pssapi.entities.DivisionDesign,
        pssapi.entities.DrawDesign,
        pssapi.entities.File,
        pssapi.entities.ItemDesignAction,
        pssapi.entities.ItemDesign,
        pssapi.entities.League,
        pssapi.entities.MissileDesign,
        pssapi.entities.MissionDesign,
        pssapi.entities.NewsDesign,
        pssapi.entities.PromotionDesign,
        pssapi.entities.ResearchDesign,
        pssapi.entities.RewardDesign,
        pssapi.entities.RoomDesignPurchase,
        pssapi.entities.RoomDesignSprite,
        pssapi.entities.RoomDesign,
        pssapi.entities.SeasonDesign,
        pssapi.entities.ShipDesign,
        pssapi.entities.SituationDesign,
        pssapi.entities.SkinSet,
        pssapi.entities.Skin,
        pssapi.entities.Sprite,
        pssapi.entities.StarSystemLink,
        pssapi.entities.StarSystemMarkerGenerator,
        pssapi.entities.StarSystem,
        pssapi.entities.TrainingDesign,
    ]
    designs = await client.design_service.list_all_designs(
        pssapi.enums.LanguageKey.ENGLISH,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    )
    assert isinstance(designs, tuple)
    assert len(designs) > 0
    for i, entity_designs in enumerate(designs):
        assert isinstance(entity_designs, list)
        assert len(entity_designs) > 0
        assert isinstance(entity_designs[0], types[i])


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "device_type")
@pytest.mark.vcr()
async def test_list_all_dynamic_designs(client: pssapi.PssApiClient, device_type: pssapi.enums.DeviceType):
    types = [pssapi.entities.ItemDesign, pssapi.entities.PromotionDesign, pssapi.entities.TaskDesign]
    get_latest_version = await client.setting_service.get_latest_version(device_type)
    designs = await client.design_service.list_all_dynamic_designs(get_latest_version.promotion_design_version, get_latest_version.task_design_version, get_latest_version.item_design_version)
    assert isinstance(designs, tuple)
    assert len(designs) > 0
    for i, entity_designs in enumerate(designs):
        assert isinstance(entity_designs, list)
        assert len(entity_designs) > 0
        assert type(entity_designs[0]) in types
        assert isinstance(entity_designs[0], types[i])


@pytest.mark.asyncio
@pytest.mark.usefixtures("client", "device_type")
@pytest.mark.vcr()
async def test_list_all_static_designs_get_all_designs(client: pssapi.PssApiClient, device_type: pssapi.enums.DeviceType):
    types = [
        pssapi.entities.AchievementDesign,
        pssapi.entities.Animation,
        pssapi.entities.Background,
        pssapi.entities.ChallengeDesign,
        pssapi.entities.CharacterDesignAction,
        pssapi.entities.CharacterDesign,
        pssapi.entities.CollectionDesign,
        pssapi.entities.CraftDesign,
        pssapi.entities.DivisionDesign,
        pssapi.entities.DrawDesign,
        pssapi.entities.File,
        pssapi.entities.ItemDesignAction,
        pssapi.entities.League,
        pssapi.entities.MissileDesign,
        pssapi.entities.MissionDesign,
        pssapi.entities.NewsDesign,
        pssapi.entities.ResearchDesign,
        pssapi.entities.RewardDesign,
        pssapi.entities.RoomDesignPurchase,
        pssapi.entities.RoomDesignSprite,
        pssapi.entities.RoomDesign,
        pssapi.entities.SeasonDesign,
        pssapi.entities.ShipDesign,
        pssapi.entities.SituationDesign,
        pssapi.entities.SkinSet,
        pssapi.entities.Skin,
        pssapi.entities.Sprite,
        pssapi.entities.StarSystemLink,
        pssapi.entities.StarSystemMarkerGenerator,
        pssapi.entities.StarSystem,
        pssapi.entities.TrainingDesign,
    ]
    get_latest_version = await client.setting_service.get_latest_version(device_type)
    designs = await client.design_service.list_all_static_designs(
        get_latest_version.achievement_design_version,
        get_latest_version.action_type_version,
        get_latest_version.challenge_design_version,
        get_latest_version.character_design_action_version,
        get_latest_version.character_design_version,
        get_latest_version.collection_design_version,
        get_latest_version.division_design_version,
        get_latest_version.draw_design_version,
        get_latest_version.mission_design_version,
        get_latest_version.news_design_version,
        get_latest_version.research_design_version,
        get_latest_version.reward_design_version,
        get_latest_version.ship_design_version,
        get_latest_version.situation_design_version,
        get_latest_version.training_design_version,
        get_latest_version.animation_version,
        get_latest_version.asset_version,
        get_latest_version.background_version,
        get_latest_version.condition_type_version,
        get_latest_version.craft_design_version,
        get_latest_version.file_version,
        get_latest_version.item_design_action_version,
        get_latest_version.league_version,
        get_latest_version.marker_generator_design_version,
        get_latest_version.missile_design_version,
        get_latest_version.room_design_purchase_version,
        get_latest_version.room_design_sprite_version,
        get_latest_version.room_design_version,
        get_latest_version.season_design_version,
        get_latest_version.skin_set_version,
        get_latest_version.skin_version,
        get_latest_version.sprite_version,
        get_latest_version.star_system_link_version,
        get_latest_version.star_system_version,
    )
    assert isinstance(designs, tuple)
    assert len(designs) > 0
    for i, entity_designs in enumerate(designs):
        assert isinstance(entity_designs, list)
        assert len(entity_designs) > 0
        assert isinstance(entity_designs[0], types[i])
