"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime
from typing import Any as _Any
from typing import Dict as _Dict

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse
from .entity_base_raw import EntityBaseRaw


class FileRaw(EntityBaseRaw):
    XML_NODE_NAME: str = "File"

    def __init__(self, file_info: _EntityInfo) -> None:
        self._dict: _Dict[str, _Any] = {}
        self._aws_filename: str = _parse.pss_str(file_info.pop("AwsFilename", None))
        self._date_updated: _datetime = _parse.pss_datetime(file_info.pop("DateUpdated", None))
        self._file_download_category: str = _parse.pss_str(file_info.pop("FileDownloadCategory", None))
        self._filename: str = _parse.pss_str(file_info.pop("Filename", None))
        self._id_: int = _parse.pss_int(file_info.pop("Id", None))
        self._is_language_specific: bool = _parse.pss_bool(file_info.pop("IsLanguageSpecific", None))
        self._size: int = _parse.pss_int(file_info.pop("Size", None))
        super().__init__(file_info)

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
            self._dict.update(super().__dict__())

        return self._dict
