
def robot_start():
    """This is the entry function, do not change"""
    co = [0,0]
    right = [0]
    left = [0]
    name = name_robot()
    command = command_input(name,co,right,left)
    logic(name,command,co,right,left)
 
def name_robot():
    name = input("What do you want to name your robot? ")
    
    print(f"{name}: Hello kiddo!")

    return name

def command_input(name,co,right,left):
    while True:

        command = input(f"{name}: What must I do next? ").lower()
        
        parsed = []
        parsed = command.split()
        if command == "":
            print(f"{name}: Sorry, I did not understand '{command.capitalize()}.'.")
            continue
        elif parsed[0] == "forward":
            if lim_on_y(name,co,command,right,left):     #check y 
                continue
            elif lim_on_x(name,co,command,right,left):#check x
                continue
            logic(name,command,co,right,left)
        
        elif parsed[0] == "sprint":
            if lim_on_y(name,co,command,right,left):     #check y 
                continue
            elif lim_on_x(name,co,command,right,left):#check x
                continue
            logic(name,command,co,right,left)
        elif parsed[0] == "back":
            logic(name,command,co,right,left)
        
        elif command_true(command):
            print(f"{name}: Sorry, I did not understand '{command.capitalize()}'.")
            continue
        elif command == "off":
            print(f"{name}: Shutting down..")
            break
        else:
            logic(name,command,co,right,left)
    return command
    
def command_true(command):
    list_0_commands = ['off','help',"forward","back","right",'left','sprint']
    split = command.split()
    #if command.lower() not in list_0_commands:
    #    return True
    if split[0].lower() not in list_0_commands:
       return True
    else:
        return False
        
def handle_help(command):
    if command == 'help':
        correct = True
        return correct
    else:
        correct = False
        return correct

def help_real(correct):

    if correct == True:
        off = "OFF  - Shut down robot"
        helpme = "HELP - provide information about commands"
        forward = "FORWARD - moves robot forward by number of steps entered"
        back = "BACK - moves robot back by number of steps entered"
        right = "turns robot to the right"
        left = "turns robot to the left"
        print(f"I can understand these commands:\n{off}\n{helpme}\n{forward}\n{back}\n{right}\n{left}\n")

        
def handle_forward(command):
    parse = []
    parse = command.split()

    if parse[0] == 'forward':
        correc = True
        return correc
 
    else:
        correc = False
        return correc

def handle_back(command):
    parse = []
    parse = command.split()

    if parse[0] == 'back':
        c2 = True
        return c2
    else:
        c2 = False
        return c2

def back_print(c2,command,name,co,right,left):
    if c2 == True:
        p2 = []
        p2 = command.split()
        stepsb = int(p2[1])
    
        print(f" > {name} moved back by {stepsb} steps.")
       
        return stepsb


def forward_print(correc,command,name,co,right,left):
 
    p = []
    p = command.split()
    stepsf = int(p[1])
    if correc == True:
        print(f" > {name} moved forward by {stepsf} steps.")
        return stepsf

def output(name,co):

    co = str(co).replace("[","(").replace("]",")").replace(" ","")
    print(f" > {name} now at position {co}.")

def right_print(name,co,right):
    if right[0] <=3:
        right[0] += 1
    print(f" > {name} turned right.")
    output(name,co)
    return right


def left_print(name,co,left):
    if left[0] <=3:
        left[0] += 1
    print(f" > {name} turned left.")
    output(name,co)
    return left

def posi(command,name,stepsf,stepsb,co,right,left):
    p3 = []
    p3 = command.split()
    
    if p3[0] == 'forward':
        if right[0] == left[0]:
            co[1] += stepsf
            output(name,co)
        elif right[0]-left[0] == 2 or left[0] - right[0] == 2:
            co[1] -= stepsf
            output(name,co)
        elif (right[0] == 1 and left[0] == 0) or (left[0] == 3 and right[0] == 0) or right[0] - left[0] == 1:
            co[0] += stepsf
            output(name,co)
        elif (right[0] == 0 and left[0] == 1) or (left[0] == 0 and right[0] == 3) or left[0] - right[0] == 1:
            co[0] -= stepsf
            output(name,co)
    
  
    
    elif p3[0] == 'back':
        if right[0] == left[0]:
            co[1] -= stepsb
            output(name,co)
        elif right[0]-left[0] == 2 or left[0] - right[0] == 2:
            co[1] += stepsb
            output(name,co)
        elif (right[0] == 1 and left[0] == 0) or (left[0] == 3 and right[0] == 0) or right[0] - left[0] == 1:
            co[0] -= stepsb
            output(name,co)
        elif (right[0] == 0 and left[0] == 1) or (left[0] == 0 and right[0] == 3) or left[0] - right[0] == 1:
            co[0] += stepsb
            output(name,co)
    
    return co

