import pytest

import pssapi


test_cases_list_all_designs = [
    pytest.param(
        pssapi.raw.services.DesignServiceRaw.list_all_designs_2,
        32,
        (
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
            pssapi.entities.ShipDesign,
            pssapi.entities.SituationDesign,
            pssapi.entities.Sprite,
            pssapi.entities.StarSystemLink,
            pssapi.entities.StarSystem,
            pssapi.entities.TrainingDesign,
        ),
        id="list_all_designs_2",
    ),
    pytest.param(
        pssapi.raw.services.DesignServiceRaw.list_all_designs_4,
        35,
        (
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
        ),
        id="list_all_designs_4",
    ),
    pytest.param(
        pssapi.raw.services.DesignServiceRaw.list_all_designs_5,
        36,
        (
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
        ),
        id="list_all_designs_5",
    ),
]


@pytest.mark.asyncio
@pytest.mark.usefixtures("client")
@pytest.mark.vcr()
@pytest.mark.parametrize(["list_all_designs_method", "param_count", "types"], test_cases_list_all_designs)
async def test_list_all_designs(list_all_designs_method, param_count: int, types: list[pssapi.entities.EntityBase]):
    designs = await list_all_designs_method(pssapi.enums.ProductionServer.DEFAULT, pssapi.enums.LanguageKey.ENGLISH, *[1 for _ in range(param_count)])
    assert isinstance(designs, tuple)
    assert len(designs) > 0
    for i, entity_designs in enumerate(designs):
        expected_type = types[i]
        assert isinstance(entity_designs, list)
        assert len(entity_designs) > 0
        assert isinstance(entity_designs[0], expected_type)
