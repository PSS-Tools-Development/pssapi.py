"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import List as _List

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class LiveOpsRaw:
    XML_NODE_NAME: str = 'LiveOps'

    def __init__(self, live_ops_info: _EntityInfo) -> None:
        self.cargo_items: str = _parse.pss_str(live_ops_info.get('CargoItems'))
        self.cargo_prices: str = _parse.pss_str(live_ops_info.get('CargoPrices'))
        self.common_crew_id: int = _parse.pss_int(live_ops_info.get('CommonCrewId'))
        self.daily_item_rewards: str = _parse.pss_str(live_ops_info.get('DailyItemRewards'))
        self.daily_reward_argument: int = _parse.pss_int(live_ops_info.get('DailyRewardArgument'))
        self.daily_reward_type: str = _parse.pss_str(live_ops_info.get('DailyRewardType'))
        self.hero_crew_id: int = _parse.pss_int(live_ops_info.get('HeroCrewId'))
        self.limited_catalog_argument: int = _parse.pss_int(live_ops_info.get('LimitedCatalogArgument'))
        self.limited_catalog_currency_amount: int = _parse.pss_int(live_ops_info.get('LimitedCatalogCurrencyAmount'))
        self.limited_catalog_currency_type: str = _parse.pss_str(live_ops_info.get('LimitedCatalogCurrencyType'))
        self.limited_catalog_expiry_date: _datetime = _parse.pss_datetime(live_ops_info.get('LimitedCatalogExpiryDate'))
        self.limited_catalog_max_total: int = _parse.pss_int(live_ops_info.get('LimitedCatalogMaxTotal'))
        self.limited_catalog_quantity: int = _parse.pss_int(live_ops_info.get('LimitedCatalogQuantity'))
        self.limited_catalog_restock_quantity: int = _parse.pss_int(live_ops_info.get('LimitedCatalogRestockQuantity'))
        self.limited_catalog_type: str = _parse.pss_str(live_ops_info.get('LimitedCatalogType'))
        self.live_ops_id: int = _parse.pss_int(live_ops_info.get('LiveOpsId'))
        self.news: str = _parse.pss_str(live_ops_info.get('News'))
        self.news_sprite_id: int = _parse.pss_int(live_ops_info.get('NewsSpriteId'))
        self.news_update_date: _datetime = _parse.pss_datetime(live_ops_info.get('NewsUpdateDate'))
        self.sale_argument: int = _parse.pss_int(live_ops_info.get('SaleArgument'))
        self.sale_end_date: _datetime = _parse.pss_datetime(live_ops_info.get('SaleEndDate'))
        self.sale_item_mask: int = _parse.pss_int(live_ops_info.get('SaleItemMask'))
        self.sale_once_only: bool = _parse.pss_bool(live_ops_info.get('SaleOnceOnly'))
        self.sale_quantity: int = _parse.pss_int(live_ops_info.get('SaleQuantity'))
        self.sale_reward_string: str = _parse.pss_str(live_ops_info.get('SaleRewardString'))
        self.sale_start_date: _datetime = _parse.pss_datetime(live_ops_info.get('SaleStartDate'))
        self.sale_title: str = _parse.pss_str(live_ops_info.get('SaleTitle'))
        self.sale_type: str = _parse.pss_str(live_ops_info.get('SaleType'))
        self.support_task_ran_date: _datetime = _parse.pss_datetime(live_ops_info.get('SupportTaskRanDate'))
        self.tournament_news: str = _parse.pss_str(live_ops_info.get('TournamentNews'))
