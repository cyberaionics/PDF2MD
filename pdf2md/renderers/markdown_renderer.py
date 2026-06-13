from pathlib import Path

from pdf2md.models.block import Block
from pdf2md.models.image import ImageBlock


class MarkdownRenderer:

    def __init__(
        self,
        markdown_path: str
    ):
        self.markdown_path = Path(
            markdown_path
        )

        self.lines = []

    def render_document(
        self,
        document
    ) -> str:

        self.lines.clear()

        self._render_metadata(
            document
        )

        for page in document.pages:

            self._render_page(
                page
            )

        return "\n".join(
            self.lines
        )

    def save(
        self,
        content: str
    ):

        with open(
            self.markdown_path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(content)

    def _render_metadata(
        self,
        document
    ):

        if document.title:

            self.lines.append(
                f"# {document.title}"
            )

            self.lines.append("")

        if document.author:

            self.lines.append(
                f"*Author:* {document.author}"
            )

            self.lines.append("")

            self.lines.append("---")
            self.lines.append("")

    def _render_page(
        self,
        page
    ):

        self.lines.append("")
        self.lines.append(
            f"<!-- Page {page.number} -->"
        )
        self.lines.append("")

        for item in page.layout_items:

            if item.item_type == "text":

                self._render_text(
                    item.payload
                )

            elif item.item_type == "image":

                self._render_image(
                    item.payload
                )

    def _render_text(
        self,
        block: Block
    ):

        if block.block_type == "heading":

            level = max(
                1,
                min(
                    block.level,
                    6
                )
            )

            self.lines.append(
                "#" * level
                + " "
                + block.content
            )

            self.lines.append("")

        else:

            self.lines.append(
                block.content
            )

            self.lines.append("")

    def _render_image(
        self,
        image: ImageBlock
    ):

        relative = image.path.replace(
            "\\",
            "/"
        )

        self.lines.append(
            f"![Image]({relative})"
        )

        self.lines.append("")