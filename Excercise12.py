# write a program that find the largest number in 3 integers a,b,c'
# input : 3 integers a,b,c
# output : Print the largest number
import math
try :
    a = int(input("Nhap so nguyen thu nhat: "))
    b = int(input("Nhap so nguyen thu hai: "))
    c = int(input("Nhap so nguyen thu ba: "))
except ValueError:
    print("Please input a integer number")
else :
    if a >= b and a >= c:
        print("the largest number is ",a)
    elif b >= a and b >= c :
        print("the largest number is ",b)
    else :
        print("the largest number is ",c)
    