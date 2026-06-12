"""Input/output guardrails: prompt-injection screening + topic scoping (PRD A4, Security 7)."""

from geoinsight.agents.state import AgentState


def guardrail_input(state: AgentState) -> AgentState:
    """Screen user message; out-of-scope/injection -> intent='out_of_scope' with polite decline."""
    ...


def guardrail_output(state: AgentState) -> AgentState:
    """Validate final answer: no fabricated dataset names/S3 paths, no unsafe content."""
    ...
