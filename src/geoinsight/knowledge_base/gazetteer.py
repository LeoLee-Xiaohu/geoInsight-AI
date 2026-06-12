"""Place name -> geometry resolution (Storm Bay -> bbox/polygon). Source TBD: IMOS GeoServer vs GeoNames."""

from pydantic import BaseModel


class PlaceMatch(BaseModel):
    """A resolved place candidate."""

    name: str
    bbox: list[float]  # [min_lon, min_lat, max_lon, max_lat]
    confidence: float


class Gazetteer:
    """Lookup table for AU coastal/marine place names."""

    def __init__(self, source_path: str) -> None: ...

    def lookup(self, place_name: str) -> list[PlaceMatch]:
        """Return ranked candidates; multiple matches trigger a clarifying question (B5)."""
        ...

    def apply_buffer(self, match: PlaceMatch, buffer_deg: float) -> list[float]:
        """Expand bbox for 'near X' phrasing; assumption stated to user (PRD 5.2)."""
        ...
