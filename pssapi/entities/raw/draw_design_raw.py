####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class DrawDesignRaw():
    XML_NODE_NAME: str = 'DrawDesign'

    def __init__(self, draw_design_info: _EntityInfo) -> None:
        self.__draw_design_id: int = _parse.pss_int(draw_design_info.get('DrawDesignId'))
        self.__draw_name: str = _parse.pss_str(draw_design_info.get('DrawName'))
        self.__draw_description: str = _parse.pss_str(draw_design_info.get('DrawDescription'))
        self.__draw_sprite_id: int = _parse.pss_int(draw_design_info.get('DrawSpriteId'))
        self.__draw_type: str = _parse.pss_str(draw_design_info.get('DrawType'))
        self.__cost: str = _parse.pss_str(draw_design_info.get('Cost'))
        self.__cost_percentage_increase: int = _parse.pss_int(draw_design_info.get('CostPercentageIncrease'))
        self.__min_crews_drawn: int = _parse.pss_int(draw_design_info.get('MinCrewsDrawn'))
        self.__max_crews_drawn: int = _parse.pss_int(draw_design_info.get('MaxCrewsDrawn'))
        self.__min_crew_rarity: int = _parse.pss_int(draw_design_info.get('MinCrewRarity'))
        self.__max_crew_rarity: int = _parse.pss_int(draw_design_info.get('MaxCrewRarity'))
        self.__bonus_increase: int = _parse.pss_int(draw_design_info.get('BonusIncrease'))
        self.__min_items: int = _parse.pss_int(draw_design_info.get('MinItems'))
        self.__max_items: int = _parse.pss_int(draw_design_info.get('MaxItems'))
        self.__max_cost_percentage_increase: int = _parse.pss_int(draw_design_info.get('MaxCostPercentageIncrease'))
        self.__order_index: int = _parse.pss_int(draw_design_info.get('OrderIndex'))
        self.__background_sprite_id: int = _parse.pss_int(draw_design_info.get('BackgroundSpriteId'))
        self.__required_research_design_id: int = _parse.pss_int(draw_design_info.get('RequiredResearchDesignId'))
        self.__collection_design_id: int = _parse.pss_int(draw_design_info.get('CollectionDesignId'))

    @property
    def draw_design_id(self) -> int:
        return self.__draw_design_id

    @property
    def draw_name(self) -> str:
        return self.__draw_name

    @property
    def draw_description(self) -> str:
        return self.__draw_description

    @property
    def draw_sprite_id(self) -> int:
        return self.__draw_sprite_id

    @property
    def draw_type(self) -> str:
        return self.__draw_type

    @property
    def cost(self) -> str:
        return self.__cost

    @property
    def cost_percentage_increase(self) -> int:
        return self.__cost_percentage_increase

    @property
    def min_crews_drawn(self) -> int:
        return self.__min_crews_drawn

    @property
    def max_crews_drawn(self) -> int:
        return self.__max_crews_drawn

    @property
    def min_crew_rarity(self) -> int:
        return self.__min_crew_rarity

    @property
    def max_crew_rarity(self) -> int:
        return self.__max_crew_rarity

    @property
    def bonus_increase(self) -> int:
        return self.__bonus_increase

    @property
    def min_items(self) -> int:
        return self.__min_items

    @property
    def max_items(self) -> int:
        return self.__max_items

    @property
    def max_cost_percentage_increase(self) -> int:
        return self.__max_cost_percentage_increase

    @property
    def order_index(self) -> int:
        return self.__order_index

    @property
    def background_sprite_id(self) -> int:
        return self.__background_sprite_id

    @property
    def required_research_design_id(self) -> int:
        return self.__required_research_design_id

    @property
    def collection_design_id(self) -> int:
        return self.__collection_design_id
