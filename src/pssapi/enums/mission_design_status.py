from .str_enum_base import StrEnumBase as _StrEnumBase

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class MissionDesignStatus(_StrEnumBase):
    NONE = "None"
    ARCHIVE = "Archive"
    DELETE_REVIEW = "DeleteReview"
    DEPENDENCY_REVIEW = "DependencyReview"
    DRAFT = "Draft"
    PUBLISHED = "Published"
    REVIEW = "Review"
