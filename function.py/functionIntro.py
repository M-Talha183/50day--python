#  uderstading the basic structure of function
# def my_sum (a,b):
#     addition = a+b
#     return (addition)
# # my_sum(2,3)


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




num1 = float(input("Enter Number : "))
num2 = float(input("Enter Number : "))
operator = str(input("Enter operator : "))


def myCal (a,b,operator):
    if(operator == "+" ):
       mySum = a+b
       print(mySum)
    elif(operator == "-" ):
       mySub = a-b
       print(mySub)
    elif(operator == "*" ):
       myMult = a*b
       print(myMult)
    elif(operator == "/" ):
       myDiv = a/b
       print(myDiv)
    else:
       print("Enter the valid operator")

myCal(num1,num2,operator)
    