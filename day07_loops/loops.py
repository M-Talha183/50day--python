# # # colors = ["red","blue","orange"]
# # # #  prent 'present after checking if red is in the list 
# # # if("red" in colors):
# # #     print("PRESENT")
# # # else:
# # #     print("absent")
# # #  there are two tpes of loop in python 
# # #  loopps are automate in tasks
# # # loopsw are iterable
# # # run muliple time under specific time lipit  
# # # for i in range(50):
# # #  print(i,"hello world")

# # a= "Talha"
# # # for i in a:
# # # #  print(i)
# # students = {
# # 'student1': {'name': 'Alice', 'age': 20, 'grades': {'math': 85, 'science': 90}},
# # 'student2': {'name': 'Bob', 'age': 22, 'grades': {'math': 78, 'science': 95}},
# # 'student3': {'name': 'Charlie', 'age': 21, 'grades': {'math': 92, 'science': 89}}
# # }
# # # for i in students:
# # #  print(i,students[i])
# # # print(students.values())
# # # for i in students:
# # #  print(students.values())



# # #  range in loop 
# # print("print output of range  = 5")
# # for i in range (5):
# #     print(i)
# # print("print output of range  (0,5)")
# # for j in range(0,5):
# #     print(j)
# # print("print output of range  (1,5)")
# # for k in range(1,5):
# #     print(k)
# # print("print output of range  (2,5)")
# # for l in range(2,5):
# #     print(l)
# # print("print output of range  (3,5)")
# # for m in range(3,5):
# #     print(m)
# # print("print output of range  (1,5)")
# # for m in range(5):
# #     print(m + 1)
# #  understanding step size in range function 
# print('\n output when range = (0,10,1)')
# for i in range (0,10,1):
#     print(i)
# print('\n output when range = (0,10,2)')
# for i in range (0,10,2):
#     print(i)
# print('\n output when range = (0,10,3)')
# for i in range (0,10,3):
#     print(i)



# #  understanding for with 'pass'
# num = int(input("Enter the number"))

# for i in range(1,11):
#     print (num ,"x", i, "=", num*i)

# understanding the break statement 
# num = 2
# for i in range(1,11):
#     if ( i == 3):
#         break
#     print (num ,"x", i, "=", num*i)

# understanding the continue statement 
# num = 2
# for i in range(1,11):
#     if ( i == 3):
#         continue
#     print (num ,"x", i, "=", num*i)


my_list1 = ["1","2"]
my_list2 = ["4","5"]
for i in my_list1:
     for j in my_list2 :
        print(i,j)