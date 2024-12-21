import math
# # """ practice Question 1 : Liberary Management System 
# # create a iberary management system that has atrribute has following atrrikbutes :
# # 1) title
# # 2) author
# # 3) isBorrow 
# # 4) isReturn 
# # that has methods :
# # borrowBook()--> set it to True if borrowed (if/else)
# # return Book () --> set it to True if retured  (if/else)
# # displayBookInfo() 
# # """
# # class Liberary :
# #     def __init__(self,title,author, isborrow , isrteturn):
# #         self.title = title
# #         self.author = author
# #         self.isborrow =isborrow 
# #         self.isisrteturn =isrteturn
# #     def borrowBook (self, b):
# #         if b == "Yes":
# #             self.isBorrow = True
# #         else:
# #             self.isBorrow = False
# #     def returnBook (self, r):
# #         if r == "Yes":
# #             self.isReturn = True
# #         else:
# #             self.isReturn = False
# #     def displayBookInfo (self):
# #         print(f'The Book Title is :{self.title} , The Book Author is : {self.author} , The Book Borrow Status is {self.isBorrow} \n
# #               the Book Return Status is {self.isReturn}')
# #  myBooks=[{id :101, "bookName" : "Karachi"},
# #              {id :102, "bookName" : "Peshawer"},
# #              {id :103, "bookName" : "Lahore"},
# #              {id :104, "bookName" : "Islamabad"},
# #              {id :105, "bookName" : "Kohat"},
# #              {id :106, "bookName" : "Istambol"},
# #              {id :107, "bookName" : "Gawader"},
# #              ]



# class BookLiberary :
#     def __init__(self, books):
#         self.books = books
#     def addBook (self,newbook):
#         self.books.append(newbook)
#     def searchBook(self,search):
#         if search in self.books:
#             print("Found")
#         else:
#             print("Not Found")
#     def displayInfo (self):
#         print(f'Collection Books {self.books}')

# myBooks =  ["Karachi", "Peshawer","Islamabad","Welcome Home", "Mind Paltter"]

# lib1 = BookLiberary (myBooks)

# userrinput = input("Do You want To Search Book").lower()
# if userrinput == "yes":
#     lib1.searchBook(input("Enter the name of book ").title())

# userAdd =  (input("Do you want add book ").lower())
# if userAdd == "yes":
    
#     lib1.addBook(input("Enter name of book you want to add ").title())

# lib1.displayInfo()


# class Calculator :
#     reult = 0
#     def __init__ (self, Num1, Num2,angle):
#         self.Num1 = Num1
#         self.Num2 = Num2
#         self.angle = angle
#     def Add (self):
#         self.reult = self.Num1 + self.Num2
#     def sub (self):
#         self.reult = self.Num1 - self.Num2
#     def mul (self):
#         self.reult = self.Num1 * self.Num2
#     def div (self):
#         self.reult = self.Num1 / self.Num2
#     def pow (self):
#         self.reult = self.Num1 ** self.Num2
#     def mySin(self):
#         self.reult = math.sin(self.angle)
#     def myCos(self):
#         self.reult = math.cos(self.angle)
#     def myTan(self):
#         self.reult = math.tan(self.angle) * (3.142/ 180)
#     def displayInfo(self):
#         print(f'{self.reult}')

# userNum1 = float(input("Enter the 1 Number "))
# userNum2 = float(input("Enter the 2 Number "))
# userNum3 = float(input("Enter the angle  "))

# myCal = Calculator(userNum1,userNum2,userNum3)

# userOperation = (input("Enter the operatopr : "))
# if userOperation == "+":
#     myCal.Add()
# if userOperation == "-":
#     myCal.sub()
# if userOperation == "*":
#     myCal.__module__()
# if userOperation == "/":
#     myCal.div()
# if userOperation == "**":
#     myCal.pow()
# if userOperation == "sin":
#     myCal.mySin()
# if userOperation == "cos":
#     myCal.myCos()
# if userOperation == "tan":
#     myCal.myTan()

# myCal.displayInfo()


