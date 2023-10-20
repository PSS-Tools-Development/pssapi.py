import json as _json


class EntityMetadata(object):
    def __init__(self, metadata: str):
        try:
            json_loads = _json.loads((metadata.strip() if metadata else "") or "{}")
        except _json.JSONDecodeError:
            json_loads = {}

        self._metadata_dict: dict = json_loads
