# write a program that calculate a second equation : 
# a*x**2 + b*x + c = 0 with a != 0
# input : float a,b,c
# output : value x
import math
try :
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    c = float(input("Input c: "))
except ValueError :
    print("Please input a valid input")
else :
    delta = b**2 - 4*a*c
    if a != 0 :
        if delta > 0:
            x_1 = (-b + math.sqrt(delta))/ (2*a) 
            x_2 = (-b - math.sqrt(delta))/ (2*a)
            print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x_1}, x2 = {x_2} ")
        elif delta == 0 :
            x_3 = -b/(2*a)
            print(f"Phương trình có nghiệm kép: x1 = x2 = {x_3}")
        else :
            print("Phương trình vô nghiệm trong tập số thực")    
    else :
        print("Not valid")        
        
        
        
    
