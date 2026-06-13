from dataclasses import dataclass
from typing import Tuple


@dataclass
class Block:

    block_type: str
    content: str

    x0: float
    y0: float
    x1: float
    y1: float

    font_size: float = 0

    level: int = 0

    @property
    def bbox(self) -> Tuple[
        float,
        float,
        float,
        float
    ]:
        return (
            self.x0,
            self.y0,
            self.x1,
            self.y1
        )