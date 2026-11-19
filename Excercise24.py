# write a program print numbers from 1 to 30
# except numbers that are divisible by 5

for i in range(1,31):
    if i % 5 == 0:
        continue
    print(i, end = "\t")
    