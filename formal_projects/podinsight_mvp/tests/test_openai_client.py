from typing import cast

import pytest

from podinsight_mvp.cache import FileCache
from podinsight_mvp.openai_client import EmbeddingClient, LLMClient
from podinsight_mvp.settings import ModelEndpointConfig
from podinsight_mvp.types import ChatCompletionPayload, EmbeddingPayload


class DummyTransport:
    def __init__(self, response: ChatCompletionPayload | EmbeddingPayload) -> None:
        self.response = response
        self.calls = []

    def create_chat_completion(self, *, model: str, messages: list[dict[str, str]]) -> ChatCompletionPayload:
        self.calls.append(("chat", model, messages))
        return cast(ChatCompletionPayload, self.response)

    def create_embedding(self, *, model: str, input_text: str) -> EmbeddingPayload:
        self.calls.append(("embedding", model, input_text))
        return cast(EmbeddingPayload, self.response)


class FailingTransport:
    def __init__(self, message: str) -> None:
        self.message = message
        self.calls = []

    def create_chat_completion(self, *, model: str, messages: list[dict[str, str]]) -> ChatCompletionPayload:
        self.calls.append(("chat", model, messages))
        raise RuntimeError(self.message)

    def create_embedding(self, *, model: str, input_text: str) -> EmbeddingPayload:
        self.calls.append(("embedding", model, input_text))
        raise RuntimeError(self.message)


def test_cached_chat_completion_reuses_response(tmp_path) -> None:
    transport = DummyTransport({"id": "chat-1", "content": "hello"})
    config = ModelEndpointConfig(base_url="http://example.com/v1", api_key="token", model="deepseek-v4-pro")
    client = LLMClient(config=config, cache=FileCache(tmp_path), transport=transport)

    first = client.complete(messages=[{"role": "user", "content": "hello"}])
    second = client.complete(messages=[{"role": "user", "content": "hello"}])

    assert first == second
    assert transport.calls == [("chat", "deepseek-v4-pro", [{"role": "user", "content": "hello"}])]


def test_cached_embedding_reuses_response(tmp_path) -> None:
    transport = DummyTransport({"embedding": [0.1, 0.2]})
    config = ModelEndpointConfig(base_url="http://example.com/v1", api_key="token", model="Qwen3-Embedding-0.6B")
    client = EmbeddingClient(config=config, cache=FileCache(tmp_path), transport=transport)

    first = client.embed("test")
    second = client.embed("test")

    assert first == second
    assert transport.calls == [("embedding", "Qwen3-Embedding-0.6B", "test")]


def test_chat_completion_surfaces_transport_errors_without_caching(tmp_path) -> None:
    transport = FailingTransport("401 auth")
    config = ModelEndpointConfig(base_url="http://example.com/v1", api_key="token", model="deepseek-v4-pro")
    client = LLMClient(config=config, cache=FileCache(tmp_path), transport=transport)

    with pytest.raises(RuntimeError, match="401 auth"):
        client.complete(messages=[{"role": "user", "content": "hello"}])
    with pytest.raises(RuntimeError, match="401 auth"):
        client.complete(messages=[{"role": "user", "content": "hello"}])

    assert transport.calls == [
        ("chat", "deepseek-v4-pro", [{"role": "user", "content": "hello"}]),
        ("chat", "deepseek-v4-pro", [{"role": "user", "content": "hello"}]),
    ]


def test_embedding_surfaces_transport_errors_without_caching(tmp_path) -> None:
    transport = FailingTransport("401 auth")
    config = ModelEndpointConfig(base_url="http://example.com/v1", api_key="token", model="Qwen3-Embedding-0.6B")
    client = EmbeddingClient(config=config, cache=FileCache(tmp_path), transport=transport)

    with pytest.raises(RuntimeError, match="401 auth"):
        client.embed("test")
    with pytest.raises(RuntimeError, match="401 auth"):
        client.embed("test")

    assert transport.calls == [
        ("embedding", "Qwen3-Embedding-0.6B", "test"),
        ("embedding", "Qwen3-Embedding-0.6B", "test"),
    ]
