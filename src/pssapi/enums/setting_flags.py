from enum import IntFlag as _IntFlag

from .int_flag_object_base import IntFlagObjectBase as _IntFlagObjectBase


class SettingFlags(_IntFlag):
    NONE = 0
    IMAC_FULL_SCREEN_SETTING_FLAG = 1
    CHINA_MODE = 2
    USE_ONE_SIGNAL = 4
    USE_FIREBASE_MESSAGING = 8
    USE_REDIS = 16
    SYNC_SERVER = 32
    NEW_TOURNAMENT_CHANGES = 64
    DOWNLOAD_ALL_DESIGNS = 128
    USE_HEARTBEAT_WEBSOCKET = 256
    USE_SHIP_SNAPSHOT = 512
    USE_REDIS_COMPRESSION = 1024
    USE_CONCURRENCY_RED_LOCK = 2048
    USE_MARKET_SNIPING_DELAY = 4096
    USE_LIVE_OPS = 8192
    USE_HISTORY_CACHE = 16384
    LEGENDARY_LEAGUE = 32768
    ALLOW_ONE_GLOBAL_MERCHANT_SHIP = 65536
    ALLOW_ONE_GLOBAL_NPC_SHIP = 131072
    USE_OPEN_SEARCH = 262144
    USE_CLIENT_BATTLE_FINALISATION_ON_LOGIN = 524288
    ALLOW_TEST_PAYMENT_IN_DEVELOPMENT = 1048576
    FORCE_CLIENT_LANGUAGE_KEY = 2097152
    USE_RECAPTCHA = 4194304
    USE_2FA_FOR_WEB_ADMIN = 8388608
    USE_AWSS3 = 16777216
    USE_ALIYUN_OSS = 33554432
    CHECK_AGE = 67108864
    DO_NOT_CHECK_IP_ADDRESS = 134217728
    ALLOW_ADMIN_LOGIN_DURING_MAINTENANCE = 268435456


class SettingFlagsObject(_IntFlagObjectBase):
    def __init__(self, setting_flags: SettingFlags):
        super().__init__(setting_flags)

    @property
    def allow_admin_login_during_maintenance(self) -> bool:
        return bool(self.value & SettingFlags.ALLOW_ADMIN_LOGIN_DURING_MAINTENANCE)

    @property
    def allow_one_global_merchant_ship(self) -> bool:
        return bool(self.value & SettingFlags.ALLOW_ONE_GLOBAL_MERCHANT_SHIP)

    @property
    def allow_one_global_npc_ship(self) -> bool:
        return bool(self.value & SettingFlags.ALLOW_ONE_GLOBAL_NPC_SHIP)

    @property
    def allow_test_payment_in_development(self) -> bool:
        return bool(self.value & SettingFlags.ALLOW_TEST_PAYMENT_IN_DEVELOPMENT)

    @property
    def check_age(self) -> bool:
        return bool(self.value & SettingFlags.CHECK_AGE)

    @property
    def china_mode(self) -> bool:
        return bool(self.value & SettingFlags.CHINA_MODE)

    @property
    def do_not_check_ip_address(self) -> bool:
        return bool(self.value & SettingFlags.DO_NOT_CHECK_IP_ADDRESS)

    @property
    def download_all_designs(self) -> bool:
        return bool(self.value & SettingFlags.DOWNLOAD_ALL_DESIGNS)

    @property
    def force_client_language_key(self) -> bool:
        return bool(self.value & SettingFlags.FORCE_CLIENT_LANGUAGE_KEY)

    @property
    def imac_full_screen_setting_flag(self) -> bool:
        return bool(self.value & SettingFlags.IMAC_FULL_SCREEN_SETTING_FLAG)

    @property
    def legendary_league(self) -> bool:
        return bool(self.value & SettingFlags.LEGENDARY_LEAGUE)

    @property
    def new_tournament_changes(self) -> bool:
        return bool(self.value & SettingFlags.NEW_TOURNAMENT_CHANGES)

    @property
    def sync_server(self) -> bool:
        return bool(self.value & SettingFlags.SYNC_SERVER)

    @property
    def use_2fa_for_web_admin(self) -> bool:
        return bool(self.value & SettingFlags.USE_2FA_FOR_WEB_ADMIN)

    @property
    def use_aliyun_oss(self) -> bool:
        return bool(self.value & SettingFlags.USE_ALIYUN_OSS)

    @property
    def use_awss3(self) -> bool:
        return bool(self.value & SettingFlags.USE_AWSS3)

    @property
    def use_client_battle_finalisation_on_login(self) -> bool:
        return bool(self.value & SettingFlags.USE_CLIENT_BATTLE_FINALISATION_ON_LOGIN)

    @property
    def use_concurrency_red_lock(self) -> bool:
        return bool(self.value & SettingFlags.USE_CONCURRENCY_RED_LOCK)

    @property
    def use_firebase_messaging(self) -> bool:
        return bool(self.value & SettingFlags.USE_FIREBASE_MESSAGING)

    @property
    def use_heartbeat_websocket(self) -> bool:
        return bool(self.value & SettingFlags.USE_HEARTBEAT_WEBSOCKET)

    @property
    def use_history_cache(self) -> bool:
        return bool(self.value & SettingFlags.USE_HISTORY_CACHE)

    @property
    def use_live_ops(self) -> bool:
        return bool(self.value & SettingFlags.USE_LIVE_OPS)

    @property
    def use_market_sniping_delay(self) -> bool:
        return bool(self.value & SettingFlags.USE_MARKET_SNIPING_DELAY)

    @property
    def use_one_signal(self) -> bool:
        return bool(self.value & SettingFlags.USE_ONE_SIGNAL)

    @property
    def use_open_search(self) -> bool:
        return bool(self.value & SettingFlags.USE_OPEN_SEARCH)

    @property
    def use_recaptcha(self) -> bool:
        return bool(self.value & SettingFlags.USE_RECAPTCHA)

    @property
    def use_redis(self) -> bool:
        return bool(self.value & SettingFlags.USE_REDIS)

    @property
    def use_redis_compression(self) -> bool:
        return bool(self.value & SettingFlags.USE_REDIS_COMPRESSION)

    @property
    def use_ship_snapshot(self) -> bool:
        return bool(self.value & SettingFlags.USE_SHIP_SNAPSHOT)

    @property
    def value(self) -> SettingFlags:
        return self._value
