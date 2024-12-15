# # # def find_max(lst):
# # #     max_value = lst [0]
# # #     for i in lst:
# # #         if i > max_value:
# # #             max_value = i
# # #     return max_value

# # # lst = [12,7,1,0,10,2,8]

# # # print(find_max(lst))
# # a = int(input("Enter the first value "))
# # b = int(input("Enter the second value "))
# # c = int(input("Enter the third value "))
# # def find_ave (a,b,c,):
   
# #    averageOfValues = (a+b+c) / 3
# #    return averageOfValues

# # print(find_ave(a,b,c))

# # def checkVowels (string):
# #     vowals = "a", "e","i","o","u"
# #     count = 0
# #     for char in string:
# #         if char in vowals:
# #             count +=1
# #     return count
# # myStr = "boundary".lower()
# # print(checkVowels(myStr))


# #  function calling in same name 
# #  see coolen 
# #  see parameter 
# #  see return statement 
# #  print statement 
# #  spallling name 
# #  assingnig the value of is it cannot assigning before the declaration 

# #  find the python program to find the maximam of 3 value 

# # def myMax (a,b,c):
# #     if a>b and a>c :
# #         print(a, "Is greaten then ")
# #     elif b > a and b>c :
# #         print(b, "Is greaten then ")
# #     elif c > a and c>b :
# #         print(c, "Is greaten then ")

# # myMax(5,10,9)
# def sumAllNumbers (myNumberList):
#     sum = 0

#     for i in myNumberList:
#         sum += i
#     return sum
# myList = [2,4,6]

# print(sumAllNumbers(myList))


# # my = "Talha"
# # i = 0
# # while i < (len(my)):
# #     print(my[i])
# #     i += 1

mySet1 = {2,3,4,5,6,7,8}
mySet2 = {2,3,4,5,6,7,8}
print(mySet1 | mySet2) # unoin
print(mySet1.difference_update(mySet2))

print(mySet1 & mySet2) # intrection
print(mySet1 ^ mySet2) # symentric difference
print(mySet1 - mySet2) #  difference 
print(mySet1.union(mySet2))
print(mySet1.intersection(mySet2))
print(mySet1.difference(mySet2))
# print(mySet1.)