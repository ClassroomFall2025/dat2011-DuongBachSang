class SinhVienPoLy:
    def __init__(self, ten_sv, nganh):
        self.__ten_sv = ten_sv
        self.__nganh = nganh

    def get_ten_sv(self):
        return self.__ten_sv
    
    def set_ten_sv(self, ten_sv):
        self.__ten_sv = ten_sv

    def get_nganh(self):
        return self.__nganh
    
    def set_nganh(self, nganh):
        self.__nganh = nganh


    
    def get_diem(self):
        pass
    
    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem < 5:
            return "Yếu"
        elif 5 <= diem < 7:
            return "Trung bình"
        elif 7 <= diem < 8:
            return "Khá"
        elif 8 <= diem < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"
    def xuat(self):
        print(f"tên sinh viên: {self.__ten_sv}")
        print(f"ngành học: {self.__nganh}")
        print(f"điểm trung bình: {self.get_diem()}")
        print(f"học lực: {self.get_hoc_luc()}")


class SinhVienIT(SinhVienPoLy):
    def __init__(self, ten_sv, nganh, java, html, css):
        super().__init__(ten_sv, nganh)
        self.java = java
        self.html = html
        self.css = css

    def get_diem(self):
        return (2 * self.java + self.html + self.css) / 4 

class SinhVienBiz(SinhVienPoLy):
    def __init__(self, ten_sv, nganh, marketing, sales):
        super().__init__(ten_sv, nganh)
        self.marketing = marketing
        self.sales = sales

    def get_diem(self):
        return (2 * self.marketing + self.sales) / 3
