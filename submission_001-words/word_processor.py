def split(delimiters, text): 
    """ Splits a string using all the delimiters supplied as input string :
    param delimiters: 
    :param text: string containing delimiters to use to split the string, 
    e.g. `,;? ` 
    :return: a list of words from splitting text using the delimiters """
    import re 
    regex_pattern = '|'.join(map(re.escape, delimiters)) 

    return re.split(regex_pattern, text, 0)

def convert_to_word_list(text):
    if type(text) != str:#test type
        return -1
    
    
    splatted = split(',;?. ',text)
    word_list = [word.lower() for word in splatted if len(word)>0]#list comprehension

    return word_list


def words_longer_than(length, text):
    if type(text) != str:#test type
        return -1
    if type(length) != int:
        return -1
    
    b = split(',;?. ',text)
    listofwords = [word.lower() for word in b if len(word) > length]#list comprehension

    return listofwords

def words_lengths_map(text): 
    if type(text) != str:#test type
        return -1
    a = split(',;?. ',text)
    letter_counts = {}
    for letter in a :
        if len(letter) > 0:
            letter_counts[len(letter)] = letter_counts.get(len(letter), 0) + 1
    
    return letter_counts



def letters_count_map(text): 
    if type(text) != str:#test type
        return -1 
    a = split(',;?. ',text)
    letter_counts = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,
                     "n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    for letter in a :
        for l in letter:
            letter_counts[l.lower()] = letter_counts.get(l, 0) + 1
    
    return letter_counts

def most_used_character(text):
    if type(text) != str:#test type
        return -1 
    if text == "":
        return None
    a = split(',;?. ',text)
    letter_counts = {}
    for letter in text :
        for l in letter:
            letter_counts[l.lower()] = letter_counts.get(l, 0) + 1
    largest = -1
    for k,v in letter_counts.items():
        if v>largest:
            largest=v
            maxusedword=k
    return maxusedword

