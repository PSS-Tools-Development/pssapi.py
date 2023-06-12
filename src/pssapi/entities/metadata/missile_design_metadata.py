from ...utils import parse as _parse
from .entity_metadata_base import EntityMetadata as _EntityMetadata
from .metadata_color import Color as _Color


class MissileDesignMetadata(_EntityMetadata):
    def __init__(self, metadata: str):
        super().__init__(metadata)
        self._extend_laser_beam_distance: bool = _parse.pss_bool(self._metadata_dict.get("ExtendLaserBeamDistance"))
        self._flight_tint_color: _Color = _parse.pss_color(self._metadata_dict.get("FlightTintColor"))
        self._hit_tint_color: _Color = _parse.pss_color(self._metadata_dict.get("HitTintColor"))
        self._launch_tint_color: _Color = _parse.pss_color(self._metadata_dict.get("LaunchTintColor"))

    @property
    def extend_laser_beam_distance(self) -> str:
        return self._extend_laser_beam_distance

    @property
    def flight_tint_color(self) -> str:
        return self._flight_tint_color

    @property
    def hit_tint_color(self) -> str:
        return self._hit_tint_color

    @property
    def launch_tint_color(self) -> str:
        return self._launch_tint_color
