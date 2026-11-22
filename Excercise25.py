# write a program that calculate a sum of even number from 1 -> n ( n >= 1)
# input : Integer n >= 1
# output : sum of even numbers from 1 -> n

try : 
    n = int(input("Please input a integer number larger than 1: "))
except ValueError :
    print(" Please input a legit number")
else :
    if n >=1 :
        t = 0
        for i in range(1,n) :
            if i % 2 == 0 :
                t = t + i
        print(f"The sum of even numbers is : {t}")        
    else :
        print("Please input a correct number")
            