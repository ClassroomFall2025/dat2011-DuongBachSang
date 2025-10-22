from ASM import *
ds_nv = []
def nhap_danh_sach_nv():
    
    print("nhập danh sách nhân viên")
    try:
        n = int(input("Nhập số lượng nhân viên: "))
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
        return
    for i in range(n):
        print(f"\n--- Nhập nhân viên thứ {i+1} ---")
        loai = input("Loại nhân viên (1: Hành chính | 2: Tiếp thị | 3: Trưởng phòng): ")

        ma_nv = input("Mã nhân viên: ")
        ho_ten = input("Họ tên: ")
        luong = float(input("Lương cơ bản: "))

        if loai == "2": 
            doanh_so = float(input("Doanh số: "))
            hoa_hong = float(input("Hoa hồng (ví dụ: 0.05): "))
            nv = TiepThi(ma_nv, ho_ten, luong, doanh_so, hoa_hong)

        elif loai == "3":  
            trach_nhiem = float(input("Lương trách nhiệm: "))
            nv = TruongPhong(ma_nv, ho_ten, luong, trach_nhiem)
        else: 
            nv = NhanVien(ma_nv, ho_ten, luong)

        ds_nv.append(nv)

    print("\n Đã nhập danh sách nhân viên thành công!")

def xuat_danh_sach_nv():
    print("xuất danh sách nhân viên")
    for nv in ds_nv:
        nv.xuat()

def xoa_nv():
    print("xóa nhân viên theo mã")
    ma = input("nhập mã nhân viên cần xóa: ")
    for nv in ds_nv:
        if nv.ma_nv == ma:
            ds_nv.remove(nv)
            print(f"đã xóa nhân viên {ma} ")
            return
        print("không tìm thấy mã nhân viên cần xóa")



def cap_nhat_nv():
    print("cập nhật thông tin nhân viên")
    ma = input("nhập mã nhân viên cần cập nhật: ")
    for nv in ds_nv:
        if nv.ma_nv == ma:
            print("nhập thông tin mới: ")
            ho_ten = input("họ tên mới: ")
            luong = input("lương mới: ")
            if ho_ten:
                nv.ho_ten = ho_ten
                nv.luong = float(luong)
                print("cập nhật thành công")
                return
    print("không tìm thấy nhân viên")

def tim_kiem_nv_theo_luong():
    print("Tìm kiếm nhân viên theo lương")
    min_luong = float("nhập lương tối thiểu: ")
    max_luong = float("nhập lương tối đa: ")

    ket_qua = list(filter(lambda nv: min_luong <= nv.luong <= max_luong, ds_nv))
    print(f"danh sách nhân viên có lương trong khoảng {min_luong:,.0f} - {max_luong:,.0f}:")
    if ket_qua:
        for nv in ket_qua:
            nv.xuat()
    else:
        print("không có nhân viên nào phù hợp")

def sap_xep_theo_ho_ten():
    print("Sắp xếp nhân viên theo họ tên")
    ds_nv.sort(key=lambda nv: nv.ho_ten)
    print("\n Danh sách nhân viên (sắp xếp theo họ tên):")
    for nv in ds_nv:
        nv.xuat()


def sap_xep_theo_thu_nhap():
    
    print(" Sắp xếp nhân viên theo thu nhập")
    ds_nv.sort(key=lambda nv: nv.getThuNhap(), reverse=True)
    print("\n Danh sách nhân viên (sắp xếp theo thu nhập):")
    for nv in ds_nv:
        nv.xuat()



def top_5_thu_nhap():
    
    print("Xuất 5 nhân viên có thu nhập cao nhất")
    top5 = sorted(ds_nv, key=lambda nv: nv.getThuNhap(), reverse=True)[:5]
    for nv in top5:
        nv.xuat()


