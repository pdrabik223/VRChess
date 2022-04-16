import unittest
from board import *

class TestBoard(unittest.TestCase):
    def test_board_init(self):
        board = Board(device=None)
    
        for x in range(board.BOARD_HEIGHT ):
            for y in range(board.BOARD_WIDTH):
                self.assertEqual(board[(x,y)] , (RGB.red(),False))
    def test_get_set_item(self):
        
        board = Board(device=None)
    
        for x in range(board.BOARD_HEIGHT ):
            for y in range(board.BOARD_WIDTH):
                board[(x,y)] = RGB(r=127,g=127,b=127)
        
        
        for x in range(board.BOARD_HEIGHT ):
            for y in range(board.BOARD_WIDTH):
                self.assertEqual( board[(x,y)] , (RGB(127,127,127),False)) 
    
    def test_conv_1_d(self):
        
        board = Board(None)
        for x in range(0,8):
            for y in range(0,8):
                self.assertEqual( board.conv_1_d((x,y)) , x * 8 + y)
                
        invalid_test_cases = [(-1,0),(0,-1),(8,0),(0,8)]
        for x,y in invalid_test_cases:
            self.assertRaises(Exception,board.conv_1_d((x,y)))
                 
                 

if __name__ == '__main__':
    unittest.main()
    