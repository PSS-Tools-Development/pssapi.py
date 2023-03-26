from datetime import datetime as _datetime
from threading import Lock as _Lock

import pssapi.core as _core
import pssapi.entities as _entities
import pssapi.enums as _enums
import pssapi.services as _services
import pssapi.services.raw as _services_raw
import pssapi.utils as _utils


class PssApiClientBase:
    __PRODUCTION_SERVER_CACHE_DURATION: int = 60  # seconds

    def __init__(self, device_type: "_enums.DeviceType" = None, language_key: "_enums.LanguageKey" = None, production_server: str = None, use_cache: bool = True):
        self.__device_type: _enums.DeviceType = device_type or _enums.DeviceType.ANDROID
        self.__language_key: _enums.LanguageKey = language_key or _enums.LanguageKey.ENGLISH
        self.__production_server: str = production_server or None  # if it's none, it'll be checked and cached for any API call
        self.__use_cache: bool = use_cache or False
        self.__latest_version_cached: str = None
        self.__latest_version_cached_at: _datetime = None
        self.__latest_version_cache_lock: _Lock = _Lock()

        self._update_services()

    @property
    def device_type(self) -> "_enums.DeviceType":
        return self.__device_type

    @property
    def language_key(self) -> "_enums.LanguageKey":
        return self.__language_key

    @property
    def production_server(self) -> str:
        return self.__production_server

    @production_server.setter
    def production_server(self, value):
        self.__production_server = value

    @property
    def achievement_service(self) -> "_services.AchievementService":
        return self.__achievement_service

    @property
    def alliance_service(self) -> "_services.AllianceService":
        return self.__alliance_service

    @property
    def animation_service(self) -> "_services.AnimationService":
        return self.__animation_service

    @property
    def background_service(self) -> "_services.BackgroundService":
        return self.__background_service

    @property
    def challenge_service(self) -> "_services.ChallengeService":
        return self.__challenge_service

    @property
    def character_service(self) -> "_services.CharacterService":
        return self.__character_service

    @property
    def collection_service(self) -> "_services.CollectionService":
        return self.__collection_service

    @property
    def design_service(self) -> "_services.DesignService":
        return self.__design_service

    @property
    def division_service(self) -> "_services.DivisionService":
        return self.__division_service

    @property
    def file_service(self) -> "_services.FileService":
        return self.__file_service

    @property
    def galaxy_service(self) -> "_services.GalaxyService":
        return self.__galaxy_service

    @property
    def history_service(self) -> "_services.HistoryService":
        return self.__history_service

    @property
    def item_service(self) -> "_services.ItemService":
        return self.__item_service

    @property
    def ladder_service(self) -> "_services.LadderService":
        return self.__ladder_service

    @property
    def league_service(self) -> "_services.LeagueService":
        return self.__league_service

    @property
    def live_ops_service(self) -> "_services.LiveOpsService":
        return self.__live_ops_service

    @property
    def market_service(self) -> "_services.MarketService":
        return self.__market_service

    @property
    def message_service(self) -> "_services.MessageService":
        return self.__message_service

    @property
    def mission_service(self) -> "_services.MissionService":
        return self.__mission_service

    @property
    def promotion_service(self) -> "_services.PromotionService":
        return self.__promotion_service

    @property
    def research_service(self) -> "_services.ResearchService":
        return self.__research_service

    @property
    def reward_service(self) -> "_services.RewardService":
        return self.__reward_service

    @property
    def room_design_sprite_service(self) -> "_services.RoomDesignSpriteService":
        return self.__room_design_sprite_service

    @property
    def room_service(self) -> "_services.RoomService":
        return self.__room_service

    @property
    def season_service(self) -> "_services.SeasonService":
        return self.__season_service

    @property
    def setting_service(self) -> "_services.SettingService":
        return self.__setting_service

    @property
    def ship_service(self) -> "_services.ShipService":
        return self.__ship_service

    @property
    def situation_service(self) -> "_services.SituationService":
        return self.__situation_service

    @property
    def task_service(self) -> "_services.TaskService":
        return self.__task_service

    @property
    def training_service(self) -> "_services.TrainingService":
        return self.__training_service

    @property
    def user_service(self) -> "_services.UserService":
        return self.__user_service

    async def get_latest_version(self, use_cache: bool = True) -> "_entities.Setting":
        if self.__use_cache and use_cache:
            with self.__latest_version_cache_lock:
                utc_now = _utils.get_utc_now()
                if (
                    not self.__latest_version_cached
                    or self.__latest_version_cached_at is None
                    or (self.__latest_version_cached_at - utc_now).total_seconds() >= PssApiClientBase.__PRODUCTION_SERVER_CACHE_DURATION
                ):
                    production_server = await _core.get_production_server(self.device_type, self.language_key)
                    self.__latest_version_cached = await _services_raw.SettingServiceRaw.get_latest_version_3(production_server, self.device_type, self.language_key)
                    self.__latest_version_cached_at = _utils.get_utc_now()
                return self.__latest_version_cached
        else:
            return await self.setting_service.get_latest_version(self.device_type)

    async def get_production_server(self, use_cache: bool = True) -> str:
        if self.__production_server:
            return self.__production_server

        return (await self.get_latest_version(use_cache=use_cache)).production_server

    def _update_services(self) -> None:
        self.__achievement_service: _services.AchievementService = _services.AchievementService(self)
        self.__alliance_service: _services.AllianceService = _services.AllianceService(self)
        self.__animation_service: _services.AnimationService = _services.AnimationService(self)
        self.__background_service: _services.BackgroundService = _services.BackgroundService(self)
        self.__challenge_service: _services.ChallengeService = _services.ChallengeService(self)
        self.__character_service: _services.CharacterService = _services.CharacterService(self)
        self.__collection_service: _services.CollectionService = _services.CollectionService(self)
        self.__design_service: _services.DesignService = _services.DesignService(self)
        self.__division_service: _services.DivisionService = _services.DivisionService(self)
        self.__file_service: _services.FileService = _services.FileService(self)
        self.__galaxy_service: _services.GalaxyService = _services.GalaxyService(self)
        self.__history_service: _services.HistoryService = _services.HistoryService(self)
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
