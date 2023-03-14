"""
    This file has been generated automatically
"""

from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class ResearchDesignRaw:
    XML_NODE_NAME: str = "ResearchDesign"

    def __init__(self, research_design_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._argument: int = _parse.pss_int(research_design_info.get("Argument"))
        self._availability_mask: int = _parse.pss_int(research_design_info.get("AvailabilityMask"))
        self._gas_cost: int = _parse.pss_int(research_design_info.get("GasCost"))
        self._image_sprite_id: int = _parse.pss_int(research_design_info.get("ImageSpriteId"))
        self._logo_sprite_id: int = _parse.pss_int(research_design_info.get("LogoSpriteId"))
        self._required_item_design_id: int = _parse.pss_int(research_design_info.get("RequiredItemDesignId"))
        self._required_lab_level: int = _parse.pss_int(research_design_info.get("RequiredLabLevel"))
        self._required_research_design_id: int = _parse.pss_int(research_design_info.get("RequiredResearchDesignId"))
        self._research_description: str = _parse.pss_str(research_design_info.get("ResearchDescription"))
        self._research_design_id: int = _parse.pss_int(research_design_info.get("ResearchDesignId"))
        self._research_design_type: str = _parse.pss_str(research_design_info.get("ResearchDesignType"))
        self._research_name: str = _parse.pss_str(research_design_info.get("ResearchName"))
        self._research_time: int = _parse.pss_int(research_design_info.get("ResearchTime"))
        self._root_research_design_id: int = _parse.pss_int(research_design_info.get("RootResearchDesignId"))
        self._starbux_cost: int = _parse.pss_int(research_design_info.get("StarbuxCost"))
        self._visibility_flags: str = _parse.pss_str(research_design_info.get("VisibilityFlags"))

    @property
    def argument(self) -> int:
        return self._argument

    @property
    def availability_mask(self) -> int:
        return self._availability_mask

    @property
    def gas_cost(self) -> int:
        return self._gas_cost

    @property
    def image_sprite_id(self) -> int:
        return self._image_sprite_id

    @property
    def logo_sprite_id(self) -> int:
        return self._logo_sprite_id

    @property
    def required_item_design_id(self) -> int:
        return self._required_item_design_id

    @property
    def required_lab_level(self) -> int:
        return self._required_lab_level

    @property
    def required_research_design_id(self) -> int:
        return self._required_research_design_id

    @property
    def research_description(self) -> str:
        return self._research_description

    @property
    def research_design_id(self) -> int:
        return self._research_design_id

    @property
    def research_design_type(self) -> str:
        return self._research_design_type

    @property
    def research_name(self) -> str:
        return self._research_name

    @property
    def research_time(self) -> int:
        return self._research_time

    @property
    def root_research_design_id(self) -> int:
        return self._root_research_design_id

    @property
    def starbux_cost(self) -> int:
        return self._starbux_cost

    @property
    def visibility_flags(self) -> str:
        return self._visibility_flags

    def _key(self):
        return (
            self.argument,
            self.availability_mask,
            self.gas_cost,
            self.image_sprite_id,
            self.logo_sprite_id,
            self.required_item_design_id,
            self.required_lab_level,
            self.required_research_design_id,
            self.research_description,
            self.research_design_id,
            self.research_design_type,
            self.research_name,
            self.research_time,
            self.root_research_design_id,
            self.starbux_cost,
            self.visibility_flags,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "Argument": self.argument,
                "AvailabilityMask": self.availability_mask,
                "GasCost": self.gas_cost,
                "ImageSpriteId": self.image_sprite_id,
                "LogoSpriteId": self.logo_sprite_id,
                "RequiredItemDesignId": self.required_item_design_id,
                "RequiredLabLevel": self.required_lab_level,
                "RequiredResearchDesignId": self.required_research_design_id,
                "ResearchDescription": self.research_description,
                "ResearchDesignId": self.research_design_id,
                "ResearchDesignType": self.research_design_type,
                "ResearchName": self.research_name,
                "ResearchTime": self.research_time,
                "RootResearchDesignId": self.root_research_design_id,
                "StarbuxCost": self.starbux_cost,
                "VisibilityFlags": self.visibility_flags,
            }

        return self._dict
