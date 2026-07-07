import time

from src.ingestion.embedding_service import generate_embedding
from src.ingestion.vector_store import search

from src.models.models import (
    RetrievedChunk,
    RetrievalResult
)


class Retriever:

    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ) -> RetrievalResult:

        start_time = time.perf_counter()

        query_embedding = generate_embedding(query)

        results = search(
        query_embedding=query_embedding,
        n_results=top_k
        )

        chunks = []

        for document, metadata, distance in results:
            chunk = RetrievedChunk(
                content=document,
                metadata=metadata,
                distance=distance
            )

        chunks.append(chunk)

        elapsed_ms = (time.perf_counter() - start_time) * 1000

        return RetrievalResult(
            query=query,
            chunks=chunks,
            retrieval_time_ms=round(elapsed_ms, 2)
        )


