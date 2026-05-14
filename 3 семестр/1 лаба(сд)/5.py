v1 = float(input("V1 = "))
v2 = float(input("V2 = "))
s = float(input("S = "))
t = float(input("T = "))
if (v1 >= 1 and v2 >= 1 and s >= 1 and t >= 1 and v1 <= 100 and v2 <= 100 and s <= 100 and t <= 100):
    print(f"Рассотяние = {abs(s - v1 * t - v2 * t):.4f}")
else:
    print("Неверные данные")