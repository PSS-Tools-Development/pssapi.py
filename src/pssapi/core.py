import base64 as base64
import json as json
import zlib as zlib
from datetime import datetime
from typing import Any, Dict, Iterable, Tuple, Type
from xml.etree import ElementTree

import aiohttp as _aiohttp

from pssapi import constants, entities, enums, utils


__LATEST_SETTINGS_BASE_PARAMS: Dict[str, str] = {
    "deviceType": str(enums.DeviceType.ANDROID),
    "languageKey": str(enums.LanguageKey.ENGLISH),
}


def create_request_content(structure: str, params: Dict[str, Any], content_type: str) -> str:
    if content_type == "json":
        return create_json_request_content(structure, params)
    elif content_type == "xml":
        pass


async def get_entities_from_path(
    entity_tags: Iterable[Tuple[Type["entities.EntityBase"], str, bool]],
    xml_parent_tag_name: str,
    production_server: str,
    path: str,
    method: str,
    request_content: str = None,
    response_gzipped: bool = False,
    **params,
):
    raw_xml = await __get_data_from_path(production_server, path, method, content=request_content, response_gzipped=response_gzipped, **params)

    root = ElementTree.fromstring(raw_xml)
    if root is None or root.tag.startswith("{http://www.w3.org/1999/xhtml}html"):
        raise utils.exceptions.PssApiError(f"A server error occured: {raw_xml}")
    if "errorMessage" in root.attrib:
        raise utils.exceptions.PssApiError(root.attrib["errorMessage"])

    if xml_parent_tag_name and root.tag != xml_parent_tag_name:
        parent_node = root.find(f".//{xml_parent_tag_name}")
    else:
        parent_node = root

    if parent_node is None:
        raise utils.exceptions.PssApiError(f"The root node {xml_parent_tag_name} could not be found.")

    result = []

    for entity_type, parent_tag_name, is_list in entity_tags:
        entity_parent_node = parent_node if xml_parent_tag_name == parent_tag_name else parent_node.find(f".//{parent_tag_name}")
        if entity_parent_node is None:
            continue

        if is_list:
            entities = []
            for entity_node in entity_parent_node:
                str(entity_node)
                entity = entity_type.from_xml_tree(entity_node)
                entity.node = entity_node
                entities.append(entity)
            result.append(entities)
        else:
            entity_node = parent_node.find(f".//{parent_tag_name}")
            entity = entity_type.from_xml_tree(entity_node)
            entity.node = entity_node
            result.append(entity)

    if len(result) > 1:
        return tuple(result)
    elif len(result) == 1:
        return result[0]


async def get_production_server(device_type: str, language_key: str) -> str:
    raw_xml = await __get_data_from_path("api.pixelstarships.com", "SettingService/GetLatestVersion3", "GET", deviceType=device_type, languageKey=language_key)
    tree = ElementTree.fromstring(raw_xml)
    setting_node = tree.find(".//Setting")
    result = setting_node.attrib.get("ProductionServer")
    if not result:
        raise Exception("Could not determine the production server! Use api.pixelstarships.com!")
    return result


def create_json_request_content(structure: str, params: Dict[str, Any]) -> str:
    d = json.loads(structure)
    __update_nested_dict_values(d, params)
    return json.dumps(d)


async def __get_data_from_path(production_server: str, path: str, method: str, content: str = None, response_gzipped: bool = False, **params) -> str:
    if path:
        path = path.strip("/")
    url = f"https://{production_server}/{path}"
    return await __get_data_from_url(url, method, content=content, response_gzipped=response_gzipped, **params)


async def __get_data_from_url(url: str, method: str, content: str = None, response_gzipped: bool = False, **params) -> str:
    # filter parameters with a None value and format datetime
    filtered_params = {}
    for key, value in params.items():
        if value is None:
            continue

        if isinstance(value, datetime):
            filtered_params[key] = value.strftime(constants.DATETIME_FORMAT_ISO)
        else:
            filtered_params[key] = value

    async with _aiohttp.ClientSession() as session:
        if method == "GET":
            async with session.get(url, params=filtered_params) as response:
                response_data = await response.read()
        elif method == "POST":
            request_data = content.encode("utf-8") if content else None
            async with session.post(url, data=request_data, params=filtered_params) as response:
                response_data = await response.read()

    if response_gzipped:
        try:
            base64_decoded_data = base64.b64decode(response_data)
            response_data = zlib.decompress(base64_decoded_data, zlib.MAX_WBITS | 32)
        except:
            pass  # If the data can't be base64-decoded or unzipped, then the endpoint returned an error message in plain xml instead.

    decoded_data = response_data.decode("utf-8")
    return decoded_data


def __get_raw_entity_xml(node: ElementTree.Element) -> dict[str, str]:
    result = node.attrib
    for child in node:
        result.setdefault(child.tag, []).append(__get_raw_entity_xml(child))
    return result


def __get_raw_entities_xml(node: ElementTree.Element) -> dict[str, str]:
    result = []
    for child in node:
        result.append(__get_raw_entity_xml(child))
    return result


def __update_nested_dict_values(d: dict, params: Dict[str, Any]) -> None:
    for key, value in d.items():
        value_is_dict = isinstance(value, dict)
        param_value = params.get(key)
        if param_value:
            if value == "datetime" and isinstance(param_value, datetime):
                d[key] = param_value.strftime(constants.DATETIME_FORMAT_ISO)
            else:
                d[key] = param_value
        elif value_is_dict:
            __update_nested_dict_values(value, params)
