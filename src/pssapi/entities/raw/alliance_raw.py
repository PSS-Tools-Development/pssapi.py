"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class AllianceRaw:
    XML_NODE_NAME: str = "Alliance"

    def __init__(self, alliance_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._alliance_country_code: str = _parse.pss_str(alliance_info.get("AllianceCountryCode"))
        self._alliance_description: str = _parse.pss_str(alliance_info.get("AllianceDescription"))
        self._alliance_id: int = _parse.pss_int(alliance_info.get("AllianceId"))
        self._alliance_name: str = _parse.pss_str(alliance_info.get("AllianceName"))
        self._alliance_ship_user_id: int = _parse.pss_int(alliance_info.get("AllianceShipUserId"))
        self._alliance_sprite_id: int = _parse.pss_int(alliance_info.get("AllianceSpriteId"))
        self._championship_score: int = _parse.pss_int(alliance_info.get("ChampionshipScore"))
        self._channel_id: int = _parse.pss_int(alliance_info.get("ChannelId"))
        self._credits: str = _parse.pss_str(alliance_info.get("Credits"))
        self._division_design_id: int = _parse.pss_int(alliance_info.get("DivisionDesignId"))
        self._enable_wars: bool = _parse.pss_bool(alliance_info.get("EnableWars"))
        self._immunity_date: _datetime = _parse.pss_datetime(alliance_info.get("ImmunityDate"))
        self._min_trophy_required: int = _parse.pss_int(alliance_info.get("MinTrophyRequired"))
        self._number_of_approved_members: int = _parse.pss_int(alliance_info.get("NumberOfApprovedMembers"))
        self._number_of_members: int = _parse.pss_int(alliance_info.get("NumberOfMembers"))
        self._ranking: int = _parse.pss_int(alliance_info.get("Ranking"))
        self._requires_approval: bool = _parse.pss_bool(alliance_info.get("RequiresApproval"))
        self._score: int = _parse.pss_int(alliance_info.get("Score"))
        self._trophy: int = _parse.pss_int(alliance_info.get("Trophy"))

    @property
    def alliance_country_code(self) -> str:
        return self._alliance_country_code

    @property
    def alliance_description(self) -> str:
        return self._alliance_description

    @property
    def alliance_id(self) -> int:
        return self._alliance_id

    @property
    def alliance_name(self) -> str:
        return self._alliance_name

    @property
    def alliance_ship_user_id(self) -> int:
        return self._alliance_ship_user_id

    @property
    def alliance_sprite_id(self) -> int:
        return self._alliance_sprite_id

    @property
    def championship_score(self) -> int:
        return self._championship_score

    @property
    def channel_id(self) -> int:
        return self._channel_id

    @property
    def credits(self) -> str:
        return self._credits

    @property
    def division_design_id(self) -> int:
        return self._division_design_id

    @property
    def enable_wars(self) -> bool:
        return self._enable_wars

    @property
    def immunity_date(self) -> _datetime:
        return self._immunity_date

    @property
    def min_trophy_required(self) -> int:
        return self._min_trophy_required

    @property
    def number_of_approved_members(self) -> int:
        return self._number_of_approved_members

    @property
    def number_of_members(self) -> int:
        return self._number_of_members

    @property
    def ranking(self) -> int:
        return self._ranking

    @property
    def requires_approval(self) -> bool:
        return self._requires_approval

    @property
    def score(self) -> int:
        return self._score

    @property
    def trophy(self) -> int:
        return self._trophy

    def _key(self):
        return (
            self.alliance_country_code,
            self.alliance_description,
            self.alliance_id,
            self.alliance_name,
            self.alliance_ship_user_id,
            self.alliance_sprite_id,
            self.championship_score,
            self.channel_id,
            self.credits,
            self.division_design_id,
            self.enable_wars,
            self.immunity_date,
            self.min_trophy_required,
            self.number_of_approved_members,
            self.number_of_members,
            self.ranking,
            self.requires_approval,
            self.score,
            self.trophy,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AllianceCountryCode": self.alliance_country_code,
                "AllianceDescription": self.alliance_description,
                "AllianceId": self.alliance_id,
                "AllianceName": self.alliance_name,
                "AllianceShipUserId": self.alliance_ship_user_id,
                "AllianceSpriteId": self.alliance_sprite_id,
                "ChampionshipScore": self.championship_score,
                "ChannelId": self.channel_id,
                "Credits": self.credits,
                "DivisionDesignId": self.division_design_id,
                "EnableWars": self.enable_wars,
                "ImmunityDate": self.immunity_date,
                "MinTrophyRequired": self.min_trophy_required,
                "NumberOfApprovedMembers": self.number_of_approved_members,
                "NumberOfMembers": self.number_of_members,
                "Ranking": self.ranking,
                "RequiresApproval": self.requires_approval,
                "Score": self.score,
                "Trophy": self.trophy,
            }

        return self._dict
