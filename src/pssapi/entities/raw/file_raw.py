"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class FileRaw(EntityBaseRaw, tag="File"):
    XML_NODE_NAME: str = "File"

    aws_filename: Optional[str] = attr(name="AwsFilename", default=None)
    date_updated: Optional[datetime] = attr(name="DateUpdated", default=None)
    file_download_category: Optional[str] = attr(name="FileDownloadCategory", default=None)
    filename: Optional[str] = attr(name="Filename", default=None)
    id_: Optional[int] = attr(name="Id", default=None)
    is_language_specific: Optional[bool] = attr(name="IsLanguageSpecific", default=None)
    size: Optional[int] = attr(name="Size", default=None)

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


__all__ = [
    "FileRaw",
]
