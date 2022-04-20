""" connection example file

"""
from Board import *
import time
def led_example()->None:
    board = Board(None)
    
    for x in range(8):
        for y in range(8):
    
            print(str(board))
            board.fill_w_color(RGB.green())# clean display with black color

            board[(x,y)] = RGB.red() # update board display

            board.display() # send update to arduino board
            board.update_board() # get current board state from arduino 
            time.sleep(1) # wait for second 
    
    board.close_connection()

def button_matrix_example()->None:
    board = Board.connect_on_port("COM3")
    while(True):
        board.update_board()
        print(str(board))
        time.sleep(1)
            
if __name__ == "__main__":
    led_example()
    # button_matrix_example()