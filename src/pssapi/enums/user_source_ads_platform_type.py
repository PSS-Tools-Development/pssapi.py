from .str_enum_base import StrEnumBase as _StrEnumBase


class UserSourceAdsPlatformType(_StrEnumBase):
    UNKNOWN = "Unknown"
    CHANYOU = "Chanyou"
    BAIDU = "Baidu"
    TIKTOK = "Tiktok"
    BILIBILI = "Bilibili"
    NO_REPORTING_USER = "NoReportingUser"
