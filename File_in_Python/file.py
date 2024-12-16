# #  open file in python (open)
# #  Read file in python (r)
# # write file in python (w)
# #  create file in python (x)
# #  append file in python (a)
# #  Line by line read file in pytthon 
# # seck and tee file in python 
# #  Truncate in python 
# #  bty default reading Mode 
# #  OS  ==> Meachine Learning 
#     # ||
#     # ==> Data science 
# #  handale Direction 
# #  Careate folder 
# # Fethch Data 


# #  Frame Works => Liberaries => Modules => => classes => Method => Functions

# # f = open (`my_file.txt`,`r`)
# #  f = open (`my_file.txt`,`rt`)
# #  f = open (`my_file.txt`,`rb`)
# #  print (f.read())  # content prient 
# #  f.close => need to write 


# # Write a file 
# #  f = open (`my_file.txt`,`w`)
# #  f = open (`my_file.txt`,`wt`)
# #  f = open (`my_file.txt`,`wb`)
# #  print (f.write("Hello"))  # content prient 
# #  f.close => need to write 

# f = open ('myText.txt','r')

# print (f)  # checking the class 
# # print(f.read())# to read whole file content 
# # #  read desired parts and / bytes of a file content 
# first_five_bytes = f.read(10)
# print(first_five_bytes)
# # first_five_bytes = f.read(40)
# # first_five_bytes = f.read(90)
# # print(first_five_bytes)

# # #  reading the content line by line 
# # for i in range(1,5):

# #     print(f.readline())

# # # reading lines automatically 
# # print(f.readline())

# #  ************************************ using with in file handling *****************************************
# with open('myText.txt','r') as myText :
#     data = myText.read()  # read 
#     print(data)
# with open('myText.txt','w') as myText :
#     myText.write("My Name is Muhammad Talha ") # writng to a file ( erases all existing data)

# with open('myText.txt','a') as myText :
#     myText.write("Makesure that time data will not lose  ") # appending to an existing data
# # with open('xyz.txt','r') as myText :
#     # print(myText.read())# Error file not found

# with open('xyz.txt','w') as myText :
#     print(myText.write("abc"))# create new file no error 

# with open('xyz.txt','a') as myText :
#     print(myText.write("abc"))# create new file no error 

# with open('myText.txt','r') as myText :
#       data = myText.read()  # read 
   
# for i in data:
#     print(i,end= "")

# def myReadFiles (file_path):
#     with open(file_path , 'r') as myText: 
#         data = myText.read()
#         for i in data:
#             print(i , end= "")
# file_path = input("Enter The File Path : ")
# myReadFiles(file_path)
# with open('abc.txt','x') as abc :
#     print(abc.create())# create new file empty 

# for i in range(1,10):
#     with open('myText.txt','a') as myText :
#       myText.write("Makesure that time data will not lose \n  ") # appending to an existing data
#   ********************************************** readline ********************************************************
# def myReadFiles (file_path):
#     with open(file_path , 'r') as myText: 
#         data = myText.readline()
#         for i in data:
#             print(i , end= "")  
# file_path = input("Enter The File Path : ")
# myReadFiles(file_path)    # out put  My Name is Muhammad Talha Makesure that time data will not lose  
#  ******************************************************* redlines ******************************
# def myReadFiles (file_path):
#     with open(file_path , 'r') as myText: 
#         data = myText.read()
#         for i in data:
#             print(i , end= "")
# file_path = input("Enter The File Path : ")
# myReadFiles(file_path) #out put My Name is Muhammad Talha Makesure that time data will not lose  
# hello !
# good morning
# Good after noon



# def myReadFiles (file_path):
#     with open(file_path , 'r') as myText: 
#         data = myText.read()
#         for i in data:
#             print(i , end= "")
# file_path = input("Enter The File Path : ")
# myReadFiles(file_path) #out put My Name is Muhammad Talha Makesure that time data will not lose  00

# with open('myText.txt','r') as myText:
#     myText.seek(6)
#     print(myText.read())

file = open('myText.txt', 'r')

if not file.closed:
    print("The file is open.")

# file.close()

# Check if the file is closed
if file.close:
    print("The file is closed.")