def lim_on_y(name,co,command,right,left):
    pp = command.split() 
    a = int(pp[1])
    if right[0] == left[0] and a >= 200 or a < -200 or co[1] >= 200:#forward
        co[1] += 0
        co = str(co).replace("[","(").replace("]",")").replace(" ","")
        print(f"{name}: Sorry, I cannot go outside my safe zone.\n > {name} now at position {co}.")
        return True
    else:
        return False

def lim_on_x(name,co,command,right,left):
    px = command.split()
    b = int(px[1])
    if ((right[0] == 1 and left[0] == 0) and  b >= 100 or b < -100 or co[0] >= 100):#right
        co[0] += 0
        co = str(co).replace("[","(").replace("]",")").replace(" ","")
        print(f"{name}: Sorry, I cannot go outside my safe zone.\n > {name} now at position {co}.")
        return True
    elif ((right[0] == 0 and left[0] == 1) and  b >= 100 or b < -100 or co[0] >= 100):#left
        co[0] += 0
        co = str(co).replace("[","(").replace("]",")").replace(" ","")
        print(f"{name}: Sorry, I cannot go outside my safe zone.\n > {name} now at position {co}.")
        return True
    else:
        return False

def sprinter(name,run,co,right,sprinting,left):
    #if len(sprinting) == 0:
        
    #    return co[1]

    if len(sprinting) > 0:
        if right[0] == left[0]:
            co[1] +=sprinting[0]
            print(f" > {name} moved forward by {len(sprinting)} steps.")
            sprinting.remove(sprinting[0]) 
            return sprinter(name,run,co,right,sprinting,left)
        
        elif right[0]-left[0] == 2 or left[0] - right[0] == 2:
            co[1] -= sprinting[0]
            print(f" > {name} moved forward by {len(sprinting)} steps.")
            sprinting.remove(sprinting[0]) 
            return sprinter(name,run,co,right,sprinting,left)
        
        elif (right[0] == 1 and left[0] == 0) or (left[0] == 3 and right[0] == 0) or right[0] - left[0] == 1:
            co[0] += sprinting[0]
            print(f" > {name} moved forward by {len(sprinting)} steps.")
            sprinting.remove(sprinting[0]) 
            return sprinter(name,run,co,right,sprinting,left)
        elif (right[0] == 0 and left[0] == 1) or (left[0] == 0 and right[0] == 3) or left[0] - right[0] == 1:
            co[0] -= sprinting[0]
            print(f" > {name} moved forward by {len(sprinting)} steps.")
            sprinting.remove(sprinting[0]) 
            return sprinter(name,run,co,right,sprinting,left)

    else:
        output(name,co)

def logic(name,command,co,right,left):
#help command
    correc = handle_forward(command)
    c2 = handle_back(command)
    correct = handle_help(command)
    L = command.split()
    
    if handle_help(command):
        help_real(correct)
    elif command == 'right':
        right_print(name,co,right)
        if right[0] > 3:
            right[0] = 0
    elif command == 'left':
        left_print(name,co,left)
        if left[0] > 3:
            left[0] = 0
    elif handle_forward(command):
        stepsf = forward_print(correc,command,name,co,right,left)
        stepsb = back_print(c2,command,name,co,right,left)
        posi(command,name,stepsf,stepsb,co,right,left)
    elif L[0] == 'sprint':
        run = int(L[1])
        sprinting = []
        for i in range(1,run+1):
            sprinting.append(i)
        sprinter(name,run,co,right,sprinting,left)

    elif handle_back(command):
        stepsf = forward_print(correc,command,name,co,right,left)
        stepsb = back_print(c2,command,name,co,right,left)
    
        posi(command,name,stepsf,stepsb,co,right,left)

if __name__ == "__main__":
    robot_start()
    

