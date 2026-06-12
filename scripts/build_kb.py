"""CLI: (re)build the IMOS Knowledge Base. Idempotent (PRD C2).

Usage: uv run python scripts/build_kb.py [--metadata PATH] [--configs DIR]
"""


def fetch_cloud_optimised_configs(dest_dir: str) -> None:
    """Download/refresh dataset configs from github.com/aodn/aodn_cloud_optimised."""
    ...


def main() -> None:
    """Parse args -> run_ingestion -> report counts (total / queryable / discoverable-only)."""
    ...


if __name__ == "__main__":
    main()
