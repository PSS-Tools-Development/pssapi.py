from .. import enums as _enums
from ..types import EntityInfo as _EntityInfo
from ..utils import parse as _parse
from .entity_base import EntityWithIdBase as _EntityWithIdBase
from .raw import UserRaw as _UserRaw


class User(_UserRaw, _EntityWithIdBase):
    def __init__(self, user_info: _EntityInfo) -> None:
        super().__init__(user_info)
        self._alliance_membership_enum: _enums.AllianceMembership = _parse.pss_str_enum(self.alliance_membership, _enums.AllianceMembership)
        self._authentication_type_enum: _enums.AuthenticationType = _parse.pss_str_enum(self.authentication_type, _enums.AuthenticationType)
        self._daily_reward_status_enum: _enums.DailyRewardStatus = _parse.pss_int_enum(self.daily_reward_status, _enums.DailyRewardStatus)
        self._email_verification_status_enum: _enums.EmailVerificationStatus = _parse.pss_str_enum(self.email_verification_status, _enums.EmailVerificationStatus)
        self._flags_enum: _enums.UserFlags = _parse.pss_int_enum(self.flags, _enums.UserFlags)
        self._gender_type_enum: _enums.GenderType = _parse.pss_str_enum(self.gender_type, _enums.GenderType)
        self._language_key_enum: _enums.LanguageKey = _parse.pss_str_enum(self.language_key, _enums.LanguageKey)
        self._league_type_enum: _enums.LeagueType = _parse.pss_str_enum(self.league_type, _enums.LeagueType)
        self._matching_status_enum: _enums.MatchingStatus = _parse.pss_str_enum(self.matching_status, _enums.MatchingStatus)
        self._race_type_enum: _enums.RaceType = _parse.pss_str_enum(self.race_type, _enums.RaceType)
        self._status_enum: _enums.UserStatus = _parse.pss_int_enum(self.status, _enums.UserStatus)
        # self._tip_status_enum: _enums. = _parse.pss_int_enum(self.tip_status, _enums.)   # enum doesn't exist up to PSS v0.994.1
        # self._tutorial_status_enum: _enums. = _parse.pss_int_enum(self.tutorial_status, _enums.)   # enum doesn't exist up to PSS v0.994.1
        self._user_source_ads_platform_type_enum: _enums.PlatformType = _parse.pss_str_enum(self.user_source_ads_platform_type, _enums.PlatformType)
        self._user_type_enum: _enums.UserType = _parse.pss_str_enum(self.user_type, _enums.UserType)

    @property
    def id(self) -> int:
        return self.id_

    @property
    def alliance_membership_enum(self) -> "_enums.AllianceMembership":
        return self._alliance_membership_enum

    @property
    def authentication_type_enum(self) -> "_enums.AuthenticationType":
        return self._authentication_type_enum

    @property
    def daily_reward_status_enum(self) -> "_enums.DailyRewardStatus":
        return self._daily_reward_status_enum

    @property
    def email_verification_status_enum(self) -> "_enums.EmailVerificationStatus":
        return self._email_verification_status_enum

    @property
    def flags_enum(self) -> "_enums.UserFlags":
        return self._flags_enum

    @property
    def gender_type_enum(self) -> "_enums.GenderType":
        return self._gender_type_enum

    @property
    def language_key_enum(self) -> "_enums.LanguageKey":
        return self._language_key_enum

    @property
    def league_type_enum(self) -> "_enums.LeagueType":
        return self._league_type_enum

    @property
    def matching_status_enum(self) -> "_enums.MatchingStatus":
        return self._matching_status_enum

    @property
    def race_type_enum(self) -> "_enums.RaceType":
        return self._race_type_enum

    @property
    def status_enum(self) -> "_enums.UserStatus":
        return self._status_enum

    # @property   # enum doesn't exist up to PSS v0.994.1
    # def tip_status_enum(self) -> "_enums.":
    #    return self._tip_status_enum

    # @property   # enum doesn't exist up to PSS v0.994.1
    # def tutorial_status_enum(self) -> "_enums.":
    #    return self._tutorial_status_enum

    @property
    def user_source_ads_platform_type_enum(self) -> "_enums.PlatformType":
        return self._user_source_ads_platform_type_enum

    @property
    def user_type_enum(self) -> "_enums.UserType":
        return self._user_type_enum
