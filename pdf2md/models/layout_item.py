from dataclasses import dataclass
from typing import Any


@dataclass
class LayoutItem:

    item_type: str
    payload: Any

    y0: float
    x0: float