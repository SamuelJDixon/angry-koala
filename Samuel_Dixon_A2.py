""" Author - Samuel Dixon
This program utilizes information from the first assessment while also using Kivy to give the user a better
experience. It is a program designed around vewing items from a CSV, being able to hire, return and add new items
to the same CSV.
"""
# Imports all the elements needed
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
import samuel_dixon_A1
# The Main function
class Main(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        samuel_dixon_A1.load()
        self.status = 'view'
    #Builds the GUI using the .kv file
    def build(self):
        self.title = "Hire Program - Main Menu"
        self.root = Builder.load_file('app.kv')
        self.create_entry_buttons()
        self.status_text = "Welcome"
        return self.root
    #Displays a message when the user clicks view
    def press_view(self):
        self.status = 'view'
        for instance in self.root.ids.auto_widget.children:
            instance.state = 'normal'
        self.status_text = 'Select an item to view its description'

    #Displays message to user
    def press_hire(self):
        for instance in self.root.ids.auto_widget.children:
            instance.state = 'normal'
        self.status = 'hire'
        self.status_text = 'Select available items to hire'
    #Displays message to user
    def press_return(self):
        self.status = 'return'
        for instance in self.root.ids.auto_widget.children:
            instance.state = 'normal'
        self.status_text = 'Select item(s) to return'
    #Creates the buttons and gives them initial colours
    def create_entry_buttons(self):
        count = 0
        for name in samuel_dixon_A1.item_list:
            # create a button for each entry
            temp_button = Button(text=name)
            if samuel_dixon_A1.item_available_list[count] == "out":
                temp_button.background_color = (0.01, 1, 0.2, 1)
            count += 1
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.auto_widget.add_widget(temp_button)
    #Function that determines what screen the user views I.E. Hire. Uses .status to accomplish this
    def press_entry(self, instance):
        if self.status == 'view':
            name = instance.text
            lookup = samuel_dixon_A1.item_list.index(name)
            if samuel_dixon_A1.item_available_list[lookup] == "in":
                available = 'available'
            else:
                available = 'unavailable'
            instance.state = 'down'
            self.status_text = "{}, ({}) ${} is {}".format(name, samuel_dixon_A1.item_desc_list[lookup], samuel_dixon_A1.item_cost_list[lookup], available)
        elif self.status == 'hire':
            name = instance.text
            lookup = samuel_dixon_A1.item_list.index(name)
            if samuel_dixon_A1.item_available_list[lookup] == "in":
                self.status_text = "{}, ${}".format(name, samuel_dixon_A1.item_cost_list[lookup])
                instance.state = 'down'
            else:
                pass
        elif self.status == 'return':
            name = instance.text
            lookup = samuel_dixon_A1.item_list.index(name)
            if samuel_dixon_A1.item_available_list[lookup] == "in":
                pass
            else:
                instance.state = 'down'
                self.status_text = "Returning {}".format(name)
    #Opens popup for adding new items
    def press_add_items(self):
        self.status_text = "Enter details for a new hire item"
        self.root.ids.popup.open()
    #Appends the items to the CSV
    def press_save(self, item_name, item_description, item_price):
        samuel_dixon_A1.item_list.append(item_name)
        samuel_dixon_A1.item_desc_list.append(item_description)
        samuel_dixon_A1.item_cost_list.append(item_price)
        samuel_dixon_A1.item_available_list.append('in')
        samuel_dixon_A1.csv_writer(samuel_dixon_A1.item_list, samuel_dixon_A1.item_desc_list, samuel_dixon_A1.item_cost_list, samuel_dixon_A1.item_available_list)

        # change the number of columns based on the number of entries (no more than 5 rows of entries)
        self.root.ids.auto_widget.cols = len(samuel_dixon_A1.item_list) // 5 + 1
        # add button for new entry (same as in create_entry_buttons())
        temp_button = Button(text=item_name)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.auto_widget.add_widget(temp_button)
        # close popup
        self.root.ids.popup.dismiss()
        self.clear_fields()

    def clear_fields(self):
        self.root.ids.item_name.text = ""
        self.root.ids.item_price.text = ""
        self.root.ids.item_description.text = ""

    def press_cancel(self):
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.status_text = ""
    #Will assess to see if .stats is hire or return, then either return or hire the items
    def press_confirm(self):
        if self.status == 'hire':
            list_of_items = []
            cost = []
            count = 0
            total = 0
            for instance in self.root.ids.auto_widget.children:
                if instance.state == 'down':
                    list_of_items.append(samuel_dixon_A1.item_list[-(count + 1)])
                    cost.append(samuel_dixon_A1.item_cost_list[-(count + 1)])
                    samuel_dixon_A1.item_available_list[-(count + 1)] = 'out'
                    new_variable_for_itemcost = float(samuel_dixon_A1.item_cost_list[-(count + 1)])
                    total += new_variable_for_itemcost
                    instance.background_color = (0.01, 1, 0.2, 1)
                    count += 1
                self.status_text = '{}, Total: ${}'.format(list_of_items, total)
        elif self.status == 'return':
            list_of_items = []
            count = 0
            for instance in self.root.ids.auto_widget.children:
                if instance.state == 'down' and samuel_dixon_A1.item_available_list[-(count + 1)] == 'out':
                    list_of_items.append(samuel_dixon_A1.item_list[-(count + 1)])
                    samuel_dixon_A1.item_available_list[-(count + 1)] = 'in'
                    instance.background_color = (1, 0.7, 0.16, 1)
                    count += 1
                self.status_text = '{} Returned'.format(list_of_items)
        samuel_dixon_A1.csv_writer(samuel_dixon_A1.item_list, samuel_dixon_A1.item_desc_list, samuel_dixon_A1.item_cost_list, samuel_dixon_A1.item_available_list)
        self.press_view()

Main().run()
