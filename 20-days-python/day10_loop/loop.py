# .

# 💻 Exercises: Day 10
# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.


# for i in range(0,11):
#     print(i , end=" ")
# print("")
# i = 0
# while i <=10 :

#     print(i, end=" ")
#     i +=1
# print("")
# Iterate 10 to 0 using for loop, do the same using while loop.

# for i in range(10,-1,-1):
#     print(i,end=" ")
# print(" ")
# i = 10
# while i >= 0 :
#     print(i,end= " ")
#     i -=1
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
st = "########"

for i in range(0,8):
    print(st[:i])
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
  
# Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

st = "# # # # # # # # #"
for i in range(0,8):
    print(st)


# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for i in range(0,11):
    print(i , "x" , i ,"=", i*i)
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in range(0,len(lst)):
    print(lst[i])
# Use for loop to iterate from 0 to 100 and print only even numbers

# for i in range(0,101):
#     if i % 2  == 0:
#         print(i , end=" ")
        
# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(0,101):
    if i % 2  == 0:
        continue
    else:
        print(i ,end=" ")
# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
sum = 0
for i in range(0,101):
    sum += i
print("\n",sum)
# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

