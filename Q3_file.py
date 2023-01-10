def student_signs():
    with open("/home/fakepickle/Downloads/Python programs/College/IP Assignment 2/Student_Signed.txt") as signed_by_student:
        list_signed = signed_by_student.read().splitlines()
        w = []
        for i in list_signed:
            if i[-1] == ':':
                l = []
                l.append(i)
                w.append(l)
        x = len(w)
        main_list = []
        for i in range(0,len(list_signed),x):
            a = []
            a.append(list_signed[i])
            a.append(list_signed[i+1])
            a.append(list_signed[i+2])
            a.append(list_signed[i+3])
            main_list.append(a)
        for i in main_list:
            for j in range(1,len(i)):
                a = i[j].split(', ')
                i[j] = a
        dict = {}
        for i in range(len(main_list)):
            a = main_list[i]
            dict1 = {}
            for j in range(1,len(a)):
                dict1[a[j][0]] = a[j][1]
            dict[a[0]] = dict1
    return dict

def signature_count(signed):
    names = []
    signs = []
    for keys,values in signed.items():
        count = 0
        for name,sign in values.items():
            count += int(sign)
        names.append(keys)
        signs.append(count)
    return names,signs

def main(names,signs):
    a = len(names)
    for i in range(a):
        if max(signs)==signs[i]:
            print("The max number of signs are for :",names[i][:-1:])
        if min(signs)==signs[i]:
            print("The minimum number of signs are for :",names[i][:-1:])

if __name__ == "__main__":
    signed = student_signs()
    names,signs = signature_count(signed)
    main(names,signs)