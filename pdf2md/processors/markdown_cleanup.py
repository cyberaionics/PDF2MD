import re


def cleanup_markdown(
    markdown: str
):
    """
    Remove excessive blank lines.
    """

    markdown = re.sub(
        r"\n{3,}",
        "\n\n",
        markdown
    )

    return markdown.strip() + "\n"