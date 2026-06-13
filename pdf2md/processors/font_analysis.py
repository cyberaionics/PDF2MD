from collections import Counter


def font_distribution(
    document
):
    """
    Return font-size histogram.
    """

    sizes = []

    for page in document.pages:

        for block in page.text_blocks:

            if block.font_size > 0:
                sizes.append(
                    round(
                        block.font_size,
                        1
                    )
                )

    return Counter(sizes)