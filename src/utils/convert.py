from xml.etree import ElementTree as _ElementTree
from typing import Dict as _Dict

from ..types import EntitiesData as _EntitiesData
from ..types import EntityInfo as _EntityInfo


###################
##     W I P     ##
###################


# ---------- XML conversions ----------

def raw_xml_to_dict(raw_xml: str, fix_attributes: bool = True) -> _EntityInfo:
    root = _ElementTree.fromstring(raw_xml)
    result = __convert_xml_to_dict(root, fix_attributes=fix_attributes)
    return result


def xmltree_to_dict2(raw_text: str) -> _EntityInfo:
    return __xmltree_to_dict(raw_text, 2)


def xmltree_to_dict3(raw_text: str) -> _EntityInfo:
    return __xmltree_to_dict(raw_text, 3)


def __convert_xml_to_dict(root: _ElementTree.Element, fix_attributes: bool = True) -> _EntityInfo:
    if root is None:
        return None

    attribute = {}
    if root.attrib:
        if fix_attributes:
            attribute = __fix_attribute(root.attrib)
        else:
            attribute = root.attrib
    result = {
        root.tag: attribute
    }

    # Retrieve all distinct names of sub tags
    tag_count_map = __get_child_tag_count(root)
    dedicated_child_tag_count = len(tag_count_map.keys())
    if dedicated_child_tag_count == 1:
        children = {}
        is_children_collection = False
    elif dedicated_child_tag_count > 1:
        if any(value > 1 for value in tag_count_map.values()):
            raise Exception('XmlParseError: Found entity collection next to non-collection entity.')
        else:
            children = []
            is_children_collection = True

    if is_children_collection:
        for child in root:
            child_dict = __convert_xml_to_dict(child, fix_attributes=fix_attributes)
            children.append(child_dict[child.tag])
    else:
        for child in root:
            children[child.tag] = __convert_xml_to_dict(child, fix_attributes=fix_attributes)

    if children:
        if is_children_collection:
            result[root.tag] = children
        else:
            result[root.tag].update(children)

    return result


def __fix_attribute(attribute: _Dict[str, str]) -> _Dict[str, str]:
    if not attribute:
        return None

    result = {}

    for key, value in attribute.items():
        if key.endswith('Xml') and value:
            raw_xml = value
            fixed_value = raw_xml_to_dict(raw_xml)
            result[key[:-3]] = fixed_value

        result[key] = value

    return result


def __get_child_tag_count(root: _ElementTree.Element) -> _Dict[str, int]:
    if root is None:
        return None

    child_tags = list(set([child_node.tag for child_node in root]))
    result = {}
    for child_tag in child_tags:
        result[child_tag] = sum(1 for child_node in root if child_node.tag == child_tag)

    return result


def __xmltree_to_dict(raw_text: str, depth: int) -> _EntitiesData:
    result = raw_xml_to_dict(raw_text)
    while depth > 0:
        found_new_root = False
        for value in result.values():
            if isinstance(value, dict):
                result = value
                depth -= 1
                found_new_root = True
                break
        if not found_new_root:
            return {}
    return result