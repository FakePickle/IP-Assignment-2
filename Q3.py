#Function to get all the names signed in the form of dictionary
def student_signs(yearbook):
    current_student = ""
    #opening the file in read format
    with open('Yearbook.txt', "r") as f:
        for line in f:
            if line == '\n':
                pass
            else:
                line = line.strip()
                if ":" in line:
                    #current student is basically the name
                    current_student = line.replace(":", "")
                    yearbook[current_student] = {}
                else:
                    #name and signed are basically the name of student and he signed or not
                    name, signed = line.split(", ")
                    yearbook[current_student][name] = int(signed)
    return yearbook

#Function to count the number of signs per person
def signature_count(signed):
    #all the names will be stored in this list
    names = []
    #the total number of signs will be stored in this list
    signs = []
    for keys,values in signed.items():
        count = 0
        for name,sign in values.items():
            #counting the number of signs
            count += int(sign)
        names.append(keys)
        signs.append(count)
    return names,signs

#Function that prints max and min number of signs per person
def main(names,signs):
    for i,j in zip(names,signs):
        if max(signs)==j:
            print("The maximum number of signs are for :",i)
    for i,j in zip(names,signs):
        if min(signs)==j:
            print("The minimum number of signs are for :",i)

#drivers code
if __name__ == "__main__":
    yearbook = {}
    yearbook = student_signs(yearbook)
    names,signs = signature_count(yearbook)
    main(names,signs)