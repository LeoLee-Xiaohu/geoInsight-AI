"""Structured catalog store (SQLite/DuckDB) for exact filters: bbox, temporal, parameter vocab."""

from geoinsight.knowledge_base.models import DatasetRecord


class CatalogStore:
    """Queryable structured-metadata store mirroring the vector store payloads."""

    def __init__(self, db_path: str) -> None: ...

    def upsert(self, records: list[DatasetRecord]) -> None:
        """Idempotent write of dataset records."""
        ...

    def get(self, uuid: str) -> DatasetRecord | None:
        """Fetch a single record by UUID."""
        ...

    def filter(
        self,
        bbox: list[float] | None = None,
        time_range: tuple[str, str] | None = None,
        parameter: str | None = None,
        queryable_only: bool = False,
    ) -> list[DatasetRecord]:
        """Exact-match filtering: bbox intersection, temporal overlap, vocab term match."""
        ...
