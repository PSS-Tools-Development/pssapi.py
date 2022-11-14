"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class AllianceRaw:
    XML_NODE_NAME: str = 'Alliance'

    def __init__(self, alliance_info: _EntityInfo) -> None:
        self.alliance_country_code: str = _parse.pss_str(alliance_info.get('AllianceCountryCode'))
        self.alliance_description: str = _parse.pss_str(alliance_info.get('AllianceDescription'))
        self.alliance_id: int = _parse.pss_int(alliance_info.get('AllianceId'))
        self.alliance_name: str = _parse.pss_str(alliance_info.get('AllianceName'))
        self.alliance_ship_user_id: int = _parse.pss_int(alliance_info.get('AllianceShipUserId'))
        self.alliance_sprite_id: int = _parse.pss_int(alliance_info.get('AllianceSpriteId'))
        self.championship_score: int = _parse.pss_int(alliance_info.get('ChampionshipScore'))
        self.channel_id: int = _parse.pss_int(alliance_info.get('ChannelId'))
        self.credits: int = _parse.pss_int(alliance_info.get('Credits'))
        self.division_design_id: int = _parse.pss_int(alliance_info.get('DivisionDesignId'))
        self.enable_wars: bool = _parse.pss_bool(alliance_info.get('EnableWars'))
        self.immunity_date: _datetime = _parse.pss__datetime(alliance_info.get('ImmunityDate'))
        self.min_trophy_required: int = _parse.pss_int(alliance_info.get('MinTrophyRequired'))
        self.number_of_approved_members: int = _parse.pss_int(alliance_info.get('NumberOfApprovedMembers'))
        self.number_of_members: int = _parse.pss_int(alliance_info.get('NumberOfMembers'))
        self.ranking: int = _parse.pss_int(alliance_info.get('Ranking'))
        self.requires_approval: bool = _parse.pss_bool(alliance_info.get('RequiresApproval'))
        self.score: int = _parse.pss_int(alliance_info.get('Score'))
        self.trophy: int = _parse.pss_int(alliance_info.get('Trophy'))
