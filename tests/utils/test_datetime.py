from datetime import datetime as _datetime

import pssapi.utils.datetime as _utils_datetime


def test_convert_to_pss_timestamp():
    assert _utils_datetime.convert_to_pss_timestamp(_datetime(2022, 5, 6, 12, 4, 2)) == "2022-05-06T12:04:02"
    assert _utils_datetime.convert_to_pss_timestamp(_datetime(1900, 1, 1, 0, 0, 0)) == "1900-01-01T00:00:00"
    assert _utils_datetime.convert_to_pss_timestamp(None) is None
