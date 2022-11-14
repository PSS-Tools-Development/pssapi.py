import json as _json
from typing import Any as _Any
from typing import Dict as _Dict
from typing import Iterable as _Iterable
from typing import List as _List
from typing import Type as _Type
from typing import Union as _Union
from xml.etree import ElementTree as _ElementTree

import aiohttp as _aiohttp

from pssapi.entities import EntityBase as _EntityBase


def create_request_content(structure: str, params: _Dict[str, _Any], content_type: str) -> str:
    if content_type == 'json':
        return __create_json_request_content(structure, params)
    elif content_type == 'xml':
        pass


def __create_json_request_content(structure: str, params: _Dict[str, _Any]) -> str:
    d = _json.loads(structure)
    __update_nested_dict_values(d, params)
    return _json.dumps(d)


def __update_nested_dict_values(d: dict, params: _Dict[str, _Any]) -> None:
    for key, value in d.items():
        if isinstance(value, dict):
            __update_nested_dict_values(value, params)
        else:
            d[key] = params[key]


async def get_entities_from_path(entity_types: _Union[_Type[_EntityBase], _Iterable[_Type[_EntityBase]]], xml_parent_tag_name: str, production_server: str, path: str, method: str, request_content: str = None, **params) -> _List[_EntityBase]:
    raw_xml = await __get_data_from_path(production_server, path, method, content=request_content, **params)
    root = _ElementTree.fromstring(raw_xml)
    parent_node = root.find(f'.//{xml_parent_tag_name}')
    result = []

    if isinstance(entity_types, _Iterable):
        for child in parent_node:
            for entity_type in entity_types:
                if entity_type.name == child.tag:
                    entity = entity_type(__get_raw_entity_xml(child))
                    result.append(entity)
    else:
        for child in parent_node:
            entity = entity_types[0](__get_raw_entity_xml(child))
            result.append(entity)
    return result


async def __get_data_from_path(production_server: str, path: str, method: str, content: str = None, **params) -> str:
    if path:
        path = path.strip('/')
    url = f'https://{production_server}/{path}'
    return await __get_data_from_url(url, method, content, **params)


async def __get_data_from_url(url: str, method: str, content: str = None, **params) -> str:
    # filter parameters with a None value
    params = {key: value for (key, value) in params.items() if value}

    async with _aiohttp.ClientSession() as session:
        if method == 'GET':
            async with session.get(url, params=params) as response:
                data = await response.text(encoding='utf-8')
        elif method == 'POST':
            async with session.get(url, data=content.encode('utf-8'), params=params) as response:
                data = await response.text(encoding='utf-8')
    return data


def __get_raw_entity_xml(node: _ElementTree.Element) -> dict[str, str]:
    result = node.attrib
    for child in node:
        result[child.tag] = __get_raw_entity_xml(child)
    return result
