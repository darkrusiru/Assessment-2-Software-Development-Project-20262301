class Requisition:
    requisition = []
    next_requisition_id = 1000
# Above I make Requisition class to store 
# requisition information and make a list to store requisition and also make a variable to store next requisition id

# Here I am going tocreate constructor to initialize the requisition object with the required attributes

    def __init__(self,date, staff_id, staff_name,items):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = requisition_id

        self.items = items
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not Available"

        for item in items:
            self.total += item[1]
    @classmethod
    def add_requisition(cls, date, staff_id, staff_name, items):

        # Check that the staff information is valid
        if not date or not staff_id or not staff_name:
            print("Date, staff ID and staff name are required.")
            return None

        # Check that the item list is not empty
        if not items:
            print("At least one item is required.")
            return None

        # Check item names and prices
        for item in items:

            if len(item) != 2:
                print("Each item must contain a name and a price.")
                return None

            if not isinstance(item[0], str) or not item[0].strip():
                print("Item name must be valid text.")
                return None

            if not isinstance(item[1], (int, float)) or isinstance(item[1], bool):
                print("Item price must be a number.")
                return None

            if item[1] <= 0:
                print("Item price must be greater than zero.")
                return None
counter = 1              # used to make a unique requisition id
all_requisitions = []    # a list to keep every requisition


# Make Requsition Class
class Requisition:

    def __init__(self, date, staff_id, staff_name):
        global counter
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = counter + 1000
        counter = counter + 1
        self.total = 0
        self.status = "Pending"
        self.approval_reference = None
        all_requisitions.append(self)    

    
    def add_requisition(self, items):
        self.total = 0
        for item in items:
            self.total = self.total + item[1]
        return self.total

    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]

    def respond_to_requisition(self, decision):
        if self.status == "Pending":
            if decision == "Approved":
                self.status = "Approved"
                self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
            elif decision == "Not approved":
                self.status = "Not approved"
        else:
            print("Requisition", self.requisition_id, "is not pending, no change.")

    def display_requisitions(self):
        for r in all_requisitions:
            print("Date:", r.date)
            print("Requisition ID:", r.requisition_id)
            print("Staff ID:", r.staff_id)
            print("Staff Name:", r.staff_name)
            print("Total: $" + str(r.total))
            print("Status:", r.status)
            if r.approval_reference is None:
                print("Approval Reference Number: Not available")
            else:
                print("Approval Reference Number:", r.approval_reference)
            print()

    def requisition_statistics(self):
        approved = 0
        pending = 0
        not_approved = 0
        for r in all_requisitions:
            if r.status == "Approved":
                approved = approved + 1
            elif r.status == "Pending":
                pending = pending + 1
            else:
                not_approved = not_approved + 1

        print("Statistics:")
        print("The total number of requisitions submitted:", len(all_requisitions))
        print("The total number of approved requisitions:", approved)
        print("The total number of pending requisitions:", pending)
        print("The total number of not approved requisitions:", not_approved)
        print()

while True:
    print("===== REQUISITION SYSTEM =====")
    print("1. Add a requisition")
    print("2. Manager response")
    print("3. Display all requisitions")
    print("4. Show statistics")
    print("5. Exit")
    choice = input("Choose (1-5): ")

    if choice == "1":
        print("Enter your information:")
        date = input("Date: ")
        staff_id = input("Staff ID: ")
        staff_name = input("Staff Name: ")

        # make a new requisition object
        requisition = Requisition(date, staff_id, staff_name)
        print("Requisition ID:", requisition.requisition_id)

        # get the items from the user (same idea as Assessment 1)
        items = []
        print("Add items:")
        while True:
            item_name = input("Item Name: ")
            item_price = float(input("Item price($): "))
            items.append((item_name, item_price))
            another_item = input("Add another item (yes/no): ")
            if another_item.lower() == "no":
                break

        requisition.add_requisition(items)
        requisition.approve_requisition()

        print("Total: $", requisition.total)
        print("Status:", requisition.status)
        if requisition.approval_reference is None:
            print("Approval Reference: Not available")
        else:
            print("Approval Reference:", requisition.approval_reference)
        print()

    elif choice == "2":
        requisition_id = int(input("Enter the Requisition ID: "))
        found = None
        for r in all_requisitions:
            if r.requisition_id == requisition_id:
                found = r
        if found is None:
            print("Requisition not found.")
        else:
            decision = input("Decision (Approved / Not approved): ")
            found.respond_to_requisition(decision)
            print("Status is now:", found.status)
        print()

    elif choice == "3":
        if len(all_requisitions) == 0:
            print("No requisitions yet.")
        else:
            all_requisitions[0].display_requisitions()

    elif choice == "4":
        if len(all_requisitions) == 0:
            print("No requisitions yet.")
        else:
            all_requisitions[0].requisition_statistics()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Wrong choice, please type a number from 1 to 5.")
        print()