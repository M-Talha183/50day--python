"""Gwetters retrives and fetch the values of an attribute with in a class 
setter are used to set the value of an aattribute within a class 

Why do we need to use them ?
1- To control access to attributes
(can't allow to set any value of attribute )
2- Validiting (confirming / checking values brfore checking them )
"""
#  get : to fetch / retrive something 
#  set : to place / insert a value 
#  with using decoders 
#  @ property  ---> builtin decorator getter in python 
#  @ <attribute>.setter ---> builtin setter in python
#  

class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age  # special attribute : positive integer 
    def displayInfo (self):
        print(f'Name : {self.name} age : {self.age}')
        