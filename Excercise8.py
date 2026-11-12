# write a program convert a no sign integer in 10 bits to 8 bits
# input : integer x from the keyboard
# output : x represent 8 bits format
# x >> 2 means x // 2^2 cause >> is shift right 2 bits
# x << 2 means x * 2^2 cause << is shift left 2 bits
# hệ cơ số là cách dùng chữ số để viết một giá trị
# Hệ 10 dùng các chữ số 0-9 để biểu diễn 1 giá trị, hệ 8 dùng các chữ số 0-7 để biểu diễn 1 giá trị
# VD : 10 hệ 10 = 12 hệ 8 ( đều có giá trị là 10)
# bits nói về độ dài biểu diễn nhị phân
# VD : số 10 hệ số 10 được viết ở hệ nhị phân là 1010 (4 bits) còn 0000001010 cx là 10 nhưng độ dài là 10 bits 
try:
    x = int(input("Nhap so nguyen he 10: "))
except ValueError:
    print("Vui long nhap mot so nguyen.")
else:
    if not x < 0:
        print(f"{x} (he 10) = {oct(x)[2:]} (he 8)")
