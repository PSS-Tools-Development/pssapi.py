"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import RoomDesignSprite


# ---------- Constants ----------

LIST_ROOM_DESIGN_SPRITES_BASE_PATH: str = "RoomDesignSpriteService/ListRoomDesignSprites"
LIST_ROOM_DESIGN_SPRITES_2_BASE_PATH: str = "RoomDesignSpriteService/ListRoomDesignSprites2"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def list_room_design_sprites(production_server: str, design_version: int, **params) -> List[RoomDesignSprite]:
    params = {"designVersion": design_version, **params}
    result = await core.get_entities_from_path(
        ((RoomDesignSprite, "RoomDesignSprites", True),), "RoomDesignSprites", production_server, LIST_ROOM_DESIGN_SPRITES_BASE_PATH, "GET", response_gzipped=False, **params
    )
    return result


async def list_room_design_sprites_2(production_server: str, client_date_time: str, design_version: int, language_key: str, **params) -> List[RoomDesignSprite]:
    params = {"clientDateTime": client_date_time, "designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(
        ((RoomDesignSprite, "RoomDesignSprites", True),), "RoomDesignSprites", production_server, LIST_ROOM_DESIGN_SPRITES_2_BASE_PATH, "GET", response_gzipped=False, **params
    )
    return result
