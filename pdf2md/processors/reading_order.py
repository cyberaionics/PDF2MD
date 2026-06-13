from pdf2md.models.layout_item import (
    LayoutItem
)


def sort_layout_items(
    items: list[LayoutItem]
):
    """
    Sort top-to-bottom,
    then left-to-right.
    """

    return sorted(
        items,
        key=lambda item: (
            round(item.y0, 1),
            round(item.x0, 1)
        )
    )