a = -3
b = -1
c = 0.2
for x in range(1, 12):
    f = (a*x + b) / pow(x, 5/3) * c + pow(x, a)
    print(f"x = {x}, f = {f:.2f}")
