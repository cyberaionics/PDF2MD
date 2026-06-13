from pdf2md.processors.heading_detector import (
    detect_headings
)

from pdf2md.processors.image_placer import (
    merge_page_content
)

from pdf2md.processors.reading_order import (
    sort_layout_items
)

from pdf2md.processors.font_analysis import (
    font_distribution
)


def analyze_page(
    page,
    base_font: float
):
    """
    Analyze page structure.
    """

    page.text_blocks = detect_headings(
        page.text_blocks,
        base_font
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

    dist = font_distribution(
        document
    )

    if dist:
        base_font = dist.most_common(1)[0][0]
    else:
        base_font = 10.0

    for page in document.pages:

        analyze_page(
            page,
            base_font
        )

    return document