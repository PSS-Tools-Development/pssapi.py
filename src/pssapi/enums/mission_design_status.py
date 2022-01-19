from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class MissionDesignStatus(_StrEnum):
    NONE = "None"
    ARCHIVE = "Archive"
    DELETE_REVIEW = "DeleteReview"
    DEPENDENCY_REVIEW = "DependencyReview"
    DRAFT = "Draft"
    PUBLISHED = "Published"
    REVIEW = "Review"
