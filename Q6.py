#function to return marks of students
def student_marks(student_marks_file):
    marks = [line.split(', ') for line in student_marks_file]
    marks_1 = []
    for i in marks:
        temp_list = []
        temp_list.append(i[0])
        for j in range(1,len(i)):
            i[j] = int(i[j])
            temp_list.append(i[j])
        marks_1.append(temp_list)
    return marks_1

#calculating the total percentile out of 100 based on weightage
def calculate_marks(marks_of_students):
    #list where all the percentile of students will be stored
    percentile_list = []
    for i in marks_of_students:
        #calculating the percentile
        percentile = 0
        for j in range(1,len(i)):
            percentile += (wts[j-1][1]*i[j]/wts[j-1][0])
        percentile_list.append(percentile)
    return percentile_list

#checking grade and then writing into a new file all the student roll number and their percentile
def write_file(student_mark,student_marks_file):
    #list where all the student grades get appended
    student_grade = []
    for i in student_mark:
        if i>80:
            student_grade.append('A')
        elif i>70:
            student_grade.append('A-')
        elif i>60:
            student_grade.append('B')
        elif i>50:
            student_grade.append('B-')
        elif i>40:
            student_grade.append('C')
        elif i>35:
            student_grade.append('C-')
        elif i>30:
            student_grade.append('D')
        elif i<=30:
            student_grade.append('F')
    #writing the content in the file
    with open("IP_Grades.txt","w+") as student_grades:
        for i in range(len(student_marks_file)):
            student_grades.write(str(student_marks_file[i][0])+', '+str(student_mark[i])+', '+str(student_grade[i])+'\n')

#drivers code
if __name__ == '__main__':
    student_marks_file = open("IP_Marks.txt","r").read().splitlines()
    #marks of assignment and percentage of grade included in the final result
    wts = [(10, 5), (20, 5), (100, 15), (40, 10), (100, 35), (100, 30)]
    marks = student_marks(student_marks_file)
    percentile = calculate_marks(marks)
    write_file(percentile,marks)