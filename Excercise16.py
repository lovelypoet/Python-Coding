# write a program that check năm nhuận, biết ràng lịch dương hiện tại được tính theo lịch Gregorius
# input : integer y là năm cần kiểm tra
# output : kết luận y là năm nhuận hay không nhuận

try :
    y = int(input("Input số năm cần kiểm tra: "))
except ValueError :
    print("Please input an integer number ")
else : 
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 :
        print(f"Năm {y} là năm nhuận")
    else :
        print(f"Năm {y} là năm dương")
        