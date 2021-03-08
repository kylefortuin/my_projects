import random

def run_game():
    code = [0,0,0,0]
    for i in range(4):
        combo = random.randint(1,8)
        while str(combo) in code:
            combo = random.randint(1,8)
        code[i] =  str(combo)

    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")

    turns = 12

    #game loop
    while turns >= 0:

        turns -= 1
        exact = 0
        position = 0

        while True:
            guess = input("Input 4 digit code: ")
            if len(guess) == 4:    
                try:
                    len(guess) < 4 or len(guess) > 0
                    guess = int(guess)
                except :
                    continue
                break
            else:
                print("Please enter exactly 4 digits.")

        guess = str(guess)
        for i in range(4):
            if guess[i] == code[i]:
                exact += 1
            elif guess[i] in code:
                position += 1
        if exact == 4:

            code = str(code).replace("[","").replace("]","").replace(',','').replace("'","").replace(" ","")

            print(f"Number of correct digits in correct place:     {exact}"+"\n"+f"Number of correct digits not in correct place: {position}")
            print("Congratulations! You are a codebreaker!"+"\n"+f"The code was: {code}") 
            break
        
        print(f"Number of correct digits in correct place:     {exact}\n"+f"Number of correct digits not in correct place: {position}\n"+f"Turns left: {turns}")
        
        
        if turns == 0:
            break
        pass

if __name__ == "__main__":
    run_game()
