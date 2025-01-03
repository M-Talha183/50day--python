# #  class syntax + constructor 
# class Person :
#     #  create constructor 
#     def __init__(self,name,age,occ):
#         self.name = name
#         self.age = age 
#         self.occ = occ
#     def showInfo (self,sal):
#         print(f'Name: {self.name}\nAge: {self.age}\nOccupation: {self.occ}\
#               Salary: {sal}')

# obj = Person("Talha",25,"Engineer")
# obj.showInfo(500000)

#  Implement using getters and setters 
# class Person :
#     #  create constructor 
#     def __init__(self,name,age,occ):
#         self.name = name
#         self.age = age 
#         self.occ = occ
#     def getname(self):
#          return self.name
#     def setname(self,name):
#         self.name = name
#     def showInfo (self,sal):
#         print(f'Name: {self.name}\nAge: {self.age}\nOccupation: {self.occ}\
#               Salary: {sal}')

# obj = Person("Talha",25,"Engineer")
# obj.showInfo(500000)

# Accessmodifiers public , (private __) ,( protected _)
class Person :
    #  create constructor 
    def __init__(self,name,age,occ):
        self.name = name
        self.age = age 
        self.occ = occ
    def getname(self):
         return self.name
    def setname(self,name):
        self.name = name
    def showInfo (self,sal):
        print(f'Name: {self.name}\nAge: {self.age}\nOccupation: {self.occ}\
              Salary: {sal}')

obj = Person("Talha",25,"Engineer")
obj.showInfo(500000)
