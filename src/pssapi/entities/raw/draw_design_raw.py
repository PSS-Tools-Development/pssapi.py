"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


from .entity_base_raw import EntityBaseRaw

class DrawDesignRaw(EntityBaseRaw):
    XML_NODE_NAME: str = "DrawDesign"

    def __init__(self, draw_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._background_sprite_id: int = _parse.pss_int(draw_design_info.pop("BackgroundSpriteId", None))
        self._bonus_increase: int = _parse.pss_int(draw_design_info.pop("BonusIncrease", None))
        self._collection_design_id: int = _parse.pss_int(draw_design_info.pop("CollectionDesignId", None))
        self._cost: str = _parse.pss_str(draw_design_info.pop("Cost", None))
        self._cost_percentage_increase: int = _parse.pss_int(draw_design_info.pop("CostPercentageIncrease", None))
        self._draw_description: str = _parse.pss_str(draw_design_info.pop("DrawDescription", None))
        self._draw_design_id: int = _parse.pss_int(draw_design_info.pop("DrawDesignId", None))
        self._draw_name: str = _parse.pss_str(draw_design_info.pop("DrawName", None))
        self._draw_sprite_id: int = _parse.pss_int(draw_design_info.pop("DrawSpriteId", None))
        self._draw_type: str = _parse.pss_str(draw_design_info.pop("DrawType", None))
        self._max_cost_percentage_increase: int = _parse.pss_int(draw_design_info.pop("MaxCostPercentageIncrease", None))
        self._max_crew_rarity: int = _parse.pss_int(draw_design_info.pop("MaxCrewRarity", None))
        self._max_crews_drawn: int = _parse.pss_int(draw_design_info.pop("MaxCrewsDrawn", None))
        self._max_items: int = _parse.pss_int(draw_design_info.pop("MaxItems", None))
        self._min_crew_rarity: int = _parse.pss_int(draw_design_info.pop("MinCrewRarity", None))
        self._min_crews_drawn: int = _parse.pss_int(draw_design_info.pop("MinCrewsDrawn", None))
        self._min_items: int = _parse.pss_int(draw_design_info.pop("MinItems", None))
        self._order_index: int = _parse.pss_int(draw_design_info.pop("OrderIndex", None))
        self._required_research_design_id: int = _parse.pss_int(draw_design_info.pop("RequiredResearchDesignId", None))
        super().__init__(draw_design_info)

    @property
    def background_sprite_id(self) -> int:
        return self._background_sprite_id

    @property
    def bonus_increase(self) -> int:
        return self._bonus_increase

    @property
    def collection_design_id(self) -> int:
        return self._collection_design_id

    @property
    def cost(self) -> str:
        return self._cost

    @property
    def cost_percentage_increase(self) -> int:
        return self._cost_percentage_increase

    @property
    def draw_description(self) -> str:
        return self._draw_description

    @property
    def draw_design_id(self) -> int:
        return self._draw_design_id

    @property
    def draw_name(self) -> str:
        return self._draw_name

    @property
    def draw_sprite_id(self) -> int:
        return self._draw_sprite_id

    @property
    def draw_type(self) -> str:
        return self._draw_type

    @property
    def max_cost_percentage_increase(self) -> int:
        return self._max_cost_percentage_increase

    @property
    def max_crew_rarity(self) -> int:
        return self._max_crew_rarity

    @property
    def max_crews_drawn(self) -> int:
        return self._max_crews_drawn

    @property
    def max_items(self) -> int:
        return self._max_items

    @property
    def min_crew_rarity(self) -> int:
        return self._min_crew_rarity

    @property
    def min_crews_drawn(self) -> int:
        return self._min_crews_drawn

    @property
    def min_items(self) -> int:
        return self._min_items

    @property
    def order_index(self) -> int:
        return self._order_index

    @property
    def required_research_design_id(self) -> int:
        return self._required_research_design_id

    def _key(self):
        return (
            self.background_sprite_id,
            self.bonus_increase,
            self.collection_design_id,
            self.cost,
            self.cost_percentage_increase,
            self.draw_description,
            self.draw_design_id,
            self.draw_name,
            self.draw_sprite_id,
            self.draw_type,
            self.max_cost_percentage_increase,
            self.max_crew_rarity,
            self.max_crews_drawn,
            self.max_items,
            self.min_crew_rarity,
            self.min_crews_drawn,
            self.min_items,
            self.order_index,
            self.required_research_design_id,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "BackgroundSpriteId": self.background_sprite_id,
                "BonusIncrease": self.bonus_increase,
                "CollectionDesignId": self.collection_design_id,
                "Cost": self.cost,
                "CostPercentageIncrease": self.cost_percentage_increase,
                "DrawDescription": self.draw_description,
                "DrawDesignId": self.draw_design_id,
                "DrawName": self.draw_name,
                "DrawSpriteId": self.draw_sprite_id,
                "DrawType": self.draw_type,
                "MaxCostPercentageIncrease": self.max_cost_percentage_increase,
                "MaxCrewRarity": self.max_crew_rarity,
                "MaxCrewsDrawn": self.max_crews_drawn,
                "MaxItems": self.max_items,
                "MinCrewRarity": self.min_crew_rarity,
                "MinCrewsDrawn": self.min_crews_drawn,
                "MinItems": self.min_items,
                "OrderIndex": self.order_index,
                "RequiredResearchDesignId": self.required_research_design_id,
            }
            self._dict.update(super().__dict__())

        return self._dict
