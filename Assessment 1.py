
MENU = "\nMenu:\n(L)ist all items\n(H)ire and item\n(R)eturn an item\n(A)dd a new item to stock\n(Q)uit"
user_name = input("Please enter name: ")



def main():
    print("Welcome", user_name, "to Samuel Dixon's online catalogue")
    open_file = open('items.csv', 'r+')
    allLines = open_file.readlines()

    #Create a new string or list, outside the nested for loops. Master string that will be saved in the end.
    #create a new integer and initialise it with zero

    for line in allLines:
        #if line index is equal to user interger.... do this
        currentLine = line.split(',')
        for element in currentLine:
            print(element)
            #add element to the string ie, if in add out

        #add a newline character to end of string
        #increment the int variable

    print(MENU)
    choice = input("Please choose a menu option: ").upper()
    while choice != "Q":
        if choice == "L":
            print(allLines)
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


