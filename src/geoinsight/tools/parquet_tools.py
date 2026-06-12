"""Parquet data access tools (pyarrow predicate pushdown on S3)."""

import pandas as pd
from langchain_core.tools import tool


@tool
def query_parquet(
    s3_uri: str,
    columns: list[str],
    bbox: list[float] | None = None,
    time_start: str | None = None,
    time_end: str | None = None,
    limit: int = 1_000_000,
) -> str:
    """Scan Parquet dataset with bbox/time predicates pushed down; return data_ref path."""
    ...


def to_geodataframe(df: pd.DataFrame):
    """Promote lat/lon columns to geometry for spatial ops (geopandas)."""
    ...
