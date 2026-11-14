# write a program that convert thang điểm 4 
# (thường dùng trong lưu trữ điểm bậc đại học tại Việt Nam) 
# sang thang 10
# Formula : GPA(10) = GPA(4) x 10/4
# input : Grade in GPA 4
# output : Grade in GPA 10

try :
    x = float(input("Please enter your GPA: "))
except ValueError :
    print("GPA must be a legit number")
else :
    if x >= 0 and x <= 4 :
        gpa_10 = x * (10/4)
        print(f"Your GPA in GPA(10) is {gpa_10:.2f}")
    else:
        print("Please enter a valid number") 