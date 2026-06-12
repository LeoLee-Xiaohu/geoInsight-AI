"""Prompt templates for each agent role (LangChain ChatPromptTemplate)."""

from langchain_core.prompts import ChatPromptTemplate

SUPERVISOR_SYSTEM_PROMPT: str = ...
"""Role, scope (IMOS data only), routing instructions, grounding rules (KB only, never invent datasets)."""

ENTITY_EXTRACTION_PROMPT: str = ...
"""Few-shot extraction of {variable, place_name, time_phrase, intent} as structured output."""

DISCOVERY_ANSWER_PROMPT: str = ...
"""Compose ranked dataset list answer citing only retrieved KB metadata fields."""

VISUALIZATION_CAPTION_PROMPT: str = ...
"""Generate plot caption from computed stats (e.g. 'avg temp rose 1.2 degC')."""


def build_supervisor_prompt() -> ChatPromptTemplate:
    """Supervisor prompt with conversation history placeholder."""
    ...


def build_extraction_prompt() -> ChatPromptTemplate:
    """Entity-extraction prompt for structured-output LLM call."""
    ...
