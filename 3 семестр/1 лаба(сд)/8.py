a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
if (a == 0):
    print("Неверные данные")
    quit()
D = b * b - 4 * a * c
if (D < 0):
    print("Корней нет")
    quit()
x1 = (-1 * b + D**(1/2)) / (2 * a)
x2 = (-1 * b - D**(1/2)) / (2 * a)
if (x1 > x2):
    print(f"x1 = {x2:.4}")
    print(f"x2 = {x1:.4}")
else:
    print(f"x1 = {x1:.4}")
    print(f"x2 = {x2:.4}")