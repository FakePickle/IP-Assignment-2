def student_marks(student_marks_file):
    marks = [line.split(', ') for line in student_marks_file]
    l1 = []
    for i in marks:
        l2 = []
        for j in i:
            j = eval(j)
            l2.append(j)
        l1.append(l2)
    return l1

def calculate_marks(marks_of_students):
    marks = []
    for i in marks_of_students:
        lb = 0
        x = 0
        for j in range(1,len(i)):
            lb += (wts[x][1]*i[j]/wts[x][0])
            x += 1
        marks.append(lb)
    return marks

def write_file(student_mark,student_marks_file):
    student_grade = []
    for i in student_mark:
        if i>=80:
            student_grade.append('A')
        elif i>=70:
            student_grade.append('A-')
        elif i>=60:
            student_grade.append('B')
        elif i>=50:
            student_grade.append('B-')
        elif i>=40:
            student_grade.append('C')
        elif i>=35:
            student_grade.append('C-')
        elif i>=30:
            student_grade.append('D')
        elif i<30:
            student_grade.append('F')
    with open("/home/fakepickle/Downloads/Python programs/College/IP Assignment 2/Student_grade.txt","w+") as student_grades:
        for i in range(len(student_marks_file)):
            student_grades.write(str(student_marks_file[i][0])+', '+str(student_mark[i])+', '+str(student_grade[i])+'\n')

if __name__ == '__main__':
    student_marks_file = open("/home/fakepickle/Downloads/Python programs/College/IP Assignment 2/Marks_of_students.txt","r").read().splitlines()
    wts = [(10, 5), (20, 5), (100, 15), (40, 10), (20,10), (10,5), (100,50)]
    l1 = student_marks(student_marks_file)
    l2 = calculate_marks(l1)
    write_file(l2,l1)