def main():
    print("The operations you can perform in the program are :- \n"
    "1. Insert a new entry \n"
    "2. Delete an existing entry \n"
    "3. Finding matches if you input partial name \n"
    "4. Finding an entry with phone number or email address \n"
    "5. Exiting the main program")
    
    file_address_book = file_entry()
    while True:
        user_input = int(input("Enter your choice from the given above choices : "))
        if not(len(str(user_input))==1):
            print("Please enter some input")
        elif(user_input==1):
            new_address_book = new_entry(file_address_book)
            main_address_book = {**file_address_book,**new_address_book}
        elif(user_input==2):
            delete_entry(main_address_book)
        elif(user_input==3):
            p,q = partial_matches(main_address_book)
            print(p,q)
        elif(user_input==4):
            enter_input = input("Do you want to find entry with email or phone number? ")
            if enter_input == "email":
                x,y = email_address_match(main_address_book)
                if y is None:
                    print("The email is not in the address book")
                else:
                    print(x+'-'+y)
            if enter_input == "phone number":
                a,b = phone_number_match(main_address_book)
                if b is None:
                    print("The phone number is not in the address book")
                else:
                    print(a+'-',end = " ")
                    for keys,values in b.items():
                        print(keys+'-'+str(values),end = ", ")
                    print('\n')
        else:
            with open("/home/fakepickle/Downloads/Python programs/College/IP Assignment 2/Address_book.txt","a") as address_book_file:
                for name,info in new_address_book.items():
                    address_book_file.write(name+', ')
                    for keys,values in info.items():
                        address_book_file.write(keys+'-'+str(values)+', ')
                    address_book_file.write('\n')
            break

def file_entry():
    with open("/home/fakepickle/Downloads/Python programs/College/IP Assignment 2/Address_book.txt","r+") as address:
        a = address.read().splitlines()
        if(len(a) == 0):
            pass
        else:
            x = []
            main = []
            for i in a:
                b = i.split(', ')
                x.append(b)
            for i in x:
                for j in i:
                    if j == "":
                        i.pop(i.index(j))
            for i in x:
                y = []
                for j in i:
                    c = j.split("-")
                    y.append(c)
                main.append(y)
            dict = {}
            for k in main:
                dict1 = {}
                for i in range(1,len(k)):
                    dict1[k[i][0]] = k[i][1]
                    dict[k[0][0]] = dict1
            return dict

def new_entry(address_book):
    user_name = input("Enter your name : ")
    user_address = input("Enter your address : ")
    user_phone = int(input("Enter your phone number : "))
    user_email = input("Enter your email address : ")
    address_book = {}
    Person_address_book = {}
    Person_address_book["Address"] = user_address
    Person_address_book["Phone Number"] = user_phone
    Person_address_book["Email Address"] = user_email
    address_book[user_name] = Person_address_book
    return address_book

def delete_entry(address_book):
    user_input = input("Enter the name of the person you want to remove address of : ")
    del address_book[user_input]
    return address_book

def partial_matches(main_address_book):
    user_input = input("Enter partial name : ")
    for keys,values in main_address_book.items():
        if user_input in keys.lower():
            return keys,main_address_book[keys]

def phone_number_match(main_address_book):
    user_input = int(input("Enter the phone number : "))
    for name,info in main_address_book.items():
        for keys,values in info.items():
            if values == user_input:
                return name,main_address_book[name]

def email_address_match(main_address_book):
    user_input = input("Enter the email address : ")
    for name,info in main_address_book.items():
        for keys,values in info.items():
            if values == user_input:
                return name,main_address_book[name]

main()