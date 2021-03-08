import unittest #import unittest module
from unittest.mock import patch
from io import StringIO 
from mastermind import create_code,check_correctness,get_user_input,take_turn #import the function/s that you want to test


class First_test(unittest.TestCase):#create class
    
    def test_create_code(self): #define test case that tests imported function 
        code = create_code()
        for test_amount in range(100):   #test function 100 times
            self.assertIs(type(code),list)
            self.assertEqual(len(code),4)
            for digit in range (4):
                self.assertTrue(0 < code[digit] <= 8)

    def test_check_correctness(self):
       
        self.assertEqual(check_correctness(12,True,4),True)
        self.assertEqual(check_correctness(12,False,1),False)
        
  
    @patch("sys.stdin", StringIO("1234\n5678\n"))
    def test_compare(self):
        answer = get_user_input()
        if len(get_user_input()) != 4:
            self.assertEqual(get_user_input(), "1234")
            self.assertEqual(get_user_input(), "5678")
    
    def test_take_turn(self):
        self.assertEqual(take_turn([2,3,4,5],[2,3,4,5]),(4,0))
        self.assertEqual(take_turn([2,3,4,5],[6,2,8,3]),(0,2))
        self.assertEqual(take_turn([2,3,4,5],[1,3,6,5]),(2,0))




if __name__ == '__main__':
    unittest.main()