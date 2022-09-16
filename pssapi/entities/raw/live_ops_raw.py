####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class LiveOpsRaw():
    XML_NODE_NAME: str = 'LiveOps'

    def __init__(self, live_ops_info: _EntityInfo) -> None:
        self.__live_ops_id: int = _parse.pss_int(live_ops_info.get('LiveOpsId'))
        self.__news: str = _parse.pss_str(live_ops_info.get('News'))
        self.__daily_reward_type: str = _parse.pss_str(live_ops_info.get('DailyRewardType'))
        self.__daily_reward_argument: int = _parse.pss_int(live_ops_info.get('DailyRewardArgument'))
        self.__sale_type: str = _parse.pss_str(live_ops_info.get('SaleType'))
        self.__sale_argument: int = _parse.pss_int(live_ops_info.get('SaleArgument'))
        self.__sale_item_mask: int = _parse.pss_int(live_ops_info.get('SaleItemMask'))
        self.__sale_once_only: bool = _parse.pss_bool(live_ops_info.get('SaleOnceOnly'))
        self.__sale_quantity: int = _parse.pss_int(live_ops_info.get('SaleQuantity'))
        self.__daily_item_rewards: str = _parse.pss_str(live_ops_info.get('DailyItemRewards'))
        self.__limited_catalog_type: str = _parse.pss_str(live_ops_info.get('LimitedCatalogType'))
        self.__limited_catalog_argument: int = _parse.pss_int(live_ops_info.get('LimitedCatalogArgument'))
        self.__limited_catalog_quantity: int = _parse.pss_int(live_ops_info.get('LimitedCatalogQuantity'))
        self.__limited_catalog_expiry_date: datetime = _parse.pss_datetime(live_ops_info.get('LimitedCatalogExpiryDate'))
        self.__limited_catalog_currency_type: str = _parse.pss_str(live_ops_info.get('LimitedCatalogCurrencyType'))
        self.__limited_catalog_currency_amount: int = _parse.pss_int(live_ops_info.get('LimitedCatalogCurrencyAmount'))
        self.__limited_catalog_max_total: int = _parse.pss_int(live_ops_info.get('LimitedCatalogMaxTotal'))
        self.__cargo_items: str = _parse.pss_str(live_ops_info.get('CargoItems'))
        self.__cargo_prices: str = _parse.pss_str(live_ops_info.get('CargoPrices'))
        self.__tournament_news: str = _parse.pss_str(live_ops_info.get('TournamentNews'))
        self.__sale_title: str = _parse.pss_str(live_ops_info.get('SaleTitle'))
        self.__limited_catalog_restock_quantity: int = _parse.pss_int(live_ops_info.get('LimitedCatalogRestockQuantity'))
        self.__sale_reward_string: str = _parse.pss_str(live_ops_info.get('SaleRewardString'))
        self.__sale_start_date: datetime = _parse.pss_datetime(live_ops_info.get('SaleStartDate'))
        self.__support_task_ran_date: datetime = _parse.pss_datetime(live_ops_info.get('SupportTaskRanDate'))
        self.__sale_end_date: datetime = _parse.pss_datetime(live_ops_info.get('SaleEndDate'))
        self.__news_sprite_id: int = _parse.pss_int(live_ops_info.get('NewsSpriteId'))
        self.__news_update_date: datetime = _parse.pss_datetime(live_ops_info.get('NewsUpdateDate'))
        self.__common_crew_id: int = _parse.pss_int(live_ops_info.get('CommonCrewId'))
        self.__hero_crew_id: int = _parse.pss_int(live_ops_info.get('HeroCrewId'))

    @property
    def live_ops_id(self) -> int:
        return self.__live_ops_id

    @property
    def news(self) -> str:
        return self.__news

    @property
    def daily_reward_type(self) -> str:
        return self.__daily_reward_type

    @property
    def daily_reward_argument(self) -> int:
        return self.__daily_reward_argument

    @property
    def sale_type(self) -> str:
        return self.__sale_type

    @property
    def sale_argument(self) -> int:
        return self.__sale_argument

    @property
    def sale_item_mask(self) -> int:
        return self.__sale_item_mask

    @property
    def sale_once_only(self) -> bool:
        return self.__sale_once_only

    @property
    def sale_quantity(self) -> int:
        return self.__sale_quantity

    @property
    def daily_item_rewards(self) -> str:
        return self.__daily_item_rewards

    @property
    def limited_catalog_type(self) -> str:
        return self.__limited_catalog_type

    @property
    def limited_catalog_argument(self) -> int:
        return self.__limited_catalog_argument

    @property
    def limited_catalog_quantity(self) -> int:
        return self.__limited_catalog_quantity

    @property
    def limited_catalog_expiry_date(self) -> datetime:
        return self.__limited_catalog_expiry_date

    @property
    def limited_catalog_currency_type(self) -> str:
        return self.__limited_catalog_currency_type

    @property
    def limited_catalog_currency_amount(self) -> int:
        return self.__limited_catalog_currency_amount

    @property
    def limited_catalog_max_total(self) -> int:
        return self.__limited_catalog_max_total

    @property
    def cargo_items(self) -> str:
        return self.__cargo_items

    @property
    def cargo_prices(self) -> str:
        return self.__cargo_prices

    @property
    def tournament_news(self) -> str:
        return self.__tournament_news

    @property
    def sale_title(self) -> str:
        return self.__sale_title

    @property
    def limited_catalog_restock_quantity(self) -> int:
        return self.__limited_catalog_restock_quantity

    @property
    def sale_reward_string(self) -> str:
        return self.__sale_reward_string

    @property
    def sale_start_date(self) -> datetime:
        return self.__sale_start_date

    @property
    def support_task_ran_date(self) -> datetime:
        return self.__support_task_ran_date

    @property
    def sale_end_date(self) -> datetime:
        return self.__sale_end_date

    @property
    def news_sprite_id(self) -> int:
        return self.__news_sprite_id

    @property
    def news_update_date(self) -> datetime:
        return self.__news_update_date

    @property
    def common_crew_id(self) -> int:
        return self.__common_crew_id

    @property
    def hero_crew_id(self) -> int:
        return self.__hero_crew_id
