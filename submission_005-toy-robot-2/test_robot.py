import unittest 
from unittest.mock import patch
from io import StringIO
from robot import name_robot,command_input,command_true,handle_help,handle_forward,handle_back,forward_print,back_print,right_print,left_print,posi
class Third_test(unittest.TestCase): 
    #name_robot 
    @patch("sys.stdin", StringIO("Bruce\n")) 
    def test_name_robot(self): 
        self.assertEqual(name_robot(), "Bruce") 
    #command_input
    @patch("sys.stdin", StringIO("off\n")) 
    def test_command_input(self): 
        #name = "kyle"
        #co = [0,0]
        #right = [0]
        #left = [0]
        self.assertEqual(command_input("kyle",[0,0],[0],[0]), "off")
    #posi
    def test_posif(self):
        self.assertEqual(posi('forward',"kyle",10,0,[0,0],[0],[0]),[0,10])
    #command_True
    def test_in_list(self): 
        self.assertEqual(command_true("off"),False)
    def test_case_sensitive(self): 
        self.assertEqual(command_true("OfF"),False) 
    def test_not_in_list(self): 
        self.assertEqual(command_true("Nuke them"),True) 

    #handle_help
    def test_handle_help(self): 
        self.assertEqual(handle_help('help'),True) 
    def test_handle_not_help(self): 
        self.assertEqual(handle_help('not_help'),False) 
    #handle_forward 
    def test_handle_f(self): 
        self.assertEqual(handle_forward('forward'),True) 
    def test_handle_n_f(self): 
        self.assertEqual(handle_forward("not_forward"),False)
    #handle_back
    def test_handle_back(self): 
        self.assertEqual(handle_back('back'),True) 
    def test_handle_not_back(self): 
        self.assertEqual(handle_back('not_back'),False) 
    #forward_print
    def test_forward_print(self):
        self.assertEqual(forward_print(True,'forward 15',"kyle",[0,0],[0],[0]),15)
    def test_not_forward_print(self):
        self.assertEqual(forward_print(False,'forward 15',"kyle",[0,0],[0],[0]),None)  
    #back_print
    def test_back_print(self):
        self.assertEqual(back_print(True,'back 15',"kyle",[0,0],[0],[0]),15)
    def test_not_forward_print(self):
        self.assertEqual(back_print(False,'back 15',"kyle",[0,0],[0],[0]),None)      
    
    #righr_print
    def test_right(self): 
        self.assertEqual(right_print("kyle",[0,0],[2]),[3]) 
    #left_print
    def test_L(self): 
        self.assertEqual(left_print("kyle",[0,0],[0]),[1]) 

'''
    def test_in_list(self): 
        self.assertEqual(command_true("off"),False) 

    def test_case_sensitive(self): 
        self.assertEqual(command_true("OfF"),False) 
    def test_not_in_list(self): 
        self.assertEqual(command_true("Nuke them"),True) 
    #handle_help tests 
    def test_handle_help(self): 
        self.assertEqual(handle_help('help'),True) 
    def test_handle_not_help(self): 
        self.assertEqual(handle_help('not_help'),False) 
    #handle_forward tests 
    def test_handle_f(self): 
        self.assertEqual(handle_forward('forward'),True) 

    def test_handle_n_f(self): 
        self.assertEqual(handle_forward("not_forward"),False) #right print 
    def test_right(self): 
        self.assertEqual(right_print("kyle",[0,0],[0]),[1]) 
    def test_L(self): 
        self.assertEqual(left_print("kyle",[0,0],[0]),[1]) 
'''
    