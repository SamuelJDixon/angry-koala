
MENU = "\nMenu:\n(L)ist all items\n(H)ire and item\n(R)eturn an item\n(A)dd a new item to stock\n(Q)uit"
user_name = input("Please enter name: ")



def main():
    print("Welcome", user_name, "to Samuel Dixon's online catalogue")
    with open('items.csv') as f:
            item_list = f.read().splitlines()

    print(MENU)
    choice = input("Please choose a menu option: ").upper()
    while choice != "Q":
        if choice == "L":
            print(item_list)
        elif choice == "H":
            print("H")
        elif choice == "R":
            print("R")
        elif choice == "A":
            print("A")
        else:
            print("Invalid Menu Choice")
        print(MENU)
        choice = input("Please choose a menu option: ").upper()

    print("Thank you for using Samuel Dixon's online catalogue")







main()


