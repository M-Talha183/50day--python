# # class person :
# #     @classmethod
# #     def splittting_input(cls,talha):
# #         myRes=talha.split("$")
# #         cls.name = myRes[0]
# #         cls.salary=int(myRes[1])
# #         cls.age=int(myRes[2])
# #         cls.company=myRes[3]
# #         print
# #     def info(self):
# #         print(f'Name    : {self.name}\nSalary  : {self.salary}\nAge     : {self.age}\ncompany : {self.company}')


# # p = person()
# # p.splittting_input("Talha$20000$28$google")
# # p.info()

# #  ************************************************ Inheritence ******************************************************

# # class Parent :
# #     def __init__(self,name):
# #         self.name = name 
# #     def showName (self):
# #         print(self.name)
    
# # class ChildClass(Parent):
# #     def show(self):
# #         print(self.name)

# # obj = ChildClass("Ahmed")
# # print((obj.name))
# # obj.show()
# # obj.showName()

# # create classes using single inheritence on the following scenario

# # parent Class  

# class Employ :
#     def __init__(self,name,id,company):
#         self.name = name
#         self.id = id
#         self.company= company

# class Occupation(Employ):
#     def occup(self,occupation):
#         self.occupation = occupation
#     def showInfo(self):
#         print(f'Name :{self.name}\nId : {self.id}\nCompany : {self.company}\nOccupation : {self.occupation}')

# myObj = Occupation("Talha",203,"Google")
# myObj.occup("Software Engineer")
# myObj.showInfo()

#  ******************************************************overriding *********************************************
# class Parent :
#     def show_name(self):
        
#         print(self.name)
# class Child(Parent):
#     def show_name(self):
#         print(self.name)

# myObj = Child()
# myObj.name = "Talha"
# myObj.show_name()

# obj = Parent()
# obj.name="Talha"
# obj.show_name()
# print*(obj.__dir__("talha"))
# obj1= Child()
# obj1.name = "XYZ"
# obj1.show_name("Xyz")

# *********************************************************************# Example 2 
# class Parent :
#     def show_name (self):
#         print(self.name)
# class Child(Parent):
#     def show_name(self):
#         print(self.name)
#         print("I am Child Class ")

# obj = Child()
# obj.name = "Talha"
# obj.show_name()
#  ****************************************************** Super KeyWord ******************************************

# class Parent :
#     def show_name (self):
#         print("Python")
# class Child(Parent):
#     def info(self):
#         print("I am a child class")
#         super().show_name()


# obj1 = Child()
# obj1.name = "xyz"
# obj1.info()

#  **************************************** Suppper Key Word on Constructor 

class Parent :
    def __init__(self,name,id):
        self.name = name 
        self.id = id 
class Child (Parent):
    def __init__(self, name, id , occ,company):
        super().__init__(name, id)
        self.occ = occ
        self.company = company
    def display (self):
        print(f'Name : {self.name}\nID : {self.id}\nOCCupation: {self.occ}\nCompany{self.company}')

obj = Child("Talha", 183,"Developer", "Facebook")
obj.display()