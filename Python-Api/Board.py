

from dataclasses import dataclass
import serial
from typing import List, Tuple
from numpy import uint16, uint8


@dataclass
class RGB:
    """
        Helper class for descrying color
    """
    r: uint8
    g: uint8
    b: uint8
# Todo more colors

    @staticmethod
    def red() :
        return RGB(r=255, g=0, b=0)

    @staticmethod
    def blue() :
        return RGB(r=0, g=0, b=255)

    @classmethod
    def green() :
        return RGB(r=0, g=255, b=0)


class Board:
    __led_strip: List[RGB] = []
    __buttons: List[bool] = []
    BOARD_WIDTH: uint16 = 8
    BOARD_HEIGHT: uint16 = 8

    def __init__(self, device: serial.Serial) -> None:
        """
        Create an Board using specified `device` to communicate with

        Args:
            device (Serial): Serial device used for communication

        """
        for _ in range(self.BOARD_HEIGHT * self.BOARD_WIDTH):
            self.__led_strip.append(RGB.red())
        for _ in range(self.BOARD_HEIGHT * self.BOARD_WIDTH):
            self.__buttons.append(False)
        self.arduino = device

    @staticmethod
    def using_serial_on_port(port: str, baudrate=115200):
        return Board(serial.Serial(port=port, baudrate=baudrate))

    def display() -> None:
        """
        Update Arduino chessboard colors with new ones 

        """
        pass

    def update_board() -> None:
        """
        Update board with reading from Arduino
        """
        pass

    def __getitem__(self, position: Tuple[uint8, uint8]) -> Tuple[RGB, bool]:
        position_1_d = self.conv_1_d(position)
        return (self.__led_strip[position_1_d], self.__buttons[position_1_d])

    def __setitem__(self, position: Tuple[uint8, uint8], color: RGB) -> None:
        position_1_d = self.conv_1_d(position)
        self.__led_strip[position_1_d] = color

    
    def conv_1_d(self, position_2_d: Tuple[uint8, uint8]) -> uint16:

        if position_2_d[0] > self.BOARD_HEIGHT or position_2_d[1] > self.BOARD_WIDTH:
            raise Exception("Incorrect position")

        return self.BOARD_HEIGHT*position_2_d[0] + position_2_d[1]
    
