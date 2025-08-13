from .entity_base import EntityBase
from .raw import UserEmailPasswordAuthorizeRaw


class UserEmailPasswordAuthorize(UserEmailPasswordAuthorizeRaw, EntityBase):
    pass


__all__ = [
    "UserEmailPasswordAuthorize",
]
