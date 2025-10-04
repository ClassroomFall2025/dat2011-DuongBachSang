import math
import datetime
def phep_tinh_co_ban():
    number1 = float(input("nhập số thứ nhất: "))
    number2 = float(input("nhập số thứ hai: "))
    operator = input("nhập phép toán (+, -, *, /): ")
    if operator == "+":
        result = number1 + number2
        print(f"kết quả là: {number1} + {number2} = {result} ")
    if operator == "-":
        result = number1 - number2
        print(f"kết quả là: {number1} - {number2} = {result} ")
    if operator == "*":
        result = number1 * number2
        print(f"kết quả là: {number1} * {number2} = {result} ")
    if operator == "/" and number2 != 0:
        result = number1 / number2
        print(f"kết quả là: {number1} / {number2} = {result} ")
        return f"{number1} {operator} {number2} = {result}"


def luy_thua():
    x = float(input("nhap so x: "))
    y = float(input("nhap so y: "))
    luy_thua = x ** y
    print("lũy thừa là:", luy_thua)
    return f"{x}^{y} = {luy_thua}"


def can_bac_hai():
    print("can bậc hai")
    x = float(input("nhap so x: "))
    can_bac_hai = math.sqrt(x)
    print("căn bậc hai là:", can_bac_hai)
    return f"√{x} = {can_bac_hai}"

def ham_luong_giac():
    print("Ham luong giac")
    sin = float(input("nhap so sin: "))
    cos = float(input("nhap so cos: ")) 
    tan = float(input("nhap so tan: "))
    sin = math.sin(sin)
    cos = math.cos(cos)
    tan = math.tan(tan)
    print("sin là:", sin)
    print("cos là:", cos)
    print("tan là:", tan)
    return f"sin = {sin}, cos = {cos}, tan = {tan}"

def logarit():
    print("Logarit")
    x = float(input("nhap so x: "))
    logarit = math.log10(x)
    print("logarit là:", logarit)
    return f"log10({x}) = {logarit}"


def giai_pt_bac_nhat():
    print("Giai phuong trinh bac nhat")
    a = float(input("nhập số a là: "))
    b = float(input("nhập số b là: "))
    if a == 0:
        if b == 0:
            print("phương trình vô số nghiệm")
        else:
            print("phương trình vô nghiệm")
    else:
        x = -b/a
        print("Vậy nghiệm của phương trình là: x = ",x)
        return f"{a}x + {b} = 0, x = {x}"

def giai_pt_bac_hai():
    print("Giai phuong trinh bac 2")
    a = float(input("nhập số a là: "))
    b = float(input("nhập số b là: "))
    c = float(input("nhập số c là: "))

    if a == 0:
        if b == 0:
            if c == 0:
                print("phương trình vô số nghiệm")
            else:
                print("phương trình vô nghiệm")
        else:
            x = -c/b
            print("phương trình có một nghiệm x = ",x)
        
    if a != 0:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("phương trình vô nghiệm")
        elif delta == 0:
            x = -b/(2*a)
            print("phương trình có nghiệm kép x1 = ",x)
        elif delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print("phương trình có hai nghiệm phân biệt x1=",x1,"và x2=",x2)
        return f"{a}x^2 + {b}x + {c} = 0, x1 = {x1}, x2 = {x2}"
    

def hien_thi_lich_su(lich_su):
    print("Lich su: Luu va xem lai cac phep tinh da thuc hien")
    if not lich_su:
        print("Chưa có phép tính nào được thực hiện.")
    else:
        print("Lịch sử các phép tính đã thực hiện:")
        for item in lich_su:
            print(item)

def hien_thi_thoi_gian():
    print("Thoi gian: Hien thi thoi gian hien tai")
    now = datetime.datetime.now()
    print("thời gian hiện tại: ", now.strftime("%H:%M:%S %d / %m / %y"))





