from pathlib import Path
import os


def relative_path(
    source_file: str,
    target_file: str
) -> str:
    """
    Compute relative path from source file
    to target file.
    """

    return os.path.relpath(
        target_file,
        start=Path(source_file).parent
    )