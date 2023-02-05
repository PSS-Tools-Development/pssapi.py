from datetime import datetime as _datetime
from threading import Lock as _Lock

from . import constants as _constants
from . import core as _core
from . import utils as _utils
from .enums import DeviceType as _DeviceType
from .enums import LanguageKey as _LanguageKey
from .services import AchievementService as _AchievementService
from .services import AllianceService as _AllianceService
from .services import AnimationService as _AnimationService
from .services import BackgroundService as _BackgroundService
from .services import ChallengeService as _ChallengeService
from .services import CharacterService as _CharacterService
from .services import CollectionService as _CollectionService
from .services import DivisionService as _DivisionService
from .services import FileService as _FileService
from .services import GalaxyService as _GalaxyService
from .services import ItemService as _ItemService
from .services import LadderService as _LadderService
from .services import LeagueService as _LeagueService
from .services import LiveOpsService as _LiveOpsService
from .services import MarketService as _MarketService
from .services import MessageService as _MessageService
from .services import MissionService as _MissionService
from .services import PromotionService as _PromotionService
from .services import ResearchService as _ResearchService
from .services import RewardService as _RewardService
from .services import RoomDesignSpriteService as _RoomDesignSpriteService
from .services import RoomService as _RoomService
from .services import SeasonService as _SeasonService
from .services import SettingService as _SettingService
from .services import ShipService as _ShipService
from .services import SituationService as _SituationService
from .services import TaskService as _TaskService
from .services import TrainingService as _TrainingService
from .services import UserService as _UserService


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
    def achievement_service(self) -> _AchievementService:
        return self.__achievement_service

    @property
    def alliance_service(self) -> _AllianceService:
        return self.__alliance_service

    @property
    def animation_service(self) -> _AnimationService:
        return self.__animation_service

    @property
    def background_service(self) -> _BackgroundService:
        return self.__background_service

    @property
    def challenge_service(self) -> _ChallengeService:
        return self.__challenge_service

    @property
    def character_service(self) -> _CharacterService:
        return self.__character_service

    @property
    def collection_service(self) -> _CollectionService:
        return self.__collection_service

    @property
    def division_service(self) -> _DivisionService:
        return self.__division_service

    @property
    def file_service(self) -> _FileService:
        return self.__file_service

    @property
    def galaxy_service(self) -> _GalaxyService:
        return self.__galaxy_service

    @property
    def item_service(self) -> _ItemService:
        return self.__item_service

    @property
    def ladder_service(self) -> _LadderService:
        return self.__ladder_service

    @property
    def league_service(self) -> _LeagueService:
        return self.__league_service

    @property
    def live_ops_service(self) -> _LiveOpsService:
        return self.__live_ops_service

    @property
    def market_service(self) -> _MarketService:
        return self.__market_service

    @property
    def message_service(self) -> _MessageService:
        return self.__message_service

    @property
    def mission_service(self) -> _MissionService:
        return self.__mission_service

    @property
    def promotion_service(self) -> _PromotionService:
        return self.__promotion_service

    @property
    def research_service(self) -> _ResearchService:
        return self.__research_service

    @property
    def reward_service(self) -> _RewardService:
        return self.__reward_service

    @property
    def room_design_sprite_service(self) -> _RoomDesignSpriteService:
        return self.__room_design_sprite_service

    @property
    def room_service(self) -> _RoomService:
        return self.__room_service

    @property
    def season_service(self) -> _SeasonService:
        return self.__season_service

    @property
    def setting_service(self) -> _SettingService:
        return self.__setting_service

    @property
    def ship_service(self) -> _ShipService:
        return self.__ship_service

    @property
    def situation_service(self) -> _SituationService:
        return self.__situation_service

    @property
    def task_service(self) -> _TaskService:
        return self.__task_service

    @property
    def training_service(self) -> _TrainingService:
        return self.__training_service

    @property
    def user_service(self) -> _UserService:
        return self.__user_service


    async def get_production_server(self) -> str:
        if self.__production_server:
            return self.__production_server

        with self.__production_server_cache_lock:
            utc_now = _utils.get_utc_now()
            if not self.__production_server_cached or (self.__production_server_cached_at - utc_now).total_seconds() >= PssApiClientBase.__PRODUCTION_SERVER_CACHE_DURATION:
                self.__production_server_cached = (await _core.get_production_server())
            return self.__production_server_cached


    async def init_production_server(self) -> None:
        setting_service = _SettingService(
            _constants.DEFAULT_PRODUCTION_SERVER, self.language_key
        )

        settings = await setting_service.get_latest_version(self.device_type)
        self.production_server = settings[0].production_server

    def _update_services(self) -> None:
        self.__achievement_service: _AchievementService = _AchievementService(self)
        self.__alliance_service: _AllianceService = _AllianceService(self)
        self.__animation_service: _AnimationService = _AnimationService(self)
        self.__background_service: _BackgroundService = _BackgroundService(self)
        self.__challenge_service: _ChallengeService = _ChallengeService(self)
        self.__character_service: _CharacterService = _CharacterService(self)
        self.__collection_service: _CollectionService = _CollectionService(self)
        self.__division_service: _DivisionService = _DivisionService(self)
        self.__file_service: _FileService = _FileService(self)
        self.__galaxy_service: _GalaxyService = _GalaxyService(self)
        self.__item_service: _ItemService = _ItemService(self)
        self.__ladder_service: _LadderService = _LadderService(self)
        self.__league_service: _LeagueService = _LeagueService(self)
        self.__live_ops_service: _LiveOpsService = _LiveOpsService(self)
        self.__market_service: _MarketService = _MarketService(self)
        self.__message_service: _MessageService = _MessageService(self)
        self.__mission_service: _MissionService = _MissionService(self)
        self.__promotion_service: _PromotionService = _PromotionService(self)
        self.__research_service: _ResearchService = _ResearchService(self)
        self.__reward_service: _RewardService = _RewardService(self)
        self.__room_design_sprite_service: _RoomDesignSpriteService = _RoomDesignSpriteService(self)
        self.__room_service: _RoomService = _RoomService(self)
        self.__season_service: _SeasonService = _SeasonService(self)
        self.__setting_service: _SettingService = _SettingService(self)
        self.__ship_service: _ShipService = _ShipService(self)
        self.__situation_service: _SituationService = _SituationService(self)
        self.__task_service: _TaskService = _TaskService(self)
        self.__training_service: _TrainingService = _TrainingService(self)
        self.__user_service: _UserService = _UserService(self)
