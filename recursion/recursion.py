
# sum of list by Normal Loop 
# L = [2,4,6,8]
# sum = 0
# for i in L:
#     sum = sum +i 
# print(sum )
#  sum of list by function 
# def sumoflist (L):
#     sum = 0
#     for i in L:
#         sum = sum + i 
#     return sum 
# print(sumoflist(L))
# L = []
# print(len(L))
# L = [2,4,6,8]
# def sumofList (L):
#     if len(L)==0:
#         return 0
#     else:
#         return sumofList (L[1:]) + L[0]
# print(sumofList(L))

# userNum = int(input("Enter The Number : "))
# sum = 0
# for i in range(1,userNum+1):
#     sum+=i
# print(f"The sum of 1 to  given range {userNum} is =  {sum}")

# L= [1,2,3,4,5,6,7,8,9,10]
# sum = 0
def febonacci (L):
    if L == 0 :
        return 0
    elif(L== 1):
        return 1
    else:
        return febonacci(L-1) + febonacci(L-2)
# print(febonacci(10))

for i in range(1,10):
    print(febonacci(i))

# print(febonacci(10))