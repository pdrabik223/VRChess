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
        self.widget.setGeometry(80, 80,2+9*82,2+8*82)
        self.widget.setStyleSheet("background-color : black")
        self.widget.setWindowTitle("Board")
        if(device == None):
            self.board_handle = Board(None)
        else:    
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
                
                
        self.chess_colors = QPushButton(self.widget)
        self.chess_colors.setGeometry(2 + 8 * 82 ,0, 80, 80)
        self.chess_colors.setStyleSheet(f"background-color : gray")
        self.chess_colors.setText("chess grid")
        self.chess_colors.clicked.connect(self.turn_on_chess)
  
        self.chess_colors = QPushButton(self.widget)
        self.chess_colors.setGeometry(2 + 8 * 82 ,1 * 82, 80, 80)
        self.chess_colors.setStyleSheet(f"background-color : gray")
        self.chess_colors.setText("chess grid animation")
        self.chess_colors.clicked.connect(self.turn_on_chess_animation)
  
        
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


    def turn_on_chess(self):
        self.board_handle.set_chess_colors()
        self.update_qui()
        self.board_handle.display()
        self.widget.show()
        
        
    def turn_on_chess_animation(self):
        for i in range (10):
            self.board_handle.set_chess_colors(white_color=RGB.black(),black_color=RGB.white())
            self.update_qui()
            self.board_handle.display()
            self.widget.show()
            time.sleep(1)

            
            self.board_handle.set_chess_colors(white_color=RGB.white(),black_color=RGB.black())
            self.update_qui()
            self.board_handle.display()
            self.widget.show()
            time.sleep(1)
            
            
    def cycle_color(self,idClicked):
        
        self.__button_states[idClicked] += 1
        
        if self.__button_states[idClicked] == 12:
            self.__button_states[idClicked] = 0
        
        color =  self.rainbow( self.__button_states[idClicked],12)
        self.board_handle.led_strip[idClicked] = RGB(round(color[0]), round(color[1]), round(color[2]))
        color = self.board_handle.led_strip[idClicked]
        print(str(color))
        self.__buttons[idClicked].setStyleSheet(f"background-color : rgb({color.r},{color.g},{color.b})")
        self.board_handle.display()
        self.widget.show()
        
    def update_qui(self):
        for i in range(BOARD_HEIGHT * BOARD_WIDTH):
            color = self.board_handle.led_strip[i]
            self.__buttons[i].setStyleSheet(f"background-color : rgb({color.r},{color.g},{color.b})")

def main():
    """
    sync board indefinitely  
    """
    window = BoardWindow("COM3")
        

if __name__ == "__main__":
    main()
