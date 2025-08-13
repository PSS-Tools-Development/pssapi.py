"""
This file has been generated automatically.
Any changes to this file will be lost eventually.
"""

from typing import List

from ... import core
from ...entities import File, Sprite


# ---------- Constants ----------

LIST_FILES_4_BASE_PATH: str = "FileService/ListFiles4"
LIST_SPRITES_2_BASE_PATH: str = "FileService/ListSprites2"

# ---------- Endpoint structure ----------


# ---------- Endpoints ----------


async def list_files_4(production_server: str, design_version: int, language_key: str, **params) -> List[File]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(((File, "Files", True),), "Files", production_server, LIST_FILES_4_BASE_PATH, "GET", response_gzipped=False, **params)
    return result


async def list_sprites_2(production_server: str, design_version: int, language_key: str, **params) -> List[Sprite]:
    params = {"designVersion": design_version, "languageKey": language_key, **params}
    result = await core.get_entities_from_path(((Sprite, "Sprites", True),), "Sprites", production_server, LIST_SPRITES_2_BASE_PATH, "GET", response_gzipped=False, **params)
    return result
