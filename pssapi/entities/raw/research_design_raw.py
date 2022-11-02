"""
    This file has been generated automatically
"""


from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ResearchDesignRaw:
    XML_NODE_NAME: str = 'ResearchDesign'

    def __init__(self, research_design_info: _EntityInfo) -> None:
        self.__gas_cost: int = _parse.pss_int(
            research_design_info.get('GasCost'))
        self.__availability_mask: int = _parse.pss_int(
            research_design_info.get('AvailabilityMask'))
        self.__required_item_design_id: int = _parse.pss_int(
            research_design_info.get('RequiredItemDesignId'))
        self.__logo_sprite_id: int = _parse.pss_int(
            research_design_info.get('LogoSpriteId'))
        self.__research_name: str = _parse.pss_str(
            research_design_info.get('ResearchName'))
        self.__visibility_flags: str = _parse.pss_str(
            research_design_info.get('VisibilityFlags'))
        self.__required_research_design_id: int = _parse.pss_int(
            research_design_info.get('RequiredResearchDesignId'))
        self.__required_lab_level: int = _parse.pss_int(
            research_design_info.get('RequiredLabLevel'))
        self.__image_sprite_id: int = _parse.pss_int(
            research_design_info.get('ImageSpriteId'))
        self.__argument: int = _parse.pss_int(
            research_design_info.get('Argument'))
        self.__research_time: int = _parse.pss_int(
            research_design_info.get('ResearchTime'))
        self.__research_description: str = _parse.pss_str(
            research_design_info.get('ResearchDescription'))
        self.__starbux_cost: int = _parse.pss_int(
            research_design_info.get('StarbuxCost'))
        self.__research_design_type: str = _parse.pss_str(
            research_design_info.get('ResearchDesignType'))
        self.__research_design_id: int = _parse.pss_int(
            research_design_info.get('ResearchDesignId'))
        self.__root_research_design_id: int = _parse.pss_int(
            research_design_info.get('RootResearchDesignId'))

    @property
    def gas_cost(self) -> int:
        return self.__gas_cost

    @property
    def availability_mask(self) -> int:
        return self.__availability_mask

    @property
    def required_item_design_id(self) -> int:
        return self.__required_item_design_id

    @property
    def logo_sprite_id(self) -> int:
        return self.__logo_sprite_id

    @property
    def research_name(self) -> str:
        return self.__research_name

    @property
    def visibility_flags(self) -> str:
        return self.__visibility_flags

    @property
    def required_research_design_id(self) -> int:
        return self.__required_research_design_id

    @property
    def required_lab_level(self) -> int:
        return self.__required_lab_level

    @property
    def image_sprite_id(self) -> int:
        return self.__image_sprite_id

    @property
    def argument(self) -> int:
        return self.__argument

    @property
    def research_time(self) -> int:
        return self.__research_time

    @property
    def research_description(self) -> str:
        return self.__research_description

    @property
    def starbux_cost(self) -> int:
        return self.__starbux_cost

    @property
    def research_design_type(self) -> str:
        return self.__research_design_type

    @property
    def research_design_id(self) -> int:
        return self.__research_design_id

    @property
    def root_research_design_id(self) -> int:
        return self.__root_research_design_id
