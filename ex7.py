tongtien = int(input("Số iền đã có: "))
songuoidonggop = 0
while tongtien <= 100000:
    donggop = int(input("Mời bạn góp tiền uống cafe: "))
    tongtien += donggop
    if tongtien > 100000: continue
    songuoidonggop +=1
else:
    print("Bạn đã có đủ tiền mời mọi người uống cafe, quyên góp gì nữa!")

print("Đã quyên góp được {} từ {} người!".format(tongtien, songuoidonggop))
