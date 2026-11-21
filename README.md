# Assessment-2-Software-Development-Project-20262301
A Python-based Requisition Management System developed using Object-Oriented Programming (OOP). This project allows staff to submit purchase requisitions, calculate costs, manage approval statuses, and generate requisition statistics. 

1. Introduction
This Is An Extent of Assessment 1 ,I had written requisition system using Python Language in assessment 1 for this assessment 2 I have to covert that work to OOP prototype using  only one Class I named Requisition. The System let staff submit requistions with items,costs,price,staff id,and date.Then the system automatically approve requisitions under $500,  price above 500 manager have to respond, then It have functions to display requsitions and show statistics.

2.Acknowledgement of Generative AI Use
I have to use Artifical Inteligence as a mentor for this assessment, which help me to understand and restructure assessment 1 code.And also have to get help to make report 
organize and structure of report designed suggest by Claude.

3. Part 1: Software Development Life Cycle (SDLC)
Instead than working in a straight line, I worked incrementally. I developed the project in gradual chunks, committed each one, tested, identified issues, and then went back to address them.

3.1 Planning
I break this whole task into sub parts.  First I install git then connect to GitHub after all i create class add the approve methods, add manager response, display and statistics method write the test and in conclusion, write this report I also planned the three required commits so my repository show progress.
3.2 Requirements Analysis

I read the assessment brief and listed what the system must do:
•	Create a class with a suitable name and set up shared data in the __init__method (date, staff ID, staff name, status).
•	Use a global variable outside the class to create unique requisition IDs.
•	Add a requisition from a list of items with costs and return the total.
•	Approve automatically when the total is under $500; otherwise, the status stays Pending.
•	Let a manager mark a pending requisition as Approved or Not approved.
•	Display all requisitions in the required format and show four statistics (submitted, approved, pending, not approved).
•	Test with at least 5 requisitions and make three commits.
3.3 Design
I decided to use one class, Requisition, with the following design:
Part 	Design Decision
Global variables	counter (makes unique requisition IDs) and all_requisitions (a list that stores every requisition object)
__Init__
	Stores date, staff ID, staff name, requisition ID, total (0), status (Pending) and approval reference (None)
add_requisition(items)	Loops through the items, adds the costs and returns the total
approve_requisition()
	If total is under 500 the status becomes Approved and an approval reference is created (staff ID plus last 3 digits of the requisition ID)
respond_to_requisition(decision)
	Only works on Pending requisitions; sets Approved or Not approved

display_requisitions()
	Loops through all objects and prints them in the required format

requisition_statistics()
	Counts each status from the objects, so the numbers are always correct


3.4 Implementation
I write the code in Python using VS Code and committed it in stages:
•	Commit 1: project setup and the Assessment 1 baseline.
•	Commit 2 and : the Requisition class with __init__, add requisition and approve requisition.



3.5 Testing and Debugging
I tested the program by creating 5 requisitions that cover different scenarios and comparing the real output with the output I expected.
         

3.6 Deployment
I push My code files to github and create it as public 
3.7 Maintenance and Future Improvements
This project began as my Assessment 1 code, which I improved into an object-oriented design. Possible future improvements:
•	Reconnect the Tkinter GUI from Assessment 1 to the new class.
•	Remove the repeated approval-reference line.
•	Add input checks, for example rejecting negative costs.
•	Save requisitions to a file so they are not lost when the program closes.
4. Software Design Principles Used
Principle	How I applied it	Where in my code
KISS (keep it simple)	I used only basic tools: one class,  methods, loops and if/else	approve_requisition is a single if/else matching the $500 rule
Encapsulation	Data and the methods that use it are grouped together in one class; each object keeps its own data	total, status and approval_reference inside Requisition
Abstraction	A user calls a method without needing to know how the rule works inside	r1.approve_requisition()
Single responsibility	Each method does one job	add, approve, respond, display, statistics
Reuse	The Assessment 1 logic was carried into the class and one class creates many requisitions	The $500 rule and the [-3:] reference
DRY 	Statistics are counted from the objects, so there are no duplicate counters	requisition_statistics

5. Commit History Summary
Commit	What changed
1:  Initial commit	README and Assessment 1 baseline
2 and 3: Class with add and approve	Requisition class, init, add_requisition, approve_requisition


6. Part 2: Error and Challenge Screenshots
 

When We talk about errors mainly I have to face validation errors and spelling mistakes and symbol missing. Furthermore, date and name and ID system get any input after that import date and time module and display user to enter format 

And other things are spelling errors which is mostly people faced problem all screenshots I have attached above both of Cases.

7. Reflection

This assignment teaches me how to combine multiple functions into a single class. Understanding self and init was the most major change because each requisition object contains its own data while utilizing shared methods. I was able to develop the display and statistics techniques by using a global list to keep track of each request.
Making sure the data were accurate when a manager replied was a difficulty. Instead of retaining separate counters, I solved issue simply counting each object's status every 
