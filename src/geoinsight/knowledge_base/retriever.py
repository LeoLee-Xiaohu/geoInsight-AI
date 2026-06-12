"""Hybrid retrieval: semantic top-k + structured filter/re-rank (system_design 3.3)."""

from geoinsight.knowledge_base.catalog import CatalogStore
from geoinsight.knowledge_base.models import RetrievalResult


class HybridRetriever:
    """Combines vector search with catalog filters; used by the Discovery agent."""

    def __init__(self, vector_store, catalog: CatalogStore) -> None: ...

    def retrieve(
        self,
        query: str,
        bbox: list[float] | None = None,
        time_range: tuple[str, str] | None = None,
        parameter: str | None = None,
        k: int = 10,
    ) -> list[RetrievalResult]:
        """Semantic search -> filter by bbox/temporal/vocab -> rank; never fabricates entries."""
        ...
