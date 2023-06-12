import json as _json


class EntityMetadata(object):
    def __init__(self, metadata: str):
        self._metadata_dict: dict = _json.loads((metadata.strip() if metadata else "") or "{}")
