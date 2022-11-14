"""
    This file has been generated automatically
"""

from datetime import datetime as _datetime

from ...types import EntityInfo as _EntityInfo
from ...utils import parse as _parse


class FileRaw:
    XML_NODE_NAME: str = 'File'

    def __init__(self, file_info: _EntityInfo) -> None:
        self.aws_filename: str = _parse.pss_str(file_info.get('AwsFilename'))
        self.date_updated: _datetime = _parse.pss_datetime(file_info.get('DateUpdated'))
        self.file_download_category: str = _parse.pss_str(file_info.get('FileDownloadCategory'))
        self.filename: str = _parse.pss_str(file_info.get('Filename'))
        self.id_: int = _parse.pss_int(file_info.get('Id'))
        self.is_language_specific: bool = _parse.pss_bool(file_info.get('IsLanguageSpecific'))
        self.size: int = _parse.pss_int(file_info.get('Size'))
