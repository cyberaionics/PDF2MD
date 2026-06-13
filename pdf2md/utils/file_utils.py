from pathlib import Path


def relative_image_path(
    markdown_file: str,
    image_file: str
) -> str:
    """
    Generate relative path from markdown file
    to image file.
    """

    md_path = Path(markdown_file)

    return str(
        Path(image_file).relative_to(
            md_path.parent
        )
    )