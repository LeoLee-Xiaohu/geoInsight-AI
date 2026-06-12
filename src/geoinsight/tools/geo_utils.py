"""Deterministic spatial utilities shared by all data agents (PRD 5.2).

Handles the real geospatial complexity: CRS normalisation, longitude
conventions, dateline-crossing bboxes, land masking. No LLM involvement.
"""

import xarray as xr


def normalise_longitude(ds: xr.Dataset, target: str = "-180-180") -> xr.Dataset:
    """Convert between 0-360 and -180-180 longitude conventions."""
    ...


def normalise_crs(ds: xr.Dataset, target_epsg: int = 4326) -> xr.Dataset:
    """Reproject/assign CRS so all slicing happens in EPSG:4326."""
    ...


def split_dateline_bbox(bbox: list[float]) -> list[list[float]]:
    """Split a bbox crossing the antimeridian into two valid bboxes."""
    ...


def bbox_intersects(a: list[float], b: list[float]) -> bool:
    """Spatial intersection test used for catalog filtering."""
    ...


def apply_land_mask(ds: xr.Dataset, variable: str) -> xr.Dataset:
    """Mask land cells for ocean variables before aggregation/plotting."""
    ...


def estimate_slice_bytes(ds: xr.Dataset, bbox: list[float], time_range: tuple[str, str]) -> int:
    """Estimate slice size from Zarr metadata BEFORE loading (B4 guardrail)."""
    ...
