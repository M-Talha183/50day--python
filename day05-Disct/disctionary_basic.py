# # disctionary is the data strucure
# my_dist = {"pakistan":'karachi',"USA": 'New York', "France":'london'}
# # # key + value = pair 
# # print(type(my_dist))
# # # print(type(my_dist)) checking data type
# # print(my_dist)
# # print(len(my_dist))
# # #  checking is typecasting is possible in dictionary
# # # print(int(my_dist)) intiger
# # my_dict2 = {'2':'1', '4':'6'}
# # print(int(my_dict2))
# # #  type casting dict to str 


# #  type casting dictionary to list 

# # my_list = [1,2,3,4] 
# # print(dict(my_list))
# # methods od dictionary 
# print(my_dist.keys())
# print(my_dist.values())
# print(my_dist.items())
# print(my_dist.get("usa"))
# # print(my_dist["india"])
# print(my_dist.pop("pakistan"))
# print(my_dist.popitem())
# employ_data = {"talha":10, "zain":15}
# employ_data.clear()
# print(employ_data)
# employ_data = {"pakistan","zindabad"}
# print(employ_data)
# employ_data ['myName'] = "talha"
# print(employ_data)
# my_dist = {"iran":"thehran","uae":"dubai"}
# my_dist.update()
# print(my_dist)

#  write a prrogram taht takes a list of multiple choice response 
# Eg: [a,b,c] and prints a dictionary of question - response pairs
# {'q':"A", q2: "B","q3":"c"}:


# Miss File 
my_dict = {"pakistan":'karachi', \
           'usa':'new york', 'france':'london'}
# # #key+ value = 1pair
# # print(my_dict)
# # print(type(my_dict)) #checking datatype of dictionary
# # a = [1,2,3,4]
# # print(type(a)) #checking datatype of list
# # print(len(my_dict)) #length = 3

# # #typecasting dict to int
# # # print(int(my_dict)) #type error: typecasting not possible

# # #typecasting dict to str
# # my_dict1 = str(my_dict)
# # print(type(my_dict1)) #possible

# # #typecasting dict to list
# # my_dict2 = list(my_dict)
# # print(type(my_dict2))

# #typecasting list to dict
# # my_list = dict([1 , 2 , 3, 4])
# # print(type(my_list)) #not possible
# my_list1 = dict(['a1', 'b1', 'c2'])
# print(type(my_list1))
# print(my_list1)

# #acessing values via keys 
# print(my_dict['pakistan'])
# print(my_dict['usa'])
# print(my_dict['france'])

#Methods of Dictionary
print(my_dict.keys()) #fetches keys
print(my_dict.values()) #fetches values
print(my_dict.items()) #fetches key-value pair
print(my_dict.get('usa')) #fetches the value if present
print(my_dict.get('india')) #no error
my_data = {"iran":"tehran", "uae":"dubai"}
my_dict.update(my_data)
print(my_dict)
# print(my_dict['India']) #key error: if key not there
print(my_dict.pop('usa')) #pops desired key
print(my_dict)


my_dict.popitem() #pops last key value pair
print(my_dict)
employee_data = {'ali':10, "ahmed":11, "sara":12}
employee_data.clear() #dict empty
print(employee_data) #{}
#updating an empty dictionary/dictionary
employee_data['name1'] = 'umer'
print(employee_data)
my_name = {'name2':'kamran'}
employee_data.update(my_name)
print(my_name)

del (employee_data)
# print(employee_data) #name error

print('original dictionary:', my_dict)
copied_dict = my_dict.copy()
print('copied dictionary:', copied_dict)

empty_dict = {}
a = {1 , 2 , 3} #dictionary : iterable
new_dict = empty_dict.fromkeys(a, 8)
print(new_dict)

# # my_list = [] #insert 2 on 10th index in this list
# # # print(my_list.insert(1,2)) 
# # # print(my_list[2])
# # my_list[10:10] = [2] #insertion
# # print(my_list)

# dictionary = {}
# # dictionary.append(10[2])
# dictionary[10] = 2
# print(dictionary)
# # "" = double quotes
# # '' = single quotes
# # , = comma 

# """Task 01: Write a program that takes a 
# list of multiple choice responses.
#  Eg. [a , b, c] and prints a dictionary of 
#  question-response pairs 
#  {'Q1': "a", "Q2" : "b", "Q3": "c"}.
#  """
