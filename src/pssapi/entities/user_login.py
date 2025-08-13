from .entity_base import EntityBase
from .raw import UserLoginRaw


class UserLogin(UserLoginRaw, EntityBase):
    pass


__all__ = [
    "UserLogin",
]
