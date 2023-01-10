def menu(l):
    x = 1
    for i in l:
        print(str(x)+'.',i[0]+', Rs.'+str(i[1]))
        x += 1
    print()

def items(l):
    while True:
        l1 = list(map(int,input("Enter item number and item quantity : ").split()))
        if not(len(l1) == 2):
            break
        l += l1

def bill(l,l1):
    x = len(l1)
    total_items = 0
    total_sum = 0
    for i in range(0,x,2):
        total_items += l1[i+1]
        b = (l[l1[i]-1][1])*(l1[i+1])
        total_sum += b
        print(l[l1[i]-1][0]+', '+str(l1[i+1])+', Rs '+str(b))
    print('TOTAL, '+str(total_items)+' items, Rs',total_sum)

if __name__ == "__main__":
    m = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
    item = []
    menu(m)
    items(item)
    bill(m,item)