"""Factories for AWS Bedrock chat and embedding models via LangChain."""

from langchain_aws import BedrockEmbeddings, ChatBedrockConverse

from geoinsight.config import Settings


def get_supervisor_llm(settings: Settings) -> ChatBedrockConverse:
    """Claude on Bedrock for supervisor reasoning / response synthesis."""
    ...


def get_extraction_llm(settings: Settings) -> ChatBedrockConverse:
    """Cheaper/faster model (Nova/Haiku) for entity extraction with structured output."""
    ...


def get_embeddings(settings: Settings) -> BedrockEmbeddings:
    """Titan embeddings for KB ingestion and query-time retrieval."""
    ...
