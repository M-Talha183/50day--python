# # interviewMarks = int(input("Enter your Interview Marks"))

# # studentObtmarks = int(input("Enter your Test Obtained Marks"))

# # testElligbleCriteria = 80
# # interviewElligbleCriteria = 70

# # if(studentObtmarks >= testElligbleCriteria ):
# #     print("Your pass test  ")
# #     if(interviewMarks >= interviewElligbleCriteria):
# #         print("Pass Interview")
# #         print("Admitted")
# # else:
# #     print("You failed Interview & test ")        

# #  task 03 
# a = float(input("Enter your Number "))
# if(a > 0 ):
#     print("The given number is positive ",a)
#     if(a % 2 == 0):
#         print("The Given number is Even Number ", a)
#     elif(a%2 != 0):
#         print("The given number is odd Number ", a)
#     else:
#         print("The number is not even or not odd ")
# elif(a < 0 ):
#     if(abs(a)>10):
#         print("Large negative ",a)
#     elif(abs(a)<10):
#         print("the number small Negative",a)
# else:
#     print("the give number is zera ", a)

# Task 04 
studentMarks = float(input("Entetr the student marks :"))

if(studentMarks >= 90):
    if(studentMarks >= 95):
        print("A+ grade ", studentMarks)
    else:
        print("A grade ")
elif(studentMarks >= 80 and studentMarks<90):
    if(studentMarks>=85 ):
        print("B+ grade ",studentMarks)
    else:
        print("B grade ")
else:
    print("C grade ")