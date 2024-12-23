class person :
    def __init__(self,name,salary,age,company):
        self.name= name
        self.salary= salary
        self.age = age
        self.company= company
    def info(self):
        print(f'Name : {self.name} Salary : {self.salary} Age: {self.age} company : {self.company}')

talha = "Ali 20000 27 Google"
myRes=talha.split()
print(myRes[0])
p = person(name = myRes[0],salary=int(myRes[1]),age=int(myRes[2]),company=myRes[3])
p.info()