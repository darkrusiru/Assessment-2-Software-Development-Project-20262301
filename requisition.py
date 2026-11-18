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