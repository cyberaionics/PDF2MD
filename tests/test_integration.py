import tempfile
from pathlib import Path
from pdf2md.models.block import Block
from pdf2md.models.page import Page
from pdf2md.models.document import Document
from pdf2md.processors.layout_analyzer import analyze_document
from pdf2md.renderers.markdown_renderer import MarkdownRenderer


def test_empty_font_sizes_handling():
    # Page with text block but no font size (e.g. font_size = 0)
    page_no_font = Page(
        number=1,
        text_blocks=[
            Block(
                block_type="text",
                content="Hello World",
                x0=10,
                y0=10,
                x1=50,
                y1=20,
                font_size=0
            )
        ]
    )

    doc = Document(pages=[page_no_font])

    # analyze_document should run successfully without raising StatisticsError
    analyzed_doc = analyze_document(doc)
    
    assert analyzed_doc is not None
    assert len(analyzed_doc.pages) == 1
    # Since font size is 0, it shouldn't be classified as a heading
    assert analyzed_doc.pages[0].text_blocks[0].block_type == "text"


def test_document_wide_heading_detection():
    # Let's verify headings are classified correctly relative to a document-wide base font.
    # Body text is 10.0, heading level 1 is 20.0
    page_1 = Page(
        number=1,
        text_blocks=[
            Block(
                block_type="text",
                content="Body line 1",
                x0=10,
                y0=10,
                x1=50,
                y1=20,
                font_size=10.0
            ),
            Block(
                block_type="text",
                content="Body line 2",
                x0=10,
                y0=30,
                x1=50,
                y1=40,
                font_size=10.0
            ),
            Block(
                block_type="text",
                content="Heading 1 Title",
                x0=10,
                y0=50,
                x1=100,
                y1=80,
                font_size=20.0
            )
        ]
    )

    # Page 2 has only a sub-heading (15.0) which is 1.5 * body font
    page_2 = Page(
        number=2,
        text_blocks=[
            Block(
                block_type="text",
                content="Sub Heading Title",
                x0=10,
                y0=10,
                x1=80,
                y1=30,
                font_size=15.0
            )
        ]
    )

    doc = Document(pages=[page_1, page_2])
    analyzed_doc = analyze_document(doc)

    # Base font should be 10.0 (most common in the document)
    # Heading on page 1 should be level 1
    h1 = analyzed_doc.pages[0].text_blocks[2]
    assert h1.block_type == "heading"
    assert h1.level == 1

    # Heading on page 2 should be level 2 (since 15.0 >= 10.0 * 1.5)
    h2 = analyzed_doc.pages[1].text_blocks[0]
    assert h2.block_type == "heading"
    assert h2.level == 2


def test_markdown_renderer_directory_creation():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a path with a non-existent nested directory
        nested_dir = Path(tmpdir) / "nested_dir" / "deeper_dir"
        output_file = nested_dir / "output.md"

        renderer = MarkdownRenderer(str(output_file))
        
        # Test file saving ensures directory creation
        renderer.save("# Test Content\n")

        assert output_file.exists()
        assert output_file.read_text(encoding="utf-8") == "# Test Content\n"
