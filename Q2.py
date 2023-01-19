#Function to check whether the user input is improper or proper
def course_check(user_input):
    #All the if conditions are according to the constraints for course number.
    if user_input[0].isalnum():
        pass
        if user_input[0][0].isalpha():
            pass
        else:
            return "Improper Course Number"
        #checking if all the letters in course number are capital or not
        for i in user_input[0]:
            if i.isalpha():
                pass
                if i.isupper():
                    pass
                else:
                    return "Improper Course Number"
        #checking if the course number ends with digit
        if user_input[0][-1].isdigit():
            pass
        else:
            return "Improper Course Number"
    else:
        return "Improper Course Number"
    #checking whether the credits is 1 2 or 4
    if user_input[1] not in credit:
        return "Incorrect Credit"
    #checking whether the grade is according to the course_grade list
    if user_input[2] not in course_grade:
        return "Incorrect Grade"

#Taking user input for inputting the course number, credits and grade
def course(course_input):
    while True:
        user_input = input("Enter Course Number, Credits and Course Grade you received : ").split()
        #A condition where if we hit return without typing anything the loop will break
        if (len(user_input)==0):
            break
        elif not(len(user_input)==3):
            print("Improper Inputs")
        #checking if the user input is proper or not
        check = course_check(user_input)
        if check is None:
            course_input.append(user_input)
            pass
        else:
            print(check)

#Function to print the transcript of the student
def Transcript(course_input,SGPA):
    total_grade = 0
    sum_credits = 0
    #Sorting the list according to the course number
    course_input.sort()
    #Calculating total credits
    for i in range(len(course_input)):
        print(course_input[i][0]+': '+course_input[i][2])
        SGPA.append(course_input[i][2])
        sum_credits += int(course_input[i][1])
    #Calculating total grade by formula that is multplying every grade by its respective credit
    for i in range(len(SGPA)):
        if SGPA[i] in course_grade:
            index_sgpa = course_grade.index(SGPA[i])
            total_grade += grade_marks[index_sgpa]*int(course_input[i][1])
    avg = total_grade/sum_credits
    print('SGPA: '+f'{avg:.2f}')

#Drivers code
if __name__ == "__main__":
    #Main course list
    course_list = ['CSE101','DES102','COM101','ECE111','MTH100']
    #Credits given in question
    credit = '124'
    #Grades
    course_grade = ['A+','A','A-','B','B-','C','C-','D','F']
    #grade marks respective to the grade list
    grade_marks = [10,10,9,8,7,6,5,4,2]
    #Empty student course list for appending all the course, credit and grade
    student_course = []
    #List where all the grades accourding to course list is appended
    Calculating_SGPA = []
    course(student_course)
    #adding this condition so if we do not input anything it will not give an error
    if len(student_course) == 0:
        pass
    else:
        Transcript(student_course,Calculating_SGPA)