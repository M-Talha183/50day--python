#  task 10 
# """Task 10: Wish 'good morning', 
# 'good noon', 'good after noon', 
# 'good evening',
#  'good night'to the user
# when a user enters the time 
# in hours:minutes:seconds """
# '02:00:01'                              

wishingTime = (input('Enter the Timestamp "0h : 0m : 0s : " '))
if(wishingTime >="05:00:00" and wishingTime <="11:59:59" ):
    print("Good Morning ")
elif(wishingTime >= "12:00:00" and wishingTime <="14:59:59" ):
    print("Good Noon")
elif(wishingTime >= "15:00:00" and wishingTime <= "16:59:59"):
    print("Good Afternoon")
elif(wishingTime > "17:00:00" and wishingTime <= "19:59:59"):
    print("Good Evening")
elif(wishingTime >= "20:00:00" and wishingTime < "23:59:59"):
    print("Good Night")
elif(wishingTime >= "00:00:00" and wishingTime < "04:59:59"):
    print("Good Late night")
  
else:
    print("Enter valid Time ")


