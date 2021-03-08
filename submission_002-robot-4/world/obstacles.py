import random
from world import obstacles

#global
list_obstacle = []

def create_ob():
    """randomly generates a random number(up to 10) of obstacles 

    Returns:
        list: contains starting point/s of the obstacle/s
    """
    global list_obstacle
    x = 0
    y = 0
    co_s = []
    number_of_obstacles = random.randint(1,10)
    for i in range(number_of_obstacles):
        x = random.randint(-100,100)
        y = random.randint(-200,200)
        co = (x,y) 
        co_s.append(co)
    
    list_obstacle = []
    for i in co_s: 
        obs = i
        
        obs_1 = (obs[0],obs[1])
        obs_2 = (obs[0]+4,obs[1])
        obs_3 = (obs[0]+4,obs[1]+4)
        obs_4 = (obs[0],obs[1]+4)
        obstacle = [obs_1,obs_2,obs_3,obs_4]
        list_obstacle.append(obstacle)
        #print(len(list_obstacle))
    return list_obstacle


def get_obstacle():
    """fully creates all co-ordinates of each obstiacle and returns a list of them

    Args:
        co_s (list):  contains starting point/s of the obstacle/s

    Returns:
        list_obstacles: a list containing full co-ordinates of obstacles
    """
    global list_obstacle

    if len(list_obstacle) == 0:
        list_obstacle = create_ob()
    return list_obstacle


def print_ob():
    """prints the posiion of obstacles generated
    """
    list_obstacle = get_obstacle()
    if list_obstacle:
        print('There are some obstacles:')
        j = 0
        for i in list_obstacle:
            obs_1 = str(list_obstacle[j][0])
            obs_4 = str(list_obstacle[j][2])
            print("- At position "+obs_1.replace(' ','').replace('(','').replace(')'," ") +obs_4.replace(" ","").replace('(',"(to "))
            j+=1


def is_position_blocked(x,y):
    """returns True if there is an obstacle at the position the robot wants to move to

    Args:
        x (int): new possible x co-ordinate
        y (int): new possible y co-ordinate


    Returns:
        booolean: True is the new position is blocked by obstacle ,False if not 
    """
    r = 0
    emp = []
    for i in list_obstacle:
        
        holder = list_obstacle[r][0]
        print(holder)
        r+=1
        minn_x = holder[0]
        maxx_x = holder[0]+4
        minn_y = holder[1]
        maxx_y = holder[1]+4
        
        a  = False
        if minn_x <= x <= maxx_x and minn_y <= y <= maxx_y:
            a = True
        emp.append(a)    
    if True in emp:
        return True
    else:
        return False    


def is_path_blocked(x1,y1, x2, y2):
    """returns True if there is an obstacle in the line between the previous and new coordinates

    Args:
        x1 (int): previous x co-ordinate
        y1 (int): previous y co-ordinate
        x2 (int): new possible x co-ordinate
        y2 (int): new possible y co-ordinate

    Returns:
        booolean: True is the path is blocked by obstacle ,False if not 
        
    """
    r = 0
    emp = []
    for i in list_obstacle:

        holder2 = list_obstacle[r][0]
        r += 1
        minn_x = holder2[0]
        maxx_x = holder2[0]+4
        minn_y = holder2[1]
        maxx_y = holder2[1]+4
        
        b  = False
        if minn_y <y1<maxx_y and y1 == y2 and x1<minn_x<x2 and x1<maxx_x<x2 and x1 != x2:#move across object x axis
            b = True
        if minn_x <x1<maxx_x and x1 == x2 and y1<minn_y<y2 and y1<maxx_y<y2 and y1 != y2:#move across object y axis
            b = True
        elif (maxx_x < 0 or minn_x < 0): 
            if minn_y <y1 <maxx_y and y1 == y2 and x1>minn_x>x2 and x1>maxx_x>x2 and x1 != x2:#move across object x axis 
                b = True
        elif (maxx_y < 0 or minn_y < 0): 
            if minn_x <x1 <maxx_x and x1 == x2 and y1>minn_y>y2 and y1>maxx_y>y2 and y1 != y2:#move across object y axis 
                b = True
        emp.append(b)    
    if True in emp : 
        return True
    else:
        return False