class ChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong


    def get_chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2
        
    def get_dien_tich(self):
        return (self.chieu_dai * self.chieu_rong)
    
    def xuat(self):
        print(f"chiều dài hình chữ nhật: {self.chieu_dai}")
        print(f"chiều rộng hình chữ nhật: {self.chieu_rong}")
        print(f"chu vi hình chữ nhật: {self.get_chu_vi()}")
        print((f"diện tích hình chữ nhật: {self.get_dien_tich()}"))
    
class HinhVuong(ChuNhat):
    def __init__(self, canh):
        self.canh = canh
        super().__init__(self.canh, self.canh)


    def xuat(self):
        print(f"cạnh hình vuông là: {self.canh}")
        print(f"chu vi hình vuông : {self.get_chu_vi()}")
        print(f"diện tích hình vuông: {self.get_dien_tich()}")
        


