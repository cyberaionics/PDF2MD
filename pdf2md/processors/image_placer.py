from pdf2md.models.layout_item import (
    LayoutItem
)


def merge_page_content(page):
    """
    Merge text and images into a
    single ordered layout list.
    """

    items = []

    for block in page.text_blocks:

        items.append(
            LayoutItem(
                item_type="text",
                payload=block,
                y0=block.y0,
                x0=block.x0
            )
        )

    for image in page.image_blocks:

        items.append(
            LayoutItem(
                item_type="image",
                payload=image,
                y0=image.y0,
                x0=image.x0
            )
        )

    return items