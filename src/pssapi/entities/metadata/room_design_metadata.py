from ...utils import parse as _parse
from .entity_metadata_base import EntityMetadata as _EntityMetadata
from .metadata_color import Color as _Color


class RoomDesignMetadata(_EntityMetadata):
    def __init__(self, metadata: str):
        super().__init__(metadata)
        self._ChargingColor: _Color = _parse.pss_color(self._metadata_dict.get("ChargingColor"))
        self._ChargingParticleMainTexture: int = _parse.pss_int(self._metadata_dict.get("ChargingParticleMainTexture"))
        self._ChargingParticleTrailTexture: int = _parse.pss_int(self._metadata_dict.get("ChargingParticleTrailTexture"))
        self._ChargingRadius: int = _parse.pss_int(self._metadata_dict.get("ChargingRadius"))

    @property
    def ChargingColor(self) -> str:
        return self._ChargingColor

    @property
    def ChargingParticleMainTexture(self) -> str:
        return self._ChargingParticleMainTexture

    @property
    def ChargingParticleTrailTexture(self) -> str:
        return self._ChargingParticleTrailTexture

    @property
    def ChargingRadius(self) -> int:
        return self._ChargingRadius
