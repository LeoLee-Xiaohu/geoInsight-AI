"""Visualization agent node: plot-type selection, rendering, captioning."""

from geoinsight.agents.state import AgentState


def visualize(state: AgentState) -> AgentState:
    """select_plot_type -> plot tool -> compute stats -> LLM caption; writes artifact."""
    ...
