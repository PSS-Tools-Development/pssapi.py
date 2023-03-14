"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import RoomDesignSprite as _RoomDesignSprite

# ---------- Constants ----------

LIST_ROOM_DESIGN_SPRITES_BASE_PATH: str = "RoomDesignSpriteService/ListRoomDesignSprites"


# ---------- Endpoints ----------


async def list_room_design_sprites(production_server: str, design_version: int, **params) -> _List[_RoomDesignSprite]:
    params = {"designVersion": design_version, **params}
    result = await _core.get_entities_from_path(((_RoomDesignSprite, "RoomDesignSprites", True),), "RoomDesignSprites", production_server, LIST_ROOM_DESIGN_SPRITES_BASE_PATH, "GET", **params)
    return result
