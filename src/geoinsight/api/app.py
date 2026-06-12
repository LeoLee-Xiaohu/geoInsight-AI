"""FastAPI application: endpoints wired to the compiled LangGraph."""

from fastapi import FastAPI

from geoinsight.api.schemas import ChatRequest, ChatResponse, DatasetSearchResponse


def create_app() -> FastAPI:
    """Build app: load settings, build graph once, register routes + rate limiting."""
    ...


async def chat(request: ChatRequest) -> ChatResponse:
    """POST /chat -- run one agent turn, return answer + artifact refs."""
    ...


async def get_artifact(artifact_id: str):
    """GET /artifacts/{id} -- serve generated PNG/HTML."""
    ...


async def search_datasets(q: str, k: int = 10) -> DatasetSearchResponse:
    """GET /datasets/search -- direct hybrid KB retrieval (C-persona / debug)."""
    ...


async def health() -> dict:
    """GET /health -- liveness/readiness."""
    ...
