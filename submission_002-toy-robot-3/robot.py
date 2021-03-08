"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 2 exercise.
"""
#string of 
num = '1234567890' 

#range list
range = []

#list that will store history
history = []

# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint','replay','replay silent','replay reversed']

# flag variables
flag1 = False
flag2 = False
flag3 = False

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
        #history.clear()
    return name.upper()


def get_command(robot_name):
    #global history
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    
    command = input(prompt)
    
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_val(value):
    """
    checks for the validity of arguments entered with the replay command
    global variable: num
    Args:
        value (string): value can be silent, reversed or a number from 0-9
    Returns:
        boolean: returns true if the arguemnt/s contain the acceptable strings only
    """
    
    r = 0
    value = value.lower()
    valsplit = value.split()
    if value == 'silent' or value == 'reversed':
        return True
    
    elif len(valsplit) > 1 or len(valsplit) == 1:
        for i in valsplit:
            if ('silent' in valsplit and i in num )or ('reversed' in valsplit) and i in num and "-" in valsplit:
                return True
            elif i in num:
                return True
        for i in valsplit[0]:
            if i == "-":
                r+=1
            if i in num and r == 1:
                return True
    if 'silent' in value.split() and "reversed" in value.split():
        return True
    else:
        return False

def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False
    

def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """

    (command_name, arg1) = split_command_input(command)
    history_add(command)

    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1) or is_val(arg1))


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
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


def show_position(robot_name):
    posi = ' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').'
    return (posi)


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    
    if update_position(steps):
        return True,' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    (command_name, arg) = split_command_input(command)
    c = command.split()


    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif command_name == 'replay':
        check(arg)
        if (flag1 and flag2) or flag2:
            (do_next,command_output) = replay_reversed(history,robot_name,flag1,arg)
        elif flag1:
            (do_next,command_output) = replay_silent(history,robot_name,arg)
        elif flag3:
            (do_next,command_output) = replay(history,robot_name,arg,flag3)
        else:
            (do_next, command_output) = replay(history,robot_name,arg,flag3)
            
    print(command_output)
    print(show_position(robot_name))
    return do_next


def replay_range(history,arg):
    """uses the numeric paramters to slice the history list to be used by other replay functions

    Args:
        history (list): [list of valid commands entered by user]
        arg (string): [argument of the replay command]
    """
    global range
    r = 0
    ran = []
    ext = arg.split()
    if len(ext) > 1:
        ran = [int(i) for i in ext if i != 'silent' and i != 'reversed' and i in num]
        
    elif len(ext) == 1:
        arg =ext[0].replace("-","")
        ran = [int(i) for i in ext[0] if i in num]
        
    if len(ran) == 1:
        a = ran[0]
        range = history[-a:]
    if len(ran) == 2:
        a = ran[0]
        b = ran[1]
        range = history[-a:-b] 
    
    

def check(arg):
    """changes boolean value of flag variables based on the second index(arg) of the split command,
        it sets the values to True if the condition is met otherwise it remains False

    global varaibles: flag1,flag2,flag3
    
    Args:
        arg (string): arguemnt of the replay command
    """
    
    global flag1
    global flag2
    global flag3
    
    flag1 = False
    flag2 = False    
    flag3 = False
    if 'silent' in arg.split() and 'reversed' in arg.split():
        flag1 = True
        flag2 = True
    elif arg == 'silent':
        flag1 = True
    elif arg == 'reversed':
        flag2 = True
    elif 'reversed' in arg.split() and arg != "":
        flag2 = True
        flag3 = True
    elif 'silent' in arg.split() and arg != "":
        flag1 = True
        flag3 = True
    elif arg != "":
        flag3 = True
    
        
        
def history_add(command):
    """appends commands to a list
    gloabl variable: history
    
    Args:
        command (string): valid command entered by the user
    """
    
    global history
    history.append(command)
    

def replay(history,robot_name,arg,flag3):
    """Filters out all non-movement commands and provides only the movement commands along with the full output.

    Args:
        history (list): list of valid commands enterede by user 
        robot_name (str): name entered by user for robot 
        arg (str): arguement of replay command
        flag3 (bool): is True if at least a number between 0-9 is present 

    Returns:
        (True,replay output text)
    """
    
    history = list(filter(lambda item: 'replay' not in item,history))
    history = list(filter(lambda item: 'REPLAY' not in item,history))
    history = list(filter(lambda item:'help' not in item,history))
    if flag3:
        #print(type(arg))
        replay_range(history,arg)
        i = 0
        while i < len(range):
            for a in range:
                handle_command(robot_name,a)
                i+=1
        return True, ' > '+robot_name+' replayed '+str(len(range))+' commands.'
    
    else:
        i = 0
        while i < len(history):
            for a in history:
                handle_command(robot_name,a)
                i+=1
        return True, ' > '+robot_name+' replayed '+str(len(history))+' commands.'
    
    
