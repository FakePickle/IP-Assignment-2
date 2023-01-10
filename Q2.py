def course_check(course_input,user_input):
    if user_input[0].isalnum():
        pass
        for i in user_input[0]:
            if i.isalpha():
                pass
                if i.isupper():
                    pass
                else:
                    return "Improper Course Number"
        if user_input[0][-1].isdigit():
            course_input.append(user_input)
            pass
        else:
            return "Improper Course Number"
    else:
        return "Improper Course Number"

def course(course_input):
    while True:
        user_input = input().split()
        if not(len(user_input)==3):
            break
        elif user_input[0] not in course_list:
            a = course_check(course_input,user_input)
            if a is None:
                pass
            else:
                print(a)
        elif user_input[1] not in credit:
            print("Incorrect Credit")
        elif user_input[2] not in course_grade:
            print("Incorrect Grade")
        else:
            course_input.append(user_input)

def Transcript(course_input,l1):
    x = len(course_input)
    total_grade = 0
    sum_credits = 0
    course_input.sort()
    for i in range(x):
        print(course_input[i][0]+': '+course_input[i][2])
        l1 += course_input[i][2]
        sum_credits += int(course_input[i][1])
    for i in range(len(l1)):
        if l1[i] in course_grade:
            a = course_grade.index(l1[i])
            total_grade += grade_marks[a]*int(course_input[i][1])
    avg = total_grade/sum_credits
    print('SGPA: '+f'{avg:.2f}')

if __name__ == "__main__":
    course_list = ['CSE101','DES102','COM101','ECE111','MTH100']
    credit = ['1','2','4']
    course_grade = ['A+','A','A-','B','B-','C','C-','D','F']
    grade_marks = [10,10,9,8,7,6,5,4,2]
    student_course = []
    Calculating_SGPA = []
    course(student_course)
    if len(student_course) == 0:
        pass
    else:
        Transcript(student_course,Calculating_SGPA)