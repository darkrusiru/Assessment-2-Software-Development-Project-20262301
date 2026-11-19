# Student Name=  Rusiru Senarath
# Student Id= 20262301
#-------------------------------
#task 1 | Staff Info Function
# in the start i used counter variable and assign value 1 to create unique requisition ids
#
counter = 1
def add_requisition():
    global counter
# in here i have to used global because in the above counter I create out side of this function
# but inside this function I have to modify the counter so that global help me to get original counter outside the function
    print("Enter your information:")

    date = input("Date:")
    staff_id = input("Staff ID:")
    staff_name = input("Staff Name:")

    requisition_id = counter + 1000
    counter = counter + 1

    print("Requisition ID:", requisition_id)
    print("Add items:")

    # i create total variable to store total price and list to add items
    total = 0
    items = []

    while True:
        item_name = input("Item Name:")
        item_price = float(input("Item price($):"))

# add input function to get input from the user then assign them to variables

        items.append((item_name,item_price))

# make user input store in a list by using .append() it stores values in end of list
        total = total + item_price

# make formula to calculate total price in the above total assign as 0 then when the user enter a item price it add to 0 then again also add other items prices to total

        another_item = input("Add another item(yes/no):")

        if another_item.lower() == "no":
            break

    print("Total: $",total)

    return date, staff_id, staff_name, requisition_id, items, total

result=add_requisition()
print("Requisition information:")
print(result)

# task 2 |  Requisition Approval Function
def requisition_approval(total,staff_id,requisition_id):
# in here I create a function to approve the requisition and make assign variables inside 
    status = "Pending"
#Put status as pending because when the user enter the requisition it will be pending until the manager approve or reject it

    if total < 500:
        status = "Approved"
        last_digit = str(requisition_id)[-3:]
    # Last digit get by [-3:] because it will get last 3 digits of the requisition id
    # assign to last_digit variable
    # create approval reference by using staff_id and last_digit
        approval_reference = staff_id + last_digit
    else:
        approval_reference = None
    print("Total: $", total)
    print("Status:", status)
    print("Approval Reference:", approval_reference)
    return status, approval_reference
status, approval_reference = requisition_approval(result[5],result[1],result[3])
# this above function recall inside that result then bracket seems confusing but it is not because result is a tuple and inside that tuple i have to get the values by using index numbers

# Task 3 | Task 3: Display Requisitions Function
def display_requisitions(date,requisition_id,staff_id,staff_name,total,status,approval_refrence):
    print("Printing requisitions:")
    print("Date:", date)
    print("Requisition ID:", requisition_id)
    print("Staff ID:", staff_id)
    print("Staff Name:", staff_name)
    print("Total: $", total)
    print("Status:", status)
    if approval_refrence is not None:
        print("Approval Reference:", approval_refrence)
display_requisitions(result[0],result[3],result[1],result[2],result[5],status,approval_reference)
#return date, staff_id, staff_name, requisition_id, items, total
#       0       1        2           3               4     5     
# --------------index Value----------------------------------
#After index5 i have to get status and approval_reference so i used the above function to display all the requisition information

