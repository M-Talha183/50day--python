# # #  Common Scence 
# # #  Error Correction  ==> Syntax (Funct , Loops , DataTtypes , Operation , Indent )
# #                     # ||
# #                     #  ==> Logical Condation , Operator 
# # #  Recursion 
# # #  Loops + Slicing 
# # #  Practice Problems ( Nested Dict , Condition ,Loops , Function )
# # # Conceptial Theoractical question '
# # #  Datatypes (Method)

# # # myTuple = (10,20,30,40,100,[1,2,3],"apple")
# # # print(myTuple [::1])
# # # print(myTuple[:1])
# # # print(myTuple[-1])

# # # givenTub = (1,2,3)
# # # (a,b,c,) = givenTub
# # # print(a)
# # # print(b)
# # # print(c)
# # myCount = (1,2,2,3,4,2)
# # # print(myCount.count(2))
# # # print(myCount.index(2))
# # count = 0
# # for i in myCount:
# #      if ( i == 2):
# #         count +=1
# #         print(i,count)

# # def mynatural ():
# #    sum = 0 
# #    for i in range(1,11):
# #     sum += i
# #    return sum

# # print(mynatural())

# # userNum = int(input("Enter the Number : "))
# # def primeNum (userNum):
# #    isPrimeNum = 1

# #    if userNum <= 1 :
# #     print("Not Prime Numeber")
# #    else:
# #     for i in range(2,userNum):
# #       if userNum % i == 0:
# #          break
# # if isPrimeNum == 1:
# #   print(f'{userNum} is Prime Number')
# # else:
# #  print(f'{userNum} is not  Prime Number')

# # primeNum(userNum)

# # myList = [2,4,6,8,8,2,6,10]
# # print(max(myList))
# # print(min(myList))
# # # print(set(myList))

# # print(myList[::-1])
# # myList.sort()
# # print(myList)

# # def myMax (Num):
# #   myMax = Num[0]
# #   for i in Num:
# #     if i > myMax:
# #       myMax = i
# #   return myMax

# # myList = [2,4,6,8,8,2,6,10]

# # print(myMax(myList))
# myList = []
# list = [2,4,6,8,10]
# i = len(list)
# # print(len(list))

# while i >= (len(list)):
#   print(list[i])
  
#   i-=1

# def covCurrency (usd):
#     inr = 83
#     inr = inr * usd
#     return inr
# print(covCurrency(73))

# userInp = int(input("Enter the number "))
# def evenOdd (num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# evenOdd(userInp)

# def factOrial(n):
#     if (n== 0 or n== 1 ):
#         return 1
#     else:
#         return n * factOrial(n-1)
# print(factOrial(5))
# n = 5
# for i in range(1,6):
#     print(i * "*")
# for i in range (n-1,0,-1):
# #         print(i * "*")
# def MyNum (char):
#     count =0

#     if len(char) == 0:
#         return 1
#     else:
#       count +=1
#       return  MyNum (len(char)-1)
    
#     print(count)
# print(MyNum("Talha"))
# myName = "Talha"
# count = 0
# for i in range(len(myName)):
#         count += 1
# print(count)
# def my_num(char):
#     # Base case: if the string is empty, return 0
#     if len(char) == 0:
#         return 0
#     else:
#         # Recursive case: count 1 for the first character and recurse with the rest
#         myName =my_num(char[1:])
#         print(myName)
#         return 1 + my_num(char[1:])

# # Example usage
# print(my_num("Talha"))  # Output: 5

def myNat():
    p