

from dataclasses import dataclass

from numpy import uint8


@dataclass
class RGB:
    r: uint8
    g: uint8
    b: uint8


class Board:
    __led_strip: List[RGB] = []
