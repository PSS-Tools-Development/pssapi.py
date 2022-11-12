"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class DrawDesignRaw:
    XML_NODE_NAME: str = 'DrawDesign'

    def __init__(self, draw_design_info: _EntityInfo) -> None:
        self.background_sprite_id: int = _parse.pss_int(
            draw_design_info.get('BackgroundSpriteId'))
        self.bonus_increase: int = _parse.pss_int(
            draw_design_info.get('BonusIncrease'))
        self.collection_design_id: int = _parse.pss_int(
            draw_design_info.get('CollectionDesignId'))
        self.cost: str = _parse.pss_str(draw_design_info.get('Cost'))
        self.cost_percentage_increase: int = _parse.pss_int(
            draw_design_info.get('CostPercentageIncrease'))
        self.draw_description: str = _parse.pss_str(
            draw_design_info.get('DrawDescription'))
        self.draw_design_id: int = _parse.pss_int(
            draw_design_info.get('DrawDesignId'))
        self.draw_name: str = _parse.pss_str(draw_design_info.get('DrawName'))
        self.draw_sprite_id: int = _parse.pss_int(
            draw_design_info.get('DrawSpriteId'))
        self.draw_type: str = _parse.pss_str(draw_design_info.get('DrawType'))
        self.max_cost_percentage_increase: int = _parse.pss_int(
            draw_design_info.get('MaxCostPercentageIncrease'))
        self.max_crew_rarity: int = _parse.pss_int(
            draw_design_info.get('MaxCrewRarity'))
        self.max_crews_drawn: int = _parse.pss_int(
            draw_design_info.get('MaxCrewsDrawn'))
        self.max_items: int = _parse.pss_int(draw_design_info.get('MaxItems'))
        self.min_crew_rarity: int = _parse.pss_int(
            draw_design_info.get('MinCrewRarity'))
        self.min_crews_drawn: int = _parse.pss_int(
            draw_design_info.get('MinCrewsDrawn'))
        self.min_items: int = _parse.pss_int(draw_design_info.get('MinItems'))
        self.order_index: int = _parse.pss_int(
            draw_design_info.get('OrderIndex'))
        self.required_research_design_id: int = _parse.pss_int(
            draw_design_info.get('RequiredResearchDesignId'))
