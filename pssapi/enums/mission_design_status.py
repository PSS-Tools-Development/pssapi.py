from enum import StrEnum as _StrEnum

"""
This file has been be generated from decompilation and might require manual
fixing, if Savy uses enum values that are python keywords.
"""


class MissionDesignStatus(_StrEnum):
    DRAFT = 'Draft'
    REVIEW = 'Review'
    PUBLISHED = 'Published'
    DEPENDENCY_REVIEW = 'DependencyReview'
    ARCHIVE = 'Archive'
    DELETE_REVIEW = 'DeleteReview'
