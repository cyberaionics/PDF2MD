from pathlib import Path


def markdown_image(
    path: str,
    alt: str = "Image"
):
    path = (
        Path(path)
        .as_posix()
    )

    return (
        f"![{alt}]({path})"
    )