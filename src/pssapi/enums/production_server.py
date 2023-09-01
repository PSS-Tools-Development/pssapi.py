from .str_enum_base import StrEnumBase as _StrEnumBase


class ProductionServer(_StrEnumBase):
    BACKUP = "apibackup.pixelstarships.com"
    CHINA = "api.pixship.anjy.net"
    CHINA_DEV = "apidev.pixship.anjy.net"
    DEFAULT = "api.pixelstarships.com"
    DEV = "apidev.pixelstarships.com"
    PROD2 = "api2.pixelstarships.com"
    STAGING = "apistaging.pixelstarships.com"
    TAP_TAP = "mobileapi.pixship.anjy.net"
    TEST = "apitest.pixelstarships.com"
