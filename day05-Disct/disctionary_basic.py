# disctionary is the data strucure
my_dist = {"pakistan":'karachi',"USA": 'New York', "France":'london'}
# key + value = pair 
print(my_dist)
print(len(my_dist))
# Accesing value via keys
print(my_dist['pakistan']) 
print(my_dist['USA']) 
print(my_dist['France'])
#  using accessing Only keys  
print(my_dist.keys())
#  accessing values 
print(my_dist.values())
# print(my_dist["talha"]) # key erroe if key is not present 
print(my_dist.get('usa')) # if you want to check your kay and in reason of 
# absent the key  you dont want to get error so use get () method 
print(my_dist.get("USA"))

# my_list = []
# my_list [10] = 2
my_dist ["10"] = "2"
print(my_dist)