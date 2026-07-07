from dataclasses import dataclass, field

@dataclass
class Source:
    document: str
    page_range: str


@dataclass
class RAGResponse:
    answer: str
    sources: list[Source] = field(default_factory=list)


