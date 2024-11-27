#  task 10 
# """Task 10: Wish 'good morning', 
# 'good noon', 'good after noon', 
# 'good evening',
#  'good night'to the user
# when a user enters the time 
# in hours:minutes:seconds """
# '02:00:01'
print("hello world ")
wishingTime = str(input('Enter the Time in Hours minute and sec make sure we are in 24 Hours system "00 : 00 : 00" '))
if(wishingTime > "24 : 00 : 00"):
    print("please enter valid time  ")
elif(wishingTime < "04:00:00" ):
    print("Good Night")
elif(wishingTime >= "05:00:00" and wishingTime < "12:00:00"):
    print("Good Morning")
elif(wishingTime >= "12:00:00" and wishingTime < "13:00:00"):
    print("Good Noon")
elif(wishingTime >= "13:00:00" and wishingTime < "17:00:00"):
    print("Good Afternoon")
elif(wishingTime >= "17:00:00" and wishingTime < "20:00:00"):
    print("Good Evening")
# elif(wishingTime >= "20:00:00" and wishingTime <= "24:00:00"):
#     print("Good Night")
else:
    print("good night")


