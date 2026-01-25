from enum import StrEnum as _StrEnum


class EngagementApprovalState(_StrEnum):
    NONE = "None"
    APPROVED = "Approved"
    PENDING = "Pending"
