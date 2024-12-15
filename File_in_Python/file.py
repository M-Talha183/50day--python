#  open file in python (open)
#  Read file in python (r)
# write file in python (w)
#  create file in python (x)
#  append file in python (a)
#  Line by line read file in pytthon 
# seck and tee file in python 
#  Truncate in python 

#  OS  ==> Meachine Learning 
    # ||
    # ==> Data science 
#  handale Direction 
#  Careate folder 
# Fethch Data 


#  Frame Works => Liberaries => Modules => => classes => Method => Functions

#  f = open (`my_file.txt`,`r`)
#  f = open (`my_file.txt`,`rt`)
#  f = open (`my_file.txt`,`rb`)
#  print (f.read())  # content prient 
#  f.close => need to write 


# Write a file 
#  f = open (`my_file.txt`,`w`)
#  f = open (`my_file.txt`,`wt`)
#  f = open (`my_file.txt`,`wb`)
#  print (f.write("Hello"))  # content prient 
#  f.close => need to write 

f = open ('myText.txt','r')
print (f)  # checking the class 
# print(f.read())# to read whole file content 
# #  read desired parts and / bytes of a file content 
# first_five_bytes = f.read(25)
# first_five_bytes = f.read(40)
# first_five_bytes = f.read(90)
# print(first_five_bytes)

#  reading the content line by line 
for i in range(1,5):

    print(f.readline())

# reading lines automatically 
print(f.readline())
(f.close())