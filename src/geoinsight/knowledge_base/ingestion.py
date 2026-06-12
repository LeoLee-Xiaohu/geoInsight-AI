"""Offline KB ingestion: imos_results.json + aodn_cloud_optimised configs -> vector + catalog stores.

Run via scripts/build_kb.py. Idempotent (C2).
"""

from geoinsight.config import Settings
from geoinsight.knowledge_base.models import DatasetRecord


def load_raw_metadata(path: str) -> list[dict]:
    """Load AODN elasticsearch export (data/raw/imos_results.json)."""
    ...


def load_cloud_optimised_configs(config_dir: str) -> dict[str, dict]:
    """Load aodn_cloud_optimised dataset JSON configs, keyed for matching."""
    ...


def join_metadata_with_configs(
    metadata: list[dict], configs: dict[str, dict]
) -> list[DatasetRecord]:
    """Join catalog records to cloud-optimised configs (UUID/title match); set `queryable`."""
    ...


def build_embedding_document(record: DatasetRecord) -> str:
    """One embedding doc per dataset: title + ai:description + parameter/platform vocab terms."""
    ...


def run_ingestion(settings: Settings) -> None:
    """Full pipeline: load -> join -> embed -> write vector store + catalog DB."""
    ...
