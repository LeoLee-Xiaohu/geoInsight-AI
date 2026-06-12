"""Gradio chat interface: multi-turn chat with inline plot rendering."""


def build_ui():
    """Construct gr.Blocks chat app: chatbot component, session handling, image artifacts inline."""
    ...


def respond(message: str, history: list, session_id: str):
    """Chat callback -> FastAPI /chat (or direct graph call in single-container POC)."""
    ...


def launch() -> None:
    """Entry point: launch Gradio app (mounted on FastAPI or standalone)."""
    ...
