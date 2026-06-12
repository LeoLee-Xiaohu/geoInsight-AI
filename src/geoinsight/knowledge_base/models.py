"""Pydantic models for KB records shared across ingestion/retrieval/agents."""

from pydantic import BaseModel


class DatasetRecord(BaseModel):
    """One IMOS dataset: catalog metadata + (optional) cloud-optimised access info.

    The metadata payload stored alongside each vector and in the catalog DB.
    """

    uuid: str
    title: str
    description: str
    bbox: list[float] | None  # [min_lon, min_lat, max_lon, max_lat]
    temporal_start: str | None
    temporal_end: str | None
    parameters: list[str]  # AODN parameter vocab terms
    platforms: list[str]
    s3_uri: str | None  # from cloud-optimised config
    data_format: str | None  # "zarr" | "parquet"
    variables: list[str]  # actual variable names in the store
    queryable: bool  # has cloud-optimised config


class RetrievalResult(BaseModel):
    """A ranked KB hit: record + semantic score + filter-match flags."""

    record: DatasetRecord
    score: float
    matched_bbox: bool
    matched_temporal: bool
    matched_parameter: bool
