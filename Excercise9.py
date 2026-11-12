#calculate the value of function : y = 5*x**2 + 3*x +2
#input : float x
# output : float y, but have to be rounded to 2 number after the decimal
import math
try :
    x = float(input("nhap x"))
except ValueError :
    print("Nhap lai so")
else :
    y = 5*x**2 + 3*x + 2
    print(f"the value of function y is {y:.2f} ")
