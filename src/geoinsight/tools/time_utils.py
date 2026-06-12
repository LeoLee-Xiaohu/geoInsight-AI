"""Deterministic temporal resolution -- relative phrases resolved in code, never by the LLM (PRD 5.2)."""

from datetime import date, datetime


def resolve_relative_time(phrase: str, reference: date | None = None) -> tuple[datetime, datetime]:
    """'past 7 days' / 'last month' -> concrete (start, end) datetimes."""
    ...


def clamp_to_dataset_coverage(
    requested: tuple[datetime, datetime],
    coverage: tuple[datetime, datetime],
) -> tuple[datetime, datetime] | None:
    """Intersect requested range with dataset coverage; None -> conversational error (UX 6)."""
    ...
