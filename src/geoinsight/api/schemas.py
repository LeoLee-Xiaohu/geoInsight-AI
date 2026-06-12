"""Request/response Pydantic schemas for the API layer."""

from pydantic import BaseModel


class ChatRequest(BaseModel):
    """Inbound chat turn."""

    session_id: str
    message: str


class ArtifactRef(BaseModel):
    """Reference to a generated plot artifact."""

    artifact_id: str
    type: str  # "png" | "html"
    caption: str | None


class ChatResponse(BaseModel):
    """Agent reply: text plus optional artifacts."""

    session_id: str
    answer: str
    artifacts: list[ArtifactRef]


class DatasetSearchResponse(BaseModel):
    """Direct KB search results (debug / portal integration)."""

    results: list[dict]
