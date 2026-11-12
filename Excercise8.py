try:
    x = int(input("Nhap so nguyen he 10: "))
except ValueError:
    print("Vui long nhap mot so nguyen.")
else:
    if x < 0:
        print("Vui long nhap so nguyen khong am.")
    else:
        print(f"{x} (he 10) = {oct(x)[2:]} (he 8)")
