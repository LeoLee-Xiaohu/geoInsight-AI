"""Plot generation tools (matplotlib). Plot type chosen from data shape (system_design 4.2)."""

from langchain_core.tools import tool


@tool
def plot_timeseries(data_ref: str, variable: str, title: str) -> str:
    """Region-mean x time -> line chart PNG; returns artifact path."""
    ...


@tool
def plot_map(data_ref: str, variable: str, timestamp: str, title: str) -> str:
    """lat x lon slice -> pcolormesh map with coastline + colorbar units (B2); returns artifact path."""
    ...


def compute_summary_stats(data_ref: str, variable: str) -> dict:
    """Mean/min/max/trend stats feeding the caption prompt ('avg temp rose 1.2 degC')."""
    ...


def select_plot_type(data_ref: str) -> str:
    """Inspect data dimensionality -> 'timeseries' | 'map'."""
    ...
