#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    folder = open(file_name,"r")
    contents = folder.readlines()
    folder.close()
    #print(contents)
    return contents


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    ran_word = random.randint(0,len(words)-1)
    sel_word = words[ran_word].strip()  
    #print(sel_word)

    ran_letter = random.randint( 0,len(sel_word)-1)
    sel_letter = sel_word[ran_letter].strip()
    #print(sel_letter)

    print( "Guess the word: " + (sel_word.replace(sel_letter,"_")) + "\n" )

    return sel_word



def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    guess = input("Guess the missing letter: " )
    return guess


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: ' + word)


if __name__ == "__main__":
    run_game('short_words.txt')

