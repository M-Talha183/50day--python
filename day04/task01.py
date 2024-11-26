print("Welcome To Metro Store")
megaDiscount = 5000
normalDiscount = 2000
customerBill = 5000
if(customerBill > megaDiscount ):
   discountBill = (customerBill * 20) / 100 
   discountBill = customerBill - discountBill
   print("congratulation You get 20% Discount on you Shopping Your discounted bill is ",discountBill)
elif (customerBill > normalDiscount and customerBill <= 5000):
   discountBill  = (customerBill * 10) / 100
   discountBill = customerBill - discountBill
   print("congratulation You get 10% Discount on you Shopping Your discounted bill is ",discountBill)
else:
   print("You are not eligible To our discount Condition please more shopping to get discount") 