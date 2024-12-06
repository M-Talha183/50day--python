import math
import random

# # #  write a program to print list in reverse order using loop 
# userNum = str(input("Enter The Number  : "))
# myLst1 = []

# myList = [10,20,30,40,50,60,70,80,90,100]
# print("Original list",myList)
# i = len(myList) -1
# j=0
# myreq = 0
# print ("Reversed The List")
# while( i >= j):
#     myreq = myList[i]
#     myLst1.append(myreq)
#     # print(myList[i])
#     i-=1
# print(myLst1)
# #  Q 2 write the program to calculate the sum  of all numbers from 1 to a given number

# userNum = int(input("Enter The Number : "))
# sum = 0
# for i in range(1,userNum+1):
#     sum+=i
# print(f"The sum of 1 to  given range {userNum} is =  {sum}")


#  prime number ******************************************

# Input: Number to check if it's prime and list primes less than it
# number = int(input("Enter a number: "))

# # Check if the input number is prime
# is_prime_number = 1  # Assume the number is prime initially (1 means prime, 0 means not prime)

# if number <= 1:
#     is_prime_number = 0  # Numbers <= 1 are not prime
# else:
#     for i in range(2, number):  # Check divisibility up to n - 1
#         if number % i == 0:
#             is_prime_number = 0  # Set to 0 if divisible by any number
#             break  # No need to check further

# # Output if the number is prime or not
# if is_prime_number == 1:
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

# # Find and print all prime numbers less than the input number
# print(f"Prime numbers less than {number} are:")

# for n in range(2, number):  # Loop through all numbers less than the input number
#     is_prime = 1  # Assume n is prime initially
#     for i in range(2, n):  # Check divisibility up to n - 1
#         if n % i == 0:
#             is_prime = 0  # Set to 0 if divisible
#             break
#     if is_prime == 1:
#         print(n, end=" ")  # Print the prime number

# #  Q 7 find the factorial of the number
# userNum = int(input("Enter The Number : "))


# fact = 1
# for i in range(1,userNum+1):
#     fact *= i
# print(f"The factorial of given number  {userNum}! is =  {fact}")

# gadgets = ["Mobole","Laptop",100,"Camera",310.28,"Speakers",27.00,"Telivesion",1000,"LaptopCase","cameraLences"]
# mySttring = []
# myNumber = []
 
# for i in gadgets :
#     j = str(i)
#     if j.isalpha() == True:
#         mySttring.append(j)
#     elif(j.isdigit()== True):
#         k = float(j)
#         myNumber.append(j)
#     else:
#         l = float(j)
#         myNumber.append(j)
# mySttring.sort()
# print(mySttring)
# mySttring.sort(reverse=True)
# myNumber.sort()
# print(myNumber)

# numbers = [3,5,23,6,5,1,2,9,8]
# greatest = 0
# for i in numbers:
#     if i > greatest:
#         greatest = i
# print(greatest)


# userNum = str(input("Enter The Word  : "))

# i = len(userNum) -1
# j=0
# print ("Reversed The List")
# while( i >= j):
#     print(userNum[i])
#     i-=1




# condition = True

# i = 0
# while(condition):
#     userNum = int(input("Enter the Number : "))
#     myNum = random.randint(1,9)
#     if(userNum == myNum):
#         print( f'You Guess The Right Number Your Number {userNum} & generate number {myNum} ')
#         condition =False
#     else:
#         print(f'Try again The Generate number is {myNum}')

# mynum = 0
# myAlpha = 0
# myVar = str(input("Enter the Data "))
# for i in myVar:
#     if (i.isalpha() == True ):
#         myAlpha +=1
#     elif(i.isdigit() == True):
#         mynum += 1

# print(f'letter = {myAlpha}')
# print(f'letter = {mynum}')

# # 17. Write a Python program to count the number of even and odd numbers from a series  of numbers. Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# evenCount = 0
# oddcount =0
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in numbers:
#     if i % 2 == 0:
#         evenCount += 1
#     else:
#         oddcount += 1
# print("The Even Count Of the Given List is ",evenCount)
# print("The Odd Count Of the Given List is ",oddcount)



# 16. Write a python program to select the maximum value from list (without using  maximum function). 
# numbers = [3,5,23,6,5,1,2,9,8]
# greatest = 0
# for i in numbers:
#     if i > greatest:
#         greatest = i
# print("The Gratest Value Of The Given Series Is ",greatest)

# 15. Write a Python program to copy elements from one list to another. 

# myList = [10,20,30,40,50,60,70,80,90,100]
# copyOfMyList = []
# for i in myList :
#     copyOfMyList.append(i)
# print("The Copy Of My List is ",copyOfMyList)

# # 14. Write a Python program that generates list of values. The values must be taken from  user as input. 

# userList = input("Enter The List : ").split()
# myList = []
# for i in userList:
#     myList.append(i)
# print(myList)

# 13. Write a Python program to print the number of vowels and consonant in your full  name. 

# myName = str(input("Enter Your Name : "))
# vowelsConter = 0
# consonantCounter = 0
# for i in myName:
#     if(i == "a" or i =="A"):
#         vowelsConter +=1
#     elif(i == "e" or i == "E"):
#         vowelsConter += 1
#     elif(i == "i" or i == "I"):
#         vowelsConter += 1
#     elif(i == "o" or i == "O"):
#         vowelsConter += 1
#     elif(i == "u" or i == "U"):
#         vowelsConter += 1
#     elif(i == " " ):
#         vowelsConter += 0
#     else:
#         consonantCounter += 1
# print("The vowels in tour name ",vowelsConter)
# print("The consonant",consonantCounter)

# 12. Write a program to calculate the length of string provide input by user (without using  len). 


# userNum = str(input("Enter The Word  : "))


wordLength=0
# print ("Reversed The List")
# while( i >= j):
#     print(userNum[i])
#     i-=1

