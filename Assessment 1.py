
MENU = "\nMenu:\n(L)ist all items\n(H)ire and item\n(R)eturn an item\n(A)dd a new item to stock\n(Q)uit"
user_name = input("Please enter name: ")
open_file = open('items.csv', 'r+')
all_lines = []
for line in open_file:
            splitline = line.split(',')
            all_lines.append((splitline[0], splitline[1], splitline[2], splitline[3]))

def main():
    print("Welcome", user_name, "to Samuel Dixon's online catalogue")

    print(MENU)
    choice = input("Please choose a menu option: ").upper()
    while choice != "Q":
        if choice == "L":
            print(all_lines)
        elif choice == "H":
            hire()
        elif choice == "R":
            return_item()
        elif choice == "A":
            add_item()
        else:
            print("Invalid Menu Choice")
        print(MENU)
        choice = input("Please choose a menu option: ").upper()

    print("Thank you for using Samuel Dixon's online catalogue")

def hire():
    item_in = []
    index = 0
    validIndex = []
    for line in all_lines:
        if "in" in line[3]:
            print(str(index)+" "+str(line))
            item_in.append(index)
            validIndex.append(index)
        index += 1
    value = int(input("Select menu item number: "))
    all_lines[value] = (all_lines[value][0], all_lines[value][1], all_lines[value][2], "out")

    for line in all_lines:
        print(line)


def return_item():
    item_out = []
    index = 0
    validIndex = []
    for line in all_lines:
        if "out" in line[3]:
            print(str(index)+" "+str(line))
            item_out.append(index)
            validIndex.append(index)
        index += 1
    value = int(input("Select menu item number: "))
    all_lines[value] = (all_lines[value][0], all_lines[value][1], all_lines[value][2], "in")

    for line in all_lines:
        print(line)


def add_item():
    # name = input("Enter a name for the item: ")
    # desc = input("Enter a description for the item: ")
    # price = float(input("Enter a price for the item: "))
    # status = "in"
    # append_item = []
    # append_item[0] = (all_lines[name][0], all_lines[desc][1], all_lines[price][2], all_lines[int(status)][3])
    #     #(name[0], desc[1], str(price)[2], statu[3])

    name = input('enter item name:')
    description = input('please enter the item description')
    price = float(input('enter the price'))
    str_price = str(price)
    status = "in"
    append_item = []
    new_item = name +','+ description +','+ str_price +','+ status
    print(new_item)
    append_item = [new_item]
    all_lines.append(append_item)

main()








    #Create a new string or list, outside the nested for loops. Master string that will be saved in the end.
    # final_string = ""
    # counter = 0
    # str_counter = str(counter)
    # for line in all_lines: #iterates through each lines
    #         str_counter = str(counter) #converts counter to a string
    #         current_line = line.split(',')
    #         final_string += str_counter #adds integer to beginning of line
    #         final_string += ': '
    #         for element in current_line:  #iterates through each element inside the current line
    #             final_string += element #add element to the string
    #             if element == 'out\n' or element == 'in\n': #tests if it is the last element
    #                 final_string += '\n' #add a new line after each item status
    #             else:
    #                 final_string += ', '
    #         counter += 1


