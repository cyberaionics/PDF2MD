from pdf2md.models.block import Block
from pdf2md.models.page import Page
from pdf2md.models.document import (
    Document
)
from pdf2md.models.layout_item import (
    LayoutItem
)

from pdf2md.renderers.markdown_renderer import (
    MarkdownRenderer
)


def test_heading_render():

    page = Page(
        number=1
    )

    page.layout_items = [

        LayoutItem(
            item_type="text",
            payload=Block(
                block_type="heading",
                content="Title",
                level=1,
                x0=0,
                y0=0,
                x1=0,
                y1=0
            ),
            x0=0,
            y0=0
        )
    ]

    doc = Document(
        pages=[page]
    )

    renderer = MarkdownRenderer(
        "test.md"
    )

    md = renderer.render_document(
        doc
    )

    assert "# Title" in md