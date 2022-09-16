import aiohttp as _aiohttp
from typing import List as _List
from typing import Type as _Type
from xml.etree import ElementTree as _ElementTree

from pssapi.entities import EntityBase as _EntityBase



async def get_entities_from_path(entity_type: _Type[_EntityBase], xml_parent_tag_name: str, production_server: str, path: str, **params) -> _List[_EntityBase]:
    raw_xml = await __get_data_from_path(production_server, path, **params)
    root = _ElementTree.fromstring(raw_xml)
    parent_node = root.find(f'.//{xml_parent_tag_name}')
    result = []
    for child in parent_node:
        entity = entity_type(__get_raw_entity_xml(child))
        result.append(entity)
    return result


async def __get_data_from_path(production_server: str, path: str, **params) -> str:
    if path:
        path = path.strip('/')
    url = f'https://{production_server}/{path}'
    return await __get_data_from_url(url, **params)


async def __get_data_from_url(url: str, **params) -> str:
    async with _aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.text(encoding='utf-8')
    return data


def __get_raw_entity_xml(node: _ElementTree.Element) -> None:
    result = node.attrib
    for child in node:
        result[child.tag] = __get_raw_entity_xml(child)
    return result