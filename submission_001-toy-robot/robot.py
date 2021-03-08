def moving_in_square():
    '''
    prints out text giving instructions
    uses variables :
    size 
    degrees 
    '''
    size = 10
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")

def moving_in_rectangle():
    '''
    prints out text giving instructions to move in a rectangle 
    uses variables :
    length
    width
    degrees
    '''
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")

def moving_in_circle():
    '''
    prints out text giving instructions  to move in a circle 
    uses variables :
    degrees 
    length
    '''
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")

def square_dancing():
    '''
    prints out text giving instructions to repeat movements in a square
    uses variables:
    length
    degrees
    size2
    '''
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        degrees = 90
        print("* Move Forward "+str(length))
        print("Moving in a square of size 20")
        for j in range(4):
            size2 = 20
            print("* Move Forward " + str(size2))
            print("* Turn Right " + str(degrees) + " degrees")
            


def crop_circles():
    '''
    prints out text giving instructions to repeats movements in a cricle
    uses variables:
    length 
    degrees
    length2
    '''
    length = 1
    degrees = 1
    print("Crop circles - 4 circles")
    for i in range(4):
        length2 = 20
        print("* Move Forward "+str(length2))
        print("Moving in a circle")
        for k in range(360):
            print("* Move Forward " + str(length))
            print("* Turn Right " + str(degrees) + " degrees")

# TODO: Decompose into functions
def move():
    moving_in_square()
    moving_in_rectangle()
    moving_in_circle()
    square_dancing()
    crop_circles()

def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
