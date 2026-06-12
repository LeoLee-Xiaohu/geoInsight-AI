"""Shared LangGraph state schema (system_design 4.1)."""

from typing import Annotated, Any, Literal, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """State threaded through the graph; checkpointed per session for follow-ups (B3)."""

    messages: Annotated[list[BaseMessage], add_messages]
    intent: Literal["discovery", "visualize", "follow_up", "out_of_scope"] | None
    variable: str | None
    region: dict[str, Any] | None  # {name, bbox}
    time_range: dict[str, str] | None  # {start, end}
    candidate_datasets: list[dict]
    selected_dataset: dict | None
    data_ref: str | None
    artifact: dict | None  # {type, path, caption}
    error: str | None
