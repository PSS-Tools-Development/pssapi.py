"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class FileRaw:
    XML_NODE_NAME: str = "File"

    def __init__(self, file_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._aws_filename: str = _parse.pss_str(file_info.get("AwsFilename"))
        self._date_updated: _datetime = _parse.pss_datetime(file_info.get("DateUpdated"))
        self._file_download_category: str = _parse.pss_str(file_info.get("FileDownloadCategory"))
        self._filename: str = _parse.pss_str(file_info.get("Filename"))
        self._id_: int = _parse.pss_int(file_info.get("Id"))
        self._is_language_specific: bool = _parse.pss_bool(file_info.get("IsLanguageSpecific"))
        self._size: int = _parse.pss_int(file_info.get("Size"))

    @property
    def aws_filename(self) -> str:
        return self._aws_filename

    @property
    def date_updated(self) -> _datetime:
        return self._date_updated

    @property
    def file_download_category(self) -> str:
        return self._file_download_category

    @property
    def filename(self) -> str:
        return self._filename

    @property
    def id_(self) -> int:
        return self._id_

    @property
    def is_language_specific(self) -> bool:
        return self._is_language_specific

    @property
    def size(self) -> int:
        return self._size

    def _key(self):
        return (
            self.aws_filename,
            self.date_updated,
            self.file_download_category,
            self.filename,
            self.id_,
            self.is_language_specific,
            self.size,
        )

    def __dict__(self):
        if not self._dict:
            self._dict = {
                "AwsFilename": self.aws_filename,
                "DateUpdated": self.date_updated,
                "FileDownloadCategory": self.file_download_category,
                "Filename": self.filename,
                "Id": self.id_,
                "IsLanguageSpecific": self.is_language_specific,
                "Size": self.size,
            }

        return self._dict
