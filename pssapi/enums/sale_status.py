from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class SaleStatus(_StrEnum):
    LISTED = 'Listed'
    SOLD = 'Sold'
    EXPIRED = 'Expired'
    PURCHASE_PENDING = 'PurchasePending'
    EXPIRY_PENDING = 'ExpiryPending'
