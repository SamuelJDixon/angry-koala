
MENU = "\nMenu:\n(L)ist all items\n(H)ire and item\n(R)eturn an item\n(A)dd a new item to stock\n(Q)uit"
user_name = input("Please enter name: ")


def main():
    print("Welcome", user_name, "to Samuel Dixon's online catalogue")
    open_file = open('items.csv', 'r+')
    #all_lines = open_file.readlines()
    all_lines = []
    for line in open_file:
            splitline = line.split(',')
            all_lines.append((splitline[0], splitline[1], splitline[2], splitline[3]))

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

    print(MENU)
    choice = input("Please choose a menu option: ").upper()
    while choice != "Q":
        if choice == "L":
            print(all_lines)
        elif choice == "H":
            item_in = []
            index = 0
            for line in all_lines:
                if "in" in line[3]:


                    for item in line:
                        if item[1]:
                            print(str(len(item_in))+" "+str(item))
                            item_in.append(index)
                        index += 1
                    value = int(input("Select menu item number: "))

                    print(list[item_in[value]])

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




