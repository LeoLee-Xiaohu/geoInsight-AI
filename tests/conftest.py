"""Shared fixtures: sample metadata records, fake settings, stub LLM/embeddings (no Bedrock calls)."""


def sample_dataset_records():
    """Fixture: small set of DatasetRecord covering queryable/non-queryable cases."""
    ...


def stub_llm():
    """Fixture: deterministic fake chat model for agent unit tests."""
    ...
