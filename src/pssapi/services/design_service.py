from typing import List as _List
from typing import Tuple as _Tuple

import pssapi.services.service_base as _service_base

from ..entities import AchievementDesign as _AchievementDesign
from ..entities import Animation as _Animation
from ..entities import Asset as _Asset
from ..entities import Background as _Background
from ..entities import ChallengeDesign as _ChallengeDesign
from ..entities import CharacterDesign as _CharacterDesign
from ..entities import CharacterDesignAction as _CharacterDesignAction
from ..entities import CollectionDesign as _CollectionDesign
from ..entities import CraftDesign as _CraftDesign
from ..entities import DivisionDesign as _DivisionDesign
from ..entities import DrawDesign as _DrawDesign
from ..entities import File as _File
from ..entities import ItemDesign as _ItemDesign
from ..entities import ItemDesignAction as _ItemDesignAction
from ..entities import League as _League
from ..entities import MissileDesign as _MissileDesign
from ..entities import MissionDesign as _MissionDesign
from ..entities import NewsDesign as _NewsDesign
from ..entities import PromotionDesign as _PromotionDesign
from ..entities import ResearchDesign as _ResearchDesign
from ..entities import RewardDesign as _RewardDesign
from ..entities import RoomDesign as _RoomDesign
from ..entities import RoomDesignPurchase as _RoomDesignPurchase
from ..entities import RoomDesignSprite as _RoomDesignSprite
from ..entities import SeasonDesign as _SeasonDesign
from ..entities import ShipDesign as _ShipDesign
from ..entities import SituationDesign as _SituationDesign
from ..entities import Sprite as _Sprite
from ..entities import StarSystem as _StarSystem
from ..entities import StarSystemLink as _StarSystemLink
from ..entities import StarSystemMarkerGenerator as _StarSystemMarkerGenerator
from ..entities import TrainingDesign as _TrainingDesign
from .raw import DesignServiceRaw as _DesignServiceRaw


class DesignService(_service_base.ServiceBase):
    async def list_all_designs(
        self,
        language_key: str,
        list_achievement_design_version: int,
        list_action_type_version: int,
        list_all_challenge_design_version: int,
        list_all_character_design_action_version: int,
        list_all_character_design_version: int,
        list_all_collection_design_version: int,
        list_all_division_design_version: int,
        list_all_draw_design_version: int,
        list_all_mission_design_version: int,
        list_all_news_design_version: int,
        list_all_promotion_design_version: int,
        list_all_research_design_version: int,
        list_all_reward_design_version: int,
        list_all_ship_design_version: int,
        list_all_situation_design_version: int,
        list_all_task_design_version: int,
        list_all_training_design_version: int,
        list_animation_version: int,
        list_asset_version: int,
        list_background_version: int,
        list_condition_type_version: int,
        list_craft_design_version: int,
        list_file_version: int,
        list_item_design_action_version: int,
        list_item_design_version: int,
        list_league_version: int,
        list_marker_generator_design_version: int,
        list_missile_design_version: int,
        list_room_design_purchase_version: int,
        list_room_design_sprite_version: int,
        list_room_design_version: int,
        list_season_design_version: int,
        list_sprite_version: int,
        list_star_system_link_version: int,
        list_star_system_version: int,
    ) -> _Tuple[
        _List[_AchievementDesign],
        _List[_Animation],
        _List[_Asset],
        _List[_Background],
        _List[_ChallengeDesign],
        _List[_CharacterDesignAction],
        _List[_CharacterDesign],
        _List[_CollectionDesign],
        _List[_CraftDesign],
        _List[_DivisionDesign],
        _List[_DrawDesign],
        _List[_File],
        _List[_ItemDesignAction],
        _List[_ItemDesign],
        _List[_League],
        _List[_MissileDesign],
        _List[_MissionDesign],
        _List[_NewsDesign],
        _List[_PromotionDesign],
        _List[_ResearchDesign],
        _List[_RewardDesign],
        _List[_RoomDesignPurchase],
        _List[_RoomDesignSprite],
        _List[_RoomDesign],
        _List[_SeasonDesign],
        _List[_ShipDesign],
        _List[_SituationDesign],
        _List[_Sprite],
        _List[_StarSystemLink],
        _List[_StarSystemMarkerGenerator],
        _List[_StarSystem],
        _List[_TrainingDesign],
    ]:
        production_server = await self.get_production_server()
        result = await _DesignServiceRaw.list_all_designs_4(
            production_server,
            language_key,
            list_achievement_design_version,
            list_action_type_version,
            list_all_challenge_design_version,
            list_all_character_design_action_version,
            list_all_character_design_version,
            list_all_collection_design_version,
            list_all_division_design_version,
            list_all_draw_design_version,
            list_all_mission_design_version,
            list_all_news_design_version,
            list_all_promotion_design_version,
            list_all_research_design_version,
            list_all_reward_design_version,
            list_all_ship_design_version,
            list_all_situation_design_version,
            list_all_task_design_version,
            list_all_training_design_version,
            list_animation_version,
            list_asset_version,
            list_background_version,
            list_condition_type_version,
            list_craft_design_version,
            list_file_version,
            list_item_design_action_version,
            list_item_design_version,
            list_league_version,
            list_marker_generator_design_version,
            list_missile_design_version,
            list_room_design_purchase_version,
            list_room_design_sprite_version,
            list_room_design_version,
            list_season_design_version,
            list_sprite_version,
            list_star_system_link_version,
            list_star_system_version,
        )
        return result
