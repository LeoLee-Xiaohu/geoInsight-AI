"""Zarr process agent node: invokes slice_zarr tool with resolved entities."""

from geoinsight.agents.state import AgentState


def process_zarr(state: AgentState) -> AgentState:
    """Size-check then slice/aggregate selected Zarr dataset; oversized -> refusal with
    suggested smaller scope (B4); writes data_ref."""
    ...
