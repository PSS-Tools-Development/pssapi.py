from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class PromotionType(_StrEnum):
    NONE = "None"
    CODE = "Code"
    DAILY_DEAL_OFFER = "DailyDealOffer"
    NON_PREMIUM_DAILY_DEAL_OFFER = "NonPremiumDailyDealOffer"
    OFFER = "Offer"
    VIP = "VIP"
    VALUE_OFFER = "ValueOffer"
    WEB_PROMOTION = "WebPromotion"
