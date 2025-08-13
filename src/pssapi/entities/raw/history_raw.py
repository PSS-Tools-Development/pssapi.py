"""
This file has been generated automatically
"""

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic_xml import attr


if TYPE_CHECKING:
    pass
from .entity_base_raw import EntityBaseRaw


class HistoryRaw(EntityBaseRaw, tag="History"):
    XML_NODE_NAME: str = "History"

    argument: Optional[int] = attr(name="Argument", default=None)
    date: Optional[datetime] = attr(name="Date", default=None)
    history_id: Optional[int] = attr(name="HistoryId", default=None)
    history_type: Optional[str] = attr(name="HistoryType", default=None)
    value: Optional[int] = attr(name="Value", default=None)

    def _key(self):
        return (
            self.argument,
            self.date,
            self.history_id,
            self.history_type,
            self.value,
        )


__all__ = [
    "HistoryRaw",
]
