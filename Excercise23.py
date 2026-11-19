# write a program that print out the number from 1 to 20
# except the number that divisible by 4

import numpy as np
t = []
for i in range(1,21):
    if i % 4 != 0 :
        t.append(i)
arr = np.array(t) 
print(f" the numbers are : {arr}")