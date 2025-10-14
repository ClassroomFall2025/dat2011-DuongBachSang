import math
import datetime
class PhepToan:
    def __init__(self):
        self.ket_qua = None

    def thuc_hien(self):
        pass
    
    def hien_ket_qua(self):
        if self.ket_qua is not None:
            print("kết quả: ", self.ket_qua)
        else:
            print("chưa có kết quả nào")



class PhepTinhCoBan(PhepToan):
    def thuc_hien(self):
        number1 = float(input("nhập số thứ nhất: "))
        number2 = float(input("nhập số thứ hai: "))
        operator = input("nhập phép toán (+, -, *, /): ")

        if operator == "+":
            result = number1 + number2
        
        if operator == "-":
            result = number1 - number2
       
        if operator == "*":
            result = number1 * number2
      
        if operator == "/" and number2 != 0:
            result = number1 / number2
       
        self.ket_qua = f"{number1} {operator} {number2} = {result}"
        print("kết quả là: ", self.ket_qua)
        return self.ket_qua

class LuyThua(PhepToan):
    def thuc_hien(self):
        x = float(input("nhap so x: "))
        y = float(input("nhap so y: "))
        luy_thua = x ** y
        self.ket_qua =  f"{x}^{y} = {luy_thua}"
        print("lũy thừa là:", luy_thua)
        return self.ket_qua


class CanBacHai(PhepToan):
    def thuc_hien(self):
        x = float(input("nhap so x: "))
        result = math.sqrt(x)
        self.ket_qua = f"√{x} = {result}"
        print("căn bậc hai là: ",self.ket_qua)
        return self.ket_qua
    
class HamLuongGiac(PhepToan):
    def thuc_hien(self):
        sin = float(input("nhap so sin: "))
        cos = float(input("nhap so cos: ")) 
        tan = float(input("nhap so tan: "))
        sin = math.sin(sin)
        cos = math.cos(cos)
        tan = math.tan(tan)
        print("sin là:", sin)
        print("cos là:", cos)
        print("tan là:", tan)
        self.ket_qua =  f"sin = {sin}, cos = {cos}, tan = {tan}"
        return self.ket_qua

class Logarit(PhepToan):
    def thuc_hien(self):
        x = float(input("nhap so x: "))
        logarit = math.log10(x)
        print("logarit là:", logarit)
        self.ket_qua =  f"log10({x}) = {logarit}"
        return self.ket_qua

class GiaiPTBacNhat(PhepToan):
    def thuc_hien(self):
        a = float(input("nhập số a là: "))
        b = float(input("nhập số b là: "))
        if a == 0:
            if b == 0:
                self.ket_qua = "phương trình vô số nghiệm"
            else:
                self.ket_qua = "phương trình vô nghiệm"
        else:
            x = -b/a
        print("Vậy nghiệm của phương trình là: x = ",x)
        self.ket_qua =  f"{a}x + {b} = 0, x = {x}"
        return self.ket_qua

class GiaiPTBacHai(PhepToan):
    def thuc_hien(self):
        print("Giai phuong trinh bac 2")
        a = float(input("nhập số a là: "))
        b = float(input("nhập số b là: "))
        c = float(input("nhập số c là: "))

        if a == 0:
            if b == 0:
                if c == 0:
                    self.ket_qua = "phương trình vô số nghiệm"
                else:
                    self.ket_qua = "phương trình vô nghiệm"
            else:
                x = -c/b
                self.ket_qua = f"phương trình có một nghiệm x = {x}"
        
        else:
            delta = b**2 - 4*a*c
            if delta < 0:
                self.ket_qua = "phương trình vô nghiệm"
            elif delta == 0:
                x = -b/(2*a)
                self.ket_qua = f"phương trình có nghiệm kép x1 = x2 {x}"
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                self.ket_qua = f"{a}x^2 + {b}x + {c} = 0, x1 = {x1}, x2 = {x2},phương trình có hai nghiệm phân biệt x1={x1},và x2={x2}"
        print(self.ket_qua)
        return self.ket_qua

class HienThiLichSu(PhepToan):
    def __init__(self,lich_su):
        super().__init__()
        self.lich_su = lich_su

    def thuc_hien(self):
        print("Lich su: Luu va xem lai cac phep tinh da thuc hien")
        if not self.lich_su:
            print("Chưa có phép tính nào được thực hiện.")
        else:
            print("Lịch sử các phép tính đã thực hiện:")
        for item in self.lich_su:
            print(item)

class HienThiThoiGian(PhepToan):
    def __init__(self):
        super().__init__()

    def thuc_hien(self):
        print("Thoi gian: Hien thi thoi gian hien tai")
        now = datetime.datetime.now()   
        print("thời gian hiện tại: ", now.strftime("%H:%M:%S %d / %m / %y"))
        return self.ket_qua