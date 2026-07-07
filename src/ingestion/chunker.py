def chunk_text(
    text: str,
    chunk_size: int = 500 #words in each chunk
) -> list[str]:
    """
    Divide un texto en chunks de N palabras.
    """

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks