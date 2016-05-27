import csv

item_list = []
item_desc_list = []
item_cost_list = []
item_available_list = []
#Loads the CSV, splits the items into named variables
def load():
    with open('items.csv') as csvfile:
         read_csv = csv.reader(csvfile, delimiter=",")
         for col in read_csv:
            item = col[0]
            item_desc = col[1]
            item_cost = col[2]
            item_available = col[3]

            item_list.append(item)
            item_desc_list.append(item_desc)
            item_cost_list.append(item_cost)
            item_available_list.append(item_available)
         return(item_desc_list, item_list, item_cost_list, item_available_list)
#Writes back to the CSV
def csv_writer(item_list, item_desc_list, item_cost_list, item_available_list):
    count = 0
    with open('items.csv', 'wt') as csvfile:
        for i in range(len(item_list)):
            csvfile.write("{},{},{},{}\n".format(item_list[i], item_desc_list[i], item_cost_list[i], item_available_list[i]))
            count += 1
    print("{} items saved to items.csv".format(count))
