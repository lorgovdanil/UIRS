a = int(input("A = "))
b = int(input("B = "))
if (a >= 0 and b >= 0):
    print('%.3f' % pow(a*b, 1/2))
else:
    print("Неверные данные")