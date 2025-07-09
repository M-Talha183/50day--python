import math
# # 💻 Exercises - Day 3
# # Declare your age as integer variable
# age = 20
# # Declare your height as a float variable
# height = 5.10
# # Declare a variable that store a complex number
# complex_num = 3 + 4j
# # Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# #     Enter base: 20
# #     Enter height: 10
# #     The area of the triangle is 100
# user_base = int(input("Enter the base : "))
# user_height = int(input("Enter the base : "))
# print(0.5 * user_base * user_height)

# # Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# # Enter side a: 5
# # Enter side b: 4
# # Enter side c: 3
# # The perimeter of the triangle is 12
# user_base = int(input("Enter the a : "))
# user_height = int(input("Enter the b : "))
# user_width = int(input("Enter the c : "))
# print(  user_base + user_height + user_width)


# # Calculate the slope, x-intercept and y-intercept of y = 2x -2

print("as we know that slope is 2 \n According to the formula y = mx+b ")
y = 2*(0)+(-2) # as we know that on y intercept x = 0
x = 0+2/2   # as we know that on x intercept y = 0
print(x,y)
# # Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
print("For slope ")
print((10-2)/(6-2))
print("Euclidean distance between point")
print(math.sqrt(((2-6)**2) + ((2-10)**2)))
# # Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
y_p = (-6 + math.sqrt(((6)**2 )-4*1*9))/2
y_n = (-6 - math.sqrt(((6)**2)-4*1*9))/2
print(y_p , "\n" , y_n)
# # Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# # Use and operator to check if 'on' is found in both 'python' and 'dragon'

if "on" in "python" and "on" in "dragon" :
    print("True")
else:
    print("False ")

# # Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# # Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# # Enter hours: 40
# # Enter rate per hour: 28
# # # Your weekly earning is 1120
# hour = int(input("Enter Hours "))
# rate_per_hour = int(input("Enter Rate per  Hours : "))
# print("Your weekly earning is : ", hour * rate_per_hour)
# # Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# # Enter number of years you have lived: 100
# # You have lived for 3153600000 seconds.

years = int(input("Enter the number of years you live "))
live = years * 365 * 24 * 60 * 60
print("you live ", live , "Seconds " )
# # Write a Python script that displays the following table
# # 1 1 1 1 1
# # 2 1 2 4 8
# # 3 1 3 9 27
# # 4 1 4 16 64
# # 5 1 5 25 125

# Display the table header
print("# # 1 1 1 1 1")

# Generate and print each row from 2 to 5
for i in range(2, 6):
    print(f"# # {i} 1 {i} {i**2} {i**3}")
