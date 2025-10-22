class SanPham:
    def __init__(self, ten_sp, gia_sp, giam_gia_sp):
        self.__ten_sp = ten_sp
        self.__gia_sp = gia_sp
        self.__giam_gia_sp= giam_gia_sp
    
    def get_ten_sp(self):
        return self.__ten_sp
    
    def set_ten_sp(self, _ten_sp):
        self.__ten_sp = _ten_sp

    def get_gia_sp(self):
        return self.__gia_sp
    
    def set_gia_sp(self, _gia_sp):
        self.__gia_sp = _gia_sp

    def get_giam_gia_sp(self):
        return self.__giam_gia_sp
    
    def set_giam_gia_sp(self, _giam_gia_sp):
        self.__giam_gia_sp = _giam_gia_sp
    

    def thue_nhap_khau(self):
        return self.__gia_sp * 0.1
    

    def xuat_thong_tin_sp(self):
        print(f"san pham {self.__ten_sp} co gia {self.__gia_sp} được giảm giá {self.__giam_gia_sp} và thuế nhập khẩu {self.thue_nhap_khau()}")

    # print("--thông tin sản phẩm 1--")
    # sp1.xuat_thong_tin_sp()

    # print("--thông tin sản phẩm 2--")
    # sp2.xuat_thong_tin_sp()

# def doc_giam_gia(self):
    #     return self.__giam_gia_sp
    
    # def ghi_giam_gia(self, giam_gia_moi):
    #     self.__giam_gia_sp = giam_gia_moi



# sử dụng xuất thông qua __str__
    # def __str__(self):
    #     return (f"san pham {self.ten_sp} co gia {self.gia_sp} được giảm giá {self.__giam_gia_sp} và thuế nhập khẩu {self.thue_nhap_khau()}")
        
# sp = SanPham("Bia", 2000000, 10000)
# # print(sp.doc_giam_gia())
# sp.xuat_thong_tin_sp()
# print(sp)

# sp.ghi_giam_gia(30000)
# print(sp)


 # code bài 2
    # def nhap_thong_tin_sp(self):
    #     self.ten_sp = input("nhập tên sản phẩm: ")
    #     self.gia_sp = float(input("nhập giá sản phẩm: "))
    #     self.__giam_gia_sp = float(input("nhập giảm giá sản phẩm: "))
# code bài 4
    # print("----nhập sản phẩm 1--- ")
    # ten1 = input("nhập tên sản phẩm 1: ")
    # gia1 = float(input("nhập giá sản phẩm 1: "))
    # giam1 = float(input("nhập giảm giá sản phẩm 1: "))
    # sp1 = SanPham (ten1, gia1, giam1)

    # print("---nhập sản phẩm 2---")
    # ten2 = input("nhập tên sản phẩm 2: ")
    # gia2 = float(input("nhập giá sản phẩm 2: "))
    # giam2 = float(input("nhập giảm giá sản phẩm 2: "))
    # sp2 = SanPham (ten2, gia2, giam2)