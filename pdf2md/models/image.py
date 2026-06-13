from dataclasses import dataclass


@dataclass
class ImageBlock:
    """
    Extracted image.
    """

    path: str

    x0: float
    y0: float
    x1: float
    y1: float

    width: float = 0
    height: float = 0