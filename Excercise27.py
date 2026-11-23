# write a program that print the value of this function
# f(x) = 1 + x + x**2 + x**3 +...+ x**n
# input : float x, integer n (n >= 0)
# ouput : float f(x)
import math
try :
    x = float(input("Input a float x: "))
    n = int(input("Input a integer n: "))
except ValueError :
    print("Please enter a legit value")
else :
    if n >= 0 and math.isfinite(x):
        t = 0
        for i in range(0,n+1) :
            t = t + x**i
        print(f"the value of f is: {t}")
    else :
        print("Please enter a legit number n")     