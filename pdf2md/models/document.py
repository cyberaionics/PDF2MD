from dataclasses import dataclass, field
from typing import List

from .page import Page


@dataclass
class Document:
    """
    Intermediate document representation.
    """

    title: str = ""
    author: str = ""

    pages: List[Page] = field(
        default_factory=list
    )