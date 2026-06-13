from pathlib import Path

from pdf2md.models.document import (
    Document
)
from pdf2md.models.page import Page

from .metadata_extractor import (
    extract_metadata
)
from .text_extractor import (
    extract_text_blocks
)
from .image_extractor import (
    extract_images
)


def extract_document(
    pdf_doc,
    image_dir: Path
) -> Document:

    document = Document()

    extract_metadata(
        pdf_doc,
        document
    )

    for page_index in range(
        len(pdf_doc)
    ):

        pdf_page = pdf_doc[
            page_index
        ]

        page = Page(
            number=page_index + 1,
            width=pdf_page.rect.width,
            height=pdf_page.rect.height
        )

        page.text_blocks = (
            extract_text_blocks(
                pdf_page
            )
        )

        page.image_blocks = (
            extract_images(
                pdf_page,
                pdf_doc,
                page.number,
                image_dir
            )
        )

        document.pages.append(
            page
        )

    return document