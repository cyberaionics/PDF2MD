from pdf2md.converter import (
    PDFToMarkdownConverter
)


def test_converter_exists():

    assert (
        PDFToMarkdownConverter
        is not None
    )