# Student Name=  Rusiru Senarath
# Student Id= 20262301
#-------------------------------
#Task 4: Tkinter
import tkinter as tk
from Programming_logic_task_part01 import *

# make a window using tkinter and assign it to a variable called window
window = tk.Tk()
window.title("Requisition System")
window.geometry("500x600")
#-----Staff Info Section-----
tk.Label(window,text="Staff Name:").pack()
# the label is used to display text on the window and pack() is used to display it on the window
staff_name_entry = tk.Entry(window)
staff_name_entry.pack()
# the entry is used to get input from the user and pack() is used to display it on the window
#Entry is used to get input from the user 
tk.Label(window,text="Staff ID:").pack()
staff_id_entry = tk.Entry(window)
staff_id_entry.pack()
tk.Label(window,text="Date:").pack()
date_entry = tk.Entry(window)
date_entry.pack()


#-----Items Section-----   
tk.Label(window,text="Item Name:").pack()
item_name_entry = tk.Entry(window)
item_name_entry.pack()
tk.Label(window,text="Item Price:").pack()
item_price_entry = tk.Entry(window)
item_price_entry.pack() 

# list of items to store the items added by the user
items = []
# Have to make other seperate function to add items to the list and calculate the total price
#Because the add_requisition() function is already used in the Programming_logic_task_part01.py file so I have to make another function to add items to the list and calculate the total price
item_list = tk.Listbox(window,height=10,width=50)
item_list.pack()

# add item function to add items to the list and calculate the total price
def add_item():
    item_name = item_name_entry.get()
    item_price = float(item_price_entry.get())
    # make above Entry for item name and item price to get input from the user and assign them to variables

    items.append((item_name,item_price))
    # make user input store in a list by using .append() it stores values in end of list
    item_list.insert(tk.END,
                     item_name + "- $ " + str(item_price)
    )
    item_name_entry.delete(0,tk.END)
    item_price_entry.delete(0,tk.END)
    # this is used to clear the entry after the user add the item to the list

#add item button to add items to the list and calculate the total price
add_item_button = tk.Button(window,text="Add Item",command=add_item)
# command is used to call the function when the button is clicked
add_item_button.pack()

# Calculate total price function to calculate the total price of the items in the list

def calculate_total():
    total = 0
    for item in items:
        total =  total + item[1]
    total_label.config(text="Total: $ " + str(total))
    # make formula to calculate total price in the above total assign as 0 then when the user enter a item price it add to 0 then again also add other items prices to total

# Calculate total button to calculate the total price of the items in the list
calculate_total_button = tk.Button(window,
                                   text="Calculate Total",
                                   command=calculate_total)

calculate_total_button.pack()

# Check Approval button to check the approval status of the requisition
def check_approval():
    total = 0
    for item in items:
        total =  total + item[1]
    staff_id = staff_id_entry.get()
    requisition_id = counter + 1000
    status, approval_reference = requisition_approval(total,staff_id,requisition_id)
    total_label.config(
        text="Total: $" + str(total)
    )

    status_label.config(
        text="Status: " + status
    )

    if approval_reference is not None:
        approval_label.config(
            text="Approval Reference: " + approval_reference
        )
    else:
        approval_label.config(
            text="Approval Reference: None"
        )

# Check Approval button

approval_button = tk.Button(
    window,
    text="Check Approval",
    command=check_approval
)

approval_button.pack()



# Output labels

total_label = tk.Label(
    window,
    text="Total: $0"
)

total_label.pack()


status_label = tk.Label(
    window,
    text="Status: Not Checked"
)

status_label.pack(pady=5)


approval_label = tk.Label(
    window,
    text="Approval Reference: None"
)

approval_label.pack(pady=5)

window.mainloop()