from pdf2md.processors.heading_detector import (
    detect_headings
)

from pdf2md.processors.image_placer import (
    merge_page_content
)

from pdf2md.processors.reading_order import (
    sort_layout_items
)


def analyze_page(page):
    """
    Analyze page structure.
    """

    page.text_blocks = detect_headings(
        page.text_blocks
    )

    merged = merge_page_content(
        page
    )

    page.layout_items = (
        sort_layout_items(
            merged
        )
    )

    return page


def analyze_document(
    document
):
    """
    Analyze every page.
    """

    for page in document.pages:

        analyze_page(page)

    return document