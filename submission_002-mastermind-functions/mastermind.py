import random


# TODO: Decompose into functions
correct = False
turns = 0
code = [0,0,0,0]
answer = ""
def code_gen():
    '''
    The function code_gen randomly generates a four digit code 
    '''
    global code
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
 

def user_input():
    '''
    The function user_input takes an input from the user
    '''
    global answer
    answer = input("Input 4 digit code: ")

def game_loop():
    '''
    In this function ,game_loop loops the entire game using the user_input function,it also contains code that validates the input 
    and compares the input to the four digit code generated by the code_gen function  
    '''
    global turns
    global correct 
    correct = False  
    global code
    #global answer

    while not correct and turns < 12:
        user_input()
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue
        correct_digits_and_position = 0
        correct_digits_only = 0
        for i in range(len(answer)):
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1
        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1
        if correct_digits_and_position == 4:
            correct = True
            print('Congratulations! You are a codebreaker!')
        else:
            print('Turns left: '+str(12 - turns))
    print('The code was: '+str(code))

def run_game():
    '''
    Within the run_game function the other two created functions(code_gen and game_loop) are called  
    '''
    
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    code_gen()
    #print(code)
    game_loop()
   
    
if __name__ == "__main__":
    run_game()
