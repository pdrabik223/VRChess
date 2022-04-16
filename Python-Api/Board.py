

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
    
    def __str__(self)->str:
        """
        RGB to string casting in HEX form, output e.g. "ff0000" for color red

        Returns:
            str: collor in HEX encoding in string form 
        """
        str_r = str(hex(self.r))[2:]
        if self.r <= 16: 
            str_r = '0' + str_r
            
        str_g = str(hex(self.g))[2:]
        if self.g <= 16: 
            str_g = '0' + str_g
        
        str_b = str(hex(self.b))[2:]
        if self.b <= 16: 
            str_b = '0' + str_b
        
        return str_r + str_g + str_b

class Board:
    __led_strip: List[RGB] = []
    __buttons: List[bool] = []
    BOARD_WIDTH: uint16 = 8
    BOARD_HEIGHT: uint16 = 8
    __action_number = 0 

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
        """
        creates board object connected to arduino board via specified port
        
        Args:
            port (str): COM port id to connect on e.g. "COM3"
            baudrate (int, optional): connection baudrate Defaults to 115200.

        Returns:
            Board: connected board object
        """
        
        return Board(serial.Serial(port=port, baudrate=baudrate))

    def display(self) -> None:
        """
        Update Arduino chessboard colors with new ones 
        """
        message = self.generate_led_state()
        self.arduino.write(bytes(message + "\n", 'utf-8'))


    def update_board(self) -> None:
        """
        Update board with reading from Arduino
        """
        read_square_states = str(self.arduino.readline())
        parsed_square_states = read_square_states.split(' ')
        
        self.__action_number = int(read_square_states[-1])
        
        for i in range(self.BOARD_HEIGHT*self.BOARD_WIDTH):
            self.__buttons[i] = bool(parsed_square_states[i])
        

    def generate_led_state(self)->str:
        state = ""
        for led in self.__led_strip:
            state += str(led) + ' '
        return state
    
        
        
    def __getitem__(self, position: Tuple[uint8, uint8]) -> Tuple[RGB, bool]:
        """getter for state of specied square 

        Args:
            position (Tuple[uint8, uint8]): position in question

        Returns:
            Tuple[RGB, bool]: color and occupation of square (in that order) 
        """
        position_1_d = self.conv_1_d(position)
        return (self.__led_strip[position_1_d], self.__buttons[position_1_d])

    def __setitem__(self, position: Tuple[uint8, uint8], color: RGB) -> None:
        """settor for specied square color 

        Args:
            position (Tuple[uint8, uint8]): position of square in question
            color (RGB): new collor of square
        """
        position_1_d = self.conv_1_d(position)
        self.__led_strip[position_1_d] = color

    
    def conv_1_d(self, position_2_d: Tuple[uint8, uint8]) -> uint16:
        """
        convert point in 2 dimension space to point in one dimension space

        Args:
            position_2_d (Tuple[uint8, uint8]): pair of values (length in x dimension, length in y dimension )

        Raises:
            Exception: Incorrect position, passed value is incorrect

        Returns:
            uint16: point in one dimension space
        """
        if position_2_d[0] > self.BOARD_HEIGHT or position_2_d[1] > self.BOARD_WIDTH:
            raise Exception("Incorrect position")

        return self.BOARD_HEIGHT*position_2_d[0] + position_2_d[1]
    
