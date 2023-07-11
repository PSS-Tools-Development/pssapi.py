from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class SaleStatus(_StrEnumBase):
    EXPIRED = "Expired"
    EXPIRY_PENDING = "ExpiryPending"
    LISTED = "Listed"
    PURCHASE_PENDING = "PurchasePending"
    SOLD = "Sold"
