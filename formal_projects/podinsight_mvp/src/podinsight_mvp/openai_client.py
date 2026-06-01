from __future__ import annotations

from typing import Protocol, cast

from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

from podinsight_mvp.cache import FileCache
from podinsight_mvp.settings import ModelEndpointConfig
from podinsight_mvp.types import ChatCompletionPayload, EmbeddingPayload


class Transport(Protocol):
    def create_chat_completion(self, *, model: str, messages: list[dict[str, str]]) -> ChatCompletionPayload: ...
    def create_embedding(self, *, model: str, input_text: str) -> EmbeddingPayload: ...


class OpenAITransport:
    def __init__(self, config: ModelEndpointConfig) -> None:
        self.client = OpenAI(base_url=config.base_url, api_key=config.api_key)

    def create_chat_completion(self, *, model: str, messages: list[dict[str, str]]) -> ChatCompletionPayload:
        typed_messages = cast(list[ChatCompletionMessageParam], messages)
        response = self.client.chat.completions.create(model=model, messages=typed_messages)
        dumped = cast(object, response.model_dump(mode="json"))
        return cast(ChatCompletionPayload, dumped)

    def create_embedding(self, *, model: str, input_text: str) -> EmbeddingPayload:
        response = self.client.embeddings.create(model=model, input=input_text)
        dumped = cast(dict[str, object], response.model_dump(mode="json"))
        data = cast(list[dict[str, object]], dumped.get("data", []))
        first = data[0] if data else {"embedding": []}
        return {"embedding": cast(list[float], first.get("embedding", []))}


class LLMClient:
    def __init__(self, config: ModelEndpointConfig, cache: FileCache, transport: Transport | None = None) -> None:
        self.config = config
        self.cache = cache
        self.transport = transport or OpenAITransport(config)

    def complete(self, messages: list[dict[str, str]]) -> ChatCompletionPayload:
        payload = {"model": self.config.model, "base_url": self.config.base_url, "messages": messages}
        cached = self.cache.get("chat", payload)
        if cached is not None:
            return cast(ChatCompletionPayload, cached)
        response = self.transport.create_chat_completion(model=self.config.model, messages=messages)
        return self.cache.set("chat", payload, response)


class EmbeddingClient:
    def __init__(self, config: ModelEndpointConfig, cache: FileCache, transport: Transport | None = None) -> None:
        self.config = config
        self.cache = cache
        self.transport = transport or OpenAITransport(config)

    def embed(self, text: str) -> EmbeddingPayload:
        payload = {"model": self.config.model, "base_url": self.config.base_url, "input": text}
        cached = self.cache.get("embedding", payload)
        if cached is not None:
            return cast(EmbeddingPayload, cached)
        response = self.transport.create_embedding(model=self.config.model, input_text=text)
        return self.cache.set("embedding", payload, response)
