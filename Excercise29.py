# write a program that check whether a number is a element number?
# input : integer n, n >= 1
# output : n is element number or not?
# element number : Chỉ có đúng 2 ước số dương (chỉ chia hết cho 1 và chính nó)

import math
try :
    n = int(input("Please enter a integer number > 1 : "))
except ValueError :
    print("Please enter a legit number")
else :
    if n < 1 :
        print("Please enter a number > 1")
    elif n == 0 or n == 1:
       print(f'{n} is not an element number')
    else :
        count = 0
        for i in range(1, n+1):
            if n % i == 0 :
                count += 1
        if count == 2 :
            print(f"{n} is an element number")
        else :
            print(f"{n} is not an element number0")
            
            
              
                 
                    
                    
                    
                
            