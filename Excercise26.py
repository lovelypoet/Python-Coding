# write a program that print out a inverted sequence, know that the sequence is being inputed
# input : a sequence s
# ouput : inverted sequence

try : 
    s = str(input("Input a string: "))
except TypeError :
    print("Please input a string")
else :
    print("".join(reversed(s)))
    
    
    
     