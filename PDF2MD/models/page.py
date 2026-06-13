from dataclasses import dataclass, field
from typing import List

from .block import Block
from .image import ImageBlock


@dataclass
class Page:
    """
    Represents a PDF page.
    """

    number: int

    text_blocks: List[Block] = field(
        default_factory=list
    )

    image_blocks: List[ImageBlock] = field(
        default_factory=list
    )