class person :
    @classmethod
    def splittting_input(cls,talha):
        myRes=talha.split("$")
        cls.name = myRes[0]
        cls.salary=int(myRes[1])
        cls.age=int(myRes[2])
        cls.company=myRes[3]
        print
    def info(self):
        print(f'Name    : {self.name}\nSalary  : {self.salary}\nAge     : {self.age}\ncompany : {self.company}')


p = person()
p.splittting_input("Talha$20000$28$google")
p.info()