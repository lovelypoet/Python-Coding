# write a program that solve a first equation : a*x+b = 0
# input : 2 float a and b
# output : the value of x

try :
    a = float(input("Please enter float number a: "))
    b = float(input("Please enter float number a: "))
except ValueError :
    print("please enter a valid number")
else :
    if a == 0 and b == 0:
         print("Phương trình vô số nghiệm")
    elif a == 0 and b != 0:
         print("Phương trình vô nghiệm")
    else :
         print(f"Phương trình có 1 nghiệm duy nhất: x = {-b/a}")   