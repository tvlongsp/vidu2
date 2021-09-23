danhsach = []
hoten = input("Nhập họ tên: ")
danhsach.append(hoten)
hoten = input("Nhập họ tên: ")
danhsach.append(hoten)
hoten = input("Nhập họ tên: ")
danhsach.append(hoten)
hoten = input("Nhập họ tên: ")
danhsach.append(hoten)
hoten = input("Nhập họ tên: ")
danhsach.append(hoten)
print(danhsach)
vitri = int(input("Bạn muốn chỉnh sửa vị trí thứ mấy:" ))
hoten = input("Nhập họ tên mới: ")
danhsach[vitri] = hoten

danhsach[7] = hoten

print(danhsach)
print(danhsach.sort())
