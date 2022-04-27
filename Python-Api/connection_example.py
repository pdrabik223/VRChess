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
    
    
def serial_monitor(port:str,baudrate=9600)->None:
    arduino = serial.Serial(port=port, baudrate=baudrate)
    while(True):
        payload = str(arduino.readline())
        print(payload)
def led_connection(port:str)->None:    
    board = Board.connect_on_port(port)
    while(True):
        for x in range(2):
            for y in range(2):
            
                print(str(board))
                board.fill_w_color(RGB.green())# clean display with green color
                board[(x,y)] = RGB.red() # update board display

                board.display() # send update to arduino board
                # board.update_board() # get current board state from arduino 
                time.sleep(1) # wait for second 
            
if __name__ == "__main__":
    # led_example()
    # button_matrix_example()
    # serial_monitor("COM3")
    led_connection("COM3")
    