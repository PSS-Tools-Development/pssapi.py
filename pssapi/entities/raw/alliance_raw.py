####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class AllianceRaw():
    XML_NODE_NAME: str = 'Alliance'

    def __init__(self, alliance_info: _EntityInfo) -> None:
        self.__alliance_name: str = _parse.pss_str(alliance_info.get('AllianceName'))
        self.__immunity_date: datetime = _parse.pss_datetime(alliance_info.get('ImmunityDate'))
        self.__championship_score: int = _parse.pss_int(alliance_info.get('ChampionshipScore'))
        self.__alliance_country_code: str = _parse.pss_str(alliance_info.get('AllianceCountryCode'))
        self.__number_of_members: int = _parse.pss_int(alliance_info.get('NumberOfMembers'))
        self.__credits: int = _parse.pss_int(alliance_info.get('Credits'))
        self.__number_of_approved_members: int = _parse.pss_int(alliance_info.get('NumberOfApprovedMembers'))
        self.__trophy: int = _parse.pss_int(alliance_info.get('Trophy'))
        self.__alliance_sprite_id: int = _parse.pss_int(alliance_info.get('AllianceSpriteId'))
        self.__score: int = _parse.pss_int(alliance_info.get('Score'))
        self.__ranking: int = _parse.pss_int(alliance_info.get('Ranking'))
        self.__requires_approval: bool = _parse.pss_bool(alliance_info.get('RequiresApproval'))
        self.__enable_wars: bool = _parse.pss_bool(alliance_info.get('EnableWars'))
        self.__division_design_id: int = _parse.pss_int(alliance_info.get('DivisionDesignId'))
        self.__alliance_description: str = _parse.pss_str(alliance_info.get('AllianceDescription'))
        self.__alliance_id: int = _parse.pss_int(alliance_info.get('AllianceId'))
        self.__min_trophy_required: int = _parse.pss_int(alliance_info.get('MinTrophyRequired'))
        self.__channel_id: int = _parse.pss_int(alliance_info.get('ChannelId'))
        self.__alliance_ship_user_id: int = _parse.pss_int(alliance_info.get('AllianceShipUserId'))

    @property
    def alliance_name(self) -> str:
        return self.__alliance_name

    @property
    def immunity_date(self) -> datetime:
        return self.__immunity_date

    @property
    def championship_score(self) -> int:
        return self.__championship_score

    @property
    def alliance_country_code(self) -> str:
        return self.__alliance_country_code

    @property
    def number_of_members(self) -> int:
        return self.__number_of_members

    @property
    def credits(self) -> int:
        return self.__credits

    @property
    def number_of_approved_members(self) -> int:
        return self.__number_of_approved_members

    @property
    def trophy(self) -> int:
        return self.__trophy

    @property
    def alliance_sprite_id(self) -> int:
        return self.__alliance_sprite_id

    @property
    def score(self) -> int:
        return self.__score

    @property
    def ranking(self) -> int:
        return self.__ranking

    @property
    def requires_approval(self) -> bool:
        return self.__requires_approval

    @property
    def enable_wars(self) -> bool:
        return self.__enable_wars

    @property
    def division_design_id(self) -> int:
        return self.__division_design_id

    @property
    def alliance_description(self) -> str:
        return self.__alliance_description

    @property
    def alliance_id(self) -> int:
        return self.__alliance_id

    @property
    def min_trophy_required(self) -> int:
        return self.__min_trophy_required

    @property
    def channel_id(self) -> int:
        return self.__channel_id

    @property
    def alliance_ship_user_id(self) -> int:
        return self.__alliance_ship_user_id
