from .entity_metadata_base import EntityMetadata as _EntityMetadata


class SkinSetMetadata(_EntityMetadata):
    def __init__(self, metadata: str):
        super().__init__(metadata)
