from dataclasses import dataclass, field
from typing import Any

@dataclass
class RetrievedChunk:
    content: str
    distance: float
    metadata: dict[str, Any]


@dataclass
class RetrievalResult:
    query: str
    chunks: list[RetrievedChunk] = field(default_factory=list)
    retrieval_time_ms: float = 0.0