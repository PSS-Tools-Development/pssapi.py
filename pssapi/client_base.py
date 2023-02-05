from datetime import datetime as _datetime
from threading import Lock as _Lock

from . import constants as _constants
from . import core as _core
from . import utils as _utils
from .enums import DeviceType as _DeviceType
from .enums import LanguageKey as _LanguageKey
import pssapi.services as _services


class PssApiClientBase:
    __PRODUCTION_SERVER_CACHE_DURATION: float = 60.0

    def __init__(self, device_type: _DeviceType = None, language_key: _LanguageKey = None, production_server: str = None) -> None:
        self.__device_type: _DeviceType = device_type or _DeviceType.DEVICE_TYPE_ANDROID
        self.__language_key: _LanguageKey = language_key or _LanguageKey.ENGLISH
        self.__production_server: str = production_server or None # if it's none, it'll be checked and cached for any API call
        self.__production_server_cached: str = None
        self.__production_server_cached_at: _datetime = None
        self.__production_server_cache_lock: _Lock = _Lock()

        self._update_services()


    @property
    def device_type(self) -> _DeviceType:
        return self.__device_type

    @property
    def language_key(self) -> _LanguageKey:
        return self.__language_key

    @property
    def production_server(self) -> str:
        return self.__production_server

    @production_server.setter
    def production_server(self, value):
        self.__production_server = value

    @property
    def achievement_service(self) -> '_services.AchievementService':
        return self.__achievement_service

    @property
    def alliance_service(self) -> '_services.AllianceService':
        return self.__alliance_service

    @property
    def animation_service(self) -> '_services.AnimationService':
        return self.__animation_service

    @property
    def background_service(self) -> '_services.BackgroundService':
        return self.__background_service

    @property
    def challenge_service(self) -> '_services.ChallengeService':
        return self.__challenge_service

    @property
    def character_service(self) -> '_services.CharacterService':
        return self.__character_service

    @property
    def collection_service(self) -> '_services.CollectionService':
        return self.__collection_service

    @property
    def division_service(self) -> '_services.DivisionService':
        return self.__division_service

    @property
    def file_service(self) -> '_services.FileService':
        return self.__file_service

    @property
    def galaxy_service(self) -> '_services.GalaxyService':
        return self.__galaxy_service

    @property
    def item_service(self) -> '_services.ItemService':
        return self.__item_service

    @property
    def ladder_service(self) -> '_services.LadderService':
        return self.__ladder_service

    @property
    def league_service(self) -> '_services.LeagueService':
        return self.__league_service

    @property
    def live_ops_service(self) -> '_services.LiveOpsService':
        return self.__live_ops_service

    @property
    def market_service(self) -> '_services.MarketService':
        return self.__market_service

    @property
    def message_service(self) -> '_services.MessageService':
        return self.__message_service

    @property
    def mission_service(self) -> '_services.MissionService':
        return self.__mission_service

    @property
    def promotion_service(self) -> '_services.PromotionService':
        return self.__promotion_service

    @property
    def research_service(self) -> '_services.ResearchService':
        return self.__research_service

    @property
    def reward_service(self) -> '_services.RewardService':
        return self.__reward_service

    @property
    def room_design_sprite_service(self) -> '_services.RoomDesignSpriteService':
        return self.__room_design_sprite_service

    @property
    def room_service(self) -> '_services.RoomService':
        return self.__room_service

    @property
    def season_service(self) -> '_services.SeasonService':
        return self.__season_service

    @property
    def setting_service(self) -> '_services.SettingService':
        return self.__setting_service

    @property
    def ship_service(self) -> '_services.ShipService':
        return self.__ship_service

    @property
    def situation_service(self) -> '_services.SituationService':
        return self.__situation_service

    @property
    def task_service(self) -> '_services.TaskService':
        return self.__task_service

    @property
    def training_service(self) -> '_services.TrainingService':
        return self.__training_service

    @property
    def user_service(self) -> '_services.UserService':
        return self.__user_service


    async def get_production_server(self) -> str:
        if self.__production_server:
            return self.__production_server

        with self.__production_server_cache_lock:
            utc_now = _utils.get_utc_now()
            if not self.__production_server_cached or self.__production_server_cached_at is None or (self.__production_server_cached_at - utc_now).total_seconds() >= PssApiClientBase.__PRODUCTION_SERVER_CACHE_DURATION:
                self.__production_server_cached_at = utc_now
                self.__production_server_cached = (await _core.get_production_server())
            return self.__production_server_cached


    async def init_production_server(self) -> None:
        setting_service = _services.SettingService(
            _constants.DEFAULT_PRODUCTION_SERVER, self.language_key
        )

        settings = await setting_service.get_latest_version(self.device_type)
        self.production_server = settings[0].production_server


    def _update_services(self) -> None:
        self.__achievement_service: _services.AchievementService = _services.AchievementService(self)
        self.__alliance_service: _services.AllianceService = _services.AllianceService(self)
        self.__animation_service: _services.AnimationService = _services.AnimationService(self)
        self.__background_service: _services.BackgroundService = _services.BackgroundService(self)
        self.__challenge_service: _services.ChallengeService = _services.ChallengeService(self)
        self.__character_service: _services.CharacterService = _services.CharacterService(self)
        self.__collection_service: _services.CollectionService = _services.CollectionService(self)
        self.__division_service: _services.DivisionService = _services.DivisionService(self)
        self.__file_service: _services.FileService = _services.FileService(self)
        self.__galaxy_service: _services.GalaxyService = _services.GalaxyService(self)
        self.__item_service: _services.ItemService = _services.ItemService(self)
        self.__ladder_service: _services.LadderService = _services.LadderService(self)
        self.__league_service: _services.LeagueService = _services.LeagueService(self)
        self.__live_ops_service: _services.LiveOpsService = _services.LiveOpsService(self)
        self.__market_service: _services.MarketService = _services.MarketService(self)
        self.__message_service: _services.MessageService = _services.MessageService(self)
        self.__mission_service: _services.MissionService = _services.MissionService(self)
        self.__promotion_service: _services.PromotionService = _services.PromotionService(self)
        self.__research_service: _services.ResearchService = _services.ResearchService(self)
        self.__reward_service: _services.RewardService = _services.RewardService(self)
        self.__room_design_sprite_service: _services.RoomDesignSpriteService = _services.RoomDesignSpriteService(self)
        self.__room_service: _services.RoomService = _services.RoomService(self)
        self.__season_service: _services.SeasonService = _services.SeasonService(self)
        self.__setting_service: _services.SettingService = _services.SettingService(self)
        self.__ship_service: _services.ShipService = _services.ShipService(self)
        self.__situation_service: _services.SituationService = _services.SituationService(self)
        self.__task_service: _services.TaskService = _services.TaskService(self)
        self.__training_service: _services.TrainingService = _services.TrainingService(self)
        self.__user_service: _services.UserService = _services.UserService(self)
