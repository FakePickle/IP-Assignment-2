#function to print menu with the prices on the side
def menu(menu_list):
    x = 1
    for i in menu_list:
        print(str(x)+'.',i[0]+', Rs.'+str(i[1]))
        x += 1
    print()

#Function to take user input and then add it to the main list
def items(items_list):
    while True:
        user_input = list(map(int,input("Enter item number and item quantity : ").split()))
        if not(len(user_input) == 2):
            break
        #Appending the user_input to the main item list where item number and quantity will be stored
        items_list += user_input

#Function to print the bill
def bill(menu_list,items_list):
    total_items = 0
    total_price = 0
    for i in range(0,len(items_list),2):
        total_items += items_list[i+1]
        #Temporary list is basically where the price is stored every time the loop goes on.
        temp_list = (menu_list[items_list[i]-1][1])*(items_list[i+1])
        total_price += temp_list
        print(menu_list[items_list[i]-1][0]+', '+str(items_list[i+1])+', Rs '+str(temp_list))
    print('TOTAL, '+str(total_items)+' items, Rs',total_price)

#drivers code
if __name__ == "__main__":
    #Main menu list
    menu_list = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
    #List where the item number and quantity will be stored
    item = []
    #Printing the menu
    menu(menu_list)
    #User input of item number and quantity
    items(item)
    #Printing the bill
    bill(menu_list,item)