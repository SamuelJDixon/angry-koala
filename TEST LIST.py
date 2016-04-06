list = [("apple",True),("bannana",False),("pear",True),("orange",True)]

is_true = []
index = 0
for item in list:
    if item[1]:
        print(str(len(is_true))+" "+str(item))
        is_true.append(index)
    index += 1

value = int(input("Select menu item number: "))

print(list[is_true[value]])



# is_true = []
# index = 0
# for item in list:
#     if item[1]:
#         is_true.append(item)
#     index += 1




# is_true = []
# index = 0
# for item in list:
#     if item[1]:
#         print(str(len(is_true))+" "+str(item))
#         is_true.append(index)
#     index += 1


out_lines = []
for line in allines:
    if line[3] == "in":

        if "in" in element[3]:

        out_lines.append(line)



list = ["thing0","thing1","thing2","thing3"]

print(list)

list[2] = "thing42"

print(list)

