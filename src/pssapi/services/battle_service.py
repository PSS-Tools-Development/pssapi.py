import datetime as _datetime
import hashlib as _hashlib

import pssapi.services.service_base as _service_base

from .. import utils as _utils
from ..entities import Engagement as _Engagement
from .raw import BattleServiceRaw as _BattleServiceRaw


class _BattleServiceUtils:
    @staticmethod
    def create_get_engagement_checksum(client_datetime: _datetime.datetime, checksum_key: str) -> str:
        """
        Generate a checksum for the `GetEngagement` endpoints.

        :param client_datetime: Current UTC date and time.
        :param checksum_key: A secret key for creating the checksum. While easily found online, it won't be included in pssapi, complying with SavySoda.
        """
        if not checksum_key:
            raise _utils.exceptions.InvalidChecksumKey()

        timestamp = _utils.datetime.convert_to_pss_timestamp(client_datetime)
        result = _hashlib.md5(f"{timestamp}{checksum_key}savysoda".encode("utf-8")).hexdigest()
        return result


class BattleService(_service_base.ServiceBase):
    utils = _BattleServiceUtils()

    async def get_engagement(self, access_token: str, checksum: str, client_date_time: _datetime.datetime, engagement_id: int) -> _Engagement:
        production_server = await self.get_production_server()
        result = await _BattleServiceRaw.get_engagement(production_server, access_token, checksum, client_date_time, engagement_id)
        return result
