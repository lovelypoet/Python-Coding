# write a program to print out the largest number that divisible by 3 and 7

# create a variable t to store the largest value, intialized value = -1
t = -1

for i in range(100,0,-1) :
    if(i % 7 == 0 and i % 3 ==0):
        t = i
        break

if t != 0:
    print(f" the number divisible by 3 and 7 is {t}")
else:
    print("there are no suitable values")