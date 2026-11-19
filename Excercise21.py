# write a program that calculate sum of odd numbers from 1 to 50
# output : sum of odd numbers

# a variable t to store the sum, initialize it = 0
t = 0

# index i
i = 1

while i <= 50 :
    if i % 2 != 0 :
        t = t + i
    i += 1
print(f"sum of odd numbers from 1 to 50 is {t}")

