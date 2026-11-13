# write a program that calculate absolute value of a integer x
# input : integer n
# output : absolute value of n
import math
try :
    n = int(input("Input a number: "))
except ValueError :
    print("Please enter a number")
else:
    print(f"the absolute value of {n} is {abs(n)}")