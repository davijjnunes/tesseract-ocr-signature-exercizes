"""Chamada ao modelo de visão no Ollama."""

# ruff: noqa: F401  (imports que as funções vão usar; tire ao implementar)
from collections.abc import Mapping, Sequence
from typing import Any, Literal

from ollama import ChatResponse, Client


def ollama_ask(
    model: str,
    messages: Sequence[Mapping[str, Any]],
    stream: Literal[False] = False,
    format: dict[str, Any] | Literal["", "json"] | None = None,
    keep_alive: str | float | None = "10m",
    think: bool | str | None = None,
    tools: Sequence[Any] | None = None,
    options: Mapping[str, Any] | None = None,
) -> ChatResponse:
    """Envia as mensagens ao Ollama e retorna a resposta do ``client.chat``.

    Criar o ``Client(host="http://localhost:11434", timeout=120)`` e usar
    ``temperature: 0`` e ``seed: 42`` nas opções para respostas estáveis.
    """
    pass
