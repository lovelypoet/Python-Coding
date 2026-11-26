# write a program that caculate factory of n : n!
# input : positive integer n >=0
# output : the value of n factory

import math
try :
    n = int(input("Please enter an positive interger number : "))
except ValueError  :
    print("Error! Please enter a legit number")
else :
    if n >= 0 :
        print(f" {n}! = {math.factorial(n)} ")
    else:
        print("Please enter a positive interger number")