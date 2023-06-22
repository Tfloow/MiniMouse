import unittest
import main
from Solver import *

class Test_Maze_Operation(unittest.TestCase):
    
    def test_write_around_top_left(self):
        original_maze = small_good_maze()
        
        # Top Left corner
        result_maze = write_around(original_maze, 0, 0, 2, 1)
        self.assertEqual(result_maze[0][1], 2,)
        self.assertEqual(result_maze[1][1], 2)
        self.assertEqual(result_maze[1][0], 2)
        
    def test_write_around_bottom_right(self):
        original_maze = small_good_maze()
        
        # Bottom Right corner
        result_maze = write_around(original_maze, 2, 2, 2, 1)
        self.assertEqual(result_maze[2][1], 2)
        self.assertEqual(result_maze[1][1], 2)
        self.assertEqual(result_maze[1][2], 2)
        
        
        
if __name__ == '__main__':
    unittest.main()