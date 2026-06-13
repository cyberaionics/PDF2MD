from pdf2md.extractors.pdf_loader import (
    load_pdf
)


def test_loader():

    assert callable(
        load_pdf
    )