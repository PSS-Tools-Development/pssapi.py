from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class SaleStatus(_StrEnum):
    EXPIRED = "Expired"
    EXPIRY_PENDING = "ExpiryPending"
    LISTED = "Listed"
    PURCHASE_PENDING = "PurchasePending"
    SOLD = "Sold"