def replay_silent(history,robot_name,arg):
    """  provides only the movement commands along without the full output text.

    Args:
        history (list): list of valid commands enterede by user 
        robot_name (str): name entered by user for robot 
        arg (str): arguement of replay command

    Returns:
            (True,replay silent output text)
    """
    
    history = list(filter(lambda item: 'replay'not in item,history))
    history = list(filter(lambda item:'help' not in item,history))
    history = list(filter(lambda item:'replay silent' not in item,history))
    history = list(filter(lambda item: 'REPLAY' not in item,history))
    if flag3:
        replay_range(history,arg)
        i = 0
        while i < len(range):
            for a in range:
                a = a.split()
                if len(a) == 1:#this is to check for single value commands after split
                    if a[0] == 'right':#right
                        do_right_turn(robot_name)
                    elif a[0] == 'left':#left
                        do_left_turn(robot_name)
                elif len(a) > 1:#this is to check for double valued commands after split
                    steps = a[1]
                    steps = int(steps)
                    if a[0] == 'forward':#forward
                        do_forward(robot_name, steps)
                    elif a[0] == 'back':#back
                        do_back(robot_name, steps)
            i+=len(range) +1
        return True, ' > '+robot_name+' replayed '+str(len(range))+' commands silently.'
        
    else:
        i = 0
        while i < len(history):
            for a in history:
                a = a.split()
                if len(a) == 1:#this is to check for single value commands after split
                    if a[0] == 'right':#right
                        do_right_turn(robot_name)
                    elif a[0] == 'left':#left
                        do_left_turn(robot_name)
                elif len(a) > 1:#this is to check for double valued commands after split
                    steps = a[1]
                    steps = int(steps)
                    if a[0] == 'forward':#forward
                        do_forward(robot_name, steps)
                    elif a[0] == 'back':#back
                        do_back(robot_name, steps)
            i+=len(history) +1
        return True, ' > '+robot_name+' replayed '+str(len(history))+' commands silently.'


def replay_reversed(history,robot_name,flag1,arg):
    """
    arranges the order of the history list in reverse and provides the movement commands along with the full output
    Args:
        history (list): list of valid commands enterede by user 
        robot_name (str): name entered by user for robot 
        flag1 (bool): is True if argument contains the string silent
        arg (str): arguement of replay command

    Returns:
        True,replay_reversed output text
    """
    
    history = list(filter(lambda item: 'replay' not in item,history))
    history = list(filter(lambda item:'help' not in item,history))
        
        
    if flag1:
        
        h = reversed(history)
        history = []
        history = [item for item in h]
        i = 0
        while i < len(history):
            for a in history:
                a = a.split()
                if len(a) == 1:#this is to check for single value commands after split
                    if a[0] == 'right':#right
                        do_right_turn(robot_name)
                    elif a[0] == 'left':#left
                        do_left_turn(robot_name)
                elif len(a) > 1:#this is to check for double valued commands after split
                    steps = a[1]
                    steps = int(steps)
                    if a[0] == 'forward':#forward
                        do_forward(robot_name, steps)
                    elif a[0] == 'back':#back
                        do_back(robot_name, steps)
            i+=len(history)+1
        #replay_silent(history,robot_name)
        return True, ' > '+robot_name+' replayed '+str(len(history))+' commands in reverse silently.'
    
    elif flag3:
        
        hr = reversed(history)
        history = [item for item in hr]
        replay_range(history,arg)
        
        i = 0
        while i < len(range):
            for a in range:
                handle_command(robot_name,a)
                i+=1
        
        
        return True, ' > '+robot_name+' replayed '+str(len(range))+' commands in reverse.'
        
    else:
        h = reversed(history)
        hr = [item for item in h]

        i = 0
        while i < len(hr):
            for a in hr:
                handle_command(robot_name,a)
                i+=1

        return True, ' > '+robot_name+' replayed '+str(len(history))+' commands in reverse.'



def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")
    history.clear()
    
    position_x = 0
    position_y = 0
    current_direction_index = 0


    command = get_command(robot_name)
    while handle_command(robot_name, command):
        command = get_command(robot_name)
    
    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()

