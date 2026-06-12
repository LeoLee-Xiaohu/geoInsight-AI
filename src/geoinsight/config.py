"""Central configuration (env-driven) for models, KB paths, S3, and limits."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment / .env.

    Covers Bedrock model IDs, AWS region, KB storage paths,
    S3 data buckets, and data-size guardrail thresholds.
    """

    aws_region: str = "ap-southeast-2"
    bedrock_supervisor_model_id: str = "anthropic.claude-sonnet-4-20250514-v1:0"
    bedrock_extraction_model_id: str = "amazon.nova-lite-v1:0"
    bedrock_embedding_model_id: str = "amazon.titan-embed-text-v2:0"

    kb_vector_store_path: str = "data/kb/chroma"
    kb_catalog_db_path: str = "data/kb/catalog.sqlite"
    raw_metadata_path: str = "data/raw/imos_results.json"
    cloud_optimised_config_dir: str = "data/raw/cloud_optimised_configs"

    artifacts_dir: str = "data/artifacts"
    max_slice_bytes: int = 100_000_000  # B4 size guardrail
    max_plot_points: int = 1_000_000
    default_place_buffer_deg: float = 0.5  # "near X" buffer


def get_settings() -> Settings:
    """Return cached singleton Settings instance."""
    ...
