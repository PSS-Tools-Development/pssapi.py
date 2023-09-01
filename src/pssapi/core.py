import json as _json
from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict
from typing import Iterable as _Iterable
from typing import Tuple as _Tuple
from typing import Type as _Type
from xml.etree import ElementTree as _ElementTree

import aiohttp as _aiohttp

import pssapi.constants as _constants
import pssapi.entities as _entities
import pssapi.enums as _enums
import pssapi.utils as _utils

__LATEST_SETTINGS_BASE_PARAMS: _Dict[str, str] = {
    "deviceType": str(_enums.DeviceType.ANDROID),
    "languageKey": str(_enums.LanguageKey.ENGLISH),
}


def create_request_content(structure: str, params: _Dict[str, _Any], content_type: str) -> str:
    if content_type == "json":
        return create_json_request_content(structure, params)
    elif content_type == "xml":
        pass


async def get_entities_from_path(
    entity_tags: _Iterable[_Tuple[_Type["_entities.EntityBase"], str, bool]], xml_parent_tag_name: str, production_server: str, path: str, method: str, request_content: str = None, **params
):
    raw_xml = await __get_data_from_path(production_server, path, method, content=request_content, **params)

    root = _ElementTree.fromstring(raw_xml)
    if not root or root.tag.startswith("{http://www.w3.org/1999/xhtml}html"):
        raise _utils.exceptions.PssApiError(f"A server error occured: {raw_xml}")
    if "errorMessage" in root.attrib:
        raise _utils.exceptions.PssApiError(root.attrib["errorMessage"])

    if xml_parent_tag_name and root.tag != xml_parent_tag_name:
        parent_node = root.find(f".//{xml_parent_tag_name}")
    else:
        parent_node = root

    result = []

    for entity_type, parent_tag_name, is_list in entity_tags:
        entity_parent_node = parent_node if xml_parent_tag_name == parent_tag_name else parent_node.find(f".//{parent_tag_name}")
        if entity_parent_node is None:
            continue

        if is_list:
            entities = [entity_type(__get_raw_entity_xml(entity)) for entity in entity_parent_node]
            result.append(entities)
        else:
            entity = entity_type(__get_raw_entity_xml(entity_parent_node))
            result.append(entity)
    if len(result) > 1:
        return tuple(result)
    elif len(result) == 1:
        return result[0]


async def get_production_server(device_type: str, language_key: str) -> str:
    raw_xml = await __get_data_from_path("api.pixelstarships.com", "SettingService/GetLatestVersion3", "GET", deviceType=device_type, languageKey=language_key)
    tree = _ElementTree.fromstring(raw_xml)
    setting_node = tree.find(".//Setting")
    result = setting_node.attrib.get("ProductionServer")
    if not result:
        raise Exception("Could not determine the production server! Use api.pixelstarships.com!")
    return result


def create_json_request_content(structure: str, params: _Dict[str, _Any]) -> str:
    d = _json.loads(structure)
    __update_nested_dict_values(d, params)
    return _json.dumps(d)


async def __get_data_from_path(production_server: str, path: str, method: str, content: str = None, **params) -> str:
    if path:
        path = path.strip("/")
    url = f"https://{production_server}/{path}"
    return await __get_data_from_url(url, method, content, **params)


async def __get_data_from_url(url: str, method: str, content: str = None, **params) -> str:
    # filter parameters with a None value and format datetime
    filtered_params = {}
    for key, value in params.items():
        if value is None:
            continue

        if isinstance(value, _datetime):
            filtered_params[key] = value.strftime(_constants.DATETIME_FORMAT_ISO)
        else:
            filtered_params[key] = value

    async with _aiohttp.ClientSession() as session:
        if method == "GET":
            async with session.get(url, params=filtered_params) as response:
                data = await response.text(encoding="utf-8")
        elif method == "POST":
            data = content.encode("utf-8") if content else None
            async with session.post(url, data=data, params=filtered_params) as response:
                data = await response.text(encoding="utf-8")
    return data


def __get_raw_entity_xml(node: _ElementTree.Element) -> dict[str, str]:
    result = node.attrib
    for child in node:
        result.setdefault(child.tag, []).append(__get_raw_entity_xml(child))
    return result


def __get_raw_entities_xml(node: _ElementTree.Element) -> dict[str, str]:
    result = []
    for child in node:
        result.append(__get_raw_entity_xml(child))
    return result


def __update_nested_dict_values(d: dict, params: _Dict[str, _Any]) -> None:
    for key, value in d.items():
        value_is_dict = isinstance(value, dict)
        param_value = params.get(key)
        if param_value:
            if value == "datetime" and isinstance(param_value, _datetime):
                d[key] = param_value.strftime(_constants.DATETIME_FORMAT_ISO)
            else:
                d[key] = param_value
        elif value_is_dict:
            __update_nested_dict_values(value, params)
