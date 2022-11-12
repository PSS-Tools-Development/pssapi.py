"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ResearchDesignRaw:
    XML_NODE_NAME: str = 'ResearchDesign'

    def __init__(self, research_design_info: _EntityInfo) -> None:
        self.argument: int = _parse.pss_int(
            research_design_info.get('Argument'))
        self.availability_mask: int = _parse.pss_int(
            research_design_info.get('AvailabilityMask'))
        self.gas_cost: int = _parse.pss_int(
            research_design_info.get('GasCost'))
        self.image_sprite_id: int = _parse.pss_int(
            research_design_info.get('ImageSpriteId'))
        self.logo_sprite_id: int = _parse.pss_int(
            research_design_info.get('LogoSpriteId'))
        self.required_item_design_id: int = _parse.pss_int(
            research_design_info.get('RequiredItemDesignId'))
        self.required_lab_level: int = _parse.pss_int(
            research_design_info.get('RequiredLabLevel'))
        self.required_research_design_id: int = _parse.pss_int(
            research_design_info.get('RequiredResearchDesignId'))
        self.research_description: str = _parse.pss_str(
            research_design_info.get('ResearchDescription'))
        self.research_design_id: int = _parse.pss_int(
            research_design_info.get('ResearchDesignId'))
        self.research_design_type: str = _parse.pss_str(
            research_design_info.get('ResearchDesignType'))
        self.research_name: str = _parse.pss_str(
            research_design_info.get('ResearchName'))
        self.research_time: int = _parse.pss_int(
            research_design_info.get('ResearchTime'))
        self.root_research_design_id: int = _parse.pss_int(
            research_design_info.get('RootResearchDesignId'))
        self.starbux_cost: int = _parse.pss_int(
            research_design_info.get('StarbuxCost'))
        self.visibility_flags: str = _parse.pss_str(
            research_design_info.get('VisibilityFlags'))
