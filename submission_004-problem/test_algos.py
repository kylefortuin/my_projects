import unittest #import unittest module
from super_algos import find_min,sum_all,find_possible_strings #import the function/s that you want to test

class Test_case(unittest.TestCase):
    #tests for find_min()
    
    
    def test_FM_empty_list(self):
        self.assertEqual(find_min([]),-1)#check empty list
    def test_FM_negative_number(self):
        self.assertEqual(find_min([1,2,3,-4]),-4)#check negative elements
    def test_FM_non_int(self):
        self.assertEqual(find_min([1,"2",3,4]),-1)#check non-integer
    def test_FM_one_item(self):
        self.assertEqual(find_min([1]),1)#check one item in list
    def test_FM_correct(self):
        self.assertEqual(find_min([1,2,3,4]),1)#check correct output
    #tests for sum_all()
    
    
    def test_SA_empty_list(self):
        self.assertEqual(sum_all([]),-1)
    def test_SA_non_int(self):        
        self.assertEqual(sum_all(["1",2]),-1)
    def test_SA_single_item(self):    
        self.assertEqual(sum_all([1]),1)
    def test_SA_neg(self):        
        self.assertEqual(sum_all([-1,-1]),-2)
    def test_SA_correct(self):        
        self.assertEqual(sum_all([1,1]),2)
    #tests for find_possible_strings


    def test_empty_list_FPS(self):
        self.assertEqual(find_possible_strings([],4),[])
    def test_non_valid_FPS(self):
        self.assertEqual(find_possible_strings(["1",2,"3"],2),[])
    def test_only_one_FPS(self):
        self.assertEqual(find_possible_strings(['a','b'],1),['a','b'])
    def test_correct_FPS(self):
        self.assertEqual(find_possible_strings(['a','b'],2),['aa','ab','ba','bb'])
    def test_neg_FPS(self):
        self.assertEqual(find_possible_strings(['a','b'],-1),[])
    def test_none_FPS(self):
        self.assertEqual(find_possible_strings(['a','b'],0),[""])
    