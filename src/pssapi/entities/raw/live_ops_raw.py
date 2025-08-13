"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class LiveOpsRaw(EntityBaseRaw, tag="LiveOps"):
    XML_NODE_NAME: str = "LiveOps"

    cargo_items: Optional[str] = attr(name="CargoItems", default=None)
    cargo_prices: Optional[str] = attr(name="CargoPrices", default=None)
    common_crew_id: Optional[int] = attr(name="CommonCrewId", default=None)
    daily_item_rewards: Optional[str] = attr(name="DailyItemRewards", default=None)
    daily_reward_argument: Optional[int] = attr(name="DailyRewardArgument", default=None)
    daily_reward_type: Optional[str] = attr(name="DailyRewardType", default=None)
    hero_crew_id: Optional[int] = attr(name="HeroCrewId", default=None)
    limited_catalog_argument: Optional[int] = attr(name="LimitedCatalogArgument", default=None)
    limited_catalog_currency_amount: Optional[int] = attr(name="LimitedCatalogCurrencyAmount", default=None)
    limited_catalog_currency_type: Optional[str] = attr(name="LimitedCatalogCurrencyType", default=None)
    limited_catalog_expiry_date: Optional[datetime] = attr(name="LimitedCatalogExpiryDate", default=None)
    limited_catalog_max_total: Optional[int] = attr(name="LimitedCatalogMaxTotal", default=None)
    limited_catalog_quantity: Optional[int] = attr(name="LimitedCatalogQuantity", default=None)
    limited_catalog_restock_quantity: Optional[int] = attr(name="LimitedCatalogRestockQuantity", default=None)
    limited_catalog_type: Optional[str] = attr(name="LimitedCatalogType", default=None)
    live_ops_id: Optional[int] = attr(name="LiveOpsId", default=None)
    news: Optional[str] = attr(name="News", default=None)
    news_sprite_id: Optional[int] = attr(name="NewsSpriteId", default=None)
    news_update_date: Optional[datetime] = attr(name="NewsUpdateDate", default=None)
    sale_argument: Optional[int] = attr(name="SaleArgument", default=None)
    sale_end_date: Optional[datetime] = attr(name="SaleEndDate", default=None)
    sale_item_mask: Optional[int] = attr(name="SaleItemMask", default=None)
    sale_once_only: Optional[bool] = attr(name="SaleOnceOnly", default=None)
    sale_quantity: Optional[int] = attr(name="SaleQuantity", default=None)
    sale_reward_string: Optional[str] = attr(name="SaleRewardString", default=None)
    sale_start_date: Optional[datetime] = attr(name="SaleStartDate", default=None)
    sale_title: Optional[str] = attr(name="SaleTitle", default=None)
    sale_type: Optional[str] = attr(name="SaleType", default=None)
    support_task_ran_date: Optional[datetime] = attr(name="SupportTaskRanDate", default=None)
    tournament_news: Optional[str] = attr(name="TournamentNews", default=None)

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


__all__ = [
    "LiveOpsRaw",
]
