a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
if (abs(a) > 100 or abs(b) > 100 or abs(c) > 100):
    print("Неверные данные")
    quit()
d = a
a = b
b = c
c = d
print(a, b, c)