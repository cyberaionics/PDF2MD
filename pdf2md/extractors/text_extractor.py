from pdf2md.models.block import Block


def extract_text_blocks(page):
    """
    Extract text blocks from a PDF page.

    Returns:
        list[Block]
    """

    blocks = []

    page_dict = page.get_text("dict")

    for block in page_dict["blocks"]:

        if block["type"] != 0:
            continue

        text = []

        font_size = 0

        for line in block["lines"]:

            for span in line["spans"]:

                text.append(
                    span["text"]
                )

                font_size = max(
                    font_size,
                    span["size"]
                )

        content = " ".join(text).strip()

        if not content:
            continue

        x0, y0, x1, y1 = block["bbox"]

        blocks.append(
            Block(
                block_type="text",
                content=content,
                x0=x0,
                y0=y0,
                x1=x1,
                y1=y1,
                font_size=font_size
            )
        )

    return blocks