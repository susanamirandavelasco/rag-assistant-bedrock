from src.embedding_service import generate_embedding
from src.vector_store import search


def semantic_search(
    query: str,
    n_results: int = 3
):

    query_embedding = generate_embedding(query)

    results = search(
        query_embedding=query_embedding,
        n_results=n_results
    )

    print(results["metadatas"])

    return results

def display_results(results):

    for i, doc in enumerate(results["documents"][0]):
        metadata = results["metadatas"][0][i]

        print("\n")
        print("=" * 80)

        print(f"RESULT {i+1}")

        print(f"Source: {metadata['source']}")

        print(f"Chunk: {metadata['chunk_number']}")

        print("=" * 80)

        print(doc[:500])