import unittest 
from unittest.mock import patch
from io import StringIO
from world import obstacles
import random
class Third_test(unittest.TestCase):
    
    def test_create_ob_x(self):
        for test in range(100):
            for i in obstacles.list_obstacle:
                
                self.assertTrue(-100 < i[0][0] <= 100)
                
    def test_create_ob_y(self):
        for test in range(100):
            for j in obstacles.list_obstacle:
                self.assertTrue(-200 < j[0][1] <= 200)

    def test_length(self):
        self.assertTrue(0<=len(obstacles.list_obstacle)<=10)

    def test_is_position_blocked_incorrect(self):
        x= 100
        y= 250
        for i in range(1000):
            self.assertEqual(obstacles.is_position_blocked(x,y),False)

    def test_is_path_blocked_incorrect(self):
        x1= 0
        y1= 45
        x2= 100 
        y2= 250
        
        for i in range(10):
            self.assertEqual(obstacles.is_path_blocked(x1,y1,x2,y2),False)

