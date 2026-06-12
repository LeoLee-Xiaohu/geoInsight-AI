"""Session management: maps session_id -> LangGraph thread (in-memory MVP -> Redis prod)."""


class SessionStore:
    """Tracks active conversation sessions and their graph thread config."""

    def __init__(self) -> None: ...

    def get_or_create(self, session_id: str) -> dict:
        """Return thread config for the session, creating on first use."""
        ...

    def expire_idle(self, max_idle_seconds: int) -> int:
        """Drop idle sessions (ephemeral by default, Security 7)."""
        ...
