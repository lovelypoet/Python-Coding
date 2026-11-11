# write a program that calculate module of a input complex z from keyboard
# input : complex z = a + b*i
# output : module of complex z is a float

import math
z = complex(input(" Nhap so phuc z: "))
a = z.real
b = z.imag
module_of_z = math.sqrt(a**2 + b**2)

print(f"Gia tri cua complex z la : {module_of_z}") 