from pathlib import Path

from pdf2md.extractors.pdf_loader import (
    load_pdf
)

from pdf2md.extractors.document_extractor import (
    extract_document
)

from pdf2md.processors.layout_analyzer import (
    analyze_document
)

from pdf2md.processors.markdown_cleanup import (
    cleanup_markdown
)

from pdf2md.renderers.markdown_renderer import (
    MarkdownRenderer
)

from pdf2md.utils.file_utils import (
    ensure_directory
)


class PDFToMarkdownConverter:

    def __init__(
        self,
        input_pdf: str,
        output_md: str,
        image_dir: str
    ):
        self.input_pdf = input_pdf
        self.output_md = output_md
        self.image_dir = image_dir

    def convert(self):

        try:

            ensure_directory(
                self.image_dir
            )

            pdf_doc = load_pdf(
                self.input_pdf
            )

            document = extract_document(
                pdf_doc,
                Path(self.image_dir)
            )

            document = analyze_document(
                document
            )

            renderer = MarkdownRenderer(
                self.output_md
            )

            markdown = (
                renderer.render_document(
                    document
                )
            )

            markdown = cleanup_markdown(
                markdown
            )

            renderer.save(
                markdown
            )

            pdf_doc.close()

            return markdown

        except Exception as exc:

            raise RuntimeError(
                f"Conversion failed: {exc}"
            )