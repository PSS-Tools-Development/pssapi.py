"""
    This file has been generated automatically
"""

from typing import List as _List

from ... import core as _core
from ...entities import File as _File
from ...entities import Sprite as _Sprite


class FileServiceRaw:

    SERVICE_NAME = 'FileService'
    LIST_FILES_4_BASE_PATH: str = 'FileService/ListFiles4'
    LIST_SPRITES_2_BASE_PATH: str = 'FileService/ListSprites2'

    @staticmethod
    async def _list_files_4(production_server: str, language_key: str, design_version: int, **params) -> _List[_File]:
        params = {
            'languageKey': language_key,
            'designVersion': design_version,
            **params
        }

        result = await _core.get_entities_from_path(_File, 'Files', production_server, FileServiceRaw.LIST_FILES_4_BASE_PATH, **params)
        return result

    @staticmethod
    async def _list_sprites_2(production_server: str, language_key: str, design_version: int, **params) -> _List[_Sprite]:
        params = {
            'languageKey': language_key,
            'designVersion': design_version,
            **params
        }

        result = await _core.get_entities_from_path(_Sprite, 'Sprites', production_server, FileServiceRaw.LIST_SPRITES_2_BASE_PATH, **params)
        return result
