# myList = [2,4,6,8,10]
# myReq= 0
# myres=0
# for i in myList:
#     myReq += i
#     myres = myReq / len(myList)

# print(myres)

# myList = [2,8,2,9,8,6,9,15]
# myres = set(myList)
# print(myres)

# def myname(text):
#     myPhal = text[::-1]
#     if text == myPhal:
#         print("Phalandrom ")
#     else:
#         print("not")

# myname("madam")

# def myWord(text):
#     myword = text.split()
#     mures = "".join(reversed(myword))
#     print(mures)
# myWord("Hello world")


# def myFun (text,subText):
#     if subText in text:
#         return True
#     else:
#         False
# print(myFun("Hello World","World"))
# try:
    
#   def myFun(x,y):
#       return x/y
#   print(myFun(5,5))
# except ZeroDivisionError as e:
#    print(e)

# try: 
#   def myFun(x):
#       myres = int(x)
#       return myres
#   print(myFun("589.8"))
# except :
#    print("Invalid Input")


# def myfile (fileName):
#     try:
#         with open(fileName,"r") as file:
#             content = file.read()
#             print(content)
#     except FileNotFoundError:
#         print("File not found ")

# myfile("C:/Users/Administrator/Desktop/50-days-python/Exam_preperation/talha.txt")

# class Student :
#     def __init__(self,name,age,grades):
#         self.name = name
#         self.age= age
#         self.grades = grades
#     def avg(self):
#         return sum(self.grades ) / len(self.grades)

# my=[80,70,80]
# i = Student("Talha",19,my)
# print(i.avg())

class Person:
    def __init__(self,name,age,adress):
        self.name=name
        self.age=age

class Employ(Person):
    def __init__(self,salary):
        super().__init__()
        self.name = name
        self.salary = salary
    def disp(self):
        print(self.name,self.age,self.salary)
my = Person("Talha",19,"E-18")
my1=Employ("50000")

