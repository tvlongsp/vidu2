def ham_mu(n):
    x = lambda x: x ** n
    return x

ketqua = ham_mu(2)
print(ketqua(10))




x = lambda a: a + 10
y = lambda a, b: a + b

print(x(20))
print(y(100, 200))




def hello6():
    pass



def plus(num1, num2):
    return num1 + num2

x = plus(2, 3)
print(x)


def hello5(dssinhvien):
    for sv in dssinhvien:
        print(f"Hello {sv}")

dssinhvien = ["Hạnh", "Hoàng", "Hoa", "Huệ"]
hello5(dssinhvien)


def hello4(name = "Thị Tẹo"):
    print(f"Helo, my name is {name}")

hello4()
hello4("Bích Ngọc")



def hello3(**info):
    print("My name is {}".format(info["name"]))
    if 'age' in info.keys():
         print("My age is {} years old".format(info["age"]))

hello3(name ="Quang Tèo")
hello3(name="Ngọc Trinh", age ="19")



def hello2(*name):
    print("There are {} arguments".format(len(name)))
    for n in name:
        print(f"Hello {n}")

hello2("Hoa", "Huệ", "Hồng")


def hello(name, age):
    print(f"Hello my name is {name}, I'm {age} years old")

hello(age=19, name= "Ngọc Trinh")


