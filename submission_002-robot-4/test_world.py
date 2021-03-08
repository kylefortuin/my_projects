
import unittest 
import world.text.world as w
class Third_test(unittest.TestCase):

    #show position
    def test_show_posi(self):
        w.position_x = 2
        w.position_y = 0
        self.assertEqual(w.show_position("BRUCE"),' > BRUCE now at position (2,0).')
    
    #is_position allowed
    def test_is_position_allowed(self):
        self.assertEqual(w.is_position_allowed(12,34),True)
    def test_position_is_not_allowed(self):
        self.assertEqual(w.is_position_allowed(250,56),False)    
        
    #update_position
    def test_update_position(self):
        steps = 1
        self.assertEqual(w.update_position(steps),True)
    def test_update_position_false(self):
        steps = 500
        self.assertEqual(w.update_position(steps),False)
    
    #do_forward 
    def test_do_forward(self):
        output1 = True,' > BRUCE moved forward by 1 steps.'
        self.assertEqual(w.do_forward("BRUCE",1),output1)
    def test_dont_do_forward(self):
        w.position_x = 0
        w.position_y = 0
        output2 = True,'BRUCE: Sorry, I cannot go outside my safe zone.'
        self.assertEqual(w.do_forward("BRUCE",240),output2)
        
    #do_back
    def test_do_back(self):
        output3 = True,' > BRUCE moved back by 1 steps.'
        self.assertEqual(w.do_back("BRUCE",1),output3)
    def test_dont_do_back(self):
        w.position_x = 0
        w.position_y = 0
        output4 = True,'BRUCE: Sorry, I cannot go outside my safe zone.'
        self.assertEqual(w.do_back("BRUCE",240),output4)
    
    ##do left turn
    def test_do_left_turn(self):
        output5 = True, ' > RON turned left.'
        self.assertEqual(w.do_left_turn("RON"),output5)
    #do right turn
    def test_do_right_turn(self):
        output5 = True, ' > RON turned right.'
        self.assertEqual(w.do_right_turn("RON"),output5)
        
    #do sprint
    def test_do_sprint_one(self):
        w.position_x = 0
        w.position_y = 0
        robot_name = "KYLE"
        steps = 1
        output = w.do_forward(robot_name, 1)
        self.assertEqual(w.do_sprint(robot_name, steps),output)
    
    def test_do_sprint_(self):
        w.position_x = 0
        w.position_y = 0
        robot_name = "KYLE"
        steps = 4
        output = w.do_sprint(robot_name, steps - 1)
        self.assertEqual(w.do_sprint(robot_name, steps),output)