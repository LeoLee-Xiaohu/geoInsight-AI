"""Parquet process agent node: invokes query_parquet tool with resolved entities."""

from geoinsight.agents.state import AgentState


def process_parquet(state: AgentState) -> AgentState:
    """Predicate-pushdown query of selected Parquet dataset; writes data_ref."""
    ...
