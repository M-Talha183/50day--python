password = str(input('Enter the pasaord to check : '))
if len(password) >= 8 :
    if(password.alnum()):
        print("strong ")
else:
    print("Weak pasworrd")