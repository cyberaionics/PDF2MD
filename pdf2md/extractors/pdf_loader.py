import fitz


def load_pdf(pdf_path: str) -> fitz.Document:
    """
    Open PDF and return PyMuPDF document.
    """

    return fitz.open(pdf_path)