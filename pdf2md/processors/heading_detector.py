from statistics import mean

from pdf2md.models.block import Block


def detect_headings(
    blocks: list[Block]
):
    """
    Convert large-font blocks
    into markdown heading levels.
    """

    if not blocks:
        return blocks

    avg_font = mean(
        block.font_size
        for block in blocks
        if block.font_size > 0
    )

    for block in blocks:

        if block.font_size >= avg_font * 2:
            block.block_type = "heading"
            block.level = 1

        elif block.font_size >= avg_font * 1.6:
            block.block_type = "heading"
            block.level = 2

        elif block.font_size >= avg_font * 1.3:
            block.block_type = "heading"
            block.level = 3

    return blocks