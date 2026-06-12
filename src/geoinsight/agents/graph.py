"""LangGraph assembly: nodes, conditional edges, checkpointer (system_design 4.2)."""

from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.graph import StateGraph

from geoinsight.agents.state import AgentState
from geoinsight.config import Settings


def build_graph(settings: Settings, checkpointer: BaseCheckpointSaver | None = None):
    """Wire the graph:

    guardrail_in -> supervisor(classify/extract -> resolve) --route--> discovery
                                                            \--------> zarr ----\
                                                            \--------> parquet --+-> visualization
    all paths -> synthesize_answer -> guardrail_out -> END

    Checkpointer (MemorySaver MVP -> Redis/DynamoDB prod) enables follow-up turns (B3).
    Returns compiled graph.
    """
    ...


def run_turn(graph, session_id: str, user_message: str) -> AgentState:
    """Execute one conversation turn against a session thread; returns final state."""
    ...
