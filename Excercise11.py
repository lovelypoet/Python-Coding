# write a program that take a string x from the keyboard,
# we need to check wether the input string have the letter "a" or not
# input : a string x
# output : True or False
import string
try :
    x = str(input("input a string"))
except ValueError:
    print("Please input a string")
else:
    if 'a' in x or str.upper('a') in x:
        print("True")
    else :
        print("False")
        