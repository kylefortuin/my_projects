import unittest 
from unittest.mock import patch
from io import StringIO
from robot import get_robot_name,get_command, output,split_command_input,is_val,is_int,valid_command,do_help,show_position,is_position_allowed,update_position,do_forward,do_back,do_left_turn,do_right_turn,do_sprint,replay,replay_range,replay_reversed,replay_silent,handle_command
import robot
class Third_test(unittest.TestCase):
    
    #name_robot 
    @patch("sys.stdin", StringIO("Bruce\n")) 
    def test_name_robot(self): 
        self.assertEqual(get_robot_name(), "BRUCE") 
    
    #get_command
    @patch("sys.stdin", StringIO("help\n"))
    def test_get_command(self):
        self.assertEqual(get_command('BRUCE'),"help") 
        
    @patch("sys.stdin", StringIO("FoRwaRd 13\n")) 
    def test_camel_get_command(self):    
        self.assertEqual(get_command('BRUCE'),"forward 13") 
    @patch("sys.stdin", StringIO("LEFT\n")) 
    def test_caps_get_command(self):    
        self.assertEqual(get_command('BRUCE'),"left") 
    #split command
    def test_split_command_input(self):
        command = "left"
        self.assertEqual(split_command_input(command),("left",''))
    
    def test_split_command_input(self):
        command = "forward 13"
        self.assertEqual(split_command_input(command),('forward','13'))
    
    #is_val
    def test_is_val_sil(self):
        value = "silent"
        self.assertEqual(is_val(value),True)
    def test_is_val_rev(self):
        value = 'reversed'
        self.assertEqual(is_val(value),True)
    def test_is_val_sil_one_num(self):
        value = "silent 4"
        self.assertEqual(is_val(value),True)
    def test_is_val_sil_two_num(self):
        value = "5-4 silent"
        self.assertEqual(is_val(value),True)
    def test_is_val_silent_reversed(self):
        value = "silent reversed"
        self.assertEqual(is_val(value),True)
    def test_is_val_extra_stroke(self):
        value = "5--4 silent"
        self.assertEqual(is_val(value),False)
    def test_is_val_random(self):
        value = "random"
        self.assertEqual(is_val(value),False)
    
    #is_int
    def test_is_int_correct(self):
        value = "1"
        self.assertEqual(is_int(value),True)
    def test_is_int_False(self):
        value = 'word'
        self.assertEqual(is_int(value),False)
    def test_is_int_correct_multiple(self):
        value = "34"
        self.assertEqual(is_int(value),True)    
    def test_is_int_empty(self):
        value = ""
        self.assertEqual(is_int(value),False)
        
    #valid command

    def test_valid_command_correct(self):
        command = "forward 5"
        self.assertEqual(valid_command(command),True)

    def test_valid_command_inrrect_order(self):
        command = "10 forward"
        self.assertEqual(valid_command(command),False)
    
    def test_valid_command_incorrect_argument(self):
        command = "forward a"
        self.assertEqual(valid_command(command),False)

    def test_valid_command_incorrect(self):
        command = "fkemrf"
        self.assertEqual(valid_command(command),False)
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
REPLAY - replays previous movement commands with full output.
REPLAY SILENT - replays movement commands showing just the results in the position changes.
REPLAY REVERSED - replays the historic commands in reverse order.
"""
        self.assertEqual(do_help(),(True,help))
        
    #show position
    def test_show_posi(self):
        robot.position_x = -55
        robot.position_y = 0
        self.assertEqual(show_position("BRUCE"),' > BRUCE now at position (-55,0).')
    #is_position allowed
    def test_is_position_allowed(self):
        self.assertEqual(is_position_allowed(12,34),True)
    def test_position_is_not_allowed(self):
        self.assertEqual(is_position_allowed(250,56),False)    
        
    #update_position
    def test_update_position(self):
        steps = 1
        self.assertEqual(update_position(steps),True)
    def test_update_position_false(self):
        steps = 500
        self.assertEqual(update_position(steps),False)
    
    #do_forward 
    def test_do_forward(self):
        output1 = True,' > BRUCE moved forward by 1 steps.'
        self.assertEqual(do_forward("BRUCE",1),output1)
    def test_dont_do_forward(self):
        robot.position_x = 0
        robot.position_y = 0
        output2 = True,'BRUCE: Sorry, I cannot go outside my safe zone.'
        self.assertEqual(do_forward("BRUCE",240),output2)
        
    #do_back
    def test_do_back(self):
        output3 = True,' > BRUCE moved back by 1 steps.'
        self.assertEqual(do_back("BRUCE",1),output3)
    def test_dont_do_back(self):
        robot.position_x = 0
        robot.position_y = 0
        output4 = True,'BRUCE: Sorry, I cannot go outside my safe zone.'
        self.assertEqual(do_back("BRUCE",240),output4)
    
    ##do left turn
    def test_do_left_turn(self):
        output5 = True, ' > RON turned left.'
        self.assertEqual(do_left_turn("RON"),output5)
    #do right turn
    def test_do_right_turn(self):
        output5 = True, ' > RON turned right.'
        self.assertEqual(do_right_turn("RON"),output5)
    #do sprint
    def test_do_sprint_one(self):
        robot.position_x = 0
        robot.position_y = 0
        robot_name = "KYLE"
        steps = 1
        output = do_forward(robot_name, 1)
        self.assertEqual(do_sprint(robot_name, steps),output)
    
    def test_do_sprint_(self):
        robot.position_x = 0
        robot.position_y = 0
        robot_name = "KYLE"
        steps = 4
        output = do_sprint(robot_name, steps - 1)
        self.assertEqual(do_sprint(robot_name, steps),output)

    #handle command
    def test_handle_command(self):
        robot_name = "KYLE"
        command = "left"
        do_next = True
        self.assertEqual(handle_command(robot_name, command),do_next)

    
    #replay range
    def test_replay(self):
        history = ['forward 10']
        robot_name = 'KYLE'
        arg = ""
        flag3 = False
        put =  True, ' > KYLE replayed 1 commands.'
        self.assertEqual(replay(history,robot_name,arg,flag3),put)
    
    def test_empty_replay(self):
        history = ''
        robot_name = 'KYLE'
        arg = ""
        flag3 = False
        put =  True, ' > KYLE replayed 0 commands.'
        self.assertEqual(replay(history,robot_name,arg,flag3),put)

    def test_replay_flag3(self):
        history = ['forward 10']
        robot_name = 'KYLE'
        arg = "1"
        flag3 = True
        put =  True, ' > KYLE replayed 1 commands.'
        self.assertEqual(replay(history,robot_name,arg,flag3),put)
    #replay silent 
    def test_replay_silent(self):
        history = ["forward 5"]
        robot_name = "KYLE"
        arg = ""
        text = True, ' > KYLE replayed 1 commands silently.'
        self.assertEqual(replay_silent(history,robot_name,arg),text)
    
    def test_replay_silent_range(self):
        history = ["forward 5"]
        robot_name = "KYLE"
        arg = "1"
        flag3 = True
        text = True, ' > KYLE replayed 1 commands silently.'
        self.assertEqual(replay_silent(history,robot_name,arg),text)

    #replay reveresed
    def test_replay_reversed(self):
        text = True, ' > KYLE replayed 1 commands in reverse.'
        self.assertEqual(replay_reversed("forward 2","KYLE",False,""),text)
    
    def test_replay_reversed_silent(self):
        text = True, ' > KYLE replayed 9 commands in reverse silently.'
        self.assertEqual(replay_reversed("forward 2","KYLE",True,""),text)
        
    