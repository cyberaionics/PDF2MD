from pdf2md.models.block import Block


def detect_headings(
    blocks: list[Block],
    base_font: float = 10.0
):
    """
    Convert large-font blocks
    into markdown heading levels based on base_font.
    """

    if not blocks:
        return blocks

    if base_font <= 0:
        base_font = 10.0

    for block in blocks:

        if block.font_size >= base_font * 2.0:
            block.block_type = "heading"
            block.level = 1

        elif block.font_size >= base_font * 1.5:
            block.block_type = "heading"
            block.level = 2

        elif block.font_size >= base_font * 1.2:
            block.block_type = "heading"
            block.level = 3

    return blocks