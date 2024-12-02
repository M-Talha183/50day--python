# Task 1: Consider a dictionary below
# # students = {
# 'student1': {'name': 'Alice', 'age': 20, 'grades': {'math': 85, 'science': 90}},
# 'student2': {'name': 'Bob', 'age': 22, 'grades': {'math': 78, 'science': 95}},
# 'student3': {'name': 'Charlie', 'age': 21, 'grades': {'math': 92, 'science': 89}}
# }

# Qs: 1 Delete Charlie’s Record
students = {
'student1': {'name': 'Alice', 'age': 20, 'grades': {'math': 85, 'science': 90}},
'student2': {'name': 'Bob', 'age': 22, 'grades': {'math': 78, 'science': 95}},
'student3': {'name': 'Charlie', 'age': 21, 'grades': {'math': 92, 'science': 89}}
}



del students["student2"]["grades"]["math"] # remove the bob meth record 
print(students)

# Task 2: Consider a following dictionary
# employees = { 101: {"name": "Alice", "department": "HR", "salary": 50000},
# 102: {"name": "Bob", "department": "IT", "salary": 60000} }
# Write a program to:
# 1. Add a new employee with ID 103.
# 2. Update the salary of the employee with ID 102.
# 3. Print the department of the employee with ID 101


employees = { 
 101: {"name": "Alice", "department": "HR", "salary": 50000},
 102: {"name": "Bob", "department": "IT", "salary": 60000}
 }
#  Add new employ data 
employees [103] = {"name": "Talha", "department": "Chemical", "salary": 70000} # Add new employ id
print(employees)
#  update the employe salary of id 102
employees [102]["salary"] = 90000
print(employees)
# print the id 101 & His department 
print(employees[101]["department"])

# Task 3: You have a dictionary of students and their grades in different subjects.
# Find the name of the student with the highest average grade.
# students = { "Alice": {"math": 90, "science": 85}, "Bob": {"math": 70, "science": 80},
# "Charlie": {"math": 88, "science": 92} }

students = { 
    "Alice": {"math": 90, "science": 85},
    "Bob":    {"math": 70, "science": 80},
    "Charlie": {"math": 88, "science": 92} 
     }
#  get  the average of the student 
stud1Average = ((students ["Alice"]["math"] + students ["Alice"]["science"]) / 2 ) 
stud2Average = ((students ["Bob"]["math"] + students ["Bob"]["science"]) / 2 ) 
stud3Average = ((students ["Charlie"]["math"] + students ["Charlie"]["science"]) / 2 ) 

# check the higrst AAverage student 
if(stud1Average > stud2Average and stud1Average > stud3Average):
    print( "Alice Has Higest Average Grade",stud1Average)
elif(stud2Average > stud1Average  and stud2Average > stud3Average):
     print("Bob Has Higest Average Grade",stud2Average)
else:
      print("Charlie Higest Average Grade",stud3Average)

# #Task 4: Library System
# #Question: Create a library management system using a nested dictionary where:
# #1. Each book has a unique ID as a key.
# #2. Each book contains details like title, author, and availability.
# #Write a program to:
# #1. Add a new book.
# #2. Borrow a book (change its availability to False).
# #3. Return a book (change its availability to True).

print("welcome To Ghalib Library")

libBooks = {
     100 : { "details" : {"title" : "The Science","author": "Talha","availability" : "True" }},
     101 : { "details" : {"title" : "The Math","author": "Zain","availability" : "True" }},
     102 : { "details" : {"title" : "The Chemist","author": "Waqar","availability" : "True" }},
     103 : { "details" : {"title" : "TheKarachi","author": "Salman","availability" : "True" }},
     104 : { "details" : {"title" : "The Peshawar","author": "Abdullah","availability" : "True" }},
     105 : { "details" : {"title" : "The Lahore","author": "Ibrar","availability" : "True" }}

}
addBook = (input("If you want to add book in liberay write true otherwise false : ").lower())
print(addBook)
if(addBook == "true"):
    idNum = int(input("Enter the id As key "))
    title = str(input("Enter the title of the book "))
    author = str(input("Enter the author of the book "))

    libBooks [idNum] = {"details" :{ "title" : title , "author" : author , "availability": True}}

    print(libBooks)
else:
    borrowBook = (input("If you want to borrow Book write true otherwise false : ").lower())
    print(borrowBook)
    if(borrowBook == "true"):
     borBookId = int(input("Enter the id As key "))
     libBooks [borBookId] ["details"] ["availability"] = False
     print(libBooks)
    else:
        returnBook = int(input("If you want to Return Book write his id : "))
        libBooks [returnBook] ["availability"] = True
        print(libBooks)
        