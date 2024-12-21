# 1) class variables 
# 2) Instance variables 



class Person :
    occupation = "Data Scientist"
    def __init__(self,name):
        self.name = name 
        self.salary = 1000
    def showDetails(self):
        print(f'{self.name},  {self.salary} {self.occupation}')

myDet = Person("Talha","engineer")
myDet.showDetails()