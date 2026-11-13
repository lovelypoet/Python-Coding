# write a program to check whether a input number is odd or even
# input : interger n
# output : n odd or n even

try :
    n = int(input("input a number: "))
except ValueError:
    print("Please enter a number")
else :
    if n % 2 == 0 :
        print(f"{n} is even number")
    else :
        print(f"{n} is odd number")