# write a program that calculate area of a square and print it
# input : float a with a > 0
# output : area of a square round up to 3 numbers after the decimal
import math
try :
    a = float(input("Input a number of length: "))
except ValueError:
    print("Please input a number")
else :
    if  math.isfinite(a) and a > 0 :
        area = a*a
        print(f"The area of a square is {math.ceil(area*1000)/1000:.3f}")
    else :
        print("Please input a finite number larger than 0 ")

# the problem with round() is that if  1.5625 -> round() -> 1.562
# (not always works as expected)
# if we mean real round up then shoud use math.ceil()
# round(1.7) -> 2, round to the nearest integer by default
# we can use round(x, 3) vd: 1.5625 -> round(x,3) -> 1.562
# math.ceil(1.2) -> 2 , round to the smallest integer >5624
# example : math.ceil(1.5626) -> return 2
# finite number : số hữu hạn