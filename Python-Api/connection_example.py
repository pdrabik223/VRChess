""" connection example file

"""
from asyncio import sleep
from board import *
def main()->None:
    board = Board(None)
    
    for x in range(8):
        for y in range(8):
    
            print(str(board))
            board.fill_w_color(RGB.green())# clean display with black color

            board[(x,y)] = RGB.red() # update board display

            board.display() # send update to arduino board
            board.update_board() # get current board state from arduino 
            sleep(1) # wait for second 
    
    board.close_connection()

if __name__ == "__main__":
    main()