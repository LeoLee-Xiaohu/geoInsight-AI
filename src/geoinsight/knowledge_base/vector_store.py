"""Vector store wrapper (Chroma for MVP; swap to OpenSearch/pgvector in prod)."""

from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore

from geoinsight.config import Settings


def get_vector_store(settings: Settings) -> VectorStore:
    """Open (or create) the persistent Chroma collection with Bedrock embeddings."""
    ...


def upsert_documents(store: VectorStore, documents: list[Document]) -> None:
    """Idempotent upsert of dataset documents keyed by uuid."""
    ...


def semantic_search(store: VectorStore, query: str, k: int = 10) -> list[Document]:
    """Top-k semantic search returning docs with metadata payloads."""
    ...
