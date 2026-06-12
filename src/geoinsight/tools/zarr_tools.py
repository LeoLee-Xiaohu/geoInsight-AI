"""Zarr data access tools (xarray + s3fs). Exposed to agents as LangChain tools."""

import xarray as xr
from langchain_core.tools import tool


def open_zarr_dataset(s3_uri: str) -> xr.Dataset:
    """Lazy-open consolidated Zarr store on S3 (read-only)."""
    ...


@tool
def slice_zarr(
    s3_uri: str,
    variable: str,
    bbox: list[float],
    time_start: str,
    time_end: str,
    aggregation: str = "daily_mean",
) -> str:
    """Slice variable by bbox/time, apply geo_utils normalisation + size guardrail,
    aggregate, persist intermediate result, return data_ref path."""
    ...


def aggregate(ds: xr.Dataset, method: str) -> xr.Dataset:
    """Supported reductions: daily_mean, spatial_mean, monthly_mean, downsample."""
    ...
