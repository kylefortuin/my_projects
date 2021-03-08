
import unittest 
from unittest.mock import patch
from io import StringIO
#from robot import get_robot_name,get_command, output,split_command_input,is_val,is_int,valid_command,do_help,show_position,is_position_allowed,update_position,do_forward,do_back,do_left_turn,do_right_turn,do_sprint,replay,replay_range,replay_reversed,replay_silent,handle_command
import robot as r
class Third_test(unittest.TestCase):
    
    #name_robot 
    @patch("sys.stdin", StringIO("BRUCE\n")) 
    def test_name_robot(self): 
        self.assertEqual(r.get_robot_name(), "BRUCE") 
    
    #get_command
    @patch("sys.stdin", StringIO("help\n"))
    def test_get_command(self):
        self.assertEqual(r.get_command('BRUCE'),"help") 
        
    @patch("sys.stdin", StringIO("FoRwaRd 13\n")) 
    def test_camel_get_command(self):    
        self.assertEqual(r.get_command('BRUCE'),"forward 13") 
    @patch("sys.stdin", StringIO("LEFT\n")) 
    def test_caps_get_command(self):    
        self.assertEqual(r.get_command('BRUCE'),"left") 
    #split command
    def test_split_command_input(self):
        command = "left"
        self.assertEqual(r.split_command_input(command),("left",''))
    
    def test_split_command_input(self):
        command = "forward 13"
        self.assertEqual(r.split_command_input(command),('forward','13'))
    

    
    #is_int
    def test_is_int_correct(self):
        value = "1"
        self.assertEqual(r.is_int(value),True)
    def test_is_int_False(self):
        value = 'word'
        self.assertEqual(r.is_int(value),False)
    def test_is_int_correct_multiple(self):
        value = "34"
        self.assertEqual(r.is_int(value),True)    
    def test_is_int_empty(self):
        value = ""
        self.assertEqual(r.is_int(value),False)
        
    #valid command

    def test_valid_command_correct(self):
        command = "forward 5"
        self.assertEqual(r.valid_command(command),True)

    def test_valid_command_inrrect_order(self):
        command = "10 forward"
        self.assertEqual(r.valid_command(command),False)
    
    def test_valid_command_incorrect_argument(self):
        command = "forward a"
        self.assertEqual(r.valid_command(command),False)

    def test_valid_command_incorrect(self):
        command = "fkemrf"
        self.assertEqual(r.valid_command(command),False)
    #do help
    def test_do_help(self):
        help =  """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
"""

        self.assertEqual(r.do_help(),(True,help))


    #handle command
    def test_handle_command(self):
        robot_name = "KYLE"
        command = "left"
        do_next = True
        self.assertEqual(r.handle_command(robot_name, command),do_next)
