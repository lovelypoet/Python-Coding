# write a program that calculate 
# Function 1: f(x) = 2**x + 3*x + 4 with x >= 1
# Function 2: f(x) = 3**x + 2*x + 1 with x < 1
# input : float x
# output : the value of either function 1 or function 2

try :
    x = float(input("Enter x"))
except ValueError :
    print("Please enter a valid value")
else :
    if x >= 1 :
        y = 2**x + 3*x + 4
        print("the value of f(x) is ", y)
    else :
        y = 3**x + 2*x + 1
        print("the value of f(x) is ",y)