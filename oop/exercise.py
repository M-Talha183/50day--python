# class person :
#     @classmethod
#     def splittting_input(cls,talha):
#         myRes=talha.split("$")
#         cls.name = myRes[0]
#         cls.salary=int(myRes[1])
#         cls.age=int(myRes[2])
#         cls.company=myRes[3]
#         print
#     def info(self):
#         print(f'Name    : {self.name}\nSalary  : {self.salary}\nAge     : {self.age}\ncompany : {self.company}')


# p = person()
# p.splittting_input("Talha$20000$28$google")
# p.info()

#  ************************************************ Inheritence ******************************************************

# class Parent :
#     def __init__(self,name):
#         self.name = name 
#     def showName (self):
#         print(self.name)
    
# class ChildClass(Parent):
#     def show(self):
#         print(self.name)

# obj = ChildClass("Ahmed")
# print((obj.name))
# obj.show()
# obj.showName()

# create classes using single inheritence on the following scenario

# parent Class  

class Employ :
    def __init__(self,name,id,company):
        self.name = name
        self.id = id
        self.company= company

class Occupation(Employ):
    def occup(self,occupation):
        self.occupation = occupation
    def showInfo(self):
        print(f'Name :{self.name}\nId : {self.id}\nCompany : {self.company}\nOccupation : {self.occupation}')

myObj = Occupation("Talha",203,"Google")
myObj.occup("Software Engineer")
myObj.showInfo()