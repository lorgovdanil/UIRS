import math

for x in range(10, 31):
    x = x / 10
    f = pow(2, x+1) - pow(math.sin(x - 1), 3)
    print(f"x = {x}, f = {f:.2f}")