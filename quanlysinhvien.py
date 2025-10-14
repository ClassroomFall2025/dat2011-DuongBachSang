import sinhvienpoly as svpl

class QuanLySinhVien:
    def __init__(self):
        self.dssv = []

    def nhap_dssv(self):
        while True:
            ten = input("nhập tên sinh viên: ")
            nganh = input("nhập ngành sinh viên học: ")

            if nganh.lower() == "it":
                java = float(input("nhập điểm Java: "))
                html = float(input("nhập điểm HTML: "))
                css = float(input("nhập điểm CSS: "))
                sv = svpl.SinhVienIT(ten, nganh, java, html, css )
                self.dssv.append(sv)
            elif nganh.lower() == "biz":
                marketing = float(input("nhập điểm marketing: "))
                sales = float(input("nhập điểm Sales: "))
                sv = svpl.SinhVienBiz(ten, nganh, marketing, sales)
                self.dssv.append(sv)
            elif nganh.lower() == "esc":
                break
            else:
                print("Ngành không hợp lệ vui lòng nhập lại")
        return self.dssv
    def xuat_dssv(self): 
        if not self.dssv:
            print("danh sách sinh viên trống")
        else:
            print(f'{"tên sinh viên"}, {"ngành"}, {"diem"}, {"học lực"}')
            for sv in self.dssv:
                sv.xuat()
    def xuat_dssv_gioi(self): 
        print("==Danh sách sinh viên giỏi==")
        for sv in self.dssv:
            if sv.get_hoc_luc() in ["Giỏi", "Xuất sắc"]:
                sv.xuat()
        print("---------------------------------")
 
    def xuat_dssv_diem(self):
        print("==Sắp xếp sinh viên theo điểm==")
        self.dssv.sort(key =lambda sv: sv.get_diem(), reverse=True)
        for sv in self.dssv:
            sv.xuat()