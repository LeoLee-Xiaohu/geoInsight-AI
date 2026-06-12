"""Discovery agent: RAG over the IMOS KB (Epic A / Milestone 1)."""

from geoinsight.agents.state import AgentState


def discover_datasets(state: AgentState) -> AgentState:
    """HybridRetriever query -> ranked candidates into state; label non-queryable datasets (A3)."""
    ...
