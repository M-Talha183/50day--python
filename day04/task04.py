a = float(input('Enter the side a : '))
b = float(input('Enter the side b : '))
c = float(input('Enter the side c : '))
if(a == b == c):
  print("Equilanterial")
else:
    if(a==b or a==c or b==c ):
       print("Isosceles")
    else:
        if(a + b> c and a + c> b and b + c > a ):
         print("is scalene")
        else:
           print("invalid triangle")