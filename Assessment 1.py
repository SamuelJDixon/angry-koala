
MENU = "\nMenu:\n(L)ist all items\n(H)ire and item\n(R)eturn an item\n(A)dd a new item to stock\n(Q)uit"

user_name = input("Please enter name: ")
import csv
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
# Below code should work for writing the CSV, having trouble and need to look into it. Adding quotes and new lines.
    # out_file = open('items.csv', 'w', newline='')
    # writer = csv.writer(out_file, dialect='excel')
    # writer.writerows(all_lines)
    # out_file.close()
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

    name = input('Enter name of the item: ')
    description = input('Please enter the item description: ')
    while True:
        try:
            price = float(input("Please enter the price of the item: "))
            break
        except ValueError:
            print("Sorry! That was not a valid number. Try again please...")
    status = "in\n"
    new_item = (name, description, price, status)
    number_change = len(all_lines)+1
    all_lines.insert(number_change, new_item)
    print("\nYou have added the item: ", new_item)

main()


