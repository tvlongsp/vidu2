sanpham = {
    "thuonghieu": "Apple",
    "sacnhanh": True,
    "namsx" : 2021,
    "mausac": ["Bạc", "Vàng", "Đen"]
}
print(sanpham)

print(sanpham["thuonghieu"])
print(sanpham.keys())
sanpham.update({"thuonghieu":"Lenovo"})
sanpham.update({"canang":"1.2kg"})
print(sanpham)