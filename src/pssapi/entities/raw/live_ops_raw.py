"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


from .entity_base_raw import EntityBaseRaw

class LiveOpsRaw(EntityBaseRaw):
    XML_NODE_NAME: str = "LiveOps"

    def __init__(self, live_ops_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._cargo_items: str = _parse.pss_str(live_ops_info.pop("CargoItems", None))
        self._cargo_prices: str = _parse.pss_str(live_ops_info.pop("CargoPrices", None))
        self._common_crew_id: int = _parse.pss_int(live_ops_info.pop("CommonCrewId", None))
        self._daily_item_rewards: str = _parse.pss_str(live_ops_info.pop("DailyItemRewards", None))
        self._daily_reward_argument: int = _parse.pss_int(live_ops_info.pop("DailyRewardArgument", None))
        self._daily_reward_type: str = _parse.pss_str(live_ops_info.pop("DailyRewardType", None))
        self._hero_crew_id: int = _parse.pss_int(live_ops_info.pop("HeroCrewId", None))
        self._limited_catalog_argument: int = _parse.pss_int(live_ops_info.pop("LimitedCatalogArgument", None))
        self._limited_catalog_currency_amount: int = _parse.pss_int(live_ops_info.pop("LimitedCatalogCurrencyAmount", None))
        self._limited_catalog_currency_type: str = _parse.pss_str(live_ops_info.pop("LimitedCatalogCurrencyType", None))
        self._limited_catalog_expiry_date: _datetime = _parse.pss_datetime(live_ops_info.pop("LimitedCatalogExpiryDate", None))
        self._limited_catalog_max_total: int = _parse.pss_int(live_ops_info.pop("LimitedCatalogMaxTotal", None))
        self._limited_catalog_quantity: int = _parse.pss_int(live_ops_info.pop("LimitedCatalogQuantity", None))
        self._limited_catalog_restock_quantity: int = _parse.pss_int(live_ops_info.pop("LimitedCatalogRestockQuantity", None))
        self._limited_catalog_type: str = _parse.pss_str(live_ops_info.pop("LimitedCatalogType", None))
        self._live_ops_id: int = _parse.pss_int(live_ops_info.pop("LiveOpsId", None))
        self._news: str = _parse.pss_str(live_ops_info.pop("News", None))
        self._news_sprite_id: int = _parse.pss_int(live_ops_info.pop("NewsSpriteId", None))
        self._news_update_date: _datetime = _parse.pss_datetime(live_ops_info.pop("NewsUpdateDate", None))
        self._sale_argument: int = _parse.pss_int(live_ops_info.pop("SaleArgument", None))
        self._sale_end_date: _datetime = _parse.pss_datetime(live_ops_info.pop("SaleEndDate", None))
        self._sale_item_mask: int = _parse.pss_int(live_ops_info.pop("SaleItemMask", None))
        self._sale_once_only: bool = _parse.pss_bool(live_ops_info.pop("SaleOnceOnly", None))
        self._sale_quantity: int = _parse.pss_int(live_ops_info.pop("SaleQuantity", None))
        self._sale_reward_string: str = _parse.pss_str(live_ops_info.pop("SaleRewardString", None))
        self._sale_start_date: _datetime = _parse.pss_datetime(live_ops_info.pop("SaleStartDate", None))
        self._sale_title: str = _parse.pss_str(live_ops_info.pop("SaleTitle", None))
        self._sale_type: str = _parse.pss_str(live_ops_info.pop("SaleType", None))
        self._support_task_ran_date: _datetime = _parse.pss_datetime(live_ops_info.pop("SupportTaskRanDate", None))
        self._tournament_news: str = _parse.pss_str(live_ops_info.pop("TournamentNews", None))
        super().__init__(live_ops_info)

    @property
    def cargo_items(self) -> str:
        return self._cargo_items

    @property
    def cargo_prices(self) -> str:
        return self._cargo_prices

    @property
    def common_crew_id(self) -> int:
        return self._common_crew_id

    @property
    def daily_item_rewards(self) -> str:
        return self._daily_item_rewards

    @property
    def daily_reward_argument(self) -> int:
        return self._daily_reward_argument

    @property
    def daily_reward_type(self) -> str:
        return self._daily_reward_type

    @property
    def hero_crew_id(self) -> int:
        return self._hero_crew_id

    @property
    def limited_catalog_argument(self) -> int:
        return self._limited_catalog_argument

    @property
    def limited_catalog_currency_amount(self) -> int:
        return self._limited_catalog_currency_amount

    @property
    def limited_catalog_currency_type(self) -> str:
        return self._limited_catalog_currency_type

    @property
    def limited_catalog_expiry_date(self) -> _datetime:
        return self._limited_catalog_expiry_date

    @property
    def limited_catalog_max_total(self) -> int:
        return self._limited_catalog_max_total

    @property
    def limited_catalog_quantity(self) -> int:
        return self._limited_catalog_quantity

    @property
    def limited_catalog_restock_quantity(self) -> int:
        return self._limited_catalog_restock_quantity

    @property
    def limited_catalog_type(self) -> str:
        return self._limited_catalog_type

    @property
    def live_ops_id(self) -> int:
        return self._live_ops_id

    @property
    def news(self) -> str:
        return self._news

    @property
    def news_sprite_id(self) -> int:
        return self._news_sprite_id

    @property
    def news_update_date(self) -> _datetime:
        return self._news_update_date

    @property
    def sale_argument(self) -> int:
        return self._sale_argument

    @property
    def sale_end_date(self) -> _datetime:
        return self._sale_end_date

    @property
    def sale_item_mask(self) -> int:
        return self._sale_item_mask

    @property
    def sale_once_only(self) -> bool:
        return self._sale_once_only

    @property
    def sale_quantity(self) -> int:
        return self._sale_quantity

    @property
    def sale_reward_string(self) -> str:
        return self._sale_reward_string

    @property
    def sale_start_date(self) -> _datetime:
        return self._sale_start_date

    @property
    def sale_title(self) -> str:
        return self._sale_title

    @property
    def sale_type(self) -> str:
        return self._sale_type

    @property
    def support_task_ran_date(self) -> _datetime:
        return self._support_task_ran_date

    @property
    def tournament_news(self) -> str:
        return self._tournament_news

    def _key(self):
        return (
            self.cargo_items,
            self.cargo_prices,
            self.common_crew_id,
            self.daily_item_rewards,
            self.daily_reward_argument,
            self.daily_reward_type,
            self.hero_crew_id,
            self.limited_catalog_argument,
            self.limited_catalog_currency_amount,
            self.limited_catalog_currency_type,
            self.limited_catalog_expiry_date,
            self.limited_catalog_max_total,
            self.limited_catalog_quantity,
            self.limited_catalog_restock_quantity,
            self.limited_catalog_type,
            self.live_ops_id,
            self.news,
            self.news_sprite_id,
            self.news_update_date,
            self.sale_argument,
            self.sale_end_date,
            self.sale_item_mask,
            self.sale_once_only,
            self.sale_quantity,
            self.sale_reward_string,
            self.sale_start_date,
            self.sale_title,
            self.sale_type,
            self.support_task_ran_date,
            self.tournament_news,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "CargoItems": self.cargo_items,
                "CargoPrices": self.cargo_prices,
                "CommonCrewId": self.common_crew_id,
                "DailyItemRewards": self.daily_item_rewards,
                "DailyRewardArgument": self.daily_reward_argument,
                "DailyRewardType": self.daily_reward_type,
                "HeroCrewId": self.hero_crew_id,
                "LimitedCatalogArgument": self.limited_catalog_argument,
                "LimitedCatalogCurrencyAmount": self.limited_catalog_currency_amount,
                "LimitedCatalogCurrencyType": self.limited_catalog_currency_type,
                "LimitedCatalogExpiryDate": self.limited_catalog_expiry_date,
                "LimitedCatalogMaxTotal": self.limited_catalog_max_total,
                "LimitedCatalogQuantity": self.limited_catalog_quantity,
                "LimitedCatalogRestockQuantity": self.limited_catalog_restock_quantity,
                "LimitedCatalogType": self.limited_catalog_type,
                "LiveOpsId": self.live_ops_id,
                "News": self.news,
                "NewsSpriteId": self.news_sprite_id,
                "NewsUpdateDate": self.news_update_date,
                "SaleArgument": self.sale_argument,
                "SaleEndDate": self.sale_end_date,
                "SaleItemMask": self.sale_item_mask,
                "SaleOnceOnly": self.sale_once_only,
                "SaleQuantity": self.sale_quantity,
                "SaleRewardString": self.sale_reward_string,
                "SaleStartDate": self.sale_start_date,
                "SaleTitle": self.sale_title,
                "SaleType": self.sale_type,
                "SupportTaskRanDate": self.support_task_ran_date,
                "TournamentNews": self.tournament_news,
            }
            self._dict.update(super().__dict__())

        return self._dict
