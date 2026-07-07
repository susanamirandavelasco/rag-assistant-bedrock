from pypdf import PdfReader


def load_pdf(pdf_path: str) -> str:
    """
    Carga un PDF completo y devuelve todo el texto concatenado.

    Args:
        pdf_path (str): Ruta al archivo PDF.

    Returns:
        str: Texto completo extraído del PDF.
    """

    reader = PdfReader(pdf_path)

    text = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text.append(page_text)

    return "\n".join(text)


def load_pdf_pages(
    pdf_path: str,
    start_page: int,
    end_page: int
) -> str:
    """
    Carga únicamente un rango de páginas.
    """

    reader = PdfReader(pdf_path)

    text = []

    for page_num in range(start_page, end_page):
        print(f"Leyendo página {page_num + 1}")
        page_text = reader.pages[page_num].extract_text()

        if page_text:
            text.append(page_text)

    return "\n".join(text)


def get_pdf_page_count(pdf_path: str) -> int:
    """
    Devuelve el número de páginas del PDF.
    """

    reader = PdfReader(pdf_path)

    return len(reader.pages)
