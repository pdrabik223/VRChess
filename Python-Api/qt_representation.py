import math
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from typing import List 
from PyQt5.QtCore import *

from Board import Board, RGB

BOARD_HEIGHT = 8
BOARD_WIDTH = 8

class BoardWindow():
    __buttons:QPushButton = [] 
    __button_states = []
    
    def __init__(self,device) -> None:
        self.app = QApplication(sys.argv)
        self.widget = QWidget()
        self.widget.setGeometry(8 * 80, 8*80,2+8*82,2+8*82)
        self.widget.setStyleSheet("background-color : black")
        self.widget.setWindowTitle("Board")
        self.board_handle = Board.connect_on_port(device)
        self.buttonGroup = QButtonGroup()
        self.buttonGroup.idClicked.connect(self.cycle_color)
        
        for x in range(BOARD_HEIGHT):
            for y in range(BOARD_WIDTH):
                self.__buttons.append(QPushButton(self.widget))
                self.__buttons[-1].setGeometry(2 + x * 82 ,2 + y * 82, 80, 80)
                self.__buttons[-1].setStyleSheet(f"background-color : red")
                self.buttonGroup.addButton(self.__buttons[-1],x*BOARD_WIDTH+y)
                self.board_handle[(x,y)] = RGB.red()
                self.__button_states.append(0)
        
        self.board_handle.display()
        self.widget.show()
        self.app.exec()         

        
    def rainbow(self, p , max):
        
        third = p // (max // 3)
        
        if third == 0:
            
            height_in_radians = p * math.pi  / (max / 3) / 2
            
            return (math.cos(height_in_radians) * 255, math.sin(height_in_radians) * 255,0)
        
        if third == 1:
            
            p -= max//3
            
            height_in_radians = p * math.pi  / (max / 3) / 2
            
            return(0, math.cos(height_in_radians) * 255,
                    math.sin(height_in_radians) * 255)
        
        if third == 2:
            
            p -=(2 * max)//3
            
            height_in_radians = p * math.pi  / (max / 3) / 2
            
            return(math.sin(height_in_radians) * 255, 0,
                    math.cos(height_in_radians) * 255)

    def cycle_color(self,idClicked):
        
        self.__button_states[idClicked] += 1
        
        if self.__button_states[idClicked] == 9:
            self.__button_states[idClicked] = 0
        
        self.board_handle.led_strip[idClicked] = self.rainbow( self.__button_states[idClicked],9)
        color = self.board_handle.led_strip[idClicked]
        print(color)
        self.__buttons[idClicked].setStyleSheet(f"background-color : rgb({color[0]},{color[1]},{color[2]})")
        self.board_handle.display()
        self.widget.show()
        
        # print("window works")

        # board = self.board_handle
        # for x in range(8):
        #    for y in range(8):

        #        print(str(board))
        #        board.fill_w_color(RGB.green())# clean display with black color
        #        board[(x,y)] = RGB.red() # update board display
        #        board.display() # send update to arduino board
        #        board.update_board() # get current board state from arduino 
        #        self.update(board.led_strip)
        #        time.sleep(3) # wait for second 

        # board.close_connection()

def main():
    """
    sync board indefinitely  
    """
    window = BoardWindow("COM3")
        

if __name__ == "__main__":
    main()
