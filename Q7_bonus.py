import json

#function where all the main operations take place
def main():
    print("The operations you can perform in the program are :- \n"
    "0. Merge Address book with your friend\n"
    "1. Insert a new entry \n"
    "2. Delete an existing entry \n"
    "3. Finding matches if you input partial name \n"
    "4. Finding an entry with phone number or email address \n"
    "5. Exiting the main program")
    address_book = {}
    #checking if the file exists
    try:
    #opening the file again to check if there is no input in file then the result will be empty dictionary
        file = open('addrbook.txt')
        if(len(file.read().splitlines())==0):
            main_address_book = address_book
        else:
            main_address_book = file_entry(address_book)
        file.close()
    #if the file doesnt exist then the main address book will become empty dictionary
    except:
        main_address_book = address_book
    while True:
        user_input = int(input("Enter your choice from the given above choices : "))
        if not(len(str(user_input))==1):
            print("Please enter some input")
        elif(user_input==0):#option to merging entry
            main_address_book = merge_friend_dictionary(address_book)
        elif(user_input==1):#inserting new entry
            new_address_book = new_entry(main_address_book,address_book)
            if main_address_book is None:
                main_address_book = new_address_book
                pass
            else:
                #merging file entry address book and new entry address book
                main_address_book = {**main_address_book,**new_address_book}
        elif(user_input==2):#deleteing entry
            del_address_book = delete_entry(main_address_book)
            if del_address_book is None:
                pass
            else:
                #since we are deleting the entry from the address book we assign that to the main address book
                main_address_book = del_address_book
        elif(user_input==3):#printing partial matches
            partial_matches(main_address_book)
        elif(user_input==4):#trying to find matches by phone number or email id
            value = phone_number_email_id_match(main_address_book)
            if value is None:
                print("There is no such email id or phone number in the address_book")
            else:
                print(value)
        elif(user_input==5):#quiting the program after writing into the file
            data_str = json.dumps(main_address_book)
            with open("addrbook.txt","w") as address:
                json.dump(main_address_book,address)
            break
        else:
            print("Invalid choice")

#making address book dictionary from the file
def file_entry(address_book):
    with open("addrbook.txt","r") as address:
        address_book = json.load(address)
    return address_book

#function to take new entries
def new_entry(main_address_book,address_book):
    user_name = input("Enter your name : ")
    user_address = input("Enter your addre  ss : ")
    user_phone = input("Enter your phone number : ")
    user_email = input("Enter your email address : ")
    address_book = {}
    address_book[user_name] = [{
        'Address': user_address,
        'Phone Number': user_phone,
        'Email Address': user_email
    }]
    if main_address_book == {}:
        main_address_book = address_book
    else:
        addr_list = []
        for k,v in main_address_book.items():
            if k == user_name:
                addr_list.extend(v)
                addr_list.extend(address_book[user_name])
        if(len(addr_list)==0):
            main_address_book = address_book
        else:
            main_address_book[k] = addr_list
    return main_address_book

#function to deleting entries
def delete_entry(address_book):
    user_input = input("Enter the name of the person you want to remove address of : ")
    if(len(address_book[user_input])>1):
        address = address_book[user_input]
        address.remove(address_book[user_input][-1])
    else:
        del address_book[user_input]
    return address_book

#finding entries based on partial name
def partial_matches(main_address_book):
    user_input = input("Enter partial name : ")
    for keys,values in main_address_book.items():
        for j in values:
            if user_input.lower() in keys.lower():
                print(keys,main_address_book[keys])

#fuction to find entries based on phone number or email id
def phone_number_email_id_match(main_address_book):
    user_input = input("Enter the phone number or email id : ")
    for name,info in main_address_book.items():
        for user_info in info:
            for j in user_info.values():
                if j == user_input:
                    return name,user_info

def merge_friend_dictionary(address_book):
    with open('friend_addrbook.txt') as inline:
        friend_dictionary = json.load(inline)
    address_book.update(friend_dictionary)
    return address_book

if __name__ == '__main__':
    main()