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
    )
    assert isinstance(designs, tuple)
    assert len(designs) > 0
    for i, entity_designs in enumerate(designs):
        assert isinstance(entity_designs, list)
        assert len(entity_designs) > 0
        assert isinstance(entity_designs[0], types[i])
