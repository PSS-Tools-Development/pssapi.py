####################################################
##   This file has been generated automatically   ##
####################################################

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class FileRaw():
    XML_NODE_NAME: str = 'File'

    def __init__(self, file_info: _EntityInfo) -> None:
        self.__id: int = _parse.pss_int(file_info.get('Id'))
        self.__filename: str = _parse.pss_str(file_info.get('Filename'))
        self.__date_updated: datetime = _parse.pss_datetime(file_info.get('DateUpdated'))
        self.__file_download_category: str = _parse.pss_str(file_info.get('FileDownloadCategory'))
        self.__size: int = _parse.pss_int(file_info.get('Size'))
        self.__is_language_specific: bool = _parse.pss_bool(file_info.get('IsLanguageSpecific'))
        self.__aws_filename: str = _parse.pss_str(file_info.get('AwsFilename'))

    @property
    def id(self) -> int:
        return self.__id

    @property
    def filename(self) -> str:
        return self.__filename

    @property
    def date_updated(self) -> datetime:
        return self.__date_updated

    @property
    def file_download_category(self) -> str:
        return self.__file_download_category

    @property
    def size(self) -> int:
        return self.__size

    @property
    def is_language_specific(self) -> bool:
        return self.__is_language_specific

    @property
    def aws_filename(self) -> str:
        return self.__aws_filename
