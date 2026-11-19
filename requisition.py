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
