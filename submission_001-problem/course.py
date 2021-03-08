def create_outline():

    """
    TODO: implement your code here
    """# 1
    Topics = set(['Introduction to Python','Tools of the Trade',
    'How to make decisions','How to repeat code',
    'How to structure data','Functions','Modules'])
    listT = list(Topics)
    listT.sort()
    print("Course Topics:")
    for listT in listT:
        print("* " + listT)
    #Step2
    TList  =list(Topics)
    TList.sort()
    probL={"Problem 1":1,
            "Problem 2":2,
            "Problem 3":3 }
    probL=list(probL)
    print("Problems:")
    for TList in TList :
        print("* "+TList +" : "+ (", ").join(probL))
    #step3 
    print("Student Progress:") 
    student1= ("Kyle" ,"Introduction to Python" ,"Problem 2 ", "[STARTED]")
    student2= ("Dean" , " How to make decisions" ,"Problem 1 ", "[GRADED]")
    student3= ("Bob" , "Tools of the Trade" , "Problem 3" ,"[COMPLETED]")
    student4= ("Jeff", "Functions" , "Problem 1" , "[STARTED]")
    student5= ('Bruce', 'Tools of the Trade',"problem 2", '[COMPLETED]')
    student6= ('Remy', 'How to structure data',"problem 3", '[GRADED]')
    student7= ('Chuck', 'Modules',"problem 1", '[STARTED]')
 
    student_list=[student1,student2,student3,student4,student5,student6,student7]
    #step 4
    student_list2 = []
    for graded in student_list:
        if graded[3] == '[STARTED]':
            student_list2.append(graded)
    for graded in student_list:
        if graded[3] == '[GRADED]':
            student_list2.append(graded)
    for graded in student_list:
        if graded[3] == '[COMPLETED]':
            student_list2.append(graded)

    x= 1
    for student, module, problem, status in student_list2:
        print(str(x) + '. ', end='')
        print(f'{student} - {module} - {problem} {status}')
        x += 1

if __name__ == "__main__":
 create_outline()

