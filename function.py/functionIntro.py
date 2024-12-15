# #  uderstading the basic structure of function
# def my_sum (a,b):
#     'This function calcuate the sum '
#     addition = a+b
#     return (addition)
# print(my_sum.__doc__)
# print(my_sum(2,2))



# def gmean (a,b,c):
#     myMean = a / b
#     myMean2 = b/c
#     if(myMean == myMean2):
#         print(myMean)
#     else:
#         print("This is not geo matic series ")

# def Gmean (a,b):
#     '"This function calculates "'
#     Gmean = a+b
#     cemean = a*b
#     return Gmean , cemean
# Gmean(5,5)


# #  calcuator ************************************************ Calcualtor ******

# num1 = float(input("Enter Number : "))
# num2 = float(input("Enter Number : "))
# operator = str(input("Enter operator : "))


# def myCal (a,b,operator):
#     if(operator == "+" ):
#        mySum = a+b
#        print(mySum)
#     elif(operator == "-" ):
#        mySub = a-b
#        print(mySub)
#     elif(operator == "*" ):
#        myMult = a*b
#        print(myMult)
#     elif(operator == "/" ):
#        myDiv = a/b
#        print(myDiv)
#     else:
#        print("Enter the valid operator")

# myCal(num1,num2,operator)

#  understanding default parameters 





#  understanding the types of aurguments 
# 1) positional Arguments 
# def subtraction (a,b):
#     subtract = a+b
#     return subtract
# x = 10
# y = 3
# print(subtraction(x,y))

# #  Arbitrary positional Arguments 
# def kide_name (*kids):
#     print("Thee first name of kids :", kids[len(kids)-1])


# #  Non- arbitrary positional Argument :
# def sub (a,b): # position maters 

#     return(a-b)
# print(sub(7,10))

#  2 Key words Arguments ( kwargs)
#  Non arbiterery 
#  key words (**)
# def subtract (a,b):
#     return a- b
# print(subtract(b=10,a=5))

# def names (fname,lname):
#     print(f'my First names is {fname}')
#     print(f'my First names is {lname}')
# names(lname="xyz",fname="abc")

def names (**kwargs):
    print(f'my First names is {kwargs["fname"]}')
    print(f'my First names is {kwargs["fname"]}')
    
names(fname = "Muhammad",lname ="Talha")
