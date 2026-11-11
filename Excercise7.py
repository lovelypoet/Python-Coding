# write a program that calculate circuit of a circle with radius r is a positive interger
# input : radius r
# output : circuit of a circle is a float type

import math 

r = int(input("Nhap ban kinh:  "))
if (r > 0):
    circuit = 2 * r * math.pi
    print(f" circuit of a circle with radius {r} is {circuit: ,.2f}")
else :
    print("Please enter a correct radius")