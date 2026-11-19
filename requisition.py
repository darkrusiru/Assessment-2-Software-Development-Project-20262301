
from datetime import datetime

counter = 1
all_requisitions = []


# Requisition Class
class Requisition:

    def __init__(self, date, staff_id, staff_name):
        global counter

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = 10000 + counter
        counter = counter + 1

        self.total = 0
        self.status = "Pending"
        self.approval_reference = None

        all_requisitions.append(self)

    # Calculate the requisition total
    def add_requisition(self, items):
        self.total = 0

        for item in items:
            self.total = self.total + item[1]

        return self.total

    # Automatically approve requisitions below $500
    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )
        else:
            self.status = "Pending"

    # Manager response
    def respond_to_requisition(self, decision):

        if self.status != "Pending":
            print("Requisition", self.requisition_id,
                  "is not pending, no change.")
            return

        decision = decision.strip().lower()

        if decision == "approved":
            self.status = "Approved"
            self.approval_reference = (
                self.staff_id + str(self.requisition_id)[-3:]
            )

        elif decision == "not approved":
            self.status = "Not approved"

        else:
            print("Invalid decision. Enter Approved or Not approved.")

    # Display all requisitions
    def display_requisitions(self):

        for r in all_requisitions:
            print("Date:", r.date)
            print("Requisition ID:", r.requisition_id)
            print("Staff ID:", r.staff_id)
            print("Staff Name:", r.staff_name)
            print("Total: $" + format(r.total, ".2f"))
            print("Status:", r.status)

            if r.approval_reference is None:
                print("Approval Reference Number: Not available")
            else:
                print("Approval Reference Number:", r.approval_reference)

            print()

    # Return requisition statistics
    def requisition_statistics(self):

        approved = 0
        pending = 0
        not_approved = 0

        for r in all_requisitions:

            if r.status == "Approved":
                approved = approved + 1

            elif r.status == "Pending":
                pending = pending + 1

            elif r.status == "Not approved":
                not_approved = not_approved + 1

        statistics = {
            "Total requisitions": len(all_requisitions),
            "Approved requisitions": approved,
            "Pending requisitions": pending,
            "Not approved requisitions": not_approved
        }

        return statistics


# Validate date
def get_valid_date():

    while True:
        date = input("Date (DD/MM/YYYY): ").strip()

        try:
            valid_date = datetime.strptime(date, "%d/%m/%Y")

            if valid_date.strftime("%d/%m/%Y") == date:
                return date
            else:
                print("Invalid date format. Use DD/MM/YYYY.")

        except ValueError:
            print("Invalid date. Please enter a real date in DD/MM/YYYY format.")


# Validate staff name
def get_valid_name():

    while True:
        name = input("Staff Name: ").strip()

        cleaned_name = name.replace(" ", "").replace("-", "").replace("'", "")

        if cleaned_name != "" and cleaned_name.isalpha():
            return name
        else:
            print("Invalid name. Use letters, spaces, hyphens or apostrophes only.")


# Validate staff ID
def get_valid_staff_id():

    while True:
        staff_id = input("Staff ID: ").strip()

        if staff_id != "":
            return staff_id
        else:
            print("Staff ID cannot be empty.")


# Validate item name
def get_valid_item_name():

    while True:
        item_name = input("Item Name: ").strip()

        if item_name != "":
            return item_name
        else:
            print("Item name cannot be empty.")


# Validate number
def get_number(message):

    while True:
        try:
            number = float(input(message))

            if number < 0:
                print("Price cannot be negative.")
            else:
                return number

        except ValueError:
            print("Invalid input. Please enter a number.")


# Main Program
while True:

    print("===== REQUISITION SYSTEM =====")
    print("1. Add a requisition")
    print("2. Manager response")
    print("3. Display all requisitions")
    print("4. Show statistics")
    print("5. Exit")

    choice = input("Choose (1-5): ").strip()

    # Add a requisition
    if choice == "1":

        print("\nEnter your information:")

        date = get_valid_date()
        staff_id = get_valid_staff_id()
        staff_name = get_valid_name()

        requisition = Requisition(date, staff_id, staff_name)

        print("Requisition ID:", requisition.requisition_id)

        items = []

        print("\nAdd items:")

        while True:

            item_name = get_valid_item_name()
            item_price = get_number("Item price ($): ")

            items.append((item_name, item_price))

            while True:
                another_item = input("Add another item (yes/no): ").strip().lower()

                if another_item == "yes":
                    break

                elif another_item == "no":
                    another_item = "no"
                    break

                else:
                    print("Please enter yes or no.")

            if another_item == "no":
                break

        requisition.add_requisition(items)
        requisition.approve_requisition()

        print("\nTotal: $" + format(requisition.total, ".2f"))
        print("Status:", requisition.status)

        if requisition.approval_reference is None:
            print("Approval Reference: Not available")
        else:
            print("Approval Reference:", requisition.approval_reference)

        print()

    # Manager response
    elif choice == "2":

        try:
            requisition_id = int(input("Enter the Requisition ID: "))

            found = None

            for r in all_requisitions:
                if r.requisition_id == requisition_id:
                    found = r
                    break

            if found is None:
                print("Requisition not found.")

            elif found.status != "Pending":
                print("This requisition is not pending.")

            else:
                decision = input(
                    "Decision (Approved / Not approved): "
                )

                found.respond_to_requisition(decision)

                print("Status is now:", found.status)

                if found.approval_reference is not None:
                    print("Approval Reference:", found.approval_reference)

        except ValueError:
            print("Invalid ID. Please enter a number.")

        print()

    # Display all requisitions
    elif choice == "3":

        if len(all_requisitions) == 0:
            print("No requisitions yet.")
        else:
            all_requisitions[0].display_requisitions()

    # Display statistics
    elif choice == "4":

        if len(all_requisitions) == 0:
            print("No requisitions yet.")

        else:
            statistics = all_requisitions[0].requisition_statistics()

            print("\n===== REQUISITION STATISTICS =====")

            print(
                "The total number of requisitions submitted:",
                statistics["Total requisitions"]
            )

            print(
                "The total number of approved requisitions:",
                statistics["Approved requisitions"]
            )

            print(
                "The total number of pending requisitions:",
                statistics["Pending requisitions"]
            )

            print(
                "The total number of not approved requisitions:",
                statistics["Not approved requisitions"]
            )

            print()

    # Exit
    elif choice == "5":

        print("Goodbye!")
        break

    else:
        print("Wrong choice, please type a number from 1 to 5.\n")
