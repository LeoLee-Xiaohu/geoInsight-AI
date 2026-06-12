"""Supervisor agent: intent classification, entity extraction, routing, answer synthesis."""

from geoinsight.agents.state import AgentState


def classify_and_extract(state: AgentState) -> AgentState:
    """LLM structured-output call -> intent + raw entities (variable, place phrase, time phrase)."""
    ...


def resolve_entities(state: AgentState) -> AgentState:
    """Deterministic resolution: gazetteer place->bbox (ask if ambiguous, B5);
    time phrase -> dates via time_utils; variable -> parameter vocab term."""
    ...


def route(state: AgentState) -> str:
    """Conditional edge: 'discovery' | 'zarr' | 'parquet' | 'clarify' | 'decline'."""
    ...


def synthesize_answer(state: AgentState) -> AgentState:
    """Compose final grounded response (dataset used, slice applied, aggregation stated -- UX 6)."""
    ...
