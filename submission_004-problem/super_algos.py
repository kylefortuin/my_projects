
def find_min(element):
    """TODO: complete for Step 1"""
    #check
    for index in element:
        if type(index) != int:#returns if object is an instance of the specified type
            return -1
    if len(element) == 1:# checks if there is only one element in list
        return element[0]
    elif len(element) == 0:#checks if list is empty
        return -1
    #main code
    else:
        min_num = find_min(element[1:]) #let variable equal rest of the list from second element
        mini = element[0]#let variable equal first index of list
        if min_num < mini:#compare current index to next index for less than
            mini = min_num#assign the less than value to variable if next index is less
        return mini        



def sum_all(element):
    """TODO: complete for Step 2"""
    for index in element:
        if type(index) != int:#returns if object is the specified type
            return -1
    if len(element) == 1:# checks if there is only one element in list
        return element[0]
    elif len(element) == 0:#checks if list is empty
        return -1
    else:
        first = element[0]
        rest = element[1:]

        return first + sum_all(rest)


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    #checks
    for index in character_set:
        if type(index) != str:
            return []
    if n == 0 :
        return [""]    
    if n < 0:
        return []
    if len(character_set) == 0:
        return []
    #main code
    new_set = set()
    for character in character_set:
        for next1 in find_possible_strings(character_set, n-1):
            new_set.add(character + next1)
    return new_set

my_list = [10,2,34,5,8,]
#the_set = ['a','b']
the_set = {'a', 'b'}

possible_strings = find_possible_strings(the_set, 2)

print(find_min(my_list))
print(sum_all(my_list))
print(possible_strings)