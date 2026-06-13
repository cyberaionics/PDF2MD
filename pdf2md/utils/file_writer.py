from pathlib import Path


def write_text(
    path: str,
    content: str
):

    output = Path(path)

    output.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        output,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)