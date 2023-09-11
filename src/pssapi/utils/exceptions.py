from typing import Tuple as _Tuple
from xml.etree.ElementTree import ParseError as _XmlParseError


class PssApiError(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self) -> str:
        msg = [type(self).__name__, self.message]
        return "\n".join(msg)

    def __repr__(self) -> str:
        return self.__str__()


class ServerMaintenanceError(PssApiError):
    pass


class PssXmlError(PssApiError, _XmlParseError):
    def __init__(self, raw_xml: str, parse_error: _XmlParseError):
        super().__init__(parse_error.msg)
        self.raw_xml: str = raw_xml
        self.parse_error: _XmlParseError = parse_error

    @property
    def position(self) -> _Tuple[int, int]:
        return self.parse_error.position
