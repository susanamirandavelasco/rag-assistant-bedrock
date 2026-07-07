from src.retriever import Retriever
from src.prompt_builder import PromptBuilder
from src.generator import Generator
from src.models.rag_response import RAGResponse, Source
from src.models.models import RetrievalResult


class RAGAssistant:

    def __init__(self):

        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()
        self.generator = Generator()

    def ask(
        self,
        query: str
    ) -> RAGResponse:

        retrieval_result = self.retriever.retrieve(query)

        prompt = self.prompt_builder.build_prompt(
            query,
            retrieval_result
        )

        answer = self.generator.generate(prompt)

        sources = self._build_sources(retrieval_result)

        return RAGResponse(
            answer=answer,
            sources=sources
        )


    def _build_sources(
        self,
        retrieval_result: RetrievalResult
        ) -> list[Source]:

        sources = []

        for chunk in retrieval_result.chunks:
            source = Source(
                document=chunk.metadata["source"],                
                page_range=chunk.metadata["page_range"],
            )

        sources.append(source)

        return sources

