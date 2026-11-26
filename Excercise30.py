# write a program that count the quantity of element number in range (1,n)
# input : positive integer n
# output : quantity of element numbers in range(1,n)

try :
    n = int(input("Nhập số nguyên dương n: "))
except ValueError :
    print("Please input a valid number")
else :
    if n >= 0 :
        count = 0
        for i in range(1,n+1) :
            for t in range(i, i+1) :
                if i % t == 0 :
                    count += 1